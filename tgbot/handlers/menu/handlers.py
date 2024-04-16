from telegram.ext import CallbackContext
from telegram.update import Update
from .keyboards import make_button_for_menu
from .static_text import category_keyboard_button


def menu(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Quyidagilardan birini tanlang""",
        reply_markup=category_keyboard_button
    )
