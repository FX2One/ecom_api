import factory

from ecom_app.models import Category, Brand, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('random_element', elements=["Category 1", "Category 2", "Category 3"])


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker('random_element', elements=["Brand 1", "Brand 2", "Brand 3"])

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('random_element', elements=["Product 1", "Product 2", "Product 3"])
    description = factory.Faker('text')
    digital = factory.Faker('boolean')
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)

