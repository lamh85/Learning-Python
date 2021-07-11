import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get("TESTING_DUMMY_VARIABLE"))
