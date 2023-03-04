# Write a program to greet all the person names stored in a list l1 and which starts with S

l1 = ["Himanshu", "Jatin", "Harsh", "Rahul"]

for name in l1:
    if name.startswith("H"):
        print("Hello " + name)