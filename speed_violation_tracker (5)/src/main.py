from src.speed_checker import is_speeding
from src.penalty import apply_penalty

def main():
    print("=== Speed Violation Tracker ===")
    plate = input("Enter license plate: ").strip().upper()
    try:
        speed = float(input("Enter vehicle speed (km/h): "))
    except ValueError:
        print("Invalid speed input.")
        return

    if is_speeding(speed):
        print("Speeding detected!")
        apply_penalty(plate)
    else:
        print("No violation. Drive safe!")

if __name__ == "__main__":
    main()
