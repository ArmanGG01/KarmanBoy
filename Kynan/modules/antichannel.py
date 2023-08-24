import html

from telegram.ext.filters import Filters
from telegram import Update, message, ParseMode
from telegram.ext import CallbackContext

from Kynan.modules.helper_funcs.decorators import Kynancmd, Kynanmsg
from Kynan.modules.helper_funcs.channel_mode import user_admin, AdminPerms
from Kynan.modules.sql.antichannel_sql import antichannel_status, disable_antichannel, enable_antichannel

@Kynancmd(command="antich", group=100)
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
def set_antichannel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            enable_antichannel(chat.id)
            message.reply_html(f"AntiChannel diaktifkan di {html.escape(chat.title)}")
        elif s in ["off", "no"]:
            disable_antichannel(chat.id)
            message.reply_html(f"Nonaktifkan antichannel di {html.escape(chat.title)}")
        else:
            message.reply_text(f"Argumen tidak dikenal {s}")
        return
    message.reply_html(
        f"Pengaturan antichannel saat ini {antichannel_status(chat.id)} in {html.escape(chat.title)}"
    )

@Kynanmsg(Filters.chat_type.groups, group=110)
def eliminate_channel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    bot = context.bot
    if not antichannel_status(chat.id):
        return
    if message.sender_chat and message.sender_chat.type == "channel" and not message.is_automatic_forward:
        message.delete()
        sender_chat = message.sender_chat
        bot.ban_chat_sender_chat(sender_chat_id=sender_chat.id, chat_id=chat.id)
        
__help__ = """
    ⚠️ PERINGATAN ⚠️
➣ *JIKA ANDA MENGGUNAKAN MODE INI, HASILNYA ADA DI GROUP SELAMANYA ANDA TIDAK BISA CHAT MENGGUNAKAN CHANNEL*
Mode Anti Saluran adalah mode untuk secara otomatis melarang pengguna yang mengobrol menggunakan Channel. 
Perintah ini hanya dapat digunakan oleh *Admins*.
ᐉ /antich <'on'/'yes'> *:* mengaktifkan mode anti-channel
ᐉ /antich <'off'/'no'> *:* mode anti-channel dinonaktifkan
"""

__mod_name__ = "Anti-Channel"
