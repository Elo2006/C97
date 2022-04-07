sentence = input("enter your sentence - ")
chcount = 0
wordcount = 1
for a in sentence:
    chcount +=1
    if(a == " "):
        wordcount +=1

print(wordcount)
print(chcount)