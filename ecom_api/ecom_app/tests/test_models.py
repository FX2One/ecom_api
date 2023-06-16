import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        x = category_factory()
        assert x.__str__() == x.name

class TestBrandModel:
    def test_str_method(self, brand_factory):
        x = brand_factory(name='Brand 1')
        assert x.__str__() == 'Brand 1'

class TestProductModel:
    def test_str_method(self, product_factory):
        x = product_factory()
        assert x.__str__() == x.name


