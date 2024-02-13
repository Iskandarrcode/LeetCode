def highest_altitude(gain):
    katta = 0
    n = 0
    for i in gain:
        n += i
        katta = max(katta, n)

    return katta

gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))
