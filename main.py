import asyncio
import os
from dotenv import load_dotenv
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, URLInputFile
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello! I'm bot-organizer. I will help you to organize your life."
    )


@dp.message(Command("weather"))
async def weather(message: Message):
    response = requests.get("https://wttr.in/moscow?format=%f")
    response = int(response.text[:-2])
    photo_url = "https://wttr.in/moscow_M.png"
    photo = URLInputFile(photo_url, filename="weather.png")
    await message.answer_photo(
        photo=photo, caption="Weather in Moscow", parse_mode="HTML"
    )
    if response >= 13:
        await message.answer("Wear a t-shirt and shorts/light pants")
    elif response < 13 and response > 5:
        await message.answer("Wear a sweatshirt/jacket and light pants/trousers")
    elif response <= 5 and response > -1:
        await message.answer("Wear a jacket/coat and pants")
    elif response <= -1 and response > -7:
        await message.answer("Wear a coat and (warm) pants")
    elif response <= -7 and response > -12:
        await message.answer("Wear a coat and warm pants")
    elif response <= -12:
        await message.answer("It's below -11°C outside, dress warmly")

class WeatherStates(StatesGroup):
    waiting_for_city = State()

@dp.message(Command("weather_city"))
async def weather_city(message: Message, state: FSMContext):
    await message.answer("Please enter a city name")
    await state.set_state(WeatherStates.waiting_for_city)

@dp.message(WeatherStates.waiting_for_city)
async def get_weather_by_city(message: Message, state: FSMContext):
    city = message.text
    response = requests.get(f"https://wttr.in/{city}?format=%f")
    response = int(response.text[:-2])
    photo_url = f"https://wttr.in/{city}_M.png"
    photo = URLInputFile(photo_url, filename="weather.png")
    await message.answer_photo(
        photo=photo, caption=f"Weather in {city}", parse_mode="HTML"
    )
    if response >= 13:
        await message.answer("Wear a t-shirt and shorts/light pants")
    elif response < 13 and response > 5:
        await message.answer("Wear a sweatshirt/jacket and light pants/trousers")
    elif response <= 5 and response > -1:
        await message.answer("Wear a jacket/coat and pants")
    elif response <= -1 and response > -7:
        await message.answer("Wear a coat and (warm) pants")
    elif response <= -7 and response > -12:
        await message.answer("Wear a coat and warm pants")
    elif response <= -12:
        await message.answer("It's below -11°C outside, dress warmly")

class TimerStates(StatesGroup):
    waiting_for_time = State()

@dp.message(Command("timer"))
async def timer_command(message: Message, state: FSMContext):
    await message.answer('Ok, for which time should I start the timer? (format: h:m:s)')
    await state.set_state(TimerStates.waiting_for_time)

@dp.message(TimerStates.waiting_for_time)
async def process_timer_time(message: Message, state: FSMContext):
    user_time = message.text
    hours, minutes, seconds = map(int, user_time.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds    
    await message.answer("Timer is set")
    await asyncio.sleep(total_seconds)
    await message.answer('End of the timer!')
    await state.clear()

class PomodoroStates(StatesGroup):
	continue_pomodoro = State()

@dp.message(Command("pomodoro"))
async def pomodoro(message: Message, state: FSMContext):
    c = 0
    while True:
        await message.answer('Have a rest')
        if c % 4 == 0 and c != 0:
            await asyncio.sleep(900)
        else:
            await asyncio.sleep(300)
        await message.answer("Pomodoro has started. Be productive!")
        await asyncio.sleep(1500)
        await message.answer('Pomodoro just ended. Should we continue?')
        c += 1
        await state.set_state(PomodoroStates.continue_pomodoro)

@dp.message(PomodoroStates.continue_pomodoro)
async def conntinue_p(message: Message, state: FSMContext):
	if message.text == "Yes":
		await state.clear()
		await pomodoro(message, state)
	else:
		await state.clear()
		await message.answer('Good job!')



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
