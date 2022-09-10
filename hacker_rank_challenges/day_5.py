if __name__ == '__main__':
    n = int(input("Please enter number for it multiples to 10: ").strip())
    ans = 0
    for num in range(1, 11):
        ans = n * num
        print(f"{n} x {num} = {ans}")
