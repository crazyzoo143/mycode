import requests

def search_character_by_name(name):
    base_url = "https://www.moogleapi.com/api/v1/characters/search"
    params = {"name": name}

if __name__ == "__main__":
    character_name = input("Enter the character name to search for: ")
    character_data = search_character_by_name(character_name)

    if character_data:
        print("Character found!")
        print("Character Data:")
        print(character_data)
    else:
        print("Character not found.")

