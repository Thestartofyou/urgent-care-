import random

# Define the maximum number of available seats at the urgent care
MAX_SEATS = 10

# Define the probabilities of seat availability based on time slots
TIME_SLOT_PROBABILITIES = {
    "morning": 0.8,
    "afternoon": 0.6,
    "evening": 0.4
}

# Track the number of booked appointments
booked_appointments = 0

# Function to calculate the probability of seat availability
def calculate_probability(time_slot):
    probability = TIME_SLOT_PROBABILITIES.get(time_slot, 0)
    return probability * (MAX_SEATS - booked_appointments) / MAX_SEATS

# Function to simulate a walk-in and check seat availability
def handle_walk_in(time_slot):
    probability = calculate_probability(time_slot)
    if random.random() < probability:
        print("Seat is available. Please proceed.")
    else:
        print("Sorry, no seats are available at the moment.")

# Function to book an appointment
def book_appointment():
    global booked_appointments
    booked_appointments += 1
    print("Appointment booked successfully.")

# Main program loop
while True:
    print("\n--- Urgent Care System ---")
    print("1. Handle Walk-in")
    print("2. Book Appointment")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        time_slot = input("Enter the time slot (morning/afternoon/evening): ")
        handle_walk_in(time_slot.lower())
    elif choice == "2":
        book_appointment()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
