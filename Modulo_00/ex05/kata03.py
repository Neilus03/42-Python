# Put this at the top of your kata03.py file 
kata = "The right format"

while len(kata) < 42:
    kata = ''.join(("-", kata))
print(kata, end="")

