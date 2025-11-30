# Computer tries to guess your number using bisection search.
# You just tell it: higher, lower, or correct.

low = 1
high = 100
print("Think of a number between 1 and 100. I’ll guess it.")

while True:
    # Middle number = my best shot
    guess = (low + high) // 2
    print(f"My guess: {guess}")

    # You tell me what's up
    feedback = input("Type 'h' for higher, 'l' for lower, 'c' for correct: ").strip().lower()

    if feedback == "c":
        print(f"Let's gooo I got it: {guess}")
        break
    elif feedback == "h":
        # Too low
        low = guess + 1
    elif feedback == "l":
        # Too high
        high = guess - 1
    else:
        print("Bruh what is that input. Try again.")

    if low > high:
        print("Bro your hints make no sense. Game over.")
        break
