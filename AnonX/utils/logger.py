from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Pʀɪᴠᴀᴛᴇ Cʜᴀᴛ"
        logger_text = f"""
**「Uɴᴋ  𓆩✘𓆪 Mᴜsɪᴄ」 Pʟᴀʏ Lᴏɢɢᴇʀ**

**Cʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**Usᴇʀ:** {message.from_user.mention}
**Usᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
**Iᴅ:** `{message.from_user.id}`
**Cʜᴀᴛ Lɪɴᴋ:** {chatusername}

**Sᴇᴀʀᴄʜᴇᴅ Fᴏʀ:** {message.text}

**Sᴛʀᴇᴀᴍ Tʏᴩᴇ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
