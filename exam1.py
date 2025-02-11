#1
with open ("testi.txt", "r") as file:
    text = file.readlines()

stripe_numbers = [i+1 for i in range(len(text))]
spaces = []
for stripe in text:
    spaces.append(stripe.count(" "))
analyzator = list(zip(stripe_numbers, spaces))
hesh = 0
for i in analyzator:
    hesh += i[0]*i[1]
print(f"Набор кортежей: {analyzator}")
print(f"Хеш файла: {hesh}")