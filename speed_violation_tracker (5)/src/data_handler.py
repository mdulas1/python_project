import json
import os

DATA_PATH = "data/driver_accounts.json"

def load_accounts():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def save_accounts(accounts):
    with open(DATA_PATH, 'w') as f:
        json.dump(accounts, f, indent=4)
