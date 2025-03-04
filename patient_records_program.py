# Data
patient_name = ["John Doe","Jane Doe", "Bill Smith","Alena Gomez","Arnold James","Jona Johnson"]
condition = ["Broken Arm", "Stomach Laceration","Kidney Stone","Intestinal issues","Broken nose","stroke" ]
hospital_room_number = ["328","329","214","410","407","414"]
nights_stayed = [2, 1, 3, 4, 5, 7]
patient_proceedure = ["Surgery","Stitches","Monitored passage","Gastronomy", "Reconstructive surgery","Stint"]
procedure_cost = [5000, 2400, 500, 1700, 14000, 400000]
room_charge = [325, 325, 325, 340, 340, 340]
inscurance_company = ["Aetna","Humana","Blue Cross","United Health Care","Cigna","Kaiser Permanente"]
copayment = [750, 0.1, 0.15, 0.12, 0.15, 500]
# idiot check for if statement thing
z = ["1","2","3","4","5","6"]

print(patient_name,"\n",condition,"\n",hospital_room_number,"\n",nights_stayed,"\n",patient_proceedure,"\n",procedure_cost,"\n",room_charge,"\n",inscurance_company,"\n",copayment,"\n",z)

# Function for the program's main menu
def main_menu():
  while True:
    print("\n   --- Hospital Admitance---   ")
    print("\nTo update a patient, selectionect 1\nTo Request patient information, selectionect 2\nTo request patient's bill, selectionect 3\nTo terminate program program, selectionect 4\n")
    selection = input("\nWhat do you want to do?")
    if selection == "1":
      print("\n   --- Patient Update---   ")
      update_patient()
    elif selection == "2":
      print("\n   --- Patient Info---   ")
      patient_info()
    elif selection == "3":
      print("\n   --- Patient Bill---   ")
      patient_billing()
    elif selection == "4":
      print("\n   --- Terminate Program---   ")
      break
    else: 
      print("\nInvalid Selection. Select a Number between 1 and 4")

# Function to update patient information
def update_patient():
  a = input("\nWhich Patient is being replaced? Enter 1-6. ")
  if a in z:
    a = int(a)
    a = a - 1
    patient_name[a] = input("\nInput Patient Name: ")
    hospital_room_number[a] = input("\nInput room number: ")
    inscurance_company[a] = input("\nInput Insurance name: ")
    copayment[a] = input("\nInput Insurance co-payment or percentage:")
    condition[a] = input("\nInput reason for admittance: ")
    patient_proceedure[a] = input("\nInput Treatment plan: ")
    print("\nRecord of patient", patient_name[a], hospital_room_number[a], copayment[a], condition[a], patient_proceedure[a])
  else:
    print("\nInvalid entry! Please eter a number 1 through 6!")
    update_patient()
    
# print patient records
def patient_info():
  a = (input("\nSelect a patient to view info. Enter 1-6. "))
  if a in z:
    a = int(a)
    a = a - 1
    print ("\nRecord of patient", patient_name[a], hospital_room_number[a], inscurance_company[a], copayment[a], condition[a], patient_proceedure[a])
    main_menu()
  else:
    print("\nInvalid Entry! Please enter a number 1 through 6!")
    patient_info()

# print patient bill
def patient_billing():
  a = input("\nselectionect a patient to view bill? Enter 1-6. ")
  if a in z:
    a = int(a)
    a= a - 1
    if isinstance (copayment[a], int):
      total = nights_stayed[a] * room_charge[a] + procedure_cost[a]
      instotal = total - copayment[a]
      print("\nTotal cost $"+ str(total))
      print("Total insurance pays $"+ str(instotal))
      print("Patient total due $"+ str(copayment[a]))
      main_menu()
    else:
      total = nights_stayed[a] * room_charge[a] + procedure_cost[a]
      ptotal = copayment[a] * total 
      instotal = total - ptotal
      print("\nTotal cost $"+ str(total))
      print("Total insurance pays $"+ str(ptotal))
      print("Patient total due $"+ str(ptotal))
      main_menu()
  else:
    print("\nInvalid Entry! Please enter a number 1 through 6!")

# Funciton to terminate the program 
def close_program():
  print("\nThis program is terminated!\nHave a nice day!")
main_menu()