import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '7998241772:AAGkLSYeR1waJOfJyL848t_iFZNRX8r_6tg'
CHANNEL_ID = '@korean_helper'

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        ["📄 Визы", "🏦 Банки"],
        ["🆔 ID карта", "🎓 Учёба / Т.Б."],
        ["⚖️ Штрафы", "🧾 Налоги"],
        ["💵 Зарплата", "🏡 Жильё"],
        ["📋 Кредиты", "📱 Полезные приложения"],
        ["📞 Позвать оператора"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot
    member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
    if member.status in ['member', 'creator', 'administrator']:
        await update.message.reply_text(
            "✅ Спасибо за подписку!"

Выберите категорию 👇",
            reply_markup=main_keyboard
        )
    else:
        await update.message.reply_text(
            "❗ Для начала подпишись на канал: https://t.me/korean_helper и нажми /start"
        )

from telegram.ext import ContextTypes

banks_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        ["1️⃣ Как открыть счёт", "2️⃣ Лимиты"],
        ["3️⃣ Перевод между странами", "4️⃣ Перевод в Южную Корею"],
        ["5️⃣ Какой банк выбрать?", "6️⃣ Назад"]
    ],
    resize_keyboard=True
)

bank_answers = {
    "1️⃣ Как открыть счёт": "Чтобы открыть счёт нужно: ID Card, справка с работы/договор аренды жилья, паспорт.",
    "2️⃣ Лимиты": "Лимиты начинаются от 300.000₩ до 1.000.000₩ в день.",
    "3️⃣ Перевод между странами": "Для перевода на родину используйте GMoney/Hanpass/e9Pay.",
    "4️⃣ Перевод в Южную Корею": "Используйте Золотую Корону + GMoney/Hanpass.",
    "5️⃣ Какой банк выбрать?": "В Hana Bank можно открыть счёт без ID карты, с загранпаспортом и удостоверением своей страны!",
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🏦 Банки":
        await update.message.reply_text("Выберите нужный пункт 👇", reply_markup=banks_keyboard)
        context.user_data["state"] = "banks"
    elif context.user_data.get("state") == "banks":
        answer = bank_answers.get(text)
        if answer:
            await update.message.reply_text(answer)
        else:
            await update.message.reply_text("Выбери пункт из меню 👇", reply_markup=banks_keyboard)
    else:
        await update.message.reply_text("Выбери категорию или нажми /start", reply_markup=main_keyboard)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
