"""
Module 6: Report Generation
Concept Used: PYTHON LIBRARIES

Why Libraries?
- Rather than writing CSV-formatting or statistics logic from scratch, Python's
  standard library already provides tested tools for exactly this:
    - csv        -> export structured data to a spreadsheet-friendly file
    - datetime   -> timestamp the report
    - statistics -> compute average / min / max of billing amounts
"""

import csv
import statistics
from datetime import datetime


def generate_patient_report(patients_dict, filename="patient_report.csv"):
    """Use the csv library to export the patient dictionary to a .csv file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Patient ID", "Name", "Age", "Gender", "Disease"])
        for pid, info in patients_dict.items():
            writer.writerow([pid, info["name"], info["age"],
                              info["gender"], info["disease"]])
    print(f"[+] Patient report exported to '{filename}'.")


def generate_billing_summary(bill_totals):
    """Use the statistics library to summarize a list of bill amounts."""
    if not bill_totals:
        print("No billing data available.")
        return

    total_revenue = sum(bill_totals)
    average_bill = statistics.mean(bill_totals)
    highest_bill = max(bill_totals)
    lowest_bill = min(bill_totals)

    print("\n--- Billing Summary Report ---")
    print(f"Generated on     : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Total Bills      : {len(bill_totals)}")
    print(f"Total Revenue    : Rs. {total_revenue}")
    print(f"Average Bill     : Rs. {average_bill:.2f}")
    print(f"Highest Bill     : Rs. {highest_bill}")
    print(f"Lowest Bill      : Rs. {lowest_bill}")


# ---- Demo run when executed directly ----
if __name__ == "__main__":
    sample_patients = {
        "P101": {"name": "Ravi Kumar", "age": 34, "gender": "Male", "disease": "Typhoid"},
        "P102": {"name": "Anita Das", "age": 29, "gender": "Female", "disease": "Fracture"},
    }
    sample_bills = [2550, 950, 1800]

    generate_patient_report(sample_patients)
    generate_billing_summary(sample_bills)
