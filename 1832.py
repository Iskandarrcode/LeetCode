def pangram(sentence):
    count = 0    
    for i in range(97, 123):
        if chr(i) in sentence:
            count += 1
    if count == 26:
        return True
    else:
        return False


sentence = "thequickbrownfoxjumpsoverthelazydog"

print(pangram(sentence))