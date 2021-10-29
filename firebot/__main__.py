import logging
from pathlib import Path
from sys import argv
import var

import telethon.utils
from telethon import TelegramClient
import os
from var import Var
from firebot import bot
from firebot.Configs import Config
from firebot.utils import load_module, start_assistant

sed = logging.getLogger("firebot")



async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()

plugin_channel = "@FireX_Plugins"
        
  test1 = await client.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)

  for ixo in total_doxx:

       mxo = test1[ixo].id ; await client.download_media(await client.get_messages(cIient, ids=mxo), "ub/modules/")

  ar = glob.glob("firebot/modules/*.py")

  f = len(ar)

  sed.info(f" loading {f} modules it may take 1 minute please wait ")

import glob

path = "firebot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "firebot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    sed.info("firebot And Assistant Bot Have Been Installed Successfully !")
else:
    sed.info("firebot Has Been Installed Sucessfully !")
    sed.info("Hope you will enjoy")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
