from parser.term import Tree

PRICE_MAP = {
    # За миллион символов
    'YANDEX': 15
}

class Translate:
    def __init__(self, tree_root):
        assert isinstance(tree_root, Tree), "Tree root should be a Tree subclass"
        self.root = tree_root

    def get_price(self, provider=None):
        _get_price = lambda symbol_length, price: (symbol_length / 1000000) * price
        _symbol_length = self.root.symbol_length()

        if provider:
            _price = PRICE_MAP.get(provider)
            assert _price, "Провайдер не найден"
            return _get_price(_symbol_length, _price)

        for provider, price in PRICE_MAP.items():
            return {
                provider: _get_price(_symbol_length, price)
            }
