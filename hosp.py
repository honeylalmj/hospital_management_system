""" Implement A hospital management system which inlcude these options 
1. Add Patient 2. Show patient info 3.Billing 4.exit.  
The patient data is a dictionary of list where list element is each patient 
information """
import json
class Hospital_Management_System():

    def __init__(self):
        self.patients = {}


    def get_integer_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("please Enter a valid number")
                

    def get_string_input(self, prompt):
        while True:
            value = input(prompt)
            if value.isnumeric():
                 print("Error: Please enter a valid string.")
            else:
                return value    
    def save_file(self) :
        with open("data.json", "w") as file :
           json.dump(self.patients,file)
           file.close()
    def load_file(self) :
        try:

            with open("data.json", "r") as file :
                patient_data = json.load(file)
                file.close()
            return patient_data    
        except (FileNotFoundError,json.decoder.JSONDecodeError,TypeError) :
            print("file not found or file is empty")
           
            return
    #Add patient
    def add(self):
        id_no = self.get_integer_input("Patient identification no:")
        name = self.get_string_input("Patient Name:")
        disease = self.get_string_input("Disease:")
        bill = self.get_integer_input("Bill Amount:")
        room_no = input("Room_no:")

        patient = [name,disease,bill,room_no]
        
        self.patients[id_no] = patient
        # print(self.patients)
        self.save_file()
        print("patient data has been added successfully to the system!!!")
    def show(self):
        patient_id = input("Enter the patient identification no:")
        self.patients = self.load_file()
        if self.patients :
            # print(self.patients)
            if patient_id in self.patients :
                detail = self.patients.get(patient_id)
                print("Patient Name:", detail[0])
                print("Disease:", detail[1])
                print("Bill Amount:", detail[2])
                print("Room Number:", detail[3])
            else :
                print("no data found")  
        else:
            print("no data found, may be due to database is missing or empty, Please add data")
            self.patients ={}
            return        
    def bill(self):
        bill_input = input("Enter the patient id to display the bill amount :")
        self.patients = self.load_file()
        if self.patients :
            if bill_input in self.patients :
                patient = self.patients.get(bill_input)
                print("Name of the patient:", patient[0])
                print("Total Bill Amount:", patient[2])
                updates = self.get_string_input("Do you want to update bill details (yes/no):").lower()
                if updates == "yes":
                    bill_value = self.get_integer_input("Enter the new bill value:")
                    patient[2] = bill_value
                    print("Patient's bill value has been updated successfully")
                    print("To check the updated bill amount, Type - 'show' & then enter patient id no :")
                    self.save_file()
            else:
                print("no data found")       
        else:
            print("no data found, may be due to database is missing or empty, Please add data")
            self.patients ={}
            return           
    def run(self):
        print("Welcome to XYZ hospital")
        while True: 
            
            print("Use the below mentioned commands for smooth running of software")
            print("'ADD' - To add the patient data")
            print("'Show' - To display the patient details")
            print("'Bill' - To dispaly the total bill amount of the patient")
            print("'q' - To exit the program")   
            patient_input = input().lower()
            if patient_input == "add":
                self.add()
            elif patient_input == "show":
                self.show()
            elif patient_input == "bill":
                self.bill()    
            elif patient_input == "q":
                exit()

if __name__ == "__main__":
    hosp = Hospital_Management_System()
    hosp.run()






