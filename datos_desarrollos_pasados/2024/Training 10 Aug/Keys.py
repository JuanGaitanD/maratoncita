price = 0
text = input()

ram = ""

for i in text:
    if i != ram and i != ram.upper() and i != ram.lower():
        price += 1
        
        if i.isupper():
            if ram.islower() or ram == "" or ram == " ":
                price += 1            
    ram = i

if text[len(text)-1] == " ":
    price -= 1

print(price)