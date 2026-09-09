"""
Module 3: Medical Records Storage
Concept Used: FILE HANDLING

Why File Handling?
- Medical records must persist even after the program closes (unlike an
  in-memory dictionary or list). Writing to disk keeps a permanent, auditable
  history for each patient.

Structure:
    One plain-text file per patient: records/<patient_id>.txt
    Each visit is appended as a new, timestamped line.
"""

import os
from datetime import datetime

RECORDS_DIR = "records"


def _ensure_dir():
    """Make sure the records folder exists before writing to it."""
    if not os.path.exists(RECORDS_DIR):
        os.makedirs(RECORDS_DIR)


def save_record(patient_id, diagnosis, treatment):
    """Append a new medical record entry for a patient (write mode: append)."""
    _ensure_dir()
    filepath = os.path.join(RECORDS_DIR, f"{patient_id}.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] Diagnosis: {diagnosis} | Treatment: {treatment}\n")
    print(f"[+] Record saved for Patient {patient_id}.")


def view_record(patient_id):
    """Read and print the full medical history of one patient."""
    filepath = os.path.join(RECORDS_DIR, f"{patient_id}.txt")
    if not os.path.exists(filepath):
        print(f"[!] No records found for Patient {patient_id}.")
        return
    print(f"\n--- Medical History: Patient {patient_id} ---")
    with open(filepath, "r") as f:
        print(f.read())


def view_all_records():
    """List every patient that has a records file, and print their history."""
    _ensure_dir()
    files = os.listdir(RECORDS_DIR)
    if not files:
        print("No medical records stored yet.")
        return
    for filename in files:
        patient_id = filename.replace(".txt", "")
        view_record(patient_id)


# ---- Demo run when executed directly ----
if __name__ == "__main__":
    save_record("P101", "Typhoid", "Antibiotics + rest for 7 days")
    save_record("P101", "Follow-up checkup", "Recovered, no medication needed")
    save_record("P103", "Fracture (left arm)", "Cast applied, review after 3 weeks")
    view_record("P101")
    view_all_records()
