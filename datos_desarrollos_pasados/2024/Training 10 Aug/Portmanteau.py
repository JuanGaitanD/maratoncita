def combine_words(word1, word2):
    vowels = 'aeiou'

    # Step 1: Process the first word
    first_letter = word1[0]
    vowel_1 = None
    letters_from_word1 = first_letter
    for char in word1[1:]:
        if char in vowels:
            vowel_1 = char
            break
        letters_from_word1 += char
    
    # Step 2: Process the second word
    last_letter = word2[-1]
    vowel_2 = None
    letters_from_word2 = last_letter
    for char in reversed(word2[:-1]):
        if char in vowels:
            vowel_2 = char
            break
        letters_from_word2 = char + letters_from_word2
        
    # Determine the merging vowel
    if vowel_2:
        merging_vowel = vowel_2
    elif vowel_1:
        merging_vowel = vowel_1
    else:
        merging_vowel = 'o'
    # Combine the results
    result = letters_from_word1 + merging_vowel + letters_from_word2
    return result

# Read input
word1 = input().strip()
word2 = input().strip()

# Output the result
print(combine_words(word1, word2))