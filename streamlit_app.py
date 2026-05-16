import streamlit as st

from engine import get_fuel_info, calculate_co2, calculate_eeoi, calculate_cii, calculate_carbon_tax
from data_handler import validate_inputs, save_to_sql, save_report, setup_database


# setup database

setup_database()


# page title

st.title("Vessel Performance & Emission Analysis Tool")


# user inputs

# vessel name input

vessel_name = st.text_input('vessel name')


# select fuel type input from drop down list 

fuel_type = st.selectbox(
    "Fuel Type",
    ['VLSFO', 'LSMGO', 'LNG']
)


# fuel quantity input

fuel_qty = st.number_input('Fuel Consumed (MT)', min_value = 0.0)


# Cargo Weight input

cargo_weight = st.number_input('Cargo weight (MT)', min_value = 0.0)


# Distance input

distance = st.number_input('Distance Travelled (NM)', min_value = 0.0)


# Vessel Type input select from Drop Down List 

vessel_type = st.selectbox(
    "Vessel Type",
    [
        "bulk_carrier",
        "tanker",
        "container_ship",
        "general_cargo",
        "gas_carrier",
        "cruise_passenger"
    ]
)


# generate report button

if st.button('Generate report'):
    
    # validate inputs
    
    validate_error = validate_inputs(vessel_name, fuel_type, fuel_qty, cargo_weight, distance)
    
    # stop if validation fails
    
    if validate_error:
        
        st.error(validate_error)
        
    
    else:
        
        # fuel information
        
        fuel_info = get_fuel_info(fuel_type)
        
        # CO2 Calculation
        
        if fuel_info is None:
            st.error("Invalid fuel information.")
            st.stop()
            
        else:
            total_co2 = calculate_co2(fuel_qty, fuel_info['cf'])
        
        
            # EEOI Calculation
        
            eeoi = calculate_eeoi(total_co2, cargo_weight, distance)
        
            # CII rating
        
            rating = calculate_cii(eeoi, vessel_type = vessel_type)
        
            # Carbon Tax
        
            tax = calculate_carbon_tax(total_co2)
        
        
            # Store data
        
            vessel_data = {
                "vessel_name": vessel_name,

                "fuel_type": fuel_type,
                "fuel_qty": fuel_qty,

                "cargo_weight": cargo_weight,
                "distance": distance,

                "total_co2": total_co2,
                "eeoi": eeoi,

                "rating": rating,
                "tax": tax
            }
        
        
            # Save to Database
        
            save_to_sql(vessel_data)
        
        
            # save report
        
            report_path = save_report(vessel_data)
        
        
            # Success Message
        
            st.success('Report Generated Successfully')
        
        
            # Display Results
        
            st.subheader('Analysis Results')
        
        
            st.write(f"Vessel Name: {vessel_name}")
        
        
            st.write(f"Fuel Type: {fuel_type}")


            st.write(f"Total CO₂ Emission: " f"{total_co2} tons")


            st.write(f"EEOI Score: {eeoi}")


            st.write(f"CII Rating: {rating}")


            st.write(f"Estimated Carbon Tax: " f"${tax:,.2f}")


            st.write(f"Report Saved: {report_path}")