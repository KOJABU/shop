from decimal import Decimal
from django.conf import settings
from main.models import Catalog


class Cart(object):
    def __init__(self, request):
        """"
        
        Инициализируем корзину
        :param request:
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем пустую корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзинке и получаем товары из базы дынных 
        :return генеретор товаров
        """
        product_ids = self.cart.keys()
        #получаем товары и добавляем их в козину
        products = Catalog.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        :return: int
        """
        #можно сделать обычным циклом
        # a = int() 
        # for item in self.cart.values():
        #     a +=item['quantity']
        # return a
        return sum(item['quantity'] for item in self.cart.values())
    
    def add(self, product, quantity = 1, update_quantity = False):
        """
        Добавление товара в корзину
        :param product: объект продукта
        :param quantity: количество товара которое нужно купить
        :param update_quantity: обновлять ли уже существующий элемент
        :return: 
        """
        
        product_id = str(product.id)
        if product_id not in self.cart:
            #Если товара не было в корзине
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True
    
    def remove(self, product):
        """
        Удаляем товар
        :param product:
        """
        
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def get_total_price(self):
        """
        Получение общей стоимости покупок
        :return: int
        """
          # a = int() 
        # for item in self.cart.values():
        #     a  = (Decimal(item['price';]) * item['quantity'])
        # return a
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        """
         Очищение корзины в сессии
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
