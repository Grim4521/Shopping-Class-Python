list = []
f = open ("Shoppinglist.txt", "x")
print ("Welcome to the shopping list.")
while True:
    question = input ("Would you like to add anything (yes to add no to continue) ")
    if question.lower() == "yes":
        listadd = input ("What would you like to add ")
        list.append(listadd)
        f.write(listadd)
    if question.lower() == "no":
        break
print ("In your list you have",list,)
f.close()
