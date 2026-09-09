"""
Module 1: Patient Registration
Concept Used: DICTIONARY

Why a Dictionary?
- Each patient has a unique ID, and we need fast lookup by that ID.
- A dictionary gives O(1) average lookup, insert, update and delete by key,
  which is exactly what a registration desk needs.

Structure:
    patients = {
        patient_id (str): {
            "name": str,
            "age": int,
            "gender": str,
            "contact": str,
            "disease": str
        },
        ...
    }
"""

# Master dictionary holding all registered patients
patients = {}


def register_patient(patient_id, name, age, gender, contact, disease):
    """Add a new patient record to the dictionary."""
    if patient_id in patients:
        print(f"[!] Patient ID {patient_id} already exists.")
        return False
    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact,
        "disease": disease
    }
    print(f"[+] Patient '{name}' registered with ID {patient_id}.")
    return True


def view_patient(patient_id):
    """Look up a single patient by ID."""
    patient = patients.get(patient_id)
    if patient:
        print(f"\nPatient ID   : {patient_id}")
        print(f"Name         : {patient['name']}")
        print(f"Age          : {patient['age']}")
        print(f"Gender       : {patient['gender']}")
        print(f"Contact      : {patient['contact']}")
        print(f"Disease      : {patient['disease']}")
    else:
        print(f"[!] No patient found with ID {patient_id}.")
    return patient


def update_patient(patient_id, **fields):
    """Update one or more fields of an existing patient record."""
    if patient_id not in patients:
        print(f"[!] No patient found with ID {patient_id}.")
        return False
    patients[patient_id].update(fields)
    print(f"[+] Patient {patient_id} updated.")
    return True


def delete_patient(patient_id):
    """Remove a patient record."""
    if patient_id in patients:
        removed = patients.pop(patient_id)
        print(f"[-] Removed patient '{removed['name']}' (ID {patient_id}).")
        return True
    print(f"[!] No patient found with ID {patient_id}.")
    return False


def list_all_patients():
    """Display every registered patient."""
    if not patients:
        print("No patients registered yet.")
        return
    print("\n--- All Registered Patients ---")
    for pid, info in patients.items():
        print(f"{pid} | {info['name']} | Age {info['age']} | {info['disease']}")


# ---- Demo run when executed directly ----
if __name__ == "__main__":
    register_patient("P101", "Ravi Kumar", 34, "Male", "9876543210", "Fever")
    register_patient("P102", "Anita Das", 29, "Female", "9123456780", "Fracture")
    list_all_patients()
    view_patient("P101")
    update_patient("P101", disease="Typhoid")
    view_patient("P101")
    delete_patient("P102")
    list_all_patients()
