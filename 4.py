class Product:
    def get_price(self):
        is_valid_price = self._is_valid_price(self.price)
        if is_valid_price:
            return self.price
        return 'Incorrect price'

    def get_volume(self):
        is_valid_volume = self._is_valid_volume(self.volume)
        if is_valid_volume:
            return self.volume
        return 'Incorrect volume'

    @staticmethod
    def _is_valid_price(price):
        if isinstance(price, float) and price > 0:
            parts_number = str(price).split('.')
            if len(parts_number[1]) == 2:
                return True
        return False

    @staticmethod
    def _is_valid_volume(volume):
        if isinstance(volume, list):
            volume = list(filter(lambda x: isinstance(x, (int, float)) and x > 0, volume))
            if len(volume) == 3:
                return True
        return False


class Phone(Product):
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume

    def get_description(self):
        return f'Phone description.\nPrice: {self.get_price()}.\nVolume: {self.get_volume()}\n'


p1 = Phone(123.45, [1, 2, 3.2])
p2 = Phone('123,67', [])

print(p1.get_description())
print(p2.get_description())