import sys
import heapq

class ParkingLotSystem:
    def __init__(self, number_of_slots):
        self.number_of_slots = number_of_slots
        self.available_slots = []
        self.slot_info = dict()
        self.vehicle_numbers = dict()
        self.age_groups = dict()
        
    def CreateParkingLot(self, input_data):
        self.number_of_slots = int(input_data[1])
        for slot_num in range(1, self.number_of_slots + 1):
            self.available_slots.append(slot_num)
            
        heapq.heapify(self.available_slots)
        print("Created parking of {} slots".format(self.number_of_slots))
            

    def Park(self, input_data):
        veh_reg_no = input_data[1]
        driver_age = input_data[3]
        nearest_available_slot = heapq.heappop(self.available_slots)
        self.slot_info[nearest_available_slot] = (veh_reg_no, driver_age)
        self.vehicle_numbers[veh_reg_no] = nearest_available_slot
        if self.age_groups.get(driver_age) is not None:
            self.age_groups[driver_age].append((veh_reg_no, nearest_available_slot))
        else:
            self.age_groups[driver_age] = [(veh_reg_no, nearest_available_slot)]
            
        print("Car with vehicle registration number \"{}\" has been parked at slot number {}".format(veh_reg_no, nearest_available_slot))
        

    def SlotNumbersForDriverOfAge(self, input_data):
        driver_age = input_data[1]
        if self.age_groups.get(driver_age) is not None:
            print(",".join(str(driver_info[1]) for driver_info in self.age_groups[driver_age]))
        else:
            print("No parked car matches the query")

    def SlotNumberForCarWithNumber(self, input_data):
        veh_no = input_data[1]
        if self.vehicle_numbers.get(veh_no) is not None:
            print("{}".format(self.vehicle_numbers[veh_no]))
        else:
            print("No parked car matches the query")

    def Leave(self, input_data):
        slot_num = int(input_data[1])
        heapq.heappush(self.available_slots, slot_num)
        veh_reg_no, driver_age = self.slot_info.get(slot_num)
        self.slot_info.pop(slot_num)
        print("Slot number {} vacated, the car with vehicle registration number \"{}\" left the space, the driver of the car was of age {}".format(slot_num, veh_reg_no, driver_age))

    def VehicleRegistrationNumberForDriverOfAge(self, input_data):
        driver_age = input_data[1]
        if self.age_groups.get(driver_age) is not None:
            print(",".join(str(driver_info[0]) for driver_info in self.age_groups[driver_age]))
        else:
            print("No parked car matches the query")

    
def main():
    input_file = sys.argv[1]
    content = []
    parkingLotSystem = ParkingLotSystem(0)
    with open(input_file) as f:
        content = f.readlines()
    for command in content:
        input_data = command.split()
        base_command = input_data[0]
        if base_command == "Create_parking_lot":
            parkingLotSystem.CreateParkingLot(input_data)
        elif base_command == "Park":
            parkingLotSystem.Park(input_data)
        elif base_command == "Slot_numbers_for_driver_of_age":
            parkingLotSystem.SlotNumbersForDriverOfAge(input_data)
        elif base_command == "Slot_number_for_car_with_number":
            parkingLotSystem.SlotNumberForCarWithNumber(input_data)
        elif base_command == "Leave":
            parkingLotSystem.Leave(input_data)
        elif base_command == "Vehicle_registration_number_for_driver_of_age":
            parkingLotSystem.VehicleRegistrationNumberForDriverOfAge(input_data)
main()
