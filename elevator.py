import time
import os

class Elevator:
    def __init__(self, id, current_floor=1):
        self.id = id
        self.current_floor = current_floor
        self.destination_floors = []
        self.direction = 'Idle'  # 'Up', 'Down', or 'Idle'
        self.status = 'Idle'     # 'Moving' or 'Idle'

    # Adds a destination floor to destination_floors and sorts it. Make sure to set status as Moving. Suppose we're at floor 1 and floor 5 and 3 come in, we sort so that we go from 1->3->5
    def add_destination(self, floor):
        return 

    # Set the direction the lift should travel in based on current_floor and destination_floors. If no destination_floors it should be Idle
    def update_direction(self):
        return

    def move(self):
        if self.direction == 'Up':
            self.current_floor += 1
        elif self.direction == 'Down':
            self.current_floor -= 1

    def step(self):
        if self.status == 'Moving':
            self.move()
            if self.current_floor == self.destination_floors[0]:
                self.destination_floors.pop(0)
                self.update_direction()

    def __str__(self):
        return f"Elevator {self.id}: Floor {self.current_floor}, Direction: {self.direction}, Destinations: {self.destination_floors}"

class Request:
    def __init__(self, current_floor, desired_floor):
        self.current_floor = current_floor
        self.desired_floor = desired_floor

class ElevatorControlSystem:
    def __init__(self, num_elevators, num_floors):
        self.elevators = [Elevator(id=i+1) for i in range(num_elevators)]
        self.num_floors = num_floors

    #This function determines which elevator should respond to a pickup request by finding the closest available elevator, preferring idle ones over busy ones. It assigns the selected elevator to stop at the request's current floor and then proceed to the desired floor.

    # Example:
    # Imagine there are three elevators:

    # Elevator A is on floor 2 and idle.
    # Elevator B is on floor 10 and moving down to floor 5.
    # Elevator C is on floor 7 and idle.
    # If a request is made from floor 6 to floor 8, the function chooses Elevator C since it is idle and closest to the request’s current floor. If all were busy, it would pick the one that could reach floor 6 the fastest.
    def pickup(self, request):
        return

    def step(self):
        for elevator in self.elevators:
            elevator.step()

    def status(self):
        for elevator in self.elevators:
            print(elevator)

    def draw_building(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        building = ''
        for floor in range(self.num_floors, 0, -1):
            floor_line = f"Floor {floor:2d} |"
            for elevator in self.elevators:
                if elevator.current_floor == floor:
                    floor_line += f" [E{elevator.id}] "
                else:
                    floor_line += " [   ] "
            building += floor_line + "\n"
        print(building)
        self.status()

def main():
    num_elevators = 3
    num_floors = 10
    ecs = ElevatorControlSystem(num_elevators, num_floors)
    print("Elevator Simulation Started")
    print("Enter requests in the format 'current_floor desired_floor'.")
    print("Press Enter without input to proceed to the next time step.")
    print("Enter 'q' to quit.")

    while True:
        ecs.draw_building()
        user_input = input("\nEnter your request or press Enter to proceed (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            break
        elif user_input == '':
            # Proceed to next time step
            ecs.step()
            print("\nTime step advanced by 1 second.\n")
            time.sleep(1)  # Simulate time passing
        else:
            try:
                current_floor, desired_floor = map(int, user_input.split())
                # Basic validation
                # if ....
                request = Request(current_floor, desired_floor)
                ecs.pickup(request)
                print(f"Request added: from floor {current_floor} to floor {desired_floor}")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

    print("Simulation ended.")

if __name__ == "__main__":
    main()
