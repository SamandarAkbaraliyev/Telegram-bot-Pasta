from telegram.update import Update
from telegram.ext import CallbackContext


def basket(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Sizning savatingiz bo'sh""")

def about_order(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🇮🇹 Italiyani yetkazib berish!
🍝 Italiyancha pasta korobochkalarda!
⏰ С 11:00 до 01:00 
🛵 Hoziroq buyurtma bering!

*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin""",
    )
