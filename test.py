import os
from dotenv import load_dotenv

load_dotenv()

my_keys = os.getenv("USER")

print(my_keys)
