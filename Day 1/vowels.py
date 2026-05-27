word=input("enter a name:sa")
count=0
for letter in word:
    if letter in "aeiou":
     count+=1
print("total vowels",count)