s = input().strip()
max_length = len(s)

spell_count = 0
current_length = 32

while current_length < max_length:
    spell_count += 1
    current_length *= 2

spell = "long " * spell_count + "long"
print(spell)