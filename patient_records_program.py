#array namesn n= name, c = condition, hrn = hospital room number, ns= night stayed, pp = patient procedure, rc= room charge, isc= insurance company, cop= co-payment
n = ["John Doe","Jane Doe", "Bill Smith","Alena Gomez","Arnold James","Jona Johnson"]
c = ["Broken Arm", "Stomach Laceration","Kidney Stone","Intestinal issues","Broken nose","stroke" ]
hrn = ["328","329","214","410","407","414"]
ns = [2, 1, 3, 4, 5, 7]
pp = ["Surgery","Stitches","Monitored passage","Gastronomy", "Reconstructive surgery","Stint"]
pc = [5000, 2400, 500, 1700, 14000, 400000]
rc = [325, 325, 325, 340, 340, 340]
insc = ["Aetna","Humana","Blue Cross","United Health Care","Cigna","Kaiser Permanente"]
cop = [750, 0.1, 0.15, 0.12, 0.15, 500]
# idiot check for if statement thing
z = ["1","2","3","4","5","6"]

print(n,"\n",c,"\n",hrn,"\n",ns,"\n",pp,"\n",pc,"\n",rc,"\n",insc,"\n",cop,"\n",z)

#start func
def sf():
  print("\n   --- Hospital Admitance---   ")
  print("\nTo update a patient, select 1\nTo Request patient information, select 2\nTo request patient's bill, select 3\nTo terminate program program, select 4\n")
  sel = input("\nWhat do you want to do?")
  if sel == "1":
    print("\n   --- Patient Update---   ")
    padmit()
  elif sel == "2":
    print("\n   --- Patient Info---   ")
    pinfo()
  elif sel == "3":
    print("\n   --- Patient Bill---   ")
    pbill()
  elif sel == "4":
    print("\n   --- Terminate Program---   ")
  else:
    print("\nInvalid Entry! Please enter 1, 2, or 3!")
# update info func
def padmit():
  a = input("\nWhich Patient is being replaced? Enter 1-6. ")
  if a in z:
    a = int(a)
    a = a - 1
    n[a] = input("\nInput Patient Name: ")
    hrn[a] = input("\nInput room number: ")
    insc[a] = input("\nInput Insurance name: ")
    cop[a] = input("\nInput Insurance co-payment or percentage:")
    c[a] = input("\nInput reason for admittance: ")
    pp[a] = input("\nInput Treatment plan: ")
    print("\nRecord of patient", n[a], hrn[a], cop[a], c[a], pp[a])
  else:
    print("\nInvalid entry! Please eter a number 1 through 6!")
    padmit()
    
# print patient records
def pinfo():
  a = (input("\nSelect a patient to view info? Enter 1-6. "))
  if a in z:
    a = int(a)
    a = a - 1
    print ("\nRecord of patient", n[a], hrn[a], insc[a], cop[a], c[a], pp[a])
    sf()
  else:
    print("\nInvalid Entry! Please enter a number 1 through 6!")
    pinfo()

# print patient bill
def pbill():
  a = input("\nSelect a patient to view bill? Enter 1-6. ")
  if a in z:
    a = int(a)
    a= a - 1;
    if isinstance (cop[a], int):
      total = ns[a] * rc[a] + pc[a]
      instotal = total - cop[a]
      print("\nTotal cost $"+ str(total))
      print("Total insurance pays $"+ str(instotal))
      print("Patient total due $"+ str(cop[a]))
      sf()
    else:
      total = ns[a] * rc[a] + pc[a]
      ptotal = cop[a] * total 
      instotal = total - ptotal
      print("\nTotal cost $"+ str(total))
      print("Total insurance pays $"+ str(ptotal))
      print("Patient total due $"+ str(ptotal))
      sf()
  else:
    print("\nInvalid Entry! Please enter a number 1 through 6!")

def close():
  print("\nThis program is terminated!\nHave a nice day!")
sf()