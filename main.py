import sys
from ParkingLot import ParkingLotSystem
from Constants import *

def main():
    input_file = sys.argv[1]
    content = []
    parkingLotSystem = ParkingLotSystem()
    with open(input_file) as f:
        content = f.readlines()
    for command in content:
        input_data = command.split()
        output = None
        if len(input_data) == 0:
            print("Invalid command")
            continue
        base_command = input_data[0]
        
        if base_command == CREATE_PARKING_LOT:
            number_of_slots = int(input_data[1])
            ret_data = parkingLotSystem.CreateParkingLot(number_of_slots)
            output = "Created parking of {} slots".format(ret_data[0])
            
        elif base_command == PARK:
            veh_reg_no = input_data[1]
            driver_age = input_data[3]
            ret_data = parkingLotSystem.Park(veh_reg_no, driver_age)
            if ret_data == None:
                output = "No available Slots"
            else:
                output = "Car with vehicle registration number \"{}\" has been parked at slot number {}".format(ret_data[0], ret_data[1])
            
        elif base_command == SLOT_NUMBERS_FOR_DRIVER_OF_AGE:
            driver_age = input_data[1]
            ret_data = parkingLotSystem.SlotNumbersForDriverOfAge(driver_age)
        
        elif base_command == SLOT_NUMBER_FOR_CAR_WITH_NUMBER:
            veh_no = input_data[1]
            ret_data = parkingLotSystem.SlotNumberForCarWithNumber(veh_no)
            
        elif base_command == LEAVE:
            slot_num = int(input_data[1])
            ret_data = parkingLotSystem.Leave(slot_num)
            output = "Slot number {} vacated, the car with vehicle registration number \"{}\" left the space, the driver of the car was of age {}".format(ret_data[0], ret_data[1], ret_data[2])
            
        elif base_command == VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE:
            driver_age = input_data[1]
            ret_data = parkingLotSystem.VehicleRegistrationNumberForDriverOfAge(driver_age)

        if not output and ret_data:
            output = ret_data
        elif ret_data is None:
            output = "No parked car matches the query"
            
        print(output)
        
    parkingLotSystem.ClearAllData()
main()
