from firebot import bot
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from firebot.utils import command, remove_plugin, load_module
from var import Var
from pathlib import Path
from firebot import LOAD_PLUG
import sys
import asyncio
import traceback
import os
import firebot.utils
from firebot.events import register


@register(pattern="^.extdl", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    chat = Var.PLUGIN_CHANNEL
    documentss = await borg.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    await event.delete()
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(await borg.get_messages(chat, ids=mxo), "firebot/plugins/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            await borg.send_message(event.chat_id, "Installed Plugin `{}` successfully.".format(os.path.basename(downloaded_file_name)))
        else:
            await borg.send_message(event.chat_id, "Plugin `{}` has been pre-installed and cannot be installed.".format(os.path.basename(downloaded_file_name)))
