'''
Name: Elijah Abel
Date: 4/15/2024
Assignment: unit 8 homework 1
'''

# Vehicle class here
class Vehicle:
    def __init__(self, num_wheels:int, num_occupants:int, color:str = 'black'):
        self.num_wheels = num_wheels
        self.num_occupants = num_occupants
        self.color = color
        self.max_occupants = 5

    def occupant_increase(self, num_of_additional_occupants):
        try:
            self.num_occupants += num_of_additional_occupants
            if self.num_occupants > self.max_occupants:
                raise ValueError
            else:
                return self.num_occupants
        except ValueError:
            print(f'You can have no more than {self.max_occupants} people in the vehicle.')
            self.num_occupants -= num_of_additional_occupants
    

def main():
    # question 2
    vehicle_1 = Vehicle(2, 1, 'red')
    vehicle_2 = Vehicle(18, 3, 'green')
    print(f'Vehicle one is carrying {vehicle_1.num_occupants} occupant.')
    print(f'Vehicle two is the color {vehicle_2.color}.')

    # question 3
    print(vehicle_1.num_occupants)
    vehicle_1.occupant_increase(6)
    print(vehicle_1.num_occupants)



if __name__ == '__main__':
    main()



