from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard



router = Router()


available_celebration = ["вне школы", "в школе"]
available_sum_to_pay = ["25", "50", "75"]
available_for_teathers = ["учавствую", "не учавствую"]
available_sum_for_teathers = ["25", "50"]
available_activ = ["/готов", "/не_готов"]



class ChoiceCelebration(StatesGroup):
    choice_celebration = State()
    choice_sum_to_pay = State()
    choice_for_teathers = State()
    choice_sum_for_teathers = State()
    choice_activ = State()


#Хэндлер на команду /Натать_опрос
@router.message(Command('Начать_опрос'))
async def cmd_commenc(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'{name}, организация детского праздника должна быть:',
reply_markup=make_row_keyboard(available_celebration)
)
    await state.set_state(ChoiceCelebration.choice_celebration)


@router.message(ChoiceCelebration.choice_celebration, F.text.in_(available_celebration))
async def celebr_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_celebration=message.text.lower())
    await message.answer(
text='Отлично. Теперь давай определим бюджет праздника',
reply_markup=make_row_keyboard(available_sum_to_pay)
    )
    await state.set_state(ChoiceCelebration.choice_sum_to_pay)




@router.message(ChoiceCelebration.choice_sum_to_pay, F.text.in_(available_sum_to_pay))
async def celebr_for_teathers(message: types.Message, state: FSMContext):

    await message.answer(
text='Следующий вопрос на обсуждении. Планируешь ли ты участие в поздравлении классного руководителя и учителей младшей школы',
reply_markup=make_row_keyboard(available_for_teathers)
    )
    await state.set_state(ChoiceCelebration.choice_for_teathers)


@router.message(ChoiceCelebration.choice_for_teathers, F.text.in_(available_for_teathers))
async def sum_for_teathers(message: types.Message, state: FSMContext):
    await state.update_data(choice_sum_for_teathers=message.text.lower())
    await message.answer(
text='Сумма для поздравления классного руководителя и учителей младшей школы',
reply_markup=make_row_keyboard(available_sum_for_teathers)
)
    await state.set_state(ChoiceCelebration.choice_sum_for_teathers)




@router.message(ChoiceCelebration.choice_for_teathers)
async def chosen_incorrectly2(message: types.Message):
    await message.answer(
'Этого варианта нет среди предложенных. Сделайте свой выбор',
reply_markup=make_row_keyboard(available_for_teathers)
)


@router.message(ChoiceCelebration.choice_sum_for_teathers, F.text.in_(available_sum_for_teathers))
async def sum_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'Подведем итог. Вы выбрали организацию выпускного {user_data.get("chosen_celebration")} на сумму {message.text.lower()}. Буду рада, если примите участие в организации ',
reply_markup=make_row_keyboard(available_activ)
    )
    await state.clear()


@router.message(ChoiceCelebration.choice_sum_to_pay)
async def sum_chosen_incorrectly(message: types.Message):
    await message.answer(
'Этого варианта нет среди предложенных. Сделайте свой выбор',
reply_markup=make_row_keyboard(available_sum_to_pay)
)

@router.message(ChoiceCelebration.choice_sum_for_teathers)
async def sum_chosen_incorrectly2(message: types.Message):
    await message.answer(
'Этого варианта нет среди предложенных. Сделайте свой выбор',
reply_markup=make_row_keyboard(available_sum_for_teathers)
)

@router.message(ChoiceCelebration.choice_celebration)
async def chosen_incorrectly(message: types.Message):
    await message.answer(
'Этого варианта нет среди предложенных. Сделайте свой выбор',
reply_markup=make_row_keyboard(available_celebration)
)


@router.message(ChoiceCelebration.choice_sum_to_pay, F.text.in_(available_sum_to_pay))
async def sum_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'Подведем итог. Вы выбрали организацию выпускного {user_data.get("chosen_celebration")} на сумму {message.text.lower()} рублей. Буду рада, если примите участие в организации ',
reply_markup=make_row_keyboard(available_activ)
    )
    await state.set_state(ChoiceCelebration.finish_choice_celebration)