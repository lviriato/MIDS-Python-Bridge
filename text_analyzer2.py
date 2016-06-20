text_input = input("Enter a line of text to analyze for vowels. ")

# Initialize vowel variables. 
a = 0
e = 0
i = 0
o = 0
u = 0
first = ""
next_char = ""

for x in text_input:
    if   x == "a": a += 1
    elif x == "e": e += 1
    elif x == "i": i += 1
    elif x == "o": o += 1
    elif x == "u": u += 1
    
    # identify the character after the first vowel
    if (first != "") & (next_char == ""): next_char = x
    
    # identify the first vowel
    if (a + e + i + o + u == 1) & (first == ""): first = x
    
print("\nvowels: ", a + e + i + o + u )
print("first vowel: ", first)
print("character immediately after the first vowel: ", next_char)