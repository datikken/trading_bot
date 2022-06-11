from dotenv import load_dotenv, dotenv_values

load_dotenv()  # take environment variables from .env.
config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

print(config['API_KEY'])