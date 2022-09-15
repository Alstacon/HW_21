from classes.products_class import Products


class TestProductsClass:

    def test_declension(self):
        unit_1 = Products("морковки")
        unit_2 = Products("картох")
        unit_3 = Products("баклажок")
        unit_4 = Products("помидорку")

        unit_1.declension()
        unit_2.declension()
        unit_3.declension()
        unit_4.declension()

        assert unit_1.product == 'морковки'
        assert unit_1.product_for_search == 'морковь'
        assert unit_2.product == 'картох'
        assert unit_2.product_for_search == 'картошка'
        assert unit_3.product == 'баклажок'
        assert unit_3.product_for_search == 'баклажаны'
        assert unit_4.product == 'помидорку'
        assert unit_4.product_for_search == 'помидоры'
