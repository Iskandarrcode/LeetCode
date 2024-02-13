def sanoq():
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    a = 0
    n = len(sequence) // len(word)

    for k in range(1, n + 1):
        if word * k in sequence:
            a = k

    return a

print(sanoq())