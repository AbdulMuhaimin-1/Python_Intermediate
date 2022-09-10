
num = int(input())


for n in range(num):
    test = input()
    even_index_letters = ""
    odd_index_letters = ""
    for letter in range(len(test)):
        if letter % 2 == 0:
            even_index_letters += test[letter]
        else:
            odd_index_letters += test[letter]

    print(even_index_letters + " " + odd_index_letters)

