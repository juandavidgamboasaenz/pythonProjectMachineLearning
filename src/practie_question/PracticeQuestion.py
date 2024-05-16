def solution():
    # A string representing solar system planets
    planets = "Earth Mars Venus Jupiter Saturn Uranus Neptune Pluto"
    solar_system = ""
    result = ""
    # Split the string into a list of planet names
    planet_list = planets.split(' ')

    print(planet_list)
    # TODO: Join the planet list into a string with '|' as a separator and assign it to the variable 'solar_system'

    for planet in planet_list:
        if "|" not in planet_list:
            solar_system = solar_system.join(planet)
            print(solar_system)
        # else:
        #     solar_system = solar_system.join("|" + planet)

    print(solar_system)

