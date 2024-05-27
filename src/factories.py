from api.models import Todo
import faker
import factory
# from factory.alchemy import SQLAlchemyModelFactory

class TodoFactory(factory.Factory):
    class Meta:
        model = Todo

    title = factory.Faker("word")
    description = factory.Faker("text")

