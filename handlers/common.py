from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import kb1



router = Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


#Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Спасибо. До свидания, {name}', reply_markup=types.ReplyKeyboardRemove())

# Хэндлер на команду /готов
@router.message(Command('готов'))
async def cmd_ok(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Отлично. {name}, спасибо за желание учавствовать в организации праздника.', reply_markup=types.ReplyKeyboardRemove())

# Хэндлер на команду /не_готов
@router.message(Command('не_готов'))
async def cmd_no(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Ваши ответы приняты. Спасибо. До свидания, {name}', reply_markup=types.ReplyKeyboardRemove())

#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет, {name}. Если ты видишь этого бота, значит твой ребенок – ученик 4 класса СШ №131')
        await message.answer(f'Скоро конец учебного года. Для организации выпускного вечера нашим детям пройдите мини - опрос', reply_markup=kb1)
    elif 'здравствуй' in msg_user:
        await message.answer(f'Здравствуй, {name}. Если ты видишь этого бота, значит твой ребенок – ученик 4 класса СШ №131')
        await message.answer(
            f'Скоро конец учебного года. Для организации выпускного вечера нашим детям пройдите мини - опрос',
            reply_markup=kb1)
    elif 'hi' in msg_user:
        await message.answer(f'Hi, {name}. Если ты видишь этого бота, значит твой ребенок – ученик 4 класса СШ №131')
        await message.answer(
        f'Скоро конец учебного года. Для организации выпускного вечера нашим детям пройдите мини - опрос',
        reply_markup=kb1)
    elif 'да' in msg_user:
        await message.answer(f'Добрый день, {name}. Если ты видишь этого бота, значит твой ребенок – ученик 4 класса СШ №131')
        await message.answer(
            f'Скоро конец учебного года. Для организации выпускного вечера нашим детям пройдите мини - опрос',
            reply_markup=kb1)
    else:
        await message.answer(
        f'Если информация, указанная ранее не относится к Вам и Вашему ребенку, проигнорируйте данное сообщение')
