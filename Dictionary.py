dictionary={
    "name":"Shabeer",
    "age": 25,
    "surname":"Syed",
    "city":"Umerkot"
}

print(dictionary["name"])
dictionary["age"]=23
print(dictionary)

std={
    "name":"Ali Mustafa",
    "subjects":{
        "maths":68,
        "chem":89,
        "phy":92,
        "eng":80
    }
}

#dictionary methods

print(std.keys())
print(std.values())
print(std.items())
print(std.get("subjects"))

std.update({"address":"HYD"})
print(std)

