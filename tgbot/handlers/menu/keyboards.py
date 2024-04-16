from telegram import KeyboardButton, ReplyKeyboardMarkup
from tgbot.handlers.onboarding.static_text import MAIN_MENU, BASKET
from product.models import Category


def make_button_for_menu() -> ReplyKeyboardMarkup:
    keyboard = [
        [BASKET],
        ['Pasta', "Qo'shimchalar"],
        ['Salatlar', "🆕 Taomlar"],
        ['Sovuq ichimliklar', '🆕 Tomato seti'],
        ['2 Kishilik set', '🆕 Ravioli ikki kishilik'],
        ['🔥 Kombo 4 kishilik', '🤩KIDS MENU'],
        [MAIN_MENU]
    ]

    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=False,
                               input_field_placeholder='Quyidagilardan birini tanlang')
