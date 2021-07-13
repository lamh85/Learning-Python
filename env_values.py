import os
from dotenv import load_dotenv
load_dotenv()

var_names = [
  "TESTING_DUMMY_VARIABLE",
  "DB_NAME",
  "DB_HOST",
  "DB_USER",
  "DB_PASSWORD",
  "DB_PORT"
]

for var_name in var_names:
  print(os.environ.get(var_name))
