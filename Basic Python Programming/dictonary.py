#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

phone = {"brand":"Apple",
        "model":"iPhone 12",
        "price":899
        }

print(phone.get("brand")) #print brand value Apple
print(phone.keys()) #only print the keys 
print(phone.values()) #only print the values of the keys
print(phone.items()) # print all the key and value pairs

phone.update({"release":2020}) # update dictornary with new key value pair
phone.update({"price":990}) # update existence key value
phone.pop("release") # delete the key value pair
#phone.clear() # remove all the dictonary key value pair

phone.update({"color": ["white","black","red"]}) # update dictornary with new key value pair

for key,value in phone.items(): # print dictonary 
    print(key,value)


