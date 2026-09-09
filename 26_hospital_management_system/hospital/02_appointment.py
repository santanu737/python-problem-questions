"""
Module 2: Appointment Scheduling
Concept Used: LIST

Why a List?
- Appointments happen in a sequence and are naturally ordered by time.
- A list lets us easily append new appointments, iterate through the day's
  schedule in order, slice a date range, and sort by time.

Structure:
    appointments = [
        {"patient_id": str, "doctor_id": str, "date": str, "time": str},
        ...
    ]
"""

# List holding every scheduled appointment
appointments = []


def schedule_appointment(patient_id, doctor_id, date, time):
    """Add a new appointment to the list."""
    appointment = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }
    appointments.append(appointment)
    print(f"[+] Appointment scheduled: Patient {patient_id} with Doctor {doctor_id} "
          f"on {date} at {time}.")


def cancel_appointment(patient_id, date):
    """Remove the first matching appointment for a patient on a given date."""
    for appt in appointments:
        if appt["patient_id"] == patient_id and appt["date"] == date:
            appointments.remove(appt)
            print(f"[-] Appointment for Patient {patient_id} on {date} cancelled.")
            return True
    print(f"[!] No appointment found for Patient {patient_id} on {date}.")
    return False


def view_appointments_by_date(date):
    """List all appointments for a specific date."""
    day_appointments = [a for a in appointments if a["date"] == date]
    if not day_appointments:
        print(f"No appointments on {date}.")
        return
    print(f"\n--- Appointments on {date} ---")
    for a in sorted(day_appointments, key=lambda x: x["time"]):
        print(f"{a['time']} | Patient {a['patient_id']} -> Doctor {a['doctor_id']}")


def view_all_appointments():
    """Display every appointment currently scheduled."""
    if not appointments:
        print("No appointments scheduled yet.")
        return
    print("\n--- All Appointments ---")
    for a in appointments:
        print(f"{a['date']} {a['time']} | Patient {a['patient_id']} -> Doctor {a['doctor_id']}")


# ---- Demo run when executed directly ----
if __name__ == "__main__":
    schedule_appointment("P101", "D01", "2026-09-12", "10:30")
    schedule_appointment("P102", "D02", "2026-09-12", "09:00")
    schedule_appointment("P103", "D01", "2026-09-13", "11:00")
    view_all_appointments()
    view_appointments_by_date("2026-09-12")
    cancel_appointment("P102", "2026-09-12")
    view_appointments_by_date("2026-09-12")
