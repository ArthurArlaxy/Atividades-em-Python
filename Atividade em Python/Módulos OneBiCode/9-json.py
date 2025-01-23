import json 

person_dict = {'name': 'Arthur', 'languages': ['Ingles', 'Portugues']}

person_json = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_json)

with open('person.txt','w') as json_file:
    json.dump(person_dict,json_file)