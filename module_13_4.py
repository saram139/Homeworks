from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Введите свой пол (м/ж):")
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    if data["gender"] == "м":
        calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    else:
        calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
