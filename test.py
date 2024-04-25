import os
from dotenv import load_dotenv

load_dotenv()

my_keys = os.getenv("DEVICE_IP")

print(my_keys)
