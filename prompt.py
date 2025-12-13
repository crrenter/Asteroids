age_input = input("whats your age?\n")
try:
    age = int(age_input)
    print(f"Age: {age}")
except:
    raise ValueError("Not a real number noob!")

