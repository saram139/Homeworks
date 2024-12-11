from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions2 import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()
users = get_all_products()

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start")],
        [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
        [KeyboardButton(text="Купить")],
        [KeyboardButton(text="Регистрация")],
    ],
    resize_keyboard=True,
)

add_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мужчина", callback_data="male"),
            InlineKeyboardButton(text="Женщина", callback_data="female"),
        ]
    ]
)

il_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Рассчитать норму калорий", callback_data="calories"
            ),
            InlineKeyboardButton(text="Формулы расчета", callback_data="formulas"),
        ]
    ]
)

product_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Че-нибудь", callback_data="product_buying"),
            InlineKeyboardButton(text="Пофигин", callback_data="product_buying"),
            InlineKeyboardButton(text="Смехозан", callback_data="product_buying"),
            InlineKeyboardButton(text="Счастье", callback_data="product_buying"),
        ]
    ]
)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит): ")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer("Введите свой email: ")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя. ")
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст: ")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data(["username", "email", "age"])
    add_user(data["username"], data["email"], int(data["age"]))
    await message.answer("Регистрация прошла успешно")
    await state.finish()


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer(
        "Для мужчин:\n10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5"
    )
    await call.message.answer(
        "Для женщин:\n10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=il_menu)


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью.", reply_markup=start_menu
    )


@dp.message_handler(text="Информация")
async def info(message):
    await message.answer(
        "Я бот помогающий твоему здоровью. Я могу помочь тебе рассчитать твою норму калорий, а так же я могу предложить тебе купить полезные продукты. "
    )


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for product in users:

        with open(f"images/{product[0]}.png", "rb") as img:
            await message.answer(
                f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
            )
            await message.answer_photo(img)

    await message.answer("Выберите продукт:", reply_markup=product_menu)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст.")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост.")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес.")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Выберите свой пол.", reply_markup=add_menu)
    await UserState.gender.set()


@dp.callback_query_handler(text="male", state=UserState.gender)
async def send_male_calories(call, state):
    await send_calories(call, state, "male")


@dp.callback_query_handler(text="female", state=UserState.gender)
async def send_female_calories(call, state):
    await send_calories(call, state, "female")


async def send_calories(call, state, gender):
    await state.update_data(gender=gender)
    data = await state.get_data()
    if gender == "male":
        calories = (
            10 * float(data["weight"])
            + 6.25 * float(data["growth"])
            - 5 * float(data["age"])
            + 5
        )
    else:
        calories = (
            10 * float(data["weight"])
            + 6.25 * float(data["growth"])
            - 5 * float(data["age"])
            - 161
        )
    await call.message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
