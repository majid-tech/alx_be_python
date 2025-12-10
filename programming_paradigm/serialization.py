import json

def process_json(data: dict, filename: str) -> dict:
    filename = json.dumps(data)
    
    with open('data.json', 'w') as file:
        json.dump(data, file)

process_json({
    'name': 'Alice',
    'age': 30,
    'city': 'Kampala'
}, 'list')


# Serialization
# data = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'Kampala'
# }

# json_string = json.dumps(data)

# with open('data.json', 'w') as file:
#     json.dump(data, file)

# # Deserialization
# data = json.loads(json_string)

# with open('data.json', 'r') as file:
#     data = json.load(file)
# print(data)