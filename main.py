from config import API

api = API()
api.login()

choose = int(input("What are we doing? (1 - post / 2 - delete post): "))

if choose == 1:
    text = input("Input your text: ")
    title = input("Input your title: ")
    api.post(text, title)
elif choose == 2:
    id = input("Input your id: ")
    api.delpost(id)
else:
    print("Oops! Error")

