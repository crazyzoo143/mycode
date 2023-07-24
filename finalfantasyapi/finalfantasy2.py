import requests

def search_character_by_name(name):
    # example URL: https://www.moogleapi.com/api/v1/characters/search?name=cloud
    base_url = "https://www.moogleapi.com/api/v1/characters/search?name=" + name
    print(base_url)
    return base_url

if __name__ == "__main__":
    character_name = input("Enter the character name to search for: ")
    character_url = search_character_by_name(character_name)

    character_data= requests.get(character_url).json()

    if isinstance(character_data, list):
        print("Character found!")
        print("Character Data:")
        print(character_data)
    else:
        print("Character not found.")

