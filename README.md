# Toronto Bike Share Ridership Analysis (Jan–Sep 2024)

## Overview
This project analyzes **Toronto Bike Share ridership data** from January to September 2024 to identify trends in daily usage, peak hours, popular stations, and weekday vs weekend patterns.  

The analysis demonstrates **data cleaning, visualization, and statistical testing** skills using Python.  

---

## Data
- **Source:** [Bike Share Toronto Ridership Data](https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/)  
- **Files:** 9 CSV files covering Jan–Sep 2024  
- **Columns Include:**  
  - Trip ID  
  - Trip Duration  
  - Start/End Station ID & Name  
  - Start/End Time  
  - Bike ID  
  - User Type  
  - Model  

---

## Tools & Libraries
- **Python 3.11**  
- **pandas** – Data cleaning and manipulation  
- **numpy** – Numerical operations  
- **matplotlib, seaborn** – Visualizations  
- **scipy.stats** – Statistical analysis (t-test)  
- **glob** – Handling multiple CSV files  
- **IDE:** VS Code  

---

## Report
The main analysis, including **daily and hourly ridership trends, weekday vs weekend comparisons, and top station insights**, is presented in the **report**.  

Refer to the report for:  
- Visualizations of ridership patterns  
- Statistical analysis (t-tests)  
- Interpretations and actionable recommendations  

**Note:** The `bike_analysis.py` script generates the underlying figures and data used in the report.

---
## How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/bike-share-analysis.git
2. Install required libraries:
   ``` bash
    pip install pandas numpy matplotlib seaborn scipy
   ```
3. Run the analysis script:
   ```bash
   python bike_analysis.py
   ```
