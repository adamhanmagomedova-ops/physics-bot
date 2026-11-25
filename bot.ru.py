import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Вставьте сюда ваш токен от @BotFather
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование, чтобы видеть ошибки в консоли
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Словарь с формулами (можно легко дополнять)
FORMULAS = {
"Механика": (
"⚙️ Основные формулы механики:\n\n"
"• Равномерное движение: S = v · t\n"
"• Ускорение: a = (v - v₀) / t\n"
"• Второй закон Ньютона: F = m · a\n"
"• Сила тяжести: F = m · g (g ≈ 9.8 м/с²)\n"
"• Кинетическая энергия: Eₖ = (m · v²) / 2\n"
"• Потенциальная энергия: Eₚ = m · g · h"
),
"Термодинамика": (
"🔥 Основные формулы термодинамики:\n\n"
"• Количество теплоты при нагревании: Q = c · m · Δt\n"
"• Уравнение Менделеева-Клапейрона: P · V = ν · R · T\n"
"• Первый закон термодинамики: Q = ΔU + A\n"
"• КПД теплового двигателя: η = (A / Q₁) · 100%"
),
"Электричество": (
"⚡ Основные формулы электричества:\n\n"
"• Сила тока: I = q / t\n"
"• Закон Ома для участка цепи: I = U / R\n"
"• Мощность тока: P = U · I\n"
"• Закон Джоуля-Ленца: Q = I² · R · t\n"
"• Закон Кулона: F = k · (|q₁| · |q₂|) / r²"
),
"Оптика": (
"🔍 Основные формулы оптики:\n\n"
"• Формула тонкой линзы: 1 / F = 1 / d + 1 / f\n"
"• Оптическая сила линзы: D = 1 / F\n"
"• Закон преломления света: sin(α) / sin(β) = n₂ / n₁"
)
}

# Создаем клавиатуру с кнопками
keyboard = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="Механика"), KeyboardButton(text="Термодинамика")],
[KeyboardButton(text="Электричество"), KeyboardButton(text="Оптика")]
],
resize_keyboard=True # Делает кнопки компактными
)

# Обработка команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
"Привет! Я помогу тебе вспомнить базовые формулы по физике.\n"
"Выбери нужный раздел на клавиатуре ниже 👇",
reply_markup=keyboard
)

# Обработка нажатий на кнопки разделов
@dp.message(F.text.in_(FORMULAS.keys()))
async def send_formulas(message: types.Message):
    topic = message.text
    await message.answer(FORMULAS[topic], parse_mode="Markdown")

# Обработка любого другого текста
@dp.message()
async def unknown_message(message: types.Message):
    await message.answer("Пожалуйста, выбери раздел с помощью кнопок ниже 👇", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())
