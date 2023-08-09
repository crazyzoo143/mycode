classinfo = {
    "all": [
	    {
	        "Name": "Alex",
	        "Spirit Animal": "Tiger",
	        "Super Power": "Telekinesis",
	        "Skill Level": "Phenomenal"
	    },
	    {
	        "Name": "Benji",
	        "Spirit Animal": "Bear",
	        "Super Power": "Time Manipulation",
	        "Skill Level": "Spectacular"
	    },
	    {
	        "Name": "Cayla",
	        "Spirit Animal": "Owl",
	        "Super Power": "Flight",
	        "Skill Level": "Magnificent"
	    },
	    {
	        "Name": "Demetra",
	        "Spirit Animal": "Dragonfly",
	        "Super Power": "Invisibility",
	        "Skill Level": "Astounding"
	    },
	    {
	        "Name": "Derek",
	        "Spirit Animal": "Wolf",
	        "Super Power": "Teleportation",
	        "Skill Level": "Marvelous"
	    },
	    {
	        "Name": "Deshawn",
	        "Spirit Animal": "Eagle",
	        "Super Power": "Super Strength",
	        "Skill Level": "Incredible"
	    },
	    {
	        "Name": "James",
	        "Spirit Animal": "Lion",
	        "Super Power": "Mind Reading",
	        "Skill Level": "Wonderful"
	    },
	    {
	        "Name": "Maria",
	        "Spirit Animal": "Fox",
	        "Super Power": "Shape-Shifting",
	        "Skill Level": "Astonishing"
	    },
	    {
	        "Name": "Marylyn",
	        "Spirit Animal": "Dolphin",
	        "Super Power": "Telepathy",
	        "Skill Level": "Epic"
	    },
	    {
	        "Name": "Nor",
	        "Spirit Animal": "Butterfly",
	        "Super Power": "Elemental Control",
	        "Skill Level": "Fantastic"
	    },
	    {
	        "Name": "Sal",
	        "Spirit Animal": "Tiger",
	        "Super Power": "Telekinesis",
	        "Skill Level": "Phenomenal"
	    },
	    {
	        "Name": "Sammy",
	        "Spirit Animal": "Bear",
	        "Super Power": "Time Manipulation",
	        "Skill Level": "Spectacular"
	    }
	]
}

# grabbed the cayla dictionary and places in a var
character = classinfo["all"][2]

name = character["Name"]
power = character["Super Power"]

print(name, "has the power of", power)

for character in classinfo["all"]:
    # character == each person's dictionary
    name = character["Name"] # Name not name
    skill = character["Skill Level"] # Skill Level not skill level
    power = character["Super Power"]
    animal = character["Spirit Animal"]

    print(f"{name}, a {skill} {animal} of a programmer, possesses a {power} factor for moonlighting as a superhero!")

