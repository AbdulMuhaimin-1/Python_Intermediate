# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale.")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this under water")
#
#     def swim(self):
#         print("moving in water")
#
#
# class Dog:
#     def __init__(self):
#         self.temperature = "loyal"
#
#
# class Labrator(Dog):
#     def __init__(self):
#         super().__init__()
#         self.temperature = "gentle"
#
#
# dog = Dog()
# print(f"A dog is {dog.temperature}")
#
# sparky = Labrator()
# print(f"Sparky is {sparky.temperature}")
arr = [1, 3, 5, 6, 11, 23]
sum_1 = 9
for n in arr[1:]:
    ans = arr[1]
    if n + ans == sum_1:
        print(n, ans)


