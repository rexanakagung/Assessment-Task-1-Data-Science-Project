print("Welcome to the Weather App!")
input("Enter any letter to start: ")

def settings_menu():
    while True:
        print("\nSettings Menu")
        print("1. Change Timezone")
        print("2. Erase Favourited City's")
        print("3. Erase Saved City's")
        print("4. Unit Of Measurements")
        print("5. Back To Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Changing timezone...")  # Replace with real function later
        elif choice == "2":
            print("Erasing favourited cities...")  # Replace with real function later
        elif choice == "3":
            print("Erasing saved cities...")  # Replace with real function later
        elif choice == "4":
            print("Changing units...")  # Replace with real function later
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


from functions import get_city_info

def main():
    while True:
        print("\nWeather App Menu:")
        print("1. Search city")
        print("2. Saved City's")
        print("3. Favourite City's")
        print("4. Settings")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter city: ")
            print(f"Searching for {name}'s details...")
            city_info = get_city_info(name)
            if city_info:
                cit = (f"City: {city_info['location']['name']}")
                cou = (f"Country: {city_info['location']['country']}")
                lat = (f"Latitude: {city_info['location']['lat']}")
            
            print(cit)
            print(cou)
            print(lat)

        elif choice == "2":
            print("Showing saved city's...")  # Replace with function later

        elif choice == "3":
            print("Showing favourited city's...")  # Replace with function later

        elif choice == "4":
            settings_menu()  # Now opens the submenu properly

        elif choice == "5":
            print("Exiting Weather App.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()