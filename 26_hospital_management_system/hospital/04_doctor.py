"""
Module 4: Doctor Information
Concept Used: TUPLE

Why a Tuple?
- A doctor's core details (ID, name, specialization, experience, fee) rarely
  change once set, and shouldn't be accidentally modified elsewhere in the
  program. Tuples are immutable, so they protect this fixed record data.

Structure:
    doctors = [
        (doctor_id, name, specialization, experience_years, consultation_fee),
        ...
    ]
    (A list OF tuples: the list lets us keep adding doctors, while each
    individual doctor record stays immutable.)
"""

# List of immutable doctor-record tuples
doctors = []


def add_doctor(doctor_id, name, specialization, experience_years, fee):
    """Create a new doctor tuple and store it."""
    doctor_record = (doctor_id, name, specialization, experience_years, fee)
    doctors.append(doctor_record)
    print(f"[+] Doctor '{name}' ({specialization}) added with ID {doctor_id}.")


def view_doctor(doctor_id):
    """Find and display a single doctor's tuple by ID."""
    for d in doctors:
        if d[0] == doctor_id:
            print(f"\nDoctor ID     : {d[0]}")
            print(f"Name          : {d[1]}")
            print(f"Specialization: {d[2]}")
            print(f"Experience    : {d[3]} years")
            print(f"Fee           : Rs. {d[4]}")
            return d
    print(f"[!] No doctor found with ID {doctor_id}.")
    return None


def search_by_specialization(specialization):
    """Return all doctor tuples matching a given specialization."""
    matches = [d for d in doctors if d[2].lower() == specialization.lower()]
    if not matches:
        print(f"No doctors found for specialization '{specialization}'.")
        return []
    print(f"\n--- Doctors specializing in {specialization} ---")
    for d in matches:
        print(f"{d[0]} | {d[1]} | {d[3]} yrs experience | Rs. {d[4]}")
    return matches


def list_all_doctors():
    """Display every doctor on record."""
    if not doctors:
        print("No doctors added yet.")
        return
    print("\n--- All Doctors ---")
    for d in doctors:
        print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} yrs | Rs. {d[4]}")


# ---- Demo run when executed directly ----
if __name__ == "__main__":
    add_doctor("D01", "Dr. Sanjay Roy", "Cardiology", 12, 800)
    add_doctor("D02", "Dr. Meera Sen", "Orthopedics", 8, 600)
    add_doctor("D03", "Dr. Arjun Bose", "Cardiology", 15, 1000)
    list_all_doctors()
    view_doctor("D01")
    search_by_specialization("Cardiology")
