from datetime import datetime

def calculate_age(birth_year):
    """Calculates age based on the given birth year."""
    current_year = datetime.now().year
    return current_year - birth_year

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        if birth_year > datetime.now().year:
            print("Invalid input! Birth year cannot be in the future.")
        else:
            age = calculate_age(birth_year)
            print(f"You are {age} years old.")
    except ValueError:
        print("Invalid input! Please enter a valid year.")

if __name__ == "__main__":
    main()
