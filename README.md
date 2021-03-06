# ParkingLotSystem
Solution for Parking lot problem, where vehicles are to be assigned a nearest slot.

ParkingLotSystem -> Class which stores the data of Parking Lot and the vehicles parked along with driver details in it.

**Operations:**
Create Parking Lot:
    Creates a min heap of all available slots.
    
Park :
    Retrieve the nearest available slot from the min heap. Assign this slot to the vehicle. Store the details of slot number, driver age and vehicle number in hash maps for efficient retrieval of data.
    
Leave :
    When a vehicle is left from a given slot, delete all its associated data.
    
Slot Numbers for drivers with a given age:
    Retrieve all the slot numbers of the drivers of given age.
    
Vehicle Registration Numbers for drivers with a given age:
    Retrieve all the vehicle numbers of the drivers of given age.

Slot Number of a given Vehicle:
    Given a vehicle number, retrieve the slot in which it is parked.
  
**How to execute the program:**
1. Download all the files to local system.
2. Download latest version of python   
3. Open Command center in the main.py folder
4. Run the following commands in terminal:
python main.py <path_to_input_file_in_local_system>
python -m unittest ParkingLot_testcases.py
