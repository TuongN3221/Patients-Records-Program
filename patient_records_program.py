# Patient Data
patient_name = ["John Doe","Jane Doe", "Bill Smith","Alena Gomeget_valid_commands","Arnold James","Jona Johnson"]
condition = ["Broken Arm", "Stomach Laceration","Kidney Stone","Intestinal Issues","Broken nose","Stroke" ]
hospital_room_number = ["328","329","214","410","407","414"]
nights_stayed = [2, 1, 3, 4, 5, 7]
patient_procedure = ["Surgery","Stitches","Monitored Passage","Gastronomy", "Reconstructive Surgery","Stint"]
procedure_cost = [5000, 2400, 500, 1700, 14000, 400000]
room_charge = [340, 340, 340, 340, 340, 340]
insurance_company = ["Aetna","Humana","Blue Cross","United Health Care","Cigna","Kaiser Permanente"]
copayment = [750, 0.1, 0.15, 0.12, 0.15, 500]
patient_dob = ["01/23/1999", "07/22/1984", "03/03/2001", "06/02/2013", "09/01/1943", "12/23/2000"]
# The above data will be stored into a file called patient_records.txt
with open("patient_records.txt", "w") as file:
  for i in range(len(patient_name)):
    file.write(f"Patient: {patient_name[i]}\n")
    file.write(f"Date of Birth: {patient_dob[i]}\n")
    file.write(f"Condition: {condition[i]}\n")
    file.write(f"Room Number: {hospital_room_number[i]}\n")
    file.write(f"Night Stayed: {nights_stayed[i]}\n")
    file.write(f"Patient Procedure: {patient_procedure[i]}\n")
    file.write(f"Procedure Cost: {procedure_cost[i]}\n")
    file.write(f"Room Charge: {room_charge[i]}\n")
    file.write(f"Insurance Company: {insurance_company[i]}\n")
    file.write(f"Copayment: {copayment[i]}\n")
    file.write("\n")  # Add a blank line between records
# The above data will be stored into a file called patient_records.txt


# Input commands for program to function
def get_valid_commands():
  return [str(i) for i in range(1, len(patient_name) + 1)]

# Function for the program's Main Menu
def main_menu():
  while True:
    print("\n   --- Hospital Admittance System---   ")
    print("\nTo update a patient, select 1\nTo add a new patient, select 2\nTo Request patient information, select 3\nTo request patient's bill, select 4\nTo view current patients, select 5\nTo terminate program program, select 6\n")
    selection = input("\nWhat do you want to do?")
    if selection == "1":
      print("\n   --- Update Patient---   ")
      update_patient()
    elif selection == "2":
      print("\n   --- Add New Patient---   ")
      add_patient()
    elif selection == "3":
      print("\n   --- Access Patient Records---   ")
      patient_info()
    elif selection == "4":
      print("\n   --- Patient Billing---   ")
      patient_billing()
    elif selection == "5":
      print("\n   --- Current Patients---   ")  
      current_patients()
    elif selection == "6":
      print("\n   --- Terminate Program---   ")
      close_program()
      break
    else: 
      print("\nInvalid Selection. Select a Number between 1 and 4")

# Function to update patient information
def update_patient():
  patient_index = input("\nWhich Patient is being replaced?")
  valid_commands = get_valid_commands()
  total_patients = len(patient_name)
  print(f"\nTotal number of patients: {total_patients}")
  if patient_index in valid_commands:
    patient_index = int(patient_index)
    patient_index = patient_index - 1
    patient_name[patient_index] = input("\nInput Patient Name: ")
    # Validate DOB format
    while True:
      dob = input("\nInput Date of Birth (MM/DD/YYYY): ")
      if len(dob) == 10 and dob[2] == '/' and dob[5] == '/':
        patient_dob[patient_index] = dob
        break
      else:
        print("Invalid Format. Use MM/DD/YYYY (e.g., 1/23/1999)")
    hospital_room_number[patient_index] = input("\nInput room number: ")
    insurance_company[patient_index] = input("\nInput Insurance name: ")
    copayment[patient_index] = input("\nInput Insurance co-payment or percentage:")
    condition[patient_index] = input("\nInput reason for admittance: ")
    patient_procedure[patient_index] = input("\nInput Treatment plan: ")
    print("\nRecord of New Patient:", 
          "\nName:",patient_name[patient_index], 
          "\nRoom Number:",hospital_room_number[patient_index], 
          "\nInsurance:", insurance_company[patient_index],
          "\nCopayment:",copayment[patient_index], 
          "\nCondition:",condition[patient_index], 
          "\nProcedure:",patient_procedure[patient_index])
    print("\nPatient record has been updated.")
    main_menu()
  else:
    print("\nInvalid entry! Enter 1-{}!".format(total_patients))
    update_patient()
    
