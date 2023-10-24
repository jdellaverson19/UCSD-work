studCount = 1000
rating = 4.99
isPublished = False
courseName = "Python"

x, y = 1, 2
age: int = 20
potat: str = "why"
print(id(x))
x += 1
print(id(x))
# vs
z = list(range(3))
print(id(z))
z.append(1)
print(id(z))
# """
# """
full = f"{x} {y}"
print(full)

potat.find("hy")
print(potat.replace("w", "p"))
print("w" in potat)
print("w" not in potat)

guess = 0
answer = 5
while answer != guess:
    guess = int(input("Guess: "))
else:
    pass


def increment(number: int, by: int = 1) -> int:
    return number + by
