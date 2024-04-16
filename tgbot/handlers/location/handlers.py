import telegram
from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.location.static_text import share_location, thanks_for_location
from tgbot.handlers.location.keyboards import send_location_keyboard
from users.models import User, Location


def ask_for_location(update: Update, context: CallbackContext) -> None:
    """ Entered /ask_location command"""
    u = User.get_user(update, context)

    context.bot.send_message(
        chat_id=u.user_id,
        text=share_location,
        reply_markup=send_location_keyboard()
    )


def location_handler(update: Update, context: CallbackContext) -> None:
    # receiving user's location
    u = User.get_user(update, context)
    lat, lon = update.message.location.latitude, update.message.location.longitude
    Location.objects.create(user=u, latitude=lat, longitude=lon)

    update.message.reply_text(
        thanks_for_location,
        reply_markup=telegram.ReplyKeyboardRemove(),
    )


def cafe_location(update: Update, context: CallbackContext) -> int:
    update.message.reply_location(latitude=41.312082, longitude=69.292853)

    update.message.reply_text(
        """🤩 Pastani kafeimizga kelib to'g'ridan-to'g'ri skovorodkadan ta'tib ko'ring - aynan shu uchun ham shaharning markazida joy ochdik, manzil Ц-1'da Ecopark va 64 maktab yonida

📌 Ish tartibi: du - pa 11:00 - 23:00 / ju 14:00 - 23:00 / sha - yak 11:00 - 23:00

Operator bilan aloqa 👉 @pastarobot""",
        # reply_markup=ReplyKeyboardMarkup(
        #     MAIN_KEYBOARD,
        #     one_time_keyboard=False,
        #     input_field_placeholder="Quyidagilardan birini tanlang",
        )
