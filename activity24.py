fruits = ["longgan", "grapes", "mango", "mangosteen", "rambutan", "banana"]

fruits_d = {"bilog":"longgan", "crunchy":"grapes", "sweet":"mango", "healty":"mangosteen", "hairy":"rambutan", "yellow":"banana"} 
print(fruits[4])
print(fruits_d["yellow"])

for x, y in fruits_d.items():
    print("hint is --", x, "the fruit is--", y)
