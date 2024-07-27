from faker import Faker
from dadjokes import Dadjoke
dadjoke = Dadjoke()
fake = Faker()
print(f"{fake.name()} says {dadjoke.joke}")
print(fake.address())