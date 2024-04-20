from telegram.update import Update
from telegram.ext import CallbackContext
from users.models import User
from order.models import CartItem, Cart
from tgbot.handlers.onboarding.static_text import MAIN_MENU, CLEAR, ORDER
from telegram import ReplyKeyboardMarkup


def basket(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    try:
        cart = Cart.objects.get(user=u)
    except Cart.DoesNotExist:
        cart = None
    if cart is None:
        update.message.reply_text(
            """Sizning savatingiz bo'sh""")
    else:
        cart_items = CartItem.objects.filter(cart=cart)
        text = ""
        buttons = [[MAIN_MENU, CLEAR]]
        for index in range(len(cart_items)):
            text += (f"{index + 1}. <b>{cart_items[index].product.title}</b>\n"
                     f"{cart_items[index].quantity} x {cart_items[index].product.price} = <b>{cart_items[index].subtotal}</b>\n\n")
            buttons.append([f'✏ {cart_items[index].product.title}'])
        total_sum = sum(cart_item.subtotal for cart_item in cart_items)

        buttons.append([ORDER])
        update.message.reply_html(
            f"""Savatingiz:\n\n{text}<b>Jami: {total_sum}</b>""", reply_markup=ReplyKeyboardMarkup(buttons))


def about_order(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🇮🇹 Italiyani yetkazib berish!
🍝 Italiyancha pasta korobochkalarda!
⏰ С 11:00 до 01:00 
🛵 Hoziroq buyurtma bering!

*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin""",
    )
