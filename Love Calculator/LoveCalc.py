print("Welcome to LoveScore Calculator")

Name1 = input("Enter your Name: \n")
Name2 = input("Enter their Name: \n")

Name = (Name1 + " " + Name2).lower()

t = Name.count('t')
r = Name.count('r')
u = Name.count('u')
e = Name.count('e')

true = t + r + u + e

l = Name.count('l')
o = Name.count('o')
v = Name.count('v')
e = Name.count('e')

love = l + o + v + e

Love_Score = int(str(true) + str(love))

if Love_Score < 10 or Love_Score > 90:
    print(f"Your love score is {Love_Score}, You make a Great Couple")
elif 40 < Love_Score < 50:
    print(f"Your love score is {Love_Score}, You are alright together")
else:
    print(f"Your love score is {Love_Score}")



