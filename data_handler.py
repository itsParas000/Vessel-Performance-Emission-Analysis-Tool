"""
Data Handling Module

This module handles:
- validation
- report generation
- SQLite database operations
"""


import os
import sqlite3
from datetime import datetime

# database name

db_name = "Vessel_data.db"


# handle the validations

# 1. validate inputs

def validate_inputs(vessel_name, fuel_type, fuel_qty, cargo_weight, distance):
    
    valid_fuels = [ "VLSFO", "LSMGO", "LNG"]
    
    
    # Vessel Name Validation
    
    if vessel_name.strip() == "":
        return "Vessel name cannot be empty."
    
    
    # Fuel type validation
    
    if fuel_type not in valid_fuels:
        return "Invalid fuel type"
    
    
    # numeric Validation
    
    numeric_values = [ fuel_qty, cargo_weight, distance]
    
    
    for value in numeric_values:
        
        if not isinstance(value, (int, float)):
            return "Numeric fields must contain numbers."
        
        if value <= 0:
            return "Fuel, Distance, and Cargo must be greater than zero"
        
    
    
    # Logical Validation
    
    # Fuel Quantity can not exceed cargo weight
    if fuel_qty > cargo_weight:
        return "Fuel Quantity cannot exceed cargo weight"
    
    return None



# Setup database to store all the data into the database for future data analysis operation

# setup database


def setup_database():
    conn = sqlite3.connect(db_name)
    
    cursor = conn.cursor()
    
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS vessel_emissions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            vessel_name TEXT,
            report_date TEXT,

            fuel_type TEXT,
            fuel_qty REAL,

            distance REAL,
            cargo_weight REAL,

            total_co2 REAL,
            eeoi_score REAL,

            cii_rating TEXT,
            carbon_tax REAL
        )

    """)
    
    conn.commit()
    conn.close()
    
    
# Save data to sql


def save_to_sql(vessel_data):
    
    conn = sqlite3.connect(db_name)
    
    cursor = conn.cursor()
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""

        INSERT INTO vessel_emissions (

            vessel_name,
            report_date,

            fuel_type,
            fuel_qty,

            distance,
            cargo_weight,

            total_co2,
            eeoi_score,

            cii_rating,
            carbon_tax

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """,(
        
        vessel_data["vessel_name"],
        current_time,

        vessel_data["fuel_type"],
        vessel_data["fuel_qty"],

        vessel_data["distance"],
        vessel_data["cargo_weight"],

        vessel_data["total_co2"],
        vessel_data["eeoi"],

        vessel_data["rating"],
        vessel_data["tax"]
    ))
    
    conn.commit()
    conn.close()
        
        
# Save report file

def save_report(vessel_data):
    
    reports_folder = 'reports'
    
    
    # Create reports folder
    
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)
        
    
    file_path = (f"{reports_folder}/"
                f"{vessel_data['vessel_name']}_summary.txt")
    
    
    
    with open(file_path, "a") as file:
        
        file.write(f'Date:{datetime.now()}\n')
        
        file.write(
            f"Vessel: {vessel_data['vessel_name']}\n"
        )

        file.write(
            f"Fuel Type: {vessel_data['fuel_type']}\n"
        )

        file.write(
            f"Fuel Quantity: "
            f"{vessel_data['fuel_qty']} MT\n"
        )

        file.write(
            f"Distance: "
            f"{vessel_data['distance']} NM\n"
        )

        file.write(
            f"Cargo Weight: "
            f"{vessel_data['cargo_weight']} MT\n"
        )

        file.write(
            f"Total CO2: "
            f"{vessel_data['total_co2']} tons\n"
        )

        file.write(
            f"EEOI Score: "
            f"{vessel_data['eeoi']}\n"
        )

        file.write(
            f"CII Rating: "
            f"{vessel_data['rating']}\n"
        )

        file.write(
            f"Estimated Carbon Tax: "
            f"${vessel_data['tax']:,.2f}\n"
        )

        file.write("-" * 40 + "\n")
        
    return file_path
