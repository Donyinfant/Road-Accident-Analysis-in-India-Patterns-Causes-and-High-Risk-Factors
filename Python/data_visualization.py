# putting all dataframes in a dictionary so i can check all of them at once
all_data = {
    'speed_injured': speed_injured,
    'speed_killed': speed_killed,
    'world_deaths': world_deaths,
    'road_features': road_features,
    'age_gender': age_gender,
    'city_violation': city_violation,
    'road_user': road_user,
    'safety_device': safety_device,
    'state_killed': state_killed,
    'state_accidents': state_accidents,
    'collision': collision,
    'license_type': license_type,
    'violation': violation,
    'victim_vehicle': victim_vehicle,
    'annual': annual,
    'density': density
}

for name in all_data:
    df = all_data[name]
    print(name, "-> rows:", df.shape[0], ", columns:", df.shape[1], ", null values:", df.isnull().sum().sum())

state_accidents.head()
state_accidents.info()
violation
