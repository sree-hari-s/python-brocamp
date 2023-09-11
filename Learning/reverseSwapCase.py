from string import digits, ascii_lowercase

def missingCharacters(s):
    return "".join(c for c in digits + ascii_lowercase if c not in s)

s = input()
result=missingCharacters(s)
print(result)
print(ascii_lowercase)