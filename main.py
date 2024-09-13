#This program is meant to list all cars and includes a function to search for them
AllowedVehiclesList = [
   'Ford F-150',
   'Chevrolet Silverado',
   'Tesla CyberTruck',
   'Toyota Tundra',
   'Nissan Titan'
]

#Define function to print the menu
def print_menu():
 print('********************************')
 print('AutoCountry Vehicle Finder v0.2')
 print('********************************')
 print('Please Enter the following number below from the following menu:')
 print('1. PRINT all Authorized Vehicles')
 print('2. SEARCH for Authorized Vehicle')
 print('3. Exit')
 print('********************************')  

#Define function to print the list of authorized vehicles
def print_vehicles():
  print('\nThe AutoCountry sales manager as authorized the purchase and selling of the following vehicles:')
  for vehicle in AllowedVehiclesList:
    print(vehicle)
  print ()

#Define function to search for a vehicle
def search_vehicle():
  vehicle_name = input('\nPlease Enter the full vehichle name: ')
  if vehicle_name in AllowedVehiclesList:
     print(f'\n{vehicle_name} is an authorized vehicle')
  else:
      print(f'\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.') 
  print () 

#Define the main loop
while True:
  print_menu()
  choice = input('\nEnter your choice:')

  if choice == '1':
    print_vehicles()
  elif choice == '2':
    search_vehicle()
  elif choice == '3':
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break
  else:
    print('Invalid choice, please try again')
    