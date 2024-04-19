from telegram.ext import CallbackContext
from telegram.update import Update
from telegram import ReplyKeyboardMarkup
from product.models import Category
from .keyboards import make_button_for_menu
from tgbot.states import CATEGORY_SELECT
from tgbot.handlers.onboarding.static_text import BASKET, BACK


def categories(update: Update, context: CallbackContext) -> int:
    categories_list = Category.objects.all()
    buttons = []
    for index in range(0, len(categories_list), 2):
        if index + 1 != len(categories_list):
            print(index)
            buttons.append([categories_list[index].title, categories_list[index + 1].title])
        else:
            buttons.append([categories_list[index].title])
    buttons.append([BACK, BASKET])
    update.message.reply_text(
        """Quyidagilardan birini tanlang""",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )
    return CATEGORY_SELECT
