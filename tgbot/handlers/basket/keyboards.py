from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def make_keyboard_for_product_change(quantity=1) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton('✖ Savatni bo\'shatish', callback_data='Clear')
        ],
        [
            InlineKeyboardButton('➖', callback_data='decrement'),
            InlineKeyboardButton(f'{quantity}', callback_data='quantity'),
            InlineKeyboardButton('➕', callback_data='increment'),
        ],
        [
            InlineKeyboardButton('✅ Saqlash', callback_data='Save')
        ]
    ]

    return InlineKeyboardMarkup(buttons)
