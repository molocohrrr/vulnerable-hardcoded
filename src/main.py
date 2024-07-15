# main.py

from config.config import DATABASE_USER, DATABASE_PASSWORD
import json

def main():
    print("Connecting to the database with user:", DATABASE_USER)
    print("Using password:", DATABASE_PASSWORD)

    with open('config/settings.json') as f:
        settings = json.load(f)
        print("API Key:", settings['api_key'])
        print("Secret Key:", settings['secret_key'])

if __name__ == "__main__":
    main()
