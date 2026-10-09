import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import shutil      # for copying files into folders

import warnings
warnings.filterwarnings('ignore')   # to hide the yellow warning messages

# speed related accidents (2008 - 2016)
speed_injured = pd.read_csv(r"Road Accident Analysis/Accidents_Due_To_Exceeding_Lawful_Speed_Persons_Injured_2008-2016.csv")
speed_killed = pd.read_csv(r"Road Accident Analysis/Accidents_Due_To_Exceeding_Lawful_Speed_Persons_Killed_2008-2016.csv")
# deaths per 1 lakh people - India vs other countries (2019)
world_deaths = pd.read_csv(r"Road Accident Analysis/Deaths from road accidents for every 100,000 people (2019) - Data For India.csv")
# 2018 data - road features and age group
road_features = pd.read_csv(r"Road Accident Analysis/Road-Accidents-2018-Annexure-23.csv")
age_gender = pd.read_csv(r"Road Accident Analysis/Road-Accidents-2018-Table-2.9.csv")

# 2024 data
city_violation = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-cities-fatalities-traffic-violation.csv")
road_user = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-fatality-road-user.csv")
safety_device = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-safety-device.csv")
state_killed = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-states-fatalities.csv")
state_accidents = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-states-road-accidents.csv")
collision = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-type-of-collision.csv")
license_type = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-type-of-license.csv")
violation = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-type-of-violation.csv")
victim_vehicle = pd.read_csv(r"Road Accident Analysis/road-accidents-2024-victims-crime-vehicle.csv")

# yearly data
annual = pd.read_csv(r"Road Accident Analysis/road-accidents-annual-2020-2024.csv")
density = pd.read_csv(r"Road Accident Analysis/road-accidents-registrations-density-2014-24.csv")

print("All files loaded successfully")
