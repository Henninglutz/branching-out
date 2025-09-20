import json


with open("users.json", "r", encoding="utf-8") as fileobj:
    user_data = json.load(fileobj)

def filter_user_age(min_age=None, max_age=None):
    result = []
    for u in user_data:
        age = u.get("age")
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue
        result.append(u)
    print(result)

filter_user_age(min_age=25, max_age=30)

