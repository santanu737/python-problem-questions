"""
Hospital Management System - Main Program
Ties together all six modules of the case study:

    1. Patient Registration      -> Dictionary        (01_patient.py)
    2. Appointment Scheduling    -> List               (02_appointment.py)
    3. Medical Records Storage   -> File Handling       (03_medical_records.py)
    4. Doctor Information        -> Tuple               (04_doctor.py)
    5. Billing System            -> Class and Object    (05_billing.py)
    6. Report Generation         -> Python Libraries    (06_report.py)

Run this file to interact with the whole system through one menu.
"""

import importlib

patient_mod = importlib.import_module("01_patient")
appointment_mod = importlib.import_module("02_appointment")
records_mod = importlib.import_module("03_medical_records")
doctor_mod = importlib.import_module("04_doctor")
billing_mod = importlib.import_module("05_billing")
report_mod = importlib.import_module("06_report")

# Keep bill totals here so the report module can summarize them later
bill_totals = []


def seed_demo_data():
    """Preload some sample data so the menu has something to show immediately."""
    patient_mod.register_patient("P101", "Ravi Kumar", 34, "Male", "9876543210", "Fever")
    patient_mod.register_patient("P102", "Anita Das", 29, "Female", "9123456780", "Fracture")

    doctor_mod.add_doctor("D01", "Dr. Sanjay Roy", "Cardiology", 12, 800)
    doctor_mod.add_doctor("D02", "Dr. Meera Sen", "Orthopedics", 8, 600)

    appointment_mod.schedule_appointment("P101", "D01", "2026-09-12", "10:30")
    appointment_mod.schedule_appointment("P102", "D02", "2026-09-13", "09:00")


def menu():
    print("""
========= HOSPITAL MANAGEMENT SYSTEM =========
 1. Register a new patient
 2. View all patients
 3. Add a doctor
 4. View all doctors
 5. Schedule an appointment
 6. View all appointments
 7. Save a medical record
 8. View a patient's medical history
 9. Generate a bill
10. Generate CSV + billing summary report
 0. Exit
================================================
""")


def run():
    seed_demo_data()

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = input("Patient ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            contact = input("Contact: ")
            disease = input("Disease: ")
            patient_mod.register_patient(pid, name, age, gender, contact, disease)

        elif choice == "2":
            patient_mod.list_all_patients()

        elif choice == "3":
            did = input("Doctor ID: ")
            name = input("Name: ")
            spec = input("Specialization: ")
            exp = int(input("Experience (years): "))
            fee = int(input("Consultation Fee: "))
            doctor_mod.add_doctor(did, name, spec, exp, fee)

        elif choice == "4":
            doctor_mod.list_all_doctors()

        elif choice == "5":
            pid = input("Patient ID: ")
            did = input("Doctor ID: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            appointment_mod.schedule_appointment(pid, did, date, time)

        elif choice == "6":
            appointment_mod.view_all_appointments()

        elif choice == "7":
            pid = input("Patient ID: ")
            diagnosis = input("Diagnosis: ")
            treatment = input("Treatment: ")
            records_mod.save_record(pid, diagnosis, treatment)

        elif choice == "8":
            pid = input("Patient ID: ")
            records_mod.view_record(pid)

        elif choice == "9":
            pid = input("Patient ID: ")
            name = input("Patient Name: ")
            cf = int(input("Consultation Fee: "))
            mc = int(input("Medicine Cost: "))
            rc = int(input("Room Charge: "))
            oc = int(input("Other Charges: "))
            bill = billing_mod.Bill(pid, name, cf, mc, rc, oc)
            total = bill.generate_invoice()
            bill_totals.append(total)

        elif choice == "10":
            report_mod.generate_patient_report(patient_mod.patients)
            report_mod.generate_billing_summary(bill_totals)

        elif choice == "0":
            print("Exiting Hospital Management System. Goodbye!")
            break

        else:
            print("[!] Invalid choice, try again.")


if __name__ == "__main__":
    run()
