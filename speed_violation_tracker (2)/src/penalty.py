from src.data_handler import load_accounts, save_accounts
from src.speed_checker import get_fine

def apply_penalty(plate_number):
    accounts = load_accounts()
    if plate_number not in accounts:
        print("Vehicle not found.")
        return

    fine = get_fine()
    accounts[plate_number]["balance"] -= fine
    print(f"Fined {fine}. New balance: {accounts[plate_number]['balance']:.2f}")
    save_accounts(accounts)

    log_violation(plate_number, fine)

def log_violation(plate, fine):
    with open("logs/violations.log", "a") as log:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} | {plate} | Speed Violation | Fine: {fine}\n")
