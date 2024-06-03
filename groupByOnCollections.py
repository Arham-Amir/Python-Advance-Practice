collections = [
{'Name': 'John', 'Department': 'HR', 'Salary': 50000, 'ID': 1, 'City': 'San Diego'},
{'Name': 'Alice', 'Department': 'IT', 'Salary': 60000, 'ID': 2, 'City': 'Houston'},
{'Name': 'Bob', 'Department': 'HR', 'Salary': 55000, 'ID': 3, 'City': 'Phoenix'},
{'Name': 'Jane', 'Department': 'IT', 'Salary': 62000, 'ID': 4, 'City': 'San Jose'},
{'Name': 'Mike', 'Department': 'Finance', 'Salary': 70000, 'ID': 5, 'City': 'New York'},
{'Name': 'Emily', 'Department': 'Finance', 'Salary': 72000, 'ID': 6, 'City': 'Los Angeles'},
{'Name': 'Chris', 'Department': 'IT', 'Salary': 58000, 'ID': 7, 'City': 'Chicago'},
{'Name': 'Sarah', 'Department': 'HR', 'Salary': 53000, 'ID': 8, 'City': 'San Antonio'},
{'Name': 'David', 'Department': 'Finance', 'Salary': 75000, 'ID': 9, 'City': 'San Diego'},
{'Name': 'Emma', 'Department': 'IT', 'Salary': 59000, 'ID': 10, 'City': 'Houston'}
]



def groupBy(columnName):
    output = {} 
    for collection in collections:
        if columnName in collection:
            if collection[columnName] in output:
                output[collection[columnName]].append(collection)
            else:
                output[collection[columnName]] = [collection]
        else:
            if 'others' in output:
                output['others'].append(collection)
            else:
                output['others'] = [collection]
    return output

columnName = 'City'
output = groupBy(columnName)

print(output)
# for key, val in output.items():
#     print(key, val, "\n")

# for key, value in output.items():
#     print(key, " : \n")
#     for el in value:
#         print(el)
    
# columnValue = "HR"
# for el in output[columnValue]:
#      print(el, "\n")