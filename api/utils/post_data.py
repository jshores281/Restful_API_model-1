
# Sends HTTPie cmds to test API endpoints with faker data


import os
from faker import Faker 


fake = Faker()


a = 0

while a < 50:
    fake_name = fake.name()
    fake_email = fake.email()
    fake_website = fake.word().title()
    fake_password = repr(fake.password())

    os.system('http POST localhost:8000/vault1 Content-Type:application/json name="{}" email="{}" website="{}.com" password="{}"'
        .format(fake_name,fake_email,fake_website,fake_password))
    a = a + 1
    


