#!/usr/bin/env python3
This simple script uses the Final Fantasy Character API to find the characters from each game

import requests

ff_characters = "https://www.moogleapi.com/api/v1/characters/search?name"


def main():

    # Get the Get Character list from Final fantasy API 
    gotDict = requests.get(ff_characters).json()

    # Characters are  under the "data" key
    characters  = gotDict.get("data")

    # We'll need a current max hp tracker to update if we find a champion with higheer base hp
    maxHp = 0
    maxHpChamp = ""

    # Now let's iterate through the champions to find out who has the highest base hp!
    for champion in champions:

        championHp = champions[champion]["stats"]["hp"]

        if championHp > maxHp:
            maxHp = championHp

    # Now, we might have more than one champion with the same base hp
    # Let's make a list of all the champions with our newly found max HP value
    highHpChampList = []

    for champion in champions:

        championHp = champions[champion]["stats"]["hp"]

        if championHp == maxHp:
            highHpChampList.append(champions[champion]["id"])

    print(f"The highest base hp value in LoL at the moment is {maxHp}\n Champions with {maxHp} hp currently include:\n{highHpChampList}")

main()


