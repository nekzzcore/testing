import json

def process_superheroes():
    with open('superhero.json', 'r') as f:
        data = json.load(f)

    # add 2+ superheroes
    new_heroes = [
        {
            "name": "Super Speedster",
            "age": 25,
            "secretIdentity": "John Doe",
            "powers": ["Super speed", "Agility"]
        },
        {
            "name": "Invisible Woman",
            "age": 35,
            "secretIdentity": "Jane Smith",
            "powers": ["Invisibility", "Force fields"]
        },
        {
            "name": "Mind Reader",
            "age": 28,
            "secretIdentity": "Bob Johnson",
            "powers": ["Telepathy", "Mind control"]
        }
    ]
    data['members'].extend(new_heroes)

    # sort by age
    data['members'].sort(key=lambda x: x['age'])

    # save to superhero_new.json
    with open('superhero_new.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    process_superheroes()