# Function to add a new patient    
def add_patient():
  # Inputs to add the new patient to the hospital records
  new_patient = input("\nEnter Patient Name: ")
  # Validates DOB format (MM/DD/YYYY)
  while True:
    new_dob = input("Enter Patient Date of Birth (MM/DD/YYYY): ")
    if len(new_dob) == 10 and new_dob[2] and new_dob[5] == '/':
      break 
    else:
      print("Invalid Format. Use MM/DD/YYYY (e.g., 01/23/1999)")
  new_condition = input("Enter Patient Condition: ")
  new_room = input("Input Patient Room: ")
  new_procedure = input("Enter Procedure: ")
  #  Validates Procedure Cost Input (Whole Number)
  while True:
    try:
      new_procedure_cost = float(input("Enter Procedure Cost: "))
      if new_procedure_cost.is_integer():
        new_procedure_cost = int(new_procedure_cost)
        break
      else:
        print("Procedure cost must be a whole number. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a valid whole number.")
  new_insurance = input("Enter Patient's Insurance: ")
  
  # Validates Co-payment Input (Percent or Whole Number)
  copay_input = input("Enter co-payment (fixed amount) or percentage (e.g., 0.15 for 15%): ")
  try:
    if '.' in copay_input:
      copayment.append(float(copay_input))
    else:
      copayment.append(int(copay_input))
  except ValueError:
    print("INVALID CO-PAYMENT INPUT. SETTING COPAYMENT TO 0")
    copayment.append(0)

  # Adds the new patient to the arrays
  patient_name.append(new_patient)
  condition.append(new_condition)
  hospital_room_number.append(new_room)
  nights_stayed.append(0)# Nights stayed set to zero due to patient being recently admitted
  patient_procedure.append(new_procedure)
  procedure_cost.append(new_procedure_cost)
  room_charge.append(340) # Default room charge for patients
  insurance_company.append(new_insurance)
  patient_dob.append(new_dob)

  # Store the new patient data in the file
  store_patient_data()
  # Print the new patient record notification
  print(f"Patient {new_patient} has been added to the system.")

  main_menu()

# Function to print patient records
def patient_info():
  total_patients = len(patient_name)
  print(f"\nTotal number of patients: {total_patients}")
  valid_commands = get_valid_commands()
  patient_index = input("\nSelect a patient to view info. Enter 1-{}: ".format(total_patients))

  if patient_index in valid_commands:
    patient_index = int(patient_index)
    patient_index = patient_index - 1
    print ("\nRecord of Requested Patient:", 
           "\nPatient:", patient_name[patient_index],
           "\nPatient Date of Birth:", patient_dob[patient_index],
           "\nRoom Number:", hospital_room_number[patient_index], 
           "\nInsurance:", insurance_company[patient_index], 
           "\nCo-payment:", copayment[patient_index], 
           "\nCondition: ", condition[patient_index], 
           "\nProcedure: ", patient_procedure[patient_index])
    main_menu()

  else:
    print("\nInvalid Entry. Enter 1-{}.".format(total_patients))
    patient_info()

# Function view patient billing information
def patient_billing():
  total_patients = len(patient_name)
  valid_commands = get_valid_commands()
  print(f"\nTotal number of patients: {total_patients}")

  patient_index = input("\nSelect a patient to their Billing Information")
  if patient_index in valid_commands:
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
    print("\nInvalid Entry. Enter a number from 1-{}.".format(total_patients))

# Function to check patients currently admitted
def current_patients():
    total_patients = len(patient_name)
    print(f"\nTotal Number of Patients: {total_patients}")
    print("\nPatient Names:")
    for i, name in enumerate(patient_name, start=1):
        print(f"{i}. {name}")
    main_menu()

# Method to store a newly added patient to patient_records.txt
def store_patient_data():
    with open("patient_records.txt", "a") as file:
        file.write(f"Patient: {patient_name[-1]}\n")
        file.write(f"Date of Birth: {patient_dob[-1]}\n")
        file.write(f"Condition: {condition[-1]}\n")
        file.write(f"Room Number: {hospital_room_number[-1]}\n")
        file.write(f"Night Stayed: {nights_stayed[-1]}\n")
        file.write(f"Patient Procedure: {patient_procedure[-1]}\n")
        file.write(f"Procedure Cost: {procedure_cost[-1]}\n")
        file.write(f"Room Charge: {room_charge[-1]}\n")
        file.write(f"Insurance Company: {insurance_company[-1]}\n")
        file.write(f"Copayment: {copayment[-1]}\n")
        file.write("\n")  # Add a blank line between records


# Funciton to terminate the program 
def close_program():
  print("\nThis program is terminated!\nHave a nice day!")

# Run the program
main_menu()