def make_numeric(df, columns):
    for col in columns:
        df[col] = df[col].astype(str).str.replace(',', '')
        df[col] = pd.to_numeric(df[col], errors='coerce')   # if something is not a number it becomes NaN
    return df
  print("Null values in speed_killed:")
print(speed_killed.isnull().sum())
print()
print(speed_killed[speed_killed.isnull().any(axis=1)])
years_before_telangana = ['2008', '2009', '2010', '2011', '2012', '2013']
year_cols = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

for df in [speed_killed, speed_injured]:
    # telangana -> 0 before 2014
    df.loc[df['States/UTs'] == 'Telangana', years_before_telangana] = 0

    # other states -> fill with the state's own average
    for i in df.index:
        state_avg = df.loc[i, year_cols].mean()
        df.loc[i, year_cols] = df.loc[i, year_cols].fillna(state_avg)

    # values are number of persons so they should be whole numbers
    df[year_cols] = df[year_cols].round(0).astype(int)

print("Nulls left in speed_killed :", speed_killed.isnull().sum().sum())
print("Nulls left in speed_injured:", speed_injured.isnull().sum().sum())
# the last row is All India total, keeping it separately
speed_killed_india = speed_killed[speed_killed['States/UTs'] == 'All India']
speed_injured_india = speed_injured[speed_injured['States/UTs'] == 'All India']

speed_killed = speed_killed[speed_killed['States/UTs'] != 'All India']
speed_injured = speed_injured[speed_injured['States/UTs'] != 'All India']

print(speed_killed.shape, speed_injured.shape)
speed_killed.head()
world_deaths.columns = ['Country', 'Deaths_per_100k']
world_deaths['Deaths_per_100k'] = world_deaths['Deaths_per_100k'].round(1)
print("Null values:", world_deaths.isnull().sum().sum())
world_deaths
# removing the Total row and the S.No column
road_features = road_features[road_features['S.No'] != 'Total']
road_features = road_features.drop(columns=['S.No'])

# removing the rank columns (we dont need rank, and the nulls were only in these columns)
rank_cols = []
for col in road_features.columns:
    if 'Rank' in col:
        rank_cols.append(col)
road_features = road_features.drop(columns=rank_cols)

# straight road columns have different names from others, so renaming them
road_features = road_features.rename(columns={
    'Straight Road - Number of Accidents - Number': 'Straight Road - Number of Accidents',
    'Straight Road - Persons Killed - Number': 'Straight Road - Persons Killed'
})

print("Shape:", road_features.shape)
print("Null values:", road_features.isnull().sum().sum())
# making a small summary table : total accidents and deaths for each road feature
features = ['Straight Road', 'Curved Road', 'Bridge', 'Culvert', 'Pot Holes',
            'Steep Grade', 'Ongoing Road Works/Under Construction', 'Others']

feature_accidents = []
feature_killed = []
for f in features:
    feature_accidents.append(road_features[f + ' - Number of Accidents'].sum())
    feature_killed.append(road_features[f + ' - Persons Killed'].sum())

feature_summary = pd.DataFrame({
    'Road Feature': features,
    'Accidents': feature_accidents,
    'Killed': feature_killed
})
feature_summary['Road Feature'] = feature_summary['Road Feature'].replace(
    'Ongoing Road Works/Under Construction', 'Road Works')
feature_summary
# removing the '% Share' rows, the Total row and the share row
age_gender = age_gender[~age_gender['Age-Group'].str.contains('Share')]
age_gender = age_gender[age_gender['Age-Group'] != 'Total']

# % change columns are not needed (they had all the NA values)
age_gender = age_gender[['Age-Group', '2016 - Male', '2016 - Female', '2017 - Male',
                         '2017 - Female', '2018 - Male', '2018 - Female']]
age_gender = age_gender.reset_index(drop=True)

print("Null values:", age_gender.isnull().sum().sum())
age_gender
# last column is completely empty
city_violation = city_violation.drop(columns=['Unnamed: 8'])

# last row has no city name (it is the total row)
city_violation = city_violation.dropna(subset=['City'])

print("Shape:", city_violation.shape)
print("Null values:", city_violation.isnull().sum().sum())
city_violation.head()
road_user = road_user[~road_user['Road-user category'].str.contains('share')]
road_user = road_user[road_user['Road-user category'] != 'Total']
road_user = make_numeric(road_user, ['Persons killed 2023', 'Persons killed 2024'])

