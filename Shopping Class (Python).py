from typing import List
import time

list = []
f = open ("Shoppinglist.txt", "a")
print ("Welcome to the shopping list.")
time.sleep(1)
while True:
    question = input ("Would you like to add anything (yes to add no to continue) ")
    if question.lower() == "yes":
        time.sleep(0.5)
        listadd = input ("What would you like to add ")
        list.append(listadd)
        f.write(listadd)
    if question.lower() == "no":
        break
time.sleep(1)
while True:
    question2 = input ("Would you like to delete anything. ")
    if question2.lower() == "yes":
        time.sleep(0.5)
        remove = input ("What would you like to remove? ")
        list.remove(remove)
    if question2.lower() == "no":
        print ("no")
        break


# try and make it delete in the file
# add a func
print ("In your list you have",list,)
f.close()
