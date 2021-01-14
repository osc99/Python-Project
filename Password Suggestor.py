import random

n = "1234567890"
u_letter = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
l_letter = "abcdefghijklmnopqrstuvwxyz"
sym = "()@#&_"

all = n + u_letter + l_letter + n + sym 

print("Please Enter the length of the required password")
l = int(input())

password = "".join(random.sample(all,l))
print("Suggested Password of Given Length is->")
print(password)