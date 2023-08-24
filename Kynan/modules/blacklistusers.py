# Module to blacklist users and prevent them from using commands by @TheRealPhoenix
import html
import Kynan.modules.sql.blacklistusers_sql as sql
from Kynan import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    dispatcher,
) 
from Kynan.modules.helper_funcs.chat_status import dev_plus
from Kynan.modules.helper_funcs.extraction import (
    extract_user,
    extract_user_and_text,
)
from Kynan.modules.log_channel import gloggable
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import mention_html

BLACKLISTWHITELIST = [OWNER_ID] + DEV_USERS + DRAGONS + WOLVES + DEMONS
BLABLEUSERS = [OWNER_ID] + DEV_USERS


@dev_plus
@gloggable
def bl_user(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("Aku ragu itu pengguna.")
        return ""

    if user_id == bot.id:
        message.reply_text("Bagaimana saya bisa melakukan pekerjaan saya jika saya mengabaikan diri saya sendiri?")
        return ""

    if user_id in BLACKLISTWHITELIST:
        message.reply_text("Tidak!\nMemperhatikan Bencana adalah tugasku.")
        return ""

    try:
        target_user = bot.get_chat(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("Sepertinya saya tidak dapat menemukan pengguna ini.")
            return ""
        raise

    sql.blacklist_user(user_id, reason)
    message.reply_text("Saya akan mengabaikan keberadaan pengguna ini!")
    log_message = (
        f"#BLACKLIST\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(target_user.id, html.escape(target_user.first_name))}"
    )
    if reason:
        log_message += f"\n<b>Alasan:</b> {reason}"

    return log_message


@dev_plus
@gloggable
def unbl_user(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)

    if not user_id:
        message.reply_text("Saya ragu itu pengguna.")
        return ""

    if user_id == bot.id:
        message.reply_text("Saya selalu memperhatikan diri saya sendiri.")
        return ""

    try:
        target_user = bot.get_chat(user_id)
    except BadRequest as excp:
        if excp.message == "User not found":
            message.reply_text("Sepertinya saya tidak dapat menemukan pengguna ini.")
            return ""
        raise

    if sql.is_user_blacklisted(user_id):

        sql.unblacklist_user(user_id)
        message.reply_text("*notices user*")
        return f"#UNBLACKLIST\n<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n<b>User:</b> {mention_html(target_user.id, html.escape(target_user.first_name))}"
    message.reply_text("Saya tidak mengabaikan mereka sama sekali!")
    return ""


@dev_plus
def bl_users(update: Update, context: CallbackContext):
    users = []
    bot = context.bot
    for each_user in sql.BLACKLIST_USERS:
        user = bot.get_chat(each_user)
        if reason := sql.get_reason(each_user):
            users.append(
                f"• {mention_html(user.id, html.escape(user.first_name))} :- {reason}",
            )
        else:
            users.append(f"• {mention_html(user.id, html.escape(user.first_name))}")

    message = "<b>Blacklisted Users</b>\n" + (
        "Belum ada yang diabaikan." if not users else "\n".join(users)
    )
    update.effective_message.reply_text(message, parse_mode=ParseMode.HTML)


def __user_info__(user_id):
    is_blacklisted = sql.is_user_blacklisted(user_id)

    text = "Blacklisted: <b>{}</b>"
    if user_id in [777000, 1087968824]:
        return ""
    if user_id == dispatcher.bot.id:
        return ""
    if int(user_id) in DRAGONS + TIGERS + WOLVES:
        return ""
    if is_blacklisted:
        text = text.format("Yes")
        if reason := sql.get_reason(user_id):
            text += f"\nAlasan: <code>{reason}</code>"
    else:
        text = text.format("No")

    return text


BL_HANDLER = CommandHandler("ignore", bl_user, run_async=True)
UNBL_HANDLER = CommandHandler("notice", unbl_user, run_async=True)
BLUSERS_HANDLER = CommandHandler("ignoredlist", bl_users, run_async=True)

dispatcher.add_handler(BL_HANDLER)
dispatcher.add_handler(UNBL_HANDLER)
dispatcher.add_handler(BLUSERS_HANDLER)

__handlers__ = [BL_HANDLER, UNBL_HANDLER, BLUSERS_HANDLER]
