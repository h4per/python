# 1
# import random
# def random_item():
#     language =["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"] 
#     random_language = random.choice(language)
#     print(random_language)
# random_item()



# 2
# Способ 1

# lorem_text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# """
# f = open('text.txt','w',encoding="utf-8")
# f.write(lorem_text)
# f.close()

# Способ 2

# lorem_text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# """
# with open('text2.txt', 'w', encoding="utf-8") as l:
#     l.write(lorem_text)



# 3
# with open('text.txt', 'r+') as t:
#     with open('wikipedia.txt', 'w+') as w:
#         w.write(t.read())
