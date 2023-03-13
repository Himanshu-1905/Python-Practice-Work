# Write a python function to remove a given word from a list and strip it at the same time

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "Himanshu is a good"
print(this)
n = remove_and_split(this, "Himanshu")
print(n)
# print(this)
# print(this.strip())
