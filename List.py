values = [ 1, 2, "Rinku", 4, 5]
#list is data type that allows multiple values and can be different data types
print(values[0])        #1
print(values[3])        #4
print(values[-1])       #last index of list
print(values[1:3])      #sub set of values start from index 1 to 3 (3 will be exclusive)
values.insert(3,"Pawar")    #to add element
print(values)
values.append("end")        # to add element at the last
print(values)
values[2] = "Dilip"         # to update values in list
print(values)
del values[0]
print(values)               #to delete element fro the list

# Same as list data type but immutable
val = (1, 2, "Dilip", 4, 5.4)      # definding tuple
#val[2] = "DILIP"                   #TypeError: 'tuple' object does not support item assignment
print(val)

# Dictionary
dic = {1:"Rinku", 2:"Dilip", "d":"Rathod"}
print(dic[1])
print(dic[2])
print(dic["d"])

dict = {}
dict ["firstname"] = " Rinku"
dict ["lastname"] = "Pawar"
print(dict)
print(dict["lastname"])