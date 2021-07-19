L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List : ",L)
vals = set( val for dic in L for val in dic.values())
print("Unique Values: ",vals)