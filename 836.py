def solishtrma(rec1, rec2):
    x_ = not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2])

    y_ = not (rec1[3] <= rec2[1] or rec1[1] >= rec2[3])

    return x_ and y_

rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]

res = solishtrma(rec1, rec2)
print(f"Do rectangles overlap? {'Yes' if res else 'No'}")
