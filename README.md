# Vessel Performance & Emission Analysis Tool

## Project Overview

The Vessel Performance & Emission Analysis Tool is a Python-based maritime analytics application developed to simulate real-world vessel emission monitoring and operational performance analysis.

This project allows captains or vessel operators to enter voyage operational data such as fuel consumption, cargo weight, and travelled distance. The system then calculates CO₂ emissions, EEOI scores, CII ratings, and estimated carbon tax values using IMO-inspired analytical logic.

The tool is designed as an educational and analytical simulation project for understanding maritime sustainability workflows and vessel performance monitoring systems.

---

# Features

- Vessel operational data entry
- Fuel emission factor calculations
- CO₂ emission estimation
- EEOI calculation
- IMO-inspired CII rating system
- Estimated carbon tax calculation
- Input validation system
- SQLite database storage
- Automatic voyage report generation
- Streamlit-based user interface

---

# Workflow

Captain enters vessel voyage data  
        ↓  
System validates operational inputs  
        ↓  
Emission & efficiency calculations performed  
        ↓  
CII rating generated  
        ↓  
Estimated carbon tax calculated  
        ↓  
Voyage data stored in SQLite database  
        ↓  
Operational report generated automatically

---

# Technologies Used

- Python
- Streamlit
- SQLite3
- OS Module
- Datetime Module

---

# Folder Structure

Vessel_Performance_Emission_Tool/

│

├── reports/

├── screenshots/

├── engine.py

├── data_handler.py

├── streamlit_app.py

├── Vessel_data.db

├── requirements.txt

├── .gitignore

└── README.md

---
# Conclusion

This project demonstrates the practical implementation of maritime operational analytics using Python and Streamlit. It combines emission calculations, validation systems, database handling, and report generation into a modular workflow-based application.

The project also reflects an understanding of modern maritime sustainability concepts such as EEOI monitoring, CII ratings, and carbon emission analysis, making it suitable as a domain-focused analytical portfolio project.


---
# Problem Solved

Shipping companies face increasing pressure to monitor fuel efficiency, vessel emissions, and environmental compliance due to IMO regulations and rising operational fuel costs.

In many real-world maritime operations, daily vessel data such as fuel consumption, cargo weight, and travelled distance must be analyzed to evaluate operational efficiency and environmental performance.

This project solves the problem by:

- collecting operational voyage data
- calculating vessel CO₂ emissions
- evaluating EEOI efficiency scores
- generating IMO-inspired CII ratings
- estimating carbon tax impact
- storing historical voyage records
- generating operational reports automatically

The tool helps simulate how maritime companies monitor vessel performance and emission efficiency for operational analysis and sustainability tracking.

---

# Screenshots  
Main User Interface

(Add Screenshot Here)

Generated Analysis Result

(Add Screenshot Here)

Validation/Error Handling

(Add Screenshot Here)




# Installation

## Clone Repository

```bash
git clone https://github.com/itsParas000/Vessel-Performance-Emission-Analysis-Tool
```


## Move Into Project Folder
```bash 
cd Vessel_Performance_Emission_Tool
```


## Install Required Libraries
```bash
pip install -r requirements.txt
```


## Run Command
```bash
streamlit run streamlit_app.py
```
