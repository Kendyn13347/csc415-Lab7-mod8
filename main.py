import math
import random


def task2_2():
    print("======================================")
    print("PART 2 — Task 2.2: Mixed-Mode (Python)")
    print("======================================")
    i, d, f = 5, 3.7, 2.1
    x = i + d
    y = d / i
    z = f + i
    print(f"i + d = {x}  (type: {type(x).__name__})")
    print(f"d / i = {y}  (type: {type(y).__name__}) -- no truncation!")
    print(f"f + i = {z}  (type: {type(z).__name__})")
    print(f"d // i (integer division) = {d // i}  (type: {type(d // i).__name__})")


def task2_3():
    print("======================================")
    print("PART 2 — Task 2.3: Explicit Casting")
    print("======================================")
    d_val = 9.8
    truncated = int(d_val)
    rounded   = round(d_val)
    print(f"Original : {d_val}")
    print(f"Truncated (int())  : {truncated}")
    print(f"Rounded   (round()): {rounded}")
    print(f"math.floor: {math.floor(d_val)}")
    print(f"math.ceil : {math.ceil(d_val)}")


def check(x, y):
    result = x > 0 and (y := y + 1) > 0
    return result, y


def task3_1():
    print("======================================")
    print("PART 3 — Task 3.1: Short-Circuit Eval")
    print("======================================")
    y_val = 10
    print(f"check(-1, y) where y=10:")
    print(f"  Before: y = {y_val}")
    _, y_after = check(-1, y_val)
    print(f"  Returned y: {y_after}  (unchanged -- short-circuit fired)")

    y_val = 10
    print(f"check(5, y) where y=10:")
    print(f"  Before: y = {y_val}")
    _, y_after = check(5, y_val)
    print(f"  Returned y: {y_after}  (incremented -- both sides evaluated)")


def task3_2():
    print("======================================")
    print("PART 3 — Task 3.2: De Morgan's Law")
    print("======================================")
    for a, b in [(True, True), (True, False), (False, True), (False, False)]:
        law1_lhs = not (a and b);  law1_rhs = (not a) or  (not b)
        law2_lhs = not (a or  b);  law2_rhs = (not a) and (not b)
        print(f"  a={a}, b={b}")
        print(f"    not(a and b) == (not a) or  (not b): {law1_lhs} == {law1_rhs} -> {law1_lhs == law1_rhs}")
        print(f"    not(a or  b) == (not a) and (not b): {law2_lhs} == {law2_rhs} -> {law2_lhs == law2_rhs}")


def grade(score):
    if   score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else:             return 'F'

def task4_1():
    print("======================================")
    print("PART 4 — Task 4.1: Grade Calculator")
    print("======================================")
    for s in [95, 85, 72, 63, 45]:
        print(f"  Score {s} -> {grade(s)}")


def task4_2():
    print("======================================")
    print("PART 4 — Task 4.2: Loop Comparison")
    print("======================================")
    print("for loop (1-10):", end="  ")
    for n in range(1, 11):
        print(n, end=" ")
    print()

    print("while loop (1-10):", end=" ")
    n = 1
    while n <= 10:
        print(n, end=" ")
        n += 1
    print()

    print("simulated do-while (1-10):", end=" ")
    n = 1
    while True:
        print(n, end=" ")
        n += 1
        if n > 10:
            break
    print()

    print("Even numbers (for + continue):", end=" ")
    for k in range(1, 11):
        if k % 2 != 0:
            continue
        print(k, end=" ")
    print()

def task4_3():
    print("======================================")
    print("PART 4 — Task 4.3: Multiplication Table")
    print("======================================")
    for r in range(1, 6):
        for c in range(1, 6):
            print(f"{r * c:3}", end=" ")
        print()


def task5_2():
    print("======================================")
    print("PART 5 — Task 5.2: Guarded Commands")
    print("======================================")
    a, b = 7, 3
    print(f"Initial: a={a}, b={b}")

    guards = []
    if a > b:  guards.append('swap')
    if a <= b: guards.append('double')
    if a == b: guards = ['swap', 'double']  # force non-determinism when equal

    choice = random.choice(guards)
    print(f"Enabled guards: {guards}")
    print(f"Randomly chosen guard: {choice}")

    if choice == 'swap':
        a, b = b, a
        print("Action: SWAP")
    else:
        a *= 2
        b *= 2
        print("Action: DOUBLE")

    print(f"Result: a={a}, b={b}")


if __name__ == "__main__":
    # task2_2()
    # task2_3()
    # task3_1()
    # task3_2()
    # task4_1()
    # task4_2()
    # task4_3()
     task5_2()