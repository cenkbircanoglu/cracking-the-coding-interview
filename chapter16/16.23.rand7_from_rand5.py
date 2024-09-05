import random


def rand5():
    """Simulates rand5(), which returns a random integer between 1 and 5."""
    return random.randint(1, 5)


def rand7():
    """Uses rand5() to generate a random number between 1 and 7."""
    while True:
        # Generate a number between 1 and 25
        num = 5 * (rand5() - 1) + rand5()  # This gives a number between 1 and 25

        # If the number is in the range [1, 21], map it to [1, 7] and return it
        if num <= 21:
            return (num - 1) % 7 + 1


# Example usage
print([rand7() for _ in range(10)])  # Generate 10 random numbers between 1 and 7
