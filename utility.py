def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Amount must be greater than zero.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")