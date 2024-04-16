from telegram.update import Update
from telegram.ext import CallbackContext, ConversationHandler
from .keyboards import make_button_for_feedback
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start

(FIKR_BILDIRISH,) = range(1)


def feedback(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Quyidagilardan birini tanlang""",
        reply_markup=make_button_for_feedback()
    )
    return FIKR_BILDIRISH


def marking(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Bahoyingiz uchun raxmat""",
        reply_markup=make_keyboard_for_start()
    )
    return ConversationHandler.END
