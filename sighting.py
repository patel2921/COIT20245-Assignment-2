# sighting.py

"""# Task 1 start 
print("Task 1 Display Menu")
def display_menu():

    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")

# Debugging the display_menu() function
display_menu()
# Task 1 End 

# Task 2 Start
print("Task 2 User Input")
def display_menu_1():
   
    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")

def main():
    
    display_menu_1()  # Display the initial help menu
    while True:
        user_input = input("wildlife> ").strip().lower()  # Prompt user for input
        if user_input == 'help':
            display_menu_1()  # Call display_menu() if user input is 'help'
        elif user_input == 'exit':
            print("Exiting the program.")
            return  # Exit the main() function if user input is 'exit'
        else:
            print("Invalid command. Please enter 'help' or 'exit'.")

# Debugging and testing the main() function
if __name__ == "__main__":
    main()
# Task 2 End # 
"""
# Task 3 Start #

def display_menu():

    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")

def search_species(city):

    return [
        {"Species": {"TaxonID":"1036","AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"TaxonID":"236","AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
  
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        Tax = species["Species"]["TaxonID"]
        print(f"TaxonID: {Tax} , Name: {name}, Pest Status: {status}")

def main():
   
    display_menu()  # Display the initial help menu
    while True:
        user_input = input("wildlife> ").strip().lower()  # Prompt user for input
        if user_input == 'help':
            display_menu()  # Call display_menu() if user input is 'help'
        elif user_input == 'exit':
            print("Exiting the program.")
            return  
        elif user_input.startswith('species'):
            city = user_input.split(maxsplit=1)[1].strip()  
            species_list = search_species(city)  
            display_species(species_list)  
        else:
            print("Invalid command. Please enter 'help', 'exit', or 'species <city>'.")

# Debugging and testing the main() function
if __name__ == "__main__":
    main()
# Task 3 End #

# Task 4 Start #

def display_menu():
    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")
    print("d. Display animal sightings in a city")

def search_species(city):
    # Stub implementation, will be replaced with actual functionality
    return [

       {"Species": {"TaxonID":"1036","AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
       {"Species": {"TaxonID":"236","AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        Tax = species["Species"]["TaxonID"]
        print(f"TaxonID: {Tax} , Name: {name}, Pest Status: {status}")

def search_sightings(taxonid, city):
    # Stub implementation, will be replaced with actual functionality
    return [
        {"properties": {"Taxonid":"1002","StartDate": "1989-02-22", "LocalityDetails": "Kew","SiteCode":"Incidental"}},
        {"properties": {"Taxonid":"1039","StartDate": "2002-12-21", "LocalityDetails": "Murrumbeena","SiteCode":"Incidental"}},
        {"properties": {"Taxonid":"202","StartDate": "1999-11-15", "LocalityDetails": "Tinaroo","SiteCode":"Incidental"}}
    ]

def display_sightings(sightings):
    """
    Display a list of animal sightings to the screen.
    """
    print("Animal sightings:")
    for sighting in sightings:
        taxonid = sighting["properties"]["Taxonid"]
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        sitecode = sighting["properties"]["SiteCode"]
        print(f"taxonid: {taxonid},Start Date: {start_date}, Locality: {locality},sitecode: {sitecode}")

def main():
    """
    Main function to handle user interaction.
    """
    display_menu()  # Display the initial help menu
    while True:
        user_input = input("wildlife> ").strip().lower()  # Prompt user for input
        if user_input == 'help':
            display_menu()
        elif user_input == 'exit':
            print("Exiting the program.")
            return
        elif user_input.startswith('species'):
            city = user_input.split(maxsplit=1)[1].strip()
            species_list = search_species(city)  # Search for species in the city
            display_species(species_list)  
        elif user_input.startswith('sightings'):
            _, species, city = user_input.split(maxsplit=2)
            sightings = search_sightings(species, city)  
            display_sightings(sightings)
        else:
            print("Invalid command. Please enter 'help', 'exit', 'species <city>', or 'sightings <species>, <city>'.")

# Debugging and testing the main() function
if __name__ == "__main__":
    main()
# Task 4 End #


# Task 5 Start #
def display_menu():
    """
    Display the menu options for the wildlife sighting program.
    """
    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")
    print("d. Display animal sightings in a city")
    print("e. Display venomous species")

def search_species(city):
    # Stub implementation, will be replaced with actual functionality
     return [
       {"Species": {"TaxonID":"1036","AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
       {"Species": {"TaxonID":"236","AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        Tax = species["Species"]["TaxonID"]
        print(f"TaxonID: {Tax} , Name: {name}, Pest Status: {status}")

def search_sightings(taxonid, city):
    # Stub implementation, will be replaced with actual functionality
    return [
        {"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_sightings(sightings):

    print("Animal sightings:")
    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        print(f"Start Date: {start_date}, Locality: {locality}")

def filter_venomous(species_list):

    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]

def main():
    display_menu()  # Display the initial help menu
    while True:
        user_input = input("wildlife> ").strip().lower()  
        if user_input == 'help':
            display_menu()  
        elif user_input == 'exit':
            print("Exiting the program.")
            return  
        elif user_input.startswith('species'):
            if 'venomous' in user_input:
                city = user_input.split(maxsplit=1)[1].split()[0] 
                species_list = search_species(city)  
                venomous_species = filter_venomous(species_list)  
                display_species(venomous_species)  
            else:
                city = user_input.split(maxsplit=1)[1].strip()  
                species_list = search_species(city)  
                display_species(species_list)  
        elif user_input.startswith('sightings'):
            _, species, city = user_input.split(maxsplit=2)  
            sightings = search_sightings(species, city)  
            display_sightings(sightings)  
        elif user_input == 'venomous':
            city = input("Enter city: ").strip()  
            species_list = search_species(city)  
            venomous_species = filter_venomous(species_list)  
            display_species(venomous_species)  
        else:
            print("Invalid command. Please enter 'help', 'exit', 'species <city>', 'sightings <species>, <city>', or 'venomous'.")


if __name__ == "__main__":
    main()
# Task 5 End #

