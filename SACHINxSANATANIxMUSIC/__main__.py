import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from SACHINxSANATANIxMUSIC import LOGGER, app, userbot
from SACHINxSANATANIxMUSIC.core.call import DAXX
from SACHINxSANATANIxMUSIC.misc import sudo
from SACHINxSANATANIxMUSIC.plugins import ALL_MODULES
from SACHINxSANATANIxMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗡𝗢𝗧 𝗙𝗜𝗟𝗟𝗘𝗗 || 𝗣𝗟𝗘𝗔𝗦𝗘 𝗙𝗜𝗟𝗟 𝗔 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗦𝗘𝗦𝗦𝗜𝗢𝗡")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SACHINxSANATANIxMUSIC.plugins" + all_module)
    LOGGER("SACHINxSANATANIxMUSIC.plugins").info("𝗔𝗹𝗹 𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 𝗟𝗢𝗔𝗗𝗘𝗗 𝗕𝗢𝗦𝗦")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("SACHINxSANATANIxMUSIC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("SACHINxSANATANIxMUSIC").info(
        "𝗦𝗔𝗖𝗛𝗜𝗡 \n 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 \n 𝗠𝗨𝗦𝗜𝗖"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SACHINxSANATANIxMUSIC").info("𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 𝗜𝗦 𝗛𝗘𝗥𝗘")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
