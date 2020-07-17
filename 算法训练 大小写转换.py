stdin = input()
stdout = " "
for c in stdin:
    if c.islower():
        stdout += c.upper()
    elif c.isupper():
        stdout += c.lower()
print(stdout[1:])
