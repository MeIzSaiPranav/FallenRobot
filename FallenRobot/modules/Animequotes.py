import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import FallenRobot.modules.animequotes_strings as animequotes_strings
from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler
from FallenRobot.modules.helper_funcs.chat_status import (is_user_admin)
from FallenRobot.modules.helper_funcs.extraction import extract_user

@run_async
def animequote(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(animequotes_strings.QUOTES_IMG))

__help__ = """
 • `/animequote `*:* Motivational Anime quotes
 
"""
ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequote", animequote)

dispatcher.add_handler(ANIMEQUOTE_HANDLER)

__mod_name__ = "AnimeQuotes"
__command_list__ = [
    "animequotes"
]
__handlers__ = [
    ANIMEQUOTES_HANDLER
]
