class Products:

    def __init__(self, product: str):
        self.product = product
        self.product_for_search = ''

    def declension(self):
        if self.product in ['картошка', 'картошек', 'картох', 'картофелин', 'картофелину', 'картошечек', 'картошку']:
            self.product_for_search = 'картошка'
        if self.product in ['морковок', 'морковки', 'морковку', 'морковочку', 'морковей', 'моркови', 'морковь']:
            self.product_for_search = 'морковь'
        if self.product in ['баклажаны', 'баклажан', 'баклажанов', 'баклажана', 'баклажанчиков',
                            'баклажок', 'баклажанец', 'баклажанчик']:
            self.product_for_search = 'баклажаны'
        if self.product in ['помидоры', 'помидор', 'помидорку', 'помидорки', 'помидоров', 'помидорей', 'помидора',
                            'помидорин']:
            self.product_for_search = 'помидоры'

        return self.product, self.product_for_search