# the 'Others' name is very long so making it short
road_user['Road-user category'] = road_user['Road-user category'].replace({
    'Other Non- Motor Vehicles (including e-rickshaw)': 'Other Non-Motor',
    'Others (other motor vehicles, animals drawn vehicle, cycle rickshaws, hand carts, & other persons)': 'Others'
})
road_user = road_user.reset_index(drop=True)
print("Null values:", road_user.isnull().sum().sum())
road_user
safety_device = safety_device[~safety_device['Category'].str.contains('Share')]
safety_device = safety_device[safety_device['Category'] != 'Total']
safety_device = make_numeric(safety_device, ['No Helmet - Killed', 'No Helmet - Injured',
                                             'No Seat belt - killed', 'No seat belt - injured'])
safety_device = safety_device.reset_index(drop=True)
safety_device
print(state_killed.tail(4))
for df_name in ['state_killed', 'state_accidents']:
    df = all_data[df_name]
    df = df.dropna(subset=['State'])           # removes empty row and footnote row
    df = df[df['State'] != 'All India']        # removes total row
    df = df.drop(columns=['Sl No'])

    # dropping ranking columns
    df = df.drop(columns=['2020 Ranking', '2021 Ranking', '2022 Ranking', '2023 Ranking', '2024 Ranking'])

    df['State'] = df['State'].replace('J & K #', 'Jammu & Kashmir')
    all_data[df_name] = df

state_killed = all_data['state_killed']
state_accidents = all_data['state_accidents']

killed_cols = ['2020 Killed', '2021 Killed', '2022 Killed', '2023 Killed', '2024 Killed']
acc_cols = ['2020 Accidents', '2021 Accidents', '2022 Accidents', '2023 Accidents', '2024 Accidents']

state_killed = make_numeric(state_killed, killed_cols)
state_accidents = make_numeric(state_accidents, acc_cols + ['Change from 2023 to 2024'])

# Ladakh 2020 -> 0
state_killed = state_killed.fillna(0)
state_accidents = state_accidents.fillna(0)

# converting to int because number of people/accidents cant be in decimal
state_killed[killed_cols] = state_killed[killed_cols].astype(int)
state_accidents[acc_cols] = state_accidents[acc_cols].astype(int)

state_killed = state_killed.reset_index(drop=True)
state_accidents = state_accidents.reset_index(drop=True)

print("state_killed    -> shape:", state_killed.shape, " nulls:", state_killed.isnull().sum().sum())
print("state_accidents -> shape:", state_accidents.shape, " nulls:", state_accidents.isnull().sum().sum())
state_accidents.head()
# collision
collision = collision[~collision['Type of collision'].str.contains('share')]
collision = collision[collision['Type of collision'] != 'Total']
collision = make_numeric(collision, ['2023-Accidents', '2023-Killed', '2023-injured',
                                     '2024-Accidents', '2024-Killed', '2024-injured'])
collision = collision.reset_index(drop=True)

# violation
violation = violation[~violation['Category'].str.contains('share')]
violation = violation[violation['Category'] != 'All India']
violation = make_numeric(violation, ['2023-Accidents', '2023-Killed', '2023-injured',
                                     '2024-Accidents', '2024-Killed', '2024-injured'])
violation['Category'] = violation['Category'].replace({
    'Drunken driving/consumption of alcohol & drug': 'Drunk Driving',
    'Driving on wrong side/Lane indiscipline': 'Wrong Side Driving'
})
violation = violation.reset_index(drop=True)

# license
license_type = license_type[~license_type['Type of license'].str.contains('share')]
license_type = license_type[license_type['Type of license'] != 'Total']
license_type = make_numeric(license_type, ['2020', '2021', '2022', '2023', '2024'])
license_type = license_type.reset_index(drop=True)

print("collision nulls   :", collision.isnull().sum().sum())
print("violation nulls   :", violation.isnull().sum().sum())
print("license nulls     :", license_type.isnull().sum().sum())
violation
victim_vehicle = victim_vehicle.rename(columns={victim_vehicle.columns[0]: 'Victim'})
victim_vehicle = victim_vehicle.drop(columns=['<-- Crime Vehicle'])   # empty column

victim_vehicle = victim_vehicle[~victim_vehicle['Victim'].str.contains('Share')]
victim_vehicle = victim_vehicle[victim_vehicle['Victim'] != 'Total']
victim_vehicle = victim_vehicle[victim_vehicle['Victim'] != 'Victim Vehicle(Column above)']

vehicle_cols = list(victim_vehicle.columns[1:])
victim_vehicle = make_numeric(victim_vehicle, vehicle_cols)

# short names for the chart
short_names = ['Pedestrian', 'Bicycle', 'Two Wheeler', 'Auto', 'Car/Taxi/LMV',
               'Truck', 'Bus', 'Non-Motor', 'Others']
victim_vehicle['Victim'] = short_names
victim_vehicle.columns = ['Victim', 'Bicycle', 'Two Wheeler', 'Auto', 'Car/Taxi/LMV',
                          'Truck', 'Bus', 'Non-Motor', 'Others', 'Total']
