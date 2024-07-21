text = 'Abcdefghijklmnopqrstuvwxyz'
fragment = text[2:5]
print(fragment)  # cde
fragment = text[:5]  # Abcde
print(fragment)
fragment = text[5:]  # fghijklmnopqrstuvwxyz
print(fragment)
fragment = text[::2]  # Acegikmoqsuwy, every second letter
print(fragment)
fragment = text[::-1]  # zyxwvutsrqponmlkjihgfedcba, reverse the string
print(fragment)
fragment = text[2:5:2]  # ce, every second letter from 2 to 5
print(fragment)
fragment = text[5:2:-1]  # fed, from 5 to 2, step -1
print(fragment)