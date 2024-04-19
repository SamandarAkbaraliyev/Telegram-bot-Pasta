from telegram.ext import CallbackContext
from telegram.update import Update
from telegram import ReplyKeyboardMarkup
from django.core.cache import cache
from product.models import Product
from users.models import User
from order.models import Cart
from tgbot.states import CATEGORY_SELECT
from tgbot.handlers.menu.keyboards import make_keyboard_for_categories


def add_to_cart(update: Update, callback: CallbackContext):
    product = cache.get('product')
    u = User.get_user(update, callback)
    cart = Cart.objects.get_or_create(user=u)[0]
    quantity = int(update.message.text)
    Cart.add_item(cart.id, Product.objects.get(title__icontains=product).id, quantity)
    update.message.reply_text(f'{product}dan savatingizga {quantity}ta qo\'shildi!')
    update.message.reply_text(f"Ajoyib tanlov, biron narsa yana buyurtma qilamizmi?",
                              reply_markup=make_keyboard_for_categories())
    return CATEGORY_SELECT
