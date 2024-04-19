from telegram.ext import CallbackContext
from telegram.update import Update
from telegram import ReplyKeyboardMarkup
from product.models import Category, Product
from .keyboards import make_button_for_menu
from tgbot.states import CATEGORY_SELECT, PRODUCT_SELECT, PRODUCT_SELECT_QUANTITY
from tgbot.handlers.onboarding.static_text import BASKET, BACK
from django.core.cache import cache
from .keyboards import make_keyboard_for_categories


def categories(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Quyidagilardan birini tanlang""",
        reply_markup=make_keyboard_for_categories()
    )
    return CATEGORY_SELECT


def product_list(update: Update, callback: CallbackContext):
    category = update.message.text
    if category is None or category == BACK:
        category = cache.get('category')
    cache.set('category', category)
    products = Product.objects.filter(category__title__icontains=category)
    if products:
        buttons = []
        for index in range(0, len(products), 2):
            if index + 1 != len(products):
                buttons.append([products[index].title, products[index + 1].title])
            else:
                buttons.append([products[index].title])
        buttons.append([BACK])
        buttons.insert(0, [BASKET])

        update.message.reply_html("Mahsulotni tanlang", reply_markup=ReplyKeyboardMarkup(buttons))
        return PRODUCT_SELECT
    else:
        update.message.reply_html("Bu Kategoriyada mahsulot topilamdi.\nIltimos Boshqa Kategoriya tanlang",
                                  reply_markup=make_keyboard_for_categories())
        return CATEGORY_SELECT


def product_quantity_select(update: Update, callback: CallbackContext):
    product = Product.objects.get(title__icontains=update.message.text)
    cache.set('product', product)
    update.message.reply_photo(
        photo=open(f'media{product.image.url}', 'rb'),
        caption=f"{product.title}\n\n{product.description}\n\nNarhi: {product.price}"
    )
    update.message.reply_text('Sonini tanlang 👇',
                              reply_markup=ReplyKeyboardMarkup([
                                  [BACK],
                                  [1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9],
                                  [10]
                              ]))
    return PRODUCT_SELECT_QUANTITY


