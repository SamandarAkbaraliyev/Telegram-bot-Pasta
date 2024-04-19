from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding import static_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(static_text.github_button_text, url="https://github.com/ohld/django-telegram-bot"),
            InlineKeyboardButton(static_text.secret_level_button_text, callback_data=f'{SECRET_LEVEL_BUTTON}')
        ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_start() -> ReplyKeyboardMarkup:
    buttons = [
        [
            static_text.CATEGORY_SELECT,
            static_text.BASKET
        ],
        [
            static_text.LOCATION,
            static_text.ABOUT_ORDER
        ],
        [
            static_text.FEEDBACK,
            static_text.CONTACT
        ],
        [
            static_text.SETTINGS
        ],
    ]

    return ReplyKeyboardMarkup(buttons, one_time_keyboard=False,
                               input_field_placeholder='Quyidagilardan birini tanlang')
