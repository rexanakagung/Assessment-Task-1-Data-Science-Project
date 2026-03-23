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
            name = input("Enter Country followed by city: ")
            print(f"Searching for {name}'s details...") #Replace with function later
        elif choice == "2":
            print(f"Showing saved city's...") #Replace with function later
        elif choice == "3":
            print(f"Showing Favourited City's...") #Replace with function later
        elif choice == "4":
            print(f"\nSettings Menu") #Replace with function later
        elif choice == "5":
            print("Exiting Weather App.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()