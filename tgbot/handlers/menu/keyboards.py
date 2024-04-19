from telegram import KeyboardButton, ReplyKeyboardMarkup
from tgbot.handlers.onboarding.static_text import MAIN_MENU, BASKET, BACK
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


def make_keyboard_for_categories():
    categories_list = Category.objects.all()
    buttons = []
    for index in range(0, len(categories_list), 2):
        if index + 1 != len(categories_list):
            buttons.append([categories_list[index].title, categories_list[index + 1].title])
        else:
            buttons.append([categories_list[index].title])
    buttons.append([BACK, BASKET])
    return ReplyKeyboardMarkup(buttons, one_time_keyboard=False,
                               input_field_placeholder='Quyidagilardan birini tanlang')