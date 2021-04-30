import sys
from ParkingLot import ParkingLotSystem

def main():
    input_file = sys.argv[1]
    content = []
    parkingLotSystem = ParkingLotSystem()
    with open(input_file) as f:
        content = f.readlines()
    for command in content:
        input_data = command.split()
        output = None
        base_command = input_data[0]
        
        if base_command == "Create_parking_lot":
            number_of_slots = int(input_data[1])
            ret_data = parkingLotSystem.CreateParkingLot(number_of_slots)
            output = "Created parking of {} slots".format(ret_data[0])
            
        elif base_command == "Park":
            veh_reg_no = input_data[1]
            driver_age = input_data[3]
            ret_data = parkingLotSystem.Park(veh_reg_no, driver_age)
            if ret_data == 0:
                output = "No Slots available"
            else:
                output = "Car with vehicle registration number \"{}\" has been parked at slot number {}".format(ret_data[0], ret_data[1])
            
        elif base_command == "Slot_numbers_for_driver_of_age":
            driver_age = input_data[1]
            ret_data = parkingLotSystem.SlotNumbersForDriverOfAge(driver_age)
        
        elif base_command == "Slot_number_for_car_with_number":
            veh_no = input_data[1]
            ret_data = parkingLotSystem.SlotNumberForCarWithNumber(veh_no)
            
        elif base_command == "Leave":
            slot_num = int(input_data[1])
            ret_data = parkingLotSystem.Leave(slot_num)
            output = "Slot number {} vacated, the car with vehicle registration number \"{}\" left the space, the driver of the car was of age {}".format(ret_data[0], ret_data[1], ret_data[2])
            
        elif base_command == "Vehicle_registration_number_for_driver_of_age":
            driver_age = input_data[1]
            ret_data = parkingLotSystem.VehicleRegistrationNumberForDriverOfAge(driver_age)

        if not output and ret_data:
            output = ret_data
        elif ret_data is None:
            output = "No parked car matches the query"
            
        print(output)
    parkingLotSystem.ClearAllData()
main()
