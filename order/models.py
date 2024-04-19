from django.db import models
from users.models import User
from django.shortcuts import get_object_or_404


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def add_item(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart_id=self, product_id=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        return cart_item

    def remove_item(self, cart_item_id):
        cart_item = get_object_or_404(CartItem, pk=cart_item_id, cart=self)
        cart_item.delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    @property
    def subtotal(self):
        return self.quantity * self.product.price
