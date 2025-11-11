import random

a = ["Very Good!", "Splendid!", "Correct! keep it up", "You Got it!"]
b = ["Wrong :( Try again!", "Nope, once more!", "It's Okay! Try Again!"]
c = ["Wrong :( Try again!: ", "Nope, once more!: ", "It's Okay! Try Again!: "]


def easy_multiplication():
    x = random.randrange(1, 10)
    y = random.randrange(1, 10)
    n = int(input(f"How much is {x} * {y}?\n"))

    while n > 0 and d == 1:
        if n == x * y:
            print(random.choice(a))
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
            n = int(input(f"How much is {x} times {y}?\n"))
        else:
            n = int(input(random.choice(b)))



def hard_multiplication():
    x = random.randrange(10, 100)
    y = random.randrange(10, 100)
    n = int(input(f"How much is {x} times {y}?\n"))
    while n > 0:
        if n == x * y:
            print(random.choice(a))
            x = random.randrange(10, 100)
            y = random.randrange(10, 100)
            n = int(input(f"How much is {x} times {y}?\n"))
        else:
            n = int(input(random.choice(b)))


def easy_division():
    x = random.randrange(5, 10)
    y = random.randrange(2, 5)
    n = 1
    while n > 0:
        m = round(x / y, 2)
        n = float(input(f"How much is {x} divided by {y}? (2 decimal places)\n"))
        if n == m:
            print(random.choice(a))
            x = random.randrange(5, 10)
            y = random.randrange(2, 5)
        else:
            print(random.choice(b))


def hard_division():
    x = random.randrange(50, 100)
    y = random.randrange(1, 50)
    n = 1
    while n > 0:
        m = round(x / y, 3)
        n = float(input(f"How much is {x} divided by {y}? (3 decimal places)\n"))
        if n == m:
            print(random.choice(a))
            x = random.randrange(50, 100)
            y = random.randrange(1, 50)
        else:
            print(random.choice(b))


def addition():
    x = random.randrange(1, 1000)
    y = random.randrange(1, 1000)
    n = int(input(f"How much is {x} + {y}?\n"))
    while n > 0:
        if n == x + y:
            print(random.choice(a))
            x = random.randrange(10, 100)
            y = random.randrange(10, 100)
            n = int(input(f"How much is {x} + {y}?\n"))
        else:
            n = int(input(random.choice(b)))


def subtraction():
    x = random.randrange(500, 1000)
    y = random.randrange(1, 500)
    n = int(input(f"How much is {x} - {y}?\n"))
    while n > 0:
        if n == x - y:
            print(random.choice(a))
            x = random.randrange(10, 100)
            y = random.randrange(10, 100)
            n = int(input(f"How much is {x} - {y}?\n"))
        else:
            n = int(input(random.choice(b)))


print(" 1: Addition\n 2: Subtraction\n 3: Multiplication\n 4: Division\n 5: Mix of All")
c = int(input("Select the type of math problems from 1-5: "))

if c == 3 or c == 4:
    d = int(input("Select difficulty level 1 or 2: "))
    print("Enter -1 to exit")
    if d == 1 and c == 3:
        easy_multiplication()
    if d == 2 and c == 3:
        hard_multiplication()
    if d == 1 and c == 4:
        easy_division()
    if d == 2 and c == 4:
        hard_division()
elif c == 1:
    addition()
elif c == 2:
    subtraction()
elif c == 5:
    while c == 5:
        math_problem = ['+', '-', '*', '/']
        random_choice = math_problem[random.randrange(0, 4)]
        if random_choice == '+':
            x = random.randrange(1, 100)
            y = random.randrange(1, 100)
            n = int(input(f"How much is {x} + {y}?\n"))
            if n == x + y:
                print(random.choice(a))
            else:
                while n != x + y:
                    n = int(input(random.choice(c)))
                    if n == x + y:
                        print(random.choice(a))
        elif random_choice == '-':
            x = random.randrange(50, 100)
            y = random.randrange(1, 50)
            n = int(input(f"How much is {x} - {y}?\n"))
            if n == x - y:
                print(random.choice(a))
            else:
                while n != x - y:
                    n = int(input(random.choice(c)))
                    if n == x - y:
                        print(random.choice(a),)
        elif random_choice == '*':
            diff = int(input("Select Multiplication difficulty 1 or 2: "))
            if diff == 1:
                x = random.randrange(1, 10)
                y = random.randrange(1, 10)
                n = int(input(f"How much is {x} * {y}?\n"))
                if n == x * y:
                    print(random.choice(a))
                else:
                    while n != x * y:
                        n = int(input(random.choice(c)))
                        if n == x * y:
                            print(random.choice(a))
            elif diff == 2:
                x = random.randrange(11, 100)
                y = random.randrange(11, 100)
                n = int(input(f"How much is {x} * {y}?\n"))
                if n == x * y:
                    print(random.choice(a))
                else:
                    while n != x * y:
                        n = int(input(random.choice(c)))
                        if n == x * y:
                            print(random.choice(a))
        elif random_choice == '/':
            diff = int(input("Select Division difficulty 1 or 2: "))
            if diff == 1:
                x = random.randrange(5, 10)
                y = random.randrange(2, 5)
                n = float(input(f"How much is {x} / {y}? (2 decimal places)\n"))
                m = x / y
                r_m = round(m, 2)
                if n == r_m:
                    print(random.choice(a))
                else:
                    while n != r_m:
                        n = float(input(random.choice(c)))
                        if n == r_m:
                            print(random.choice(a))
            elif diff == 2:
                x = random.randrange(50, 100)
                y = random.randrange(2, 50)
                n = float(input(f"How much is {x} / {y}? (3 decimal places)\n"))
                m = x / y
                r_m = round(m, 3)
                if n == r_m:
                    print(random.choice(a))
                else:
                    while n != r_m:
                        n = float(input(random.choice(c)))
                        if n == r_m:
                            print(random.choice(a))