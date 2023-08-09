# Part 1 and 2
character = classinfo["all"][2]
name = character["name"]
power = character["super power"]
print(name, "has the power of", power)

# Part 3
for character in classinfo["all"]:
    name = character["name"]
    skill = character["skill level"]
    power = character["super power"]
    animal = character["spirit animal"]

    print(f"{name}, a {skill} {animal} of a programmer, possesses a {power} factor for moonlighting as a superhero!")