victim_vehicle = victim_vehicle.reset_index(drop=True)

print("Null values:", victim_vehicle.isnull().sum().sum())
victim_vehicle
annual.columns = ['Year', 'Accidents', 'Accidents % Change', 'Fatalities',
                  'Fatalities % Change', 'Injured', 'Injured % Change']
annual = make_numeric(annual, ['Accidents', 'Fatalities', 'Injured'])
print("Null values:", annual.isnull().sum().sum())
annual
density.tail(6)
 removing CAGR row, empty row and the note rows at the bottom
density = density.dropna(subset=['Year'])
density = density[density['Year'].str.isnumeric()]
density['Year'] = density['Year'].astype(int)

# removing the (P) from road length
density["Road length ('000 km)"] = density["Road length ('000 km)"].str.replace('(P)', '', regex=False)

density = make_numeric(density, ["Road accidents ('000)", "Registered vehicles ('000)", "Road length ('000 km)"])
density.columns = ['Year', 'Accidents_000', 'Deaths_000', 'Injuries_000', 'Vehicles_000',
                   'Road_length_000km', 'Death_rate_per_10k_vehicles', 'Vehicle_density']

print(density.isnull().sum())
density_vehicles = density.dropna()
print("Rows before:", density.shape[0], " Rows after removing nulls:", density_vehicles.shape[0])
density_vehicles
clean_data = {
    'speed_injured': speed_injured, 'speed_killed': speed_killed, 'world_deaths': world_deaths,
    'road_features': road_features, 'feature_summary': feature_summary, 'age_gender': age_gender,
    'city_violation': city_violation, 'road_user': road_user, 'safety_device': safety_device,
    'state_killed': state_killed, 'state_accidents': state_accidents, 'collision': collision,
    'license_type': license_type, 'violation': violation, 'victim_vehicle': victim_vehicle,
    'annual': annual, 'density_vehicles': density_vehicles
}

for name in clean_data:
    print(name.ljust(18), "shape:", str(clean_data[name].shape).ljust(10), " nulls:", clean_data[name].isnull().sum().sum())
  clean_path = 'cleaned_data/'

# create the folder if it is not already there
if not os.path.exists(clean_path):
    os.makedirs(clean_path)
    print("cleaned_data folder created")
else:
    print("cleaned_data folder already exists")
# accident trend 2014-2024 (only the columns which have no missing values)
accident_trend = density[['Year', 'Accidents_000', 'Deaths_000', 'Injuries_000']]

speed_injured.to_csv(clean_path + 'cleaned_speed_injured_2008_2016.csv', index=False)
speed_killed.to_csv(clean_path + 'cleaned_speed_killed_2008_2016.csv', index=False)
world_deaths.to_csv(clean_path + 'cleaned_world_deaths_2019.csv', index=False)
road_features.to_csv(clean_path + 'cleaned_road_features_2018.csv', index=False)
feature_summary.to_csv(clean_path + 'cleaned_road_feature_summary_2018.csv', index=False)
age_gender.to_csv(clean_path + 'cleaned_age_gender_2016_2018.csv', index=False)
city_violation.to_csv(clean_path + 'cleaned_city_violation_2024.csv', index=False)
road_user.to_csv(clean_path + 'cleaned_road_user_2024.csv', index=False)
safety_device.to_csv(clean_path + 'cleaned_safety_device_2024.csv', index=False)
state_killed.to_csv(clean_path + 'cleaned_state_fatalities_2020_2024.csv', index=False)
state_accidents.to_csv(clean_path + 'cleaned_state_accidents_2020_2024.csv', index=False)
collision.to_csv(clean_path + 'cleaned_collision_type_2024.csv', index=False)
license_type.to_csv(clean_path + 'cleaned_license_type_2020_2024.csv', index=False)
violation.to_csv(clean_path + 'cleaned_violation_type_2024.csv', index=False)
victim_vehicle.to_csv(clean_path + 'cleaned_victim_crime_vehicle_2024.csv', index=False)
annual.to_csv(clean_path + 'cleaned_annual_2020_2024.csv', index=False)
density_vehicles.to_csv(clean_path + 'cleaned_vehicle_density_2014_2022.csv', index=False)
accident_trend.to_csv(clean_path + 'cleaned_accident_trend_2014_2024.csv', index=False)

print("All cleaned files saved!")
# checking the saved files - reading them again to make sure there are no nulls
print("Files in cleaned_data folder:\n")
for file in sorted(os.listdir(clean_path)):
    df = pd.read_csv(clean_path + file)
    print(file.ljust(45), "shape:", str(df.shape).ljust(10), " nulls:", df.isnull().sum().sum())
