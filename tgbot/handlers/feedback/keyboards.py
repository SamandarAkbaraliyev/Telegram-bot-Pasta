from telegram import KeyboardButton, ReplyKeyboardMarkup
from tgbot.handlers.onboarding.static_text import MAIN_MENU


def make_button_for_feedback() -> ReplyKeyboardMarkup:
    keyboard = [
        ['😊Hammasi yoqdi ❤️'],
        ['☺️Yaxshi ⭐️⭐️⭐️⭐️'],
        ['😐 Yoqmadi ⭐️⭐️⭐️'],
        ['☹️ Yomon ⭐️⭐️'],
        ['😤 Juda yomon👎🏻'],
        [MAIN_MENU]
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=False,
                               input_field_placeholder='Quyidagilardan birini tanlang')
