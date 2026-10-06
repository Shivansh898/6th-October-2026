Set2 = set("abcdefghijklmnopqrstuvwxyz")

UserInput = input("Enter a pangram: ").lower()

Set1 = set(UserInput)

if Set2.difference(Set1) == set():
    print("This is a pangram!")
else:
    print("This is not a pangram!")