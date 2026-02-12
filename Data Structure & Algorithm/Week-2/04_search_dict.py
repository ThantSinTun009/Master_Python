myDict = {'Name':'Mg Mg', 'Age':21, 'Address':'Sagaing', 'education':'data science'}

def search_dict(dict, target):
    for key in dict:
        if dict[key] == target:
            return key, target
    return 'The target does not exist'

print(search_dict(myDict, 'Sagaing'))