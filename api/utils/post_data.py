
import os

# HTTPie cmds to test API endpoints


fake_name = "jason"
fake_website = "jason.com"
fake_password = "jasons password"




a = 0

while a < 5:
    os.system(f'http POST localhost:8000/vault1 Content-Type:application/json name="{fake_name}" website="{fake_website}" password="{fake_password}"')
    a = a + 1
    


