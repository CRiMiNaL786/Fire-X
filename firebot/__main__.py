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

#####################################

async def a():

  sed.info("Connecting...") ; 

  o = o2 = o3 = o4 = ""

  la = 0

  try:

     await bot.start() ; sed.info("client connected") ; o = "Client1"

  except:

    sed.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)

  if client2:

      try:

        await bot2.start() ; sed.info("client2 connected") ; o2 = ", Client2"

      except:

         sed.info("client2 Session string Wrong/Expired Please add new string session or delete var S2") ; quit(1)

  if client3:

      try:

         await bot3.start() ; sed.info("client3 connected") ; o3 = ", Client3"

      except:

         sed.info("client3 Session string Wrong/Expired Please add new string  or delete var S3 ") ; quit(1)

  
  test1 = await bot.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) 

  for ixo in total_doxx:

       mxo = test1[ixo].id ; await client.download_media(await client.get_messages(cIient, ids=mxo), "firebot/modules/")

  ar = glob.glob("firebot/modules/*.py")

  f = len(ar)

  sed.info(f" loading {f} modules it may take 1 minute please wait")

  for i in ar:

     br = os.path.basename(i)

     cr = (os.path.splitext(br)[0])

     load_module(f"firebot.modules.{cr}")

     la += 1

     sed.info(f" loaded {la}/{f} modules by channel #mrunal ")  

  #os.system("rm userbot/modules/*.py") ; 

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
