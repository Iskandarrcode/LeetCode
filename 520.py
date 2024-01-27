word = "Ulfglafa"
if word.isupper() or word.islower():
    print("true")
elif word[0].isupper() and word[1:].islower():
    print("true")
else:
    print("false")