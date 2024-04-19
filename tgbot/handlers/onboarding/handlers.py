import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

import tgbot.states
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from users.models import User
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command, make_keyboard_for_start


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text,
                              reply_markup=make_keyboard_for_start_command())


def secret_level(update: Update, context: CallbackContext) -> None:
    """
    Processes the 'secret_level_button_text' callback after the /start command.

    Parameters:
    - update (Update): The incoming update from Telegram.
    - context (CallbackContext): The current context object.

    Returns:
    - None: This function does not return any value.

    Raises:
    - None: This function does not raise any exceptions.

    Usage:
    - This function is called when a user presses the 'secret_level_button_text' after the /start command.
    """
    # callback_data: SECRET_LEVEL_BUTTON variable from manage_data.py
    user_id = extract_user_data_from_update(update)['user_id']
    text = static_text.unlock_secret_room.format(
        user_count=User.objects.count(),
        active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
    )

    context.bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=update.callback_query.message.message_id,
        parse_mode=ParseMode.HTML
    )


def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""

    update.message.reply_text(
        f"CIAO {update.effective_user.first_name}! Kichik Italiyaga xush kelibsiz!\n\nNima buyurtma qilamiz?",
        reply_markup=make_keyboard_for_start()
    )
    return tgbot.states.MAIN_MENU_STATE


def contact(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        f"Buyurtma va boshqa savollar bo'yicha javob olish uchun https://t.me/pastarobot'ga murojaat qiling, barchasiga javob beramiz :)"
    )

