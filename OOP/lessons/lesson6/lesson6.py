import re

text = "Geeks - знания с гарантией!"
result = re.match(r"Geeks", text)
print (result)

result = re.search(r"гарантией", text)
print (result)

result = re.findall(r"г[а-я]р", text)
print (result)

result = re.split(r" ", text)
print (result)

result = re.sub(r" ", r":", text)
print (result)