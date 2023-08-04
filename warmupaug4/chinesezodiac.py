def main():
    zodiac_traits = {
        0: ("Monkey", "sharp, smart, curious, and mischievous"),
        1: ("Rooster", "hardworking, resourceful, courageous, and talented"),
        2: ("Dog", "loyal, honest, cautious, and kind"),
        3: ("Pig", "a symbol of wealth, honesty, and practicality"),
        4: ("Rat", "artistic, sociable, industrious, charming, and intelligent"),
        5: ("Ox", "strong, thorough, determined, loyal, and reliable"),
        6: ("Tiger", "courageous, enthusiastic, confident, charismatic, and a leader"),
        7: ("Rabbit", "vigilant, witty, quick-minded, and ingenious"),
        8: ("Dragon", "talented, powerful, lucky, and successful"),
        9: ("Snake", "wise, like to work alone, and determined"),
        10: ("Horse", "animated, active, and energetic"),
        11: ("Sheep", "creative, resilient, gentle, mild-mannered, and shy"),
    }

    usr_name = input("Please enter your name:\n>").title()
    usr_date = int(input("Please enter your birth year in YYYY format, e.g., 2010 or 2012%12:\n"))

    usr_date %= 12  # Apply modulo operation to handle variations like 2012%12

    if usr_date in zodiac_traits:
        zodiac_sign, traits = zodiac_traits[usr_date]
        print(f"{usr_name}, your zodiac sign is {zodiac_sign}, you are {traits}.")

main()

