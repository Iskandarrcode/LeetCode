def shaxmat(coordinates):
    dc = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    for key, value in dc.items():
        if coordinates[0] == key:
            if value % 2 != 0:
                if int(coordinates[1]) % 2 == 0:
                    return True
                else:
                    return False
            if value % 2 == 0:
                if int(coordinates[1]) % 2 != 0:
                    return True
                else:
                    return False
    return False
                

coordinates = input("Yo'nalishni kiriting: ")

print(shaxmat(coordinates))