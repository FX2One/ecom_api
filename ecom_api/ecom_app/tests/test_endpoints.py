import pytest
import factory
import json

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    ep = '/api/category/'
    def test_category_get(self, category_factory, api_client):
        category_factory.create_batch(5)

        response = api_client.get(self.ep)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5


class TestBrandEndpoints:
    ep = '/api/brand/'

    def test_brand_get(self, brand_factory, api_client):
        brand_factory.create_batch(5)

        response = api_client.get(self.ep)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5


class TestProductEndpoints:
    ep = '/api/product/'

    def test_product_get(self,product_factory, api_client):
        product_factory.create_batch(5)

        response = api_client.get(self.ep)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        print((json.loads(response.content)))