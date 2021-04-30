import unittest
from ParkingLot import ParkingLotSystem

class TestParkingLotSystem(unittest.TestCase):
    ''' Class to test ParkingLot System '''
    
    def setUp(self):
        self.parkingLotSystem = ParkingLotSystem()
        
    def test_0_create_parking_lot(self):
        ''' Test if CreateParkingLot() creates the given number of slots '''
        
        ret_data = self.parkingLotSystem.CreateParkingLot(10)
        self.assertEqual(ret_data[0], 10)

    def test_1_park(self):
        ''' Test if Park() returns the nearest slots available ''' 
        
        self.parkingLotSystem.CreateParkingLot(10)
        for number in range(0, 10):
            veh_reg_no = "APZ1254U" + str(number)
            driver_age = 20 + number
            ret_data = self.parkingLotSystem.Park(veh_reg_no, driver_age)
            self.assertNotEqual(ret_data, 0)
            self.assertEqual(number + 1, ret_data[1]) 
        self.parkingLotSystem.Leave(9)
        self.parkingLotSystem.Leave(3)
        ret_data = self.parkingLotSystem.Park("ABCD13523", 34)

        #check if the nearest available slot is allocated 
        self.assertNotEqual(ret_data, 0)
        self.assertEqual(3, ret_data[1])
        
        self.parkingLotSystem.Park("ABBD13523", 34)
        ret_data = self.parkingLotSystem.Park("ABCB13523", 34)

        #Check if no slot is allocated as there is no available space
        self.assertEqual(ret_data, 0)

    def test_2_slot_numbers_for_driver_of_age(self):
        ''' Test if slot numbers of cars whose driver age is given are retrieved correctly'''
        
        self.parkingLotSystem.CreateParkingLot(10)
        for number in range(0, 10):
            veh_reg_no = "APZ1254U" + str(number)
            driver_age = 20 + (number%2)
            self.parkingLotSystem.Park(veh_reg_no, driver_age)
        self.assertEqual(self.parkingLotSystem.SlotNumbersForDriverOfAge(20), '1,3,5,7,9')
        self.assertEqual(self.parkingLotSystem.SlotNumbersForDriverOfAge(21), '2,4,6,8,10')

        #No Driver has the given age
        self.assertEqual(self.parkingLotSystem.SlotNumbersForDriverOfAge(22), None)


    def test_3_slot_number_for_car_with_number(self):
        ''' Test if the slot number for the given car is retrieved correctly '''
        
        self.parkingLotSystem.CreateParkingLot(10)
        for number in range(0, 10):
            veh_reg_no = "APZ1254U" + str(number)
            driver_age = 20 + (number%2)
            self.parkingLotSystem.Park(veh_reg_no, driver_age)
        self.assertEqual(self.parkingLotSystem.SlotNumberForCarWithNumber("APZ1254U0"), '1')
        self.assertEqual(self.parkingLotSystem.SlotNumberForCarWithNumber("APZ1254N0"), None)
        self.assertEqual(self.parkingLotSystem.SlotNumberForCarWithNumber("APZ1254U9"), '10')


    def test_4_leave(self):
        ''' Test leave the car at a particular slot '''
        
        self.parkingLotSystem.CreateParkingLot(10)
        for number in range(0, 10):
            veh_reg_no = "APZ1254U" + str(number)
            driver_age = 20 + (number%2)
            self.parkingLotSystem.Park(veh_reg_no, driver_age)
        ret = self.parkingLotSystem.Leave(9)
        self.assertEqual(ret[1], "APZ1254U8")
        ret = self.parkingLotSystem.Leave(2)
        self.assertEqual(ret[1], "APZ1254U1")
        ret = self.parkingLotSystem.Leave(8)
        self.assertEqual(ret[1], "APZ1254U7")
        ret = self.parkingLotSystem.Leave(8)

        #Slot is already empty
        self.assertEqual(ret, None)

    def test_5_vehicle_registration_number_for_driver_of_age(self):
        ''' Test if vehicle registration numbers of cars whose driver age is given are retrieved correctly '''
        self.parkingLotSystem.CreateParkingLot(10)
        for number in range(0, 4):
            veh_reg_no = "APZ1254U" + str(number)
            driver_age = 20 + (number%2)
            self.parkingLotSystem.Park(veh_reg_no, driver_age)
            
        self.assertEqual(self.parkingLotSystem.VehicleRegistrationNumberForDriverOfAge(20), 'APZ1254U0,APZ1254U2')
        self.assertEqual(self.parkingLotSystem.VehicleRegistrationNumberForDriverOfAge(21), 'APZ1254U1,APZ1254U3')

        #No driver of given age is available
        self.assertEqual(self.parkingLotSystem.VehicleRegistrationNumberForDriverOfAge(22), None)
        

    def tearDown(self):
        self.parkingLotSystem.ClearAllData()


