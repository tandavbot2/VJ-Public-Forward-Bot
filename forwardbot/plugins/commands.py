# Import necessary components
from forwardbot import Config, bot
from forwardbot.utils import forwardbot_cmd, is_sudo
from ethon.mystarts import start_srb

# Global variables
MessageCount = 0
BOT_STATUS = "0"
status = set(int(x) for x in (BOT_STATUS).split())
help_msg = Config.HELP_MSG
sudo_users = Config.SUDO_USERS

@forwardbot_cmd("start", is_args=False)
async def start(event):
    text = f"**ʜɪ ɪ ᴀᴍ ᴀ ᴘᴜʙʟɪᴄ ғᴏʀᴡᴀʀᴅᴇʀ ʙᴏᴛ.** \n**ᴜsɪɴɢ ᴍᴇ ʏᴏᴜ ᴄᴀɴ ғᴏʀᴡᴀʀᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴇᴀsɪʟʏ** \n**ᴍʏ ᴀᴄᴄᴏᴜɴᴛ ɢᴇᴛ ʙᴀɴ ᴀɴʏᴛɪᴍᴇ ᴀɴᴅ ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ, sᴏ ᴊᴏɪɴ ᴏᴜʀ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ](https://t.me/vj_botz) ғᴏʀ ɴᴇᴡ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇ.**\n**/help ғᴏʀ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʙᴏᴛ**"
    await start_srb(event, text)

@forwardbot_cmd("help", is_args=False)
async def handler(event):
    await event.respond(help_msg)

@forwardbot_cmd("test", is_args=False)
async def handler(event):
    await event.respond(bot.owner)

@forwardbot_cmd("admin", is_args=False)
async def handler(event):
    if str(event.sender_id) in sudo_users:
        await event.respond("You are an admin")
    else:
        await event.respond("You are not an admin")
