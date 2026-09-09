"""
Module 5: Billing System
Concept Used: CLASS AND OBJECT (OOP)

Why a Class?
- A bill has its own data (fees, charges) AND its own behavior (calculating
  the total, printing an invoice). Bundling data + behavior together is
  exactly what a class is for. Each patient's bill becomes a separate
  object with its own independent values.
"""

from datetime import datetime


class Bill:
    """Represents one patient's hospital bill."""

    def __init__(self, patient_id, patient_name, consultation_fee=0,
                 medicine_cost=0, room_charge=0, other_charges=0):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.consultation_fee = consultation_fee
        self.medicine_cost = medicine_cost
        self.room_charge = room_charge
        self.other_charges = other_charges
        self.date = datetime.now().strftime("%Y-%m-%d")

    def calculate_total(self):
        """Sum all charges into a final bill amount."""
        return (self.consultation_fee + self.medicine_cost +
                self.room_charge + self.other_charges)

    def generate_invoice(self):
        """Print a formatted invoice for this bill object."""
        total = self.calculate_total()
        print("\n========= HOSPITAL INVOICE =========")
        print(f"Date            : {self.date}")
        print(f"Patient ID      : {self.patient_id}")
        print(f"Patient Name    : {self.patient_name}")
        print("-------------------------------------")
        print(f"Consultation Fee: Rs. {self.consultation_fee}")
        print(f"Medicine Cost   : Rs. {self.medicine_cost}")
        print(f"Room Charges    : Rs. {self.room_charge}")
        print(f"Other Charges   : Rs. {self.other_charges}")
        print("-------------------------------------")
        print(f"TOTAL AMOUNT    : Rs. {total}")
        print("=====================================")
        return total


# ---- Demo run when executed directly ----
if __name__ == "__main__":
    bill1 = Bill("P101", "Ravi Kumar", consultation_fee=800,
                 medicine_cost=450, room_charge=1200, other_charges=100)
    bill1.generate_invoice()

    bill2 = Bill("P103", "Suman Ghosh", consultation_fee=600,
                 medicine_cost=300, room_charge=0, other_charges=50)
    bill2.generate_invoice()
