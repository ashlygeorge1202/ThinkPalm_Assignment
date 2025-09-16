from faker import Faker

class FakerFactory:
    def __init__(self, locale='en_US'):
        self.faker = Faker(locale)

    def random_user(self):
        return {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'address': self.faker.address(),
            'phone': self.faker.phone_number(),
        }
