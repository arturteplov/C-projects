#Exercise 1 Goal: Practice lists, sets, and loops.

items = []
counter = 0 
#Ask user to type items until they type "stop".

while True: 
    item = input ("Enter the item (type 'stop' to exit): ")
    if item == "stop":
        break
    else:

        items.append(item) #storing in list
        counter +=1 

new_set = set(items) # converting to set 

print(items)

print(new_set)

----

#Exercise 2: Student Grades Summary (Dictionary + For Loop)


#Create a dictionary: keys = student names, values = list of grades.

#Use a for loop to calculate average grade per student.

#Print student with the highest average.

#👉 Extension: Also print class average.



students = {"Artur": [3, 2, 1, 4, 5, 3], 
           "John": [1, 4, 2, 1, 4, 5], 
           "Sapachiy": [2, 1, 3, 4, 2, 5]} 

 

students_new_num = {}

#Calculating average in dictionary
for name in students:
    grades = students [name]
    avr_grade = sum(grades)/len(grades)
    students_new_num[name] = avr_grade


#Find the highest average 

best_student = max(students_new_num, key = students_new_num.get)

print(f"The student with highest average : {best_student} {students_new_num[best_student]: .2f}")

----
#3. Simple Phone Book (Dictionary + While Loop)


#Start with empty dictionary {}.

#While user doesn’t type "exit":

#Ask: "Enter name:" and "Enter phone number:".

#Save in dictionary.

#Print the full phonebook at the end.

#👉 Extension: Add option to search by name.



phone_book = {}

while True:
    name = input ("Enter name: ")
    number = input ("Enter phone number: ")
    
    if name == "exit" or number == "exit":
        break
    else:
        phone_book[name] = number

for key, values in phone_book.items():
    print(f"{key}: {values}")


while True:
    name_search = input ("Enter name to search: ")
    if name_search == "exit":
        break
    elif name_search in phone_book:
        print(f"{name_search} -> {phone_book[name_search]}")
    else:
        print(f"{name_search} wasn't found")
        
    

-----
#Exercise 4. Tuple Coordinate Distance Calculator (Tuple + For Loop)

import math



x1 = float (input("Enter the x1 number: "))
y1 = float (input("Enter the y1 number: "))
x2 = float (input("Enter the x2 number: "))
y2 = float (input("Enter the y2 number: "))

stuff1 = (x1,y1)
stuff2 = (x2,y2)




distance = math.sqrt((stuff2[1] - stuff1[0])**2 + (stuff2[1] - stuff1[1])**2)
print(f"Computed distance: {distance}")



----

#5. Word Frequency Counter (List + Dictionary + For Loop)

#Input a sentence.

#Split into list of words.

#Use dictionary to count frequency.

#Print word with highest count.

#Extension: Use a set to display unique words.

stuff = {}
words = []
words = input ("Enter a sentence: ").split()
stuff.update ({w: None for w in words})


for k in stuff.keys():
    counter = 0
    for kk in words:
        if k == kk:
            counter +=1 
    stuff[k] = counter





high_freq = max(stuff, key = stuff.get)

print(f"Word with highest count is -{high_freq}-")


----

#Exercise 6. Number Guessing Game (While Loop + Sets)


#Computer picks a random number (1–20).

#While user hasn’t guessed it:

#Ask for input.

#Track guessed numbers in a set.

#Print how many tries it took.

import random

number = random.choice(range(1,21))
guesses= set ()
counter = 0

while True:
    guess = int(input ("Guess the number: "))
    counter += 1
    guesses.add(guess) #add <guess> to set (add(10) always need a number, append for lists
    if guess != number: #for integers;  not in -> for lists
        print("Wrong, try again...")
    elif guess == number:
        print(f"Number {guess} is correct! Total tries: {counter}")
        break
    


---

