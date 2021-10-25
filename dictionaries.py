dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}

print(dictionary)
print(phone_numbers)
print(dictionary["cat"])
print(phone_numbers["boss"])

print()
print("Return the keys")

for i in dictionary:
    print(i)

print()
print("Return the keys")

for i in dictionary.keys():
    print(i)

print()
print("Return the value of the keys")

for i in dictionary:
    print(dictionary[i])

print()
print("Return the value of the keys")

for i in dictionary.values():
    print(i)

print()
print("Return a tuple with the key and its value")

for i in dictionary.items():
    print(i)

print()
print("Return the key and its value")

for key, value in dictionary.items():
    print(key, value)

print()
print("change value")

dictionary["cat"] = "Flat"

print()
print("add key and value(mejor y mas comodo)")

dictionary["bird"] = "Larry"
print(dictionary)

print()
print("add key and value")

dictionary.update({"beetle":"Paco"})
print(dictionary)

print()
print("Delete a key (we can do it with a pop too)")

del dictionary["bird"]
print(dictionary)

"""Mini excercise"""

json_dic = {
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": True,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": None
}
print("Print ejer")
print(json_dic["address"]["state"])
print(json_dic["phoneNumbers"][1]["number"])

print("add a phone number")
json_dic["phoneNumbers"].append({
    "type": "private",
    "number": "608 555-1234"
})

print(json_dic["phoneNumbers"]["number"])