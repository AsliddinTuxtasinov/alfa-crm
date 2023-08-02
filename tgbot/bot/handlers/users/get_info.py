import typing

from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from tgbot.bot.loader import dp


@dp.message_handler(Command("me"))
async def get_info(message: types.Message):
    # Your code to process the /me command goes here
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    response_text = f"Your user ID: {user_id}\nYour name: {user_name}"

    # Reply to the user
    await message.reply(response_text)
