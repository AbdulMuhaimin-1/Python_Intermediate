if __name__ == '__main__':
    n = int(input().strip())


    arr = list(map(int, input().rstrip().split()))
    x = arr[::-1]
    print(*x)
    for i in x:
        print(i, end=" ")
