# Patient Data
patient_name = ["John Doe","Jane Doe", "Bill Smith","Alena Gomeinput_commands","Arnold James","Jona Johnson"]
condition = ["Broken Arm", "Stomach Laceration","Kidney Stone","Intestinal issues","Broken nose","stroke" ]
hospital_room_number = ["328","329","214","410","407","414"]
nights_stayed = [2, 1, 3, 4, 5, 7]
patient_proceedure = ["Surgery","Stitches","Monitored passage","Gastronomy", "Reconstructive surgery","Stint"]
procedure_cost = [5000, 2400, 500, 1700, 14000, 400000]
room_charge = [325, 325, 325, 340, 340, 340]
insurance_company = ["Aetna","Humana","Blue Cross","United Health Care","Cigna","Kaiser Permanente"]
copayment = [750, 0.1, 0.15, 0.12, 0.15, 500]

# Input commands for program to function
input_commands = ["1","2","3","4","5","6"]

# Function for the program's Main Menu
def main_menu():
  while True:
    print("\n   --- Hospital Admittance System---   ")
    print("\nTo update a patient, select 1\nTo Request patient information, select 2\nTo request patient's bill, select 3\nTo view current patients, select 4\nTo terminate program program, select 5\n")
    selection = input("\nWhat do you want to do?")
    if selection == "1":
      print("\n   --- Update Patient---   ")
      update_patient()
    elif selection == "2":
      print("\n   --- Patient Records---   ")
      patient_info()
    elif selection == "3":
      print("\n   --- Patient Billing---   ")
      patient_billing()
    elif selection == "4":
      print("\n   --- Current Patients---   ")  
      current_patients()
    elif selection == "5":
      print("\n   --- Terminate Program---   ")
      close_program()
      break
    else: 
      print("\nInvalid Selection. Select a Number between 1 and 4")

# Function to update patient information
def update_patient():
  patient_index = input("\nWhich Patient is being replaced? Enter 1-6. ")
  if patient_index in input_commands:
    patient_index = int(patient_index)
    patient_index = patient_index - 1
    patient_name[patient_index] = input("\nInput Patient Name: ")
    hospital_room_number[patient_index] = input("\nInput room number: ")
    insurance_company[patient_index] = input("\nInput Insurance name: ")
    copayment[patient_index] = input("\nInput Insurance co-payment or percentage:")
    condition[patient_index] = input("\nInput reason for admittance: ")
    patient_proceedure[patient_index] = input("\nInput Treatment plan: ")
    print("\nRecord of New Patient:", 
          "\nName:",patient_name[patient_index], 
          "\nRoom Number:",hospital_room_number[patient_index], 
          "\nInsurance:", insurance_company[patient_index],
          "\nCopayment:",copayment[patient_index], 
          "\nCondition:",condition[patient_index], 
          "\nProcedure:",patient_proceedure[patient_index])

  else:
    print("\nInvalid entry! Please enter a number 1 through 6!")
    update_patient()
    
# Function to print patient records
def patient_info():
  total_patients = len(patient_name)
  print(f"\nTotal number of patients: {total_patients}")
  patient_index = (input("\nSelect a patient to view info. Enter 1-6. "))

  if patient_index in input_commands:
    patient_index = int(patient_index)
    patient_index = patient_index - 1
    print ("\nRecord of Requested Patient:", 
           "\nPatient:", patient_name[patient_index], 
           "\nRoom Number:", hospital_room_number[patient_index], 
           "\nInsurance:", insurance_company[patient_index], 
           "\nCo-payment:", copayment[patient_index], 
           "\nCondition: ", condition[patient_index], 
           "\nProcedure: ", patient_proceedure[patient_index])
    main_menu()

  else:
    print("\nInvalid Entry. Please enter a number 1 through 6.")
    patient_info()

# Function view patient billing information
def patient_billing():
  total_patients = len(patient_name)
  print(f"\nTotal number of patients: {total_patients}")

  patient_index = input("\nSelect a patient to their Billing Information? Enter 1-6. ")
  if patient_index in input_commands:
    patient_index = int(patient_index)
    patient_index = patient_index - 1

    if isinstance (copayment[patient_index], int):
      total = nights_stayed[patient_index] * room_charge[patient_index] + procedure_cost[patient_index]
      instotal = total - copayment[patient_index]
      print("\nTotal cost $"+ str(total))
      print("Total insurance pays $"+ str(instotal))
      print("Patient total due $"+ str(copayment[patient_index]))
      main_menu()

    else:
      total = nights_stayed[patient_index] * room_charge[patient_index] + procedure_cost[patient_index]
      ptotal = copayment[patient_index] * total 
      instotal = total - ptotal
      print("\nTotal cost $"+ str(total))
      print("Total insurance pays $"+ str(ptotal))
      print("Patient total due $"+ str(ptotal))
      main_menu()

  else:
    print("\nInvalid Entry! Please enter a number 1 through 6.")

def current_patients():
    total_patients = len(patient_name)
    print(f"\nTotal Number of Patients: {total_patients}")
    print("\nPatient Names:")
    for i, name in enumerate(patient_name, start=1):
        print(f"{i}. {name}")
    main_menu()

# Funciton to terminate the program 
def close_program():
  print("\nThis program is terminated!\nHave a nice day!")

# Run the program
main_menu()