def count_matching_items(items, ruleKey, ruleValue):
    count = 0
    for i in items:
        if ruleKey == "type" and ruleValue == i[0]:
            count += 1
        elif ruleKey == "color" and ruleValue == i[1]:
            count += 1
        elif ruleKey == "name" and ruleValue == i[2]:
            count += 1
    return count

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(count_matching_items(items, ruleKey, ruleValue))
