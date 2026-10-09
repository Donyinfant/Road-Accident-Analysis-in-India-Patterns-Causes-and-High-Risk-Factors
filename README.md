# Road Accident Analysis in India: Patterns, Causes, and High-Risk Factors

A Python data analysis project that explores road accident data from India to find **patterns** over time and across states and cities, the main **causes** of accidents, and the **high-risk factors** behind road deaths.

---

## Table of Contents

- [Industry](#industry)
- [Problem Statement](#problem-statement)
- [Proposed Solution / Analysis Questions](#proposed-solution--analysis-questions)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Project Workflow](#project-workflow)
- [Data Cleaning & Transformation](#data-cleaning--transformation)
- [Data Analysis & Visualization](#data-analysis--visualization)
- [Key Insights](#key-insights)
- [Recommendations](#recommendations)
- [Limitations](#limitations)
- [Visualization Screenshots](#visualization-screenshots)
- [Project Folder Structure](#project-folder-structure)
- [How to Run](#how-to-run)
- [Author](#author)

---

## Industry

[Enter your industry name]

---

## Problem Statement

[Enter your real-world/industry problem statement]

---

## Proposed Solution / Analysis Questions

The project uses Python to clean and analyse official road accident data. The Exploratory Data Analysis (EDA) is divided into three parts, based on the project title:

**Part A – Patterns**
- How have accidents, deaths and injuries changed from 2014 to 2024?
- How many people die per 100 accidents (severity) each year?
- Are registered vehicles increasing, and is the death rate per vehicle also increasing?
- Which states and cities have the most accidents and deaths?
- Which states have the most severe accidents, and which are growing fastest?
- How does India compare with other countries?

**Part B – Causes**
- Which traffic violations cause the most deaths?
- How have over-speeding deaths changed over the years (2008 – 2016)?
- Which types of collision are the most deadly?
- Which road features / road conditions are the most deadly?
- What are the main reasons for deaths in the top cities?

**Part C – High-Risk Factors**
- Which road users die the most?
- Which vehicles kill which victims (victim vehicle vs crime vehicle)?
- How many deaths are linked to not wearing a helmet or seat belt?
- Which age groups and genders are most affected?
- What type of driving licence do drivers involved in accidents hold?

---

## Dataset

**Dataset Name:** Road Accidents in India (16 CSV files, 2008 – 2024)

**Dataset Source:**
- Ministry of Road Transport & Highways (MoRTH) reports
- data.gov.in
- WHO (for country comparison)

| File | Description |
|------|-------------|
| `Accidents_Due_To_Exceeding_Lawful_Speed_Persons_Injured_2008-2016.csv` | Persons injured due to over-speeding, state-wise |
| `Accidents_Due_To_Exceeding_Lawful_Speed_Persons_Killed_2008-2016.csv` | Persons killed due to over-speeding, state-wise |
| `Deaths from road accidents for every 100,000 people (2019) - Data For India.csv` | Road deaths per 1 lakh people – India vs other countries |
| `Road-Accidents-2018-Annexure-23.csv` | Accidents and deaths by road feature (2018) |
| `Road-Accidents-2018-Table-2.9.csv` | Deaths by age group and gender (2016 – 2018) |
| `road-accidents-2024-cities-fatalities-traffic-violation.csv` | City-wise deaths by traffic violation (2024) |
| `road-accidents-2024-fatality-road-user.csv` | Deaths by road-user category (2023 – 2024) |
| `road-accidents-2024-safety-device.csv` | Deaths/injuries without helmet or seat belt (2024) |
| `road-accidents-2024-states-fatalities.csv` | State-wise deaths (2020 – 2024) |
| `road-accidents-2024-states-road-accidents.csv` | State-wise accidents (2020 – 2024) |
| `road-accidents-2024-type-of-collision.csv` | Accidents and deaths by type of collision (2023 – 2024) |
| `road-accidents-2024-type-of-license.csv` | Accidents by type of driving licence (2020 – 2024) |
| `road-accidents-2024-type-of-violation.csv` | Accidents and deaths by traffic violation (2023 – 2024) |
| `road-accidents-2024-victims-crime-vehicle.csv` | Victim vehicle vs crime vehicle deaths (2024) |
| `road-accidents-annual-2020-2024.csv` | All-India accidents, deaths and injuries (2020 – 2024) |
| `road-accidents-registrations-density-2014-24.csv` | Accidents, registered vehicles, road length and vehicle density (2014 – 2024) |

---

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- os, shutil (folder and file handling)

---

## Project Workflow

```text
Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations
```

---

## Data Cleaning & Transformation

**Problems found in the raw data**
1. Numbers stored as text with Indian-style commas (e.g. `3,72,181`).
2. Extra **"% share"** rows mixed between the real data rows.
3. **Total / All India** rows and footnote rows at the bottom of files.
4. Empty columns (e.g. `Unnamed: 8`).
5. Missing values written as **NA**.
6. Provisional values such as `6498 (P)` in road length.

**How they were handled**
- A custom `make_numeric()` function removes commas and converts text to numbers.
- Removed "% share", Total / All India, empty and footnote rows; dropped empty columns and ranking columns.
- **Telangana (2008 – 2013):** filled with 0 because the state was formed in 2014.
- **Other missing values in speed data:** filled with the average of that state across the other years.
- **Ladakh 2020:** filled with 0 because it was counted inside J&K in 2020.
- **Vehicle and road data for 2023 – 2024:** not available, so these rows were removed only for the vehicle analysis.
- Removed the `(P)` flag from road length values.
- Renamed long column and category names into shorter ones.

**New features created**
- Deaths per 100 accidents (severity) – yearly, state-wise, by violation, collision type and road feature
- % growth in deaths by state (2020 → 2024)
- % share of deaths by violation and road-user type
- Road feature summary table (total accidents and deaths per feature)

**Result:** 18 cleaned datasets with **0 null values**, saved in a separate `cleaned_data` folder.

---

## Data Analysis & Visualization

| Analysis Type | What was analysed | Chart |
|---------------|-------------------|-------|
| Descriptive Statistics | Summary statistics of state-wise accidents (2020 – 2024) | `describe()` table |
| Trend / Time-based Analysis | Accidents, injuries and deaths (2014 – 2024) | Line chart |
| Trend Analysis | Deaths per 100 accidents (2020 – 2024) | Bar chart |
| Relationship Analysis | Registered vehicles vs death rate per 10,000 vehicles (2014 – 2022) | Bar + line (dual axis) |
| Comparison Analysis | Top 10 states by accidents and deaths (2024) | Horizontal bar charts |
| Category-wise Analysis | Severity (deaths per 100 accidents) by state (2024) | Bar chart with India average line |
| Correlation Analysis | State accidents vs deaths | Scatter plot, heatmap |
| Comparison Analysis | % growth in deaths by state (2020 → 2024) | Bar chart |
| Comparison Analysis | Top 10 cities by road deaths (2024) | Bar chart |
| Comparison Analysis | India vs other countries – deaths per 1 lakh people (2019) | Horizontal bar chart |
| Category-wise Analysis | Deaths and % share by traffic violation (2024) | Bar charts |
| Trend Analysis | Over-speeding deaths and injuries (2008 – 2016) | Line chart |
| Comparison Analysis | Top 10 states by over-speeding deaths (2008 – 2016) | Horizontal bar chart |
| Category-wise Analysis | Deaths and severity by type of collision (2024) | Horizontal bar chart |
| Category-wise Analysis | Accidents and severity by road feature (2018) | Bar charts |
| Category-wise Analysis | Reasons for deaths in the top 10 cities (2024) | Stacked bar chart |
| Category-wise Analysis | Deaths by road-user type (2024) | Bar chart |
| Relationship Analysis | Victim vehicle vs crime vehicle (2024) | Heatmap |
| Comparison Analysis | Deaths without helmet / seat belt – drivers vs passengers (2024) | Grouped bar chart |
| Distribution Analysis | Deaths by age group and gender (2018) | Grouped bar chart |
| Trend Analysis | Accidents by type of driving licence (2020 – 2024) | Line chart |

---

## Key Insights

**Patterns**
- Road deaths increased by about **26%**, from 1.40 lakh (2014) to 1.77 lakh (2024), even though accidents did not increase much.
- Accidents dropped sharply in **2020 due to the COVID lockdown**, then rose again to about 4.88 lakh in 2024.
- About **36 – 37 people die in every 100 accidents** in India, with little improvement from 2020 to 2024.
- Registered vehicles almost **doubled** (19 crore in 2014 → 35 crore in 2022). Deaths per 10,000 vehicles fell from 7.0 to 4.8, but total deaths still increased.
- The **top 5 states (UP, Tamil Nadu, Maharashtra, Madhya Pradesh, Karnataka) account for about 48% of all road deaths**.
- **Tamil Nadu** has the most accidents, while **Uttar Pradesh** has the most deaths (24,118).
- **Bihar, Jharkhand and Punjab** have about **80 deaths per 100 accidents**, more than double the India average (36.3). **Kerala** has the lowest (7.9).
- State accidents and deaths have a correlation of **0.86**; UP is far above the trend and Kerala far below it.
- **Chhattisgarh (+51%), Bihar (+40%) and Maharashtra (+36%)** had the fastest growth in road deaths from 2020 to 2024.
- **Delhi** has the most road deaths among cities (1,551), almost double Bengaluru (894) and Jaipur (860).
- India's death rate (**15.6 per lakh people**) is the same as the South Asia average and slightly below the world average (16.7).

**Causes**
- **Over-speeding causes about 70% of all road deaths** (1.24 lakh deaths in 2024).
- Per accident, **mobile phone use (40.6) and drunk driving (38.7)** are the most deadly violations.
- Over-speeding deaths rose from **59,246 (2008) to 73,896 (2016)**; Maharashtra and Tamil Nadu had the most.
- **Hit from back** causes the most deaths (37,404), but **hit and run is the most deadly** (49.6 deaths per 100 accidents).
- Most accidents happen on **straight roads**, but **potholes are the most deadly road condition** (41.4 deaths per 100 accidents).
- In Bengaluru, Jaipur, Raipur and Jabalpur almost all deaths are due to over-speeding; Kanpur has a high share of drunk driving and mobile phone use; Prayagraj has many wrong-side driving deaths.

**High-Risk Factors**
- **Two-wheeler riders (46.2%) and pedestrians (20.6%)** make up about two-thirds of all road deaths.
- The largest victim/crime-vehicle combination is **two-wheeler hitting two-wheeler (30,561 deaths)**.
- **54,122 people died without a helmet** – about **66% of all two-wheeler deaths**. 14,466 died without a seat belt.
- **86% of people killed are male**, and about **70% are aged 18 – 45** (25 – 35 is the highest).
- About **68% of accidents involve drivers with a valid licence**, and the **"Not known"** licence category keeps increasing (53k → 1 lakh).

---

## Recommendations

Based on the findings above:

1. **Control over-speeding** – stronger speed enforcement, since over-speeding causes about 70% of road deaths.
2. **Enforce helmet use for riders and pillion passengers** – not wearing a helmet is linked to about 66% of two-wheeler deaths.
3. **Protect vulnerable road users** – two-wheeler riders and pedestrians together are about two-thirds of all deaths.
4. **Focus on high-severity states** – Bihar, Jharkhand and Punjab have about 80 deaths per 100 accidents; faster emergency response and trauma care can help reduce deaths.
5. **Act against mobile phone use and drunk driving** – these are the most deadly violations per accident.
6. **Repair potholes and improve road works safety** – potholes, steep grades and road works have the highest severity among road features.
7. **Improve data recording** – reduce the large "Others" and "Not known" categories so causes can be identified clearly.

---

## Limitations

- State-level data is aggregated; there are no accident-level records.
- Some years have missing values.
- Different files cover different years (2008 – 2024).
- Many cases are recorded as "Others" or "Not known".

**Next step:** Feature engineering and applying Machine Learning models (clustering states by risk level and predicting severity).

---

## Visualization Screenshots

### Road Accidents in India (2014 – 2024)

![Road Accidents in India 2014-2024](Visualizations/A2_accidents_deaths_trend_2014_2024.png)

### Deaths per 100 Accidents (2020 – 2024)

![Deaths per 100 Accidents](Visualizations/A3_deaths_per_100_accidents_yearly.png)

### Registered Vehicles vs Death Rate (2014 – 2022)

![Registered Vehicles vs Death Rate](Visualizations/A4_vehicles_vs_death_rate.png)

### Top 10 States – Accidents and Deaths (2024)

![Top 10 States](Visualizations/A5_top10_states_accidents_deaths.png)

### Deaths per 100 Accidents by State (2024)

![State Severity](Visualizations/A6_state_severity_2024.png)

### Accidents vs Deaths – Scatter Plot

![Accidents vs Deaths Scatter](Visualizations/A7_accidents_vs_deaths_scatter.png)

### Accidents vs Deaths – Heatmap

![Accidents vs Deaths Heatmap](Visualizations/A7_accidents_vs_deaths_heatmap.png)

### % Increase in Road Deaths (2020 – 2024)

![State Growth](Visualizations/A8_state_growth_2020_2024.png)

### Top 10 Cities by Road Deaths (2024)

![Top 10 Cities](Visualizations/A9_top10_cities_deaths.png)

### India vs Other Countries (2019)

![India vs World](Visualizations/A10_india_vs_world.png)

### Deaths by Type of Violation (2024)

![Violation Deaths](Visualizations/B1_violation_deaths.png)

### Over-speeding Accidents – All India (2008 – 2016)

![Over-speeding Trend](Visualizations/B2_overspeeding_trend_2008_2016.png)

### Top 10 States – Over-speeding Deaths (2008 – 2016)

![Top 10 States Over-speeding](Visualizations/B2_top10_states_overspeeding.png)

### Deaths by Type of Collision (2024)

![Collision Type](Visualizations/B3_collision_type_deaths.png)

### Road Features (2018)

![Road Features](Visualizations/B4_road_features.png)

### Reasons for Deaths in Top 10 Cities (2024)

![City Violation Stacked](Visualizations/B5_city_violation_stacked.png)

### Persons Killed by Road User Type (2024)

![Road User Deaths](Visualizations/C1_road_user_deaths.png)

### Victim vs Crime Vehicle (2024)

![Victim vs Crime Vehicle](Visualizations/C2_victim_vs_crime_vehicle.png)

### Deaths due to not using Safety Devices (2024)

![Helmet and Seat Belt](Visualizations/C3_helmet_seatbelt.png)

### Road Deaths by Age Group and Gender (2018)

![Age and Gender](Visualizations/C4_age_gender.png)

### Accidents by Type of Driving Licence (2020 – 2024)

![Licence Type](Visualizations/C5_license_type.png)

---

## Project Folder Structure

```text
Road_Accident_Analysis_India/
│
├── README.md
│
├── Dataset/
│   ├── raw_data/
│   │   ├── Accidents_Due_To_Exceeding_Lawful_Speed_Persons_Injured_2008-2016.csv
│   │   ├── Accidents_Due_To_Exceeding_Lawful_Speed_Persons_Killed_2008-2016.csv
│   │   ├── Deaths from road accidents for every 100,000 people (2019) - Data For India.csv
│   │   ├── Road-Accidents-2018-Annexure-23.csv
│   │   ├── Road-Accidents-2018-Table-2.9.csv
│   │   ├── road-accidents-2024-cities-fatalities-traffic-violation.csv
│   │   ├── road-accidents-2024-fatality-road-user.csv
│   │   ├── road-accidents-2024-safety-device.csv
│   │   ├── road-accidents-2024-states-fatalities.csv
│   │   ├── road-accidents-2024-states-road-accidents.csv
│   │   ├── road-accidents-2024-type-of-collision.csv
│   │   ├── road-accidents-2024-type-of-license.csv
│   │   ├── road-accidents-2024-type-of-violation.csv
│   │   ├── road-accidents-2024-victims-crime-vehicle.csv
│   │   ├── road-accidents-annual-2020-2024.csv
│   │   └── road-accidents-registrations-density-2014-24.csv
│   │
│   └── cleaned_data/
│       ├── cleaned_accident_trend_2014_2024.csv
│       ├── cleaned_age_gender_2016_2018.csv
│       ├── cleaned_annual_2020_2024.csv
│       ├── cleaned_city_violation_2024.csv
│       ├── cleaned_collision_type_2024.csv
│       ├── cleaned_license_type_2020_2024.csv
│       ├── cleaned_road_feature_summary_2018.csv
│       ├── cleaned_road_features_2018.csv
│       ├── cleaned_road_user_2024.csv
│       ├── cleaned_safety_device_2024.csv
│       ├── cleaned_speed_injured_2008_2016.csv
│       ├── cleaned_speed_killed_2008_2016.csv
│       ├── cleaned_state_accidents_2020_2024.csv
│       ├── cleaned_state_fatalities_2020_2024.csv
│       ├── cleaned_vehicle_density_2014_2022.csv
│       ├── cleaned_victim_crime_vehicle_2024.csv
│       ├── cleaned_violation_type_2024.csv
│       └── cleaned_world_deaths_2019.csv
│
├── Notebook/
│   └── Road_Accident_Analysis_EDA.ipynb
│
└── Visualizations/
    ├── A2_accidents_deaths_trend_2014_2024.png
    ├── A3_deaths_per_100_accidents_yearly.png
    ├── A4_vehicles_vs_death_rate.png
    ├── A5_top10_states_accidents_deaths.png
    ├── A6_state_severity_2024.png
    ├── A7_accidents_vs_deaths_heatmap.png
    ├── A7_accidents_vs_deaths_scatter.png
    ├── A8_state_growth_2020_2024.png
    ├── A9_top10_cities_deaths.png
    ├── A10_india_vs_world.png
    ├── B1_violation_deaths.png
    ├── B2_overspeeding_trend_2008_2016.png
    ├── B2_top10_states_overspeeding.png
    ├── B3_collision_type_deaths.png
    ├── B4_road_features.png
    ├── B5_city_violation_stacked.png
    ├── C1_road_user_deaths.png
    ├── C2_victim_vs_crime_vehicle.png
    ├── C3_helmet_seatbelt.png
    ├── C4_age_gender.png
    └── C5_license_type.png
```

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Road_Accident_Analysis_India.git
   ```
2. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn jupyter
   ```
3. Open the notebook:
   ```bash
   jupyter notebook Notebook/Road_Accident_Analysis_EDA.ipynb
   ```
4. Update the dataset and figure folder paths in the notebook if your folder layout is different.

---

## Author

- Name: DONY INFANT EDISON M
- Student ID: AF05309200
- Organization: Anudip Foundation
- Course: AIML
- Batch Code: ANP-D7444
