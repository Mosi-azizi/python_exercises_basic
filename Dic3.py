me = {
    "name": "mohammad",
    "family": "ordookhani",
    "email": "moh96ordo@gmail.com"
}

print(me)
# print(me.pop("name"))
# print(me)
# print(me.popitem())
# print(me)
second = {
    "name":"Ali",
    "age":50
}
print(second)
second.update(me)
print(second)
second["name"] = "sara"
print(second)