print("SMART BUS JOURNEY RECOMMENDATION AGENT")
while True:
    source = input("Enter your current location: ").lower()
    destination = input("Enter your destination: ").lower()
    print("\nChecking available buses\n")

    if source == "margao" and destination == "panaji":
        print("Available buses:")
        print("Bus 101 - Arrival: 5 min - Running - Fare: Rs.60")
        print("Bus 102 - Arrival: 8 min - Delayed - Fare: Rs.50")
        print("Bus 103 - Cancelled")
        print("\nAgent is checking the buses")
        print("\nRecommended Bus: 101")
        print("Arrival Time: 5 minutes")
        print("Status: Running")
        print("Fare: Rs.60")
        print("Reason: Fastest available bus with no delay.")

    elif source == "margao" and destination == "vasco":
        print("Available buses:")
        print("Bus 201 - Arrival: 7 min - Running - Fare: Rs.40")
        print("Bus 202 - Arrival: 12 min - Delayed - Fare: Rs.35")
        print("\nRecommended Bus: 201")
        print("Arrival Time: 7 minutes")
        print("Status: Running")
        print("Fare: Rs.40")
        print("Reason: Arrives earlier and has no delay.")

    else:
        print("\nNo bus information available for this route.")
        print("Please try another source and destination.")

    again = input("\nDo you want to search again? (yes/no): ").lower()

    if again == "no":
        print("\nThank you for using the Smart Bus Journey Recommendation Agent.")
        break

