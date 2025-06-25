def pyramid_pattern(n):
    print("\n Pyramid Pattern:\n")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def right_aligned_triangle(n):
    print("\n Right-Aligned Triangle:\n")
    for i in range(1, n + 1):
        print("  " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def number_triangle(n):
    print("\n Number Triangle:\n")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def reverse_number_triangle(n):
    print("\n Reverse Number Triangle:\n")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def diamond_pattern(n):
    print("\n Diamond Number Pattern:\n")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input(" Enter the number of rows for the patterns: "))
    
pyramid_pattern(n)
right_aligned_triangle(n)
number_triangle(n)
reverse_number_triangle(n)
diamond_pattern(n)

print("\nAll 5 patterns displayed successfully!")

