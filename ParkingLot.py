import heapq
class ParkingLotSystem:
    
    ''' This class is used to store information about Parking Lot. It stores total number of slots, available slots, information of the car and driver parked at a slot'''
    
    def __init__(self):
        self.number_of_slots = 0
        self.available_slots = []
        self.slot_info = dict()
        self.vehicle_numbers = dict()
        self.age_groups = dict()
        
    def CreateParkingLot(self, number_of_slots):
        
        ''' Initializes a heap which stores all available slots '''
        
        if number_of_slots <= 0:
            return None
        self.number_of_slots = number_of_slots
        for slot_num in range(1, self.number_of_slots + 1):
            self.available_slots.append(slot_num)
        heapq.heapify(self.available_slots)
        ret_data = (self.number_of_slots, )
        return ret_data
            

    def Park(self, veh_reg_no, driver_age):
        
        ''' Allocates nearest available slot and stores the information about driver and car '''

        if len(self.available_slots) == 0 or driver_age <= 0:
            return None

        nearest_available_slot = heapq.heappop(self.available_slots)
        self.slot_info[nearest_available_slot] = (veh_reg_no, driver_age)
        self.vehicle_numbers[veh_reg_no] = nearest_available_slot
        if self.age_groups.get(driver_age) is not None:
            self.age_groups[driver_age].append((veh_reg_no, nearest_available_slot))
        else:
            self.age_groups[driver_age] = [(veh_reg_no, nearest_available_slot)]
            
        ret_data = (veh_reg_no, nearest_available_slot)
        return ret_data
        

    def SlotNumbersForDriverOfAge(self, driver_age):
        
        ''' Retrieves all the slot numbers of drivers of given age '''

        ret_data = None
        if self.age_groups.get(driver_age) is not None and len(self.age_groups.get(driver_age)) > 0:
            ret_data = ",".join(str(driver_info[1]) for driver_info in self.age_groups[driver_age])

        return ret_data

    def SlotNumberForCarWithNumber(self, veh_no):

        ''' Retrieves slot number of car with given Vehicle Number '''

        ret_data = None
        if self.vehicle_numbers.get(veh_no) is not None:
            ret_data = "{}".format(self.vehicle_numbers[veh_no])
        
        return ret_data

    def Leave(self, slot_num):

        ''' Deletes all the records of car which left at a particular slot'''

        if self.slot_info.get(slot_num) is None:
            return None
        
        veh_reg_no, driver_age = self.slot_info.get(slot_num)
        heapq.heappush(self.available_slots, slot_num)
        self.slot_info.pop(slot_num)
        self.age_groups[driver_age].remove((veh_reg_no, slot_num))
        self.vehicle_numbers.pop(veh_reg_no)
        ret_data = (slot_num, veh_reg_no, driver_age)
        return ret_data

    def VehicleRegistrationNumberForDriverOfAge(self, driver_age):

        ''' Retrieves vehicle registration numbers of all cars whose driver's age is given '''

        ret_data = None
        if self.age_groups.get(driver_age) is not None and len(self.age_groups.get(driver_age)) > 0:
            ret_data = ",".join(str(driver_info[0]) for driver_info in self.age_groups[driver_age])
        
        return ret_data

    def ClearAllData(self):
        
        ''' Clears all the allocated data '''
        
        self.available_slots.clear()
        self.slot_info.clear()
        self.vehicle_numbers.clear()
        self.age_groups.clear()
        



