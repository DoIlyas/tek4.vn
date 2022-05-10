prompt = '> '

text = input(prompt + "Enter your test: ")
k = int(input(prompt + "k = "))

result = ''

print("Plain text:" + text)
print("Shift pattern:" + str(k))

for i in range(len(text)):
    char = text[i]
    if "A" <= char <= "Z":     # A->Z = 65->90
        result = result + chr((ord(char) + k - 65) % 26 + 65)
    elif 97 <= ord(char) <= 122:
        result = result + chr((ord(char) + k -97) % 26 + 97)
    else:
        result += char

print(result)

