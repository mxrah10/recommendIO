from dotenv import load_dotenv
import os

load_dotenv('pass.env')

print (os.getenv('DATABASE_URL'))