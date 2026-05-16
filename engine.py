
"""
Core Maritime Emission & Performance Calculation Engine

This module handles:
- fuel emission factors
- CO₂ calculations
- EEOI calculations
- IMO-inspired CII ratings
- estimated carbon tax calculations

NOTE:
This project uses simplified IMO-inspired logic
for educational and analytical purposes.
"""


# fuel data with emission factor

fuel_data = {
    "VLSFO":{
        "cf": 3.114
    },
    
    "LSMGO":{
        "cf": 3.206
    },
    
    "LNG":{
        "cf": 2.750
    }
}


# fuel info
# define the function to get the info about the fuel type

def get_fuel_info(fuel_type):
    
    return fuel_data.get(fuel_type)



# CO₂ Emission Calculation
# define the function to get the CO₂ Emission

def calculate_co2(fuel_qty, carbon_factor):
    
    total_co2 = fuel_qty * carbon_factor
    
    return round(total_co2, 2)



# EEOI Calculation
# define the function to get the EEOI(Energy Efficiency Operational Indicator)

def calculate_eeoi(total_co2, cargo_weight, distance):
    
    if cargo_weight <= 0 or distance <= 0:
        return 0.0
    
    eeoi = (
        (total_co2 * 1000000)/
        (cargo_weight * distance)
    )
    
    return round(eeoi, 2)



# CII Rating Function
# define the fucntion to calculate and the the grade of CII(Carbon Intensity Indicator)


# Simplified IMO-based CII Rating Logic
def calculate_cii(attained_cii, required_cii = 10.00, vessel_type = 'bulk_carrier'):
    
    imo_boundaries = {

        "bulk_carrier": {
            "d1": 0.86,
            "d2": 0.94,
            "d3": 1.06,
            "d4": 1.18
        },

        "tanker": {
            "d1": 0.82,
            "d2": 0.93,
            "d3": 1.08,
            "d4": 1.28
        },

        "container_ship": {
            "d1": 0.83,
            "d2": 0.94,
            "d3": 1.07,
            "d4": 1.19
        },

        "general_cargo": {
            "d1": 0.83,
            "d2": 0.94,
            "d3": 1.06,
            "d4": 1.19
        },

        "gas_carrier": {
            "d1": 0.85,
            "d2": 0.95,
            "d3": 1.06,
            "d4": 1.25
        },

        "cruise_passenger": {
            "d1": 0.87,
            "d2": 0.95,
            "d3": 1.06,
            "d4": 1.16
        }
    }
    
    
    # fallback to bulk_carrier if vessel type is invalid    
    
    if vessel_type not in imo_boundaries:
        vessel_type = 'bulk_carrier'
       
    # to store the vessel_type factors
    
    factors = imo_boundaries[vessel_type]
    
    threshold_A = required_cii * factors['d1']
    threshold_B = required_cii * factors['d2']
    threshold_C = required_cii * factors['d3']
    threshold_D = required_cii * factors['d4']
    
    
    # IMO rating to ensure where the vessel falls into ('A', 'B', 'C', 'D', 'E')
    
    if attained_cii <= threshold_A:
        return 'A (Superior)'
    
    elif attained_cii <= threshold_B:
        return 'B (Good)'
    
    elif attained_cii <= threshold_C:
        return 'C (Moderate)'
    
    elif attained_cii <= threshold_D:
        return 'D (Below Average)'
    
    else:
        return 'E (Inferior)'

    
    

# Carbon Tax Estimation

def calculate_carbon_tax(total_co2):
    
    tax_rate = 100
    
    tax = total_co2 * tax_rate
    
    return round(tax, 2)
    
    