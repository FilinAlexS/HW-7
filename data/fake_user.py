from faker import Faker

faker = Faker(locale="RU")


def fake_name():
    return faker.first_name()


def fake_last_name():
    return faker.last_name()


def fake_email():
    return faker.email()


def fake_phone():
    return faker.phone_number()


def fake_password():
    return faker.password()
