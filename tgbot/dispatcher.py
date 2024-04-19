"""
    Telegram event handlers
"""
from telegram.ext import (
    Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler, ConversationHandler
)

from dtb.settings import DEBUG
from tgbot.handlers.broadcast_message.manage_data import CONFIRM_DECLINE_BROADCAST
from tgbot.handlers.broadcast_message.static_text import broadcast_command
from tgbot.handlers.feedback.handlers import FIKR_BILDIRISH
from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON

from tgbot.handlers.utils import files, error
from tgbot.handlers.admin import handlers as admin_handlers
from tgbot.handlers.location import handlers as location_handlers
from tgbot.handlers.onboarding import handlers as onboarding_handlers
from tgbot.handlers.menu import handlers as menu_handlers
from tgbot.handlers.broadcast_message import handlers as broadcast_handlers
from tgbot.main import bot
from tgbot.handlers.order import handlers as order_handlers
from tgbot.handlers.onboarding import static_text as onboarding_static_text
from tgbot.handlers.basket.handlers import basket, about_order
from tgbot.handlers.feedback.handlers import feedback, marking
from tgbot import states


def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """
    # onboarding
    dp.add_handler(MessageHandler(Filters.text(onboarding_static_text.CONTACT), onboarding_handlers.contact))

    # admin commands
    dp.add_handler(CommandHandler("admin", admin_handlers.admin))
    dp.add_handler(CommandHandler("stats", admin_handlers.stats))
    dp.add_handler(CommandHandler('export_users', admin_handlers.export_users))

    # location
    dp.add_handler(CommandHandler("ask_location", location_handlers.ask_for_location))
    dp.add_handler(MessageHandler(Filters.location, location_handlers.location_handler))
    dp.add_handler(MessageHandler(Filters.text(onboarding_static_text.LOCATION), location_handlers.cafe_location))

    # secret level
    dp.add_handler(CallbackQueryHandler(onboarding_handlers.secret_level, pattern=f"^{SECRET_LEVEL_BUTTON}"))

    # broadcast message
    dp.add_handler(
        MessageHandler(Filters.regex(rf'^{broadcast_command}(/s)?.*'),
                       broadcast_handlers.broadcast_command_with_message)
    )
    dp.add_handler(
        CallbackQueryHandler(broadcast_handlers.broadcast_decision_handler, pattern=f"^{CONFIRM_DECLINE_BROADCAST}")
    )

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', onboarding_handlers.start),
            MessageHandler(Filters.text, onboarding_handlers.start),
        ],
        states={
            states.MAIN_MENU_STATE: [
                MessageHandler(Filters.text(onboarding_static_text.FEEDBACK), feedback),
                MessageHandler(Filters.text(onboarding_static_text.BASKET), basket),
                MessageHandler(Filters.text(onboarding_static_text.ABOUT_ORDER), about_order),
                MessageHandler(Filters.text(onboarding_static_text.CONTACT), onboarding_handlers.contact),
                MessageHandler(Filters.text(onboarding_static_text.CATEGORY_SELECT), menu_handlers.categories),
                MessageHandler(Filters.text, onboarding_handlers.start)
            ],
            states.FIKR_BILDIRISH: [
                MessageHandler(Filters.regex(
                    '^(😊Hammasi yoqdi ❤️|☺️Yaxshi ⭐️⭐️⭐️⭐️|😐 Yoqmadi ⭐️⭐️⭐️|☹️ Yomon ⭐️⭐️|😤 Juda yomon👎🏻)$'), marking)
            ],
            states.CATEGORY_SELECT: [
                MessageHandler(Filters.text(onboarding_static_text.BASKET), basket),
                MessageHandler(Filters.text(onboarding_static_text.BACK), onboarding_handlers.start),
                MessageHandler(Filters.text, menu_handlers.product_list),
            ],
            states.PRODUCT_SELECT: [
                MessageHandler(Filters.text(onboarding_static_text.BACK), menu_handlers.categories),
                MessageHandler(Filters.text(onboarding_static_text.BASKET), basket),
                MessageHandler(Filters.text, menu_handlers.product_quantity_select),
            ],
            states.PRODUCT_SELECT_QUANTITY: [
                MessageHandler(Filters.text(onboarding_static_text.BACK), menu_handlers.product_list),
                MessageHandler(Filters.text(onboarding_static_text.BASKET), basket),
                MessageHandler(Filters.text, order_handlers.add_to_cart),
            ]
        },
        fallbacks=[
            CommandHandler('start', onboarding_handlers.start),
            # MessageHandler(Filters.text, onboarding_handlers.start),
        ]
    )
    # menu
    # dp.add_handler(MessageHandler(Filters.text(onboarding_static_text.MENU), menu_handlers.menu))

    # files
    dp.add_handler(MessageHandler(
        Filters.animation, files.show_file_id,
    ))

    # handling errors
    dp.add_error_handler(error.send_stacktrace_to_tg_chat)

    dp.add_handler(conv_handler)

    dp.add_handler(MessageHandler(Filters.text(onboarding_static_text.MAIN_MENU), onboarding_handlers.start))

    # EXAMPLES FOR HANDLERS
    # dp.add_handler(MessageHandler(Filters.text, <function_handler>))
    # dp.add_handler(MessageHandler(
    #     Filters.document, <function_handler>,
    # ))
    # dp.add_handler(CallbackQueryHandler(<function_handler>, pattern="^r\d+_\d+"))
    # dp.add_handler(MessageHandler(
    #     Filters.chat(chat_id=int(TELEGRAM_FILESTORAGE_ID)),
    #     # & Filters.forwarded & (Filters.photo | Filters.video | Filters.animation),
    #     <function_handler>,
    # ))

    return dp


n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))
