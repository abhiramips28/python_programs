""" Q1. Convert two lists into a dictionary."""
# keys = ["ten","twenty","thirty"]
# values = [10,20,30]
# new_dict = dict(zip(keys,values))
# print(new_dict)
#

"""another method"""
# list1 = ["name","age"]
# list2 = ["anvi",3]
# print(list1)
# print(list2)
# dict1 = {}
# for k in list1:
#     for v in list2:
#         dict1[k] = v
#         list2.remove(v)
#         # break
# print(dict1)

""" Q2. Merge two python dictionaries into one. """
# dict1 = {"name":"vishnu","place":"chry"}
# dict2 = {"daughter":"anvi","age":3}
# dict1.update(dict2)
# print(dict1)

"""Q3. Print the value of key 'history' from the below dict.   """
# sampledict = {"class":{"student":{"name":"mike","marks":{"physics":80,"history":85}}}}
# print(sampledict["class"]["student"]["marks"]["history"])

"""Q4. Initialize dictionary with default values.  """
keys = ["dict1","dict2"]
defaults = {"place":"abc","phn:":23456}

result = dict.fromkeys(keys,defaults)
print(result)

"""Q5. Create a dictionary by extracting the keys from  a given dictionary.   """









"""Q6. Delete a list of keys from a dictionary.    """







"""Q7.Check if a value exists in a dictionary. """
# dict1 = {"name":"anvi","age":3}
# x = dict1.values()
# print(x)
# if 3 in dict1.values():
#     print("3 is present")

"""Q8. Rename key of a dictionary.    """
# dict1 = {"name":"anvi","place":"chry"}
# dict1['city'] = dict1.pop('place')
# print(dict1)



"""Q9. Get the key of a minimum value from the following dictionary.  """
# dict1 = {"name":"anvi","age":3,"place":"chry"}
# x = dict1.values()
# y = []
# for i in x:
#     x = str(i)
#     y.append(x)
# print(min(y))



"""Q10. Change value of a key in a nested dictionary. """
# sample_dict = {
#     'dict1' : {"name":"chitra","age":22,"course":"python"},
#     'dict2' : {"place":"abc"},
#     'dict3' : {"job":"pythondev","sal":25488}
# }
# sample_dict['dict3']['job'] = 'software engineer'
# print(sample_dict)