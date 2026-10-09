fig_path = r"D:/Road Accident Analysis/figures/"

if not os.path.exists(fig_path):
    os.makedirs(fig_path)
    print("figures folder created")
else:
    print("figures folder already exists")
state_accidents[acc_cols].describe()
plt.figure(figsize=(10, 5))
plt.plot(density['Year'], density['Accidents_000'], marker='o', label='Accidents')
plt.plot(density['Year'], density['Injuries_000'], marker='o', label='Injured')
plt.plot(density['Year'], density['Deaths_000'], marker='o', label='Deaths')
plt.title('Road Accidents in India (2014 - 2024)')
plt.xlabel('Year')
plt.ylabel("Count (in thousands)")
plt.xticks(density['Year'])
plt.legend()
plt.grid(alpha=0.3)
plt.savefig(fig_path + 'A2_accidents_deaths_trend_2014_2024.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
 death % change from 2014 to 2024
d2014 = density[density['Year'] == 2014]['Deaths_000'].values[0]
d2024 = density[density['Year'] == 2024]['Deaths_000'].values[0]
print("Deaths in 2014:", d2014, "thousand")
print("Deaths in 2024:", d2024, "thousand")
print("Increase:", round((d2024 - d2014) / d2014 * 100, 1), "%")
annual['Deaths per 100 Accidents'] = (annual['Fatalities'] / annual['Accidents'] * 100).round(2)
print(annual[['Year', 'Accidents', 'Fatalities', 'Deaths per 100 Accidents']])

plt.figure(figsize=(8, 4))
plt.bar(annual['Year'], annual['Deaths per 100 Accidents'], color='indianred')
plt.title('Deaths per 100 Accidents (2020 - 2024)')
plt.xlabel('Year')
plt.ylabel('Deaths per 100 accidents')
plt.ylim(30, 40)
for i in range(len(annual)):
    plt.text(annual['Year'][i], annual['Deaths per 100 Accidents'][i] + 0.2,
             annual['Deaths per 100 Accidents'][i], ha='center')
plt.savefig(fig_path + 'A3_deaths_per_100_accidents_yearly.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
ig, ax1 = plt.subplots(figsize=(10, 5))

ax1.bar(density_vehicles['Year'], density_vehicles['Vehicles_000'] / 1000, color='lightsteelblue', label='Registered Vehicles')
ax1.set_xlabel('Year')
ax1.set_ylabel('Registered Vehicles (in millions)')

ax2 = ax1.twinx()   # second y axis
ax2.plot(density_vehicles['Year'], density_vehicles['Death_rate_per_10k_vehicles'], color='red', marker='o', label='Death rate')
ax2.set_ylabel('Deaths per 10,000 vehicles', color='red')

plt.title('Registered Vehicles vs Death Rate (2014 - 2022)')
plt.savefig(fig_path + 'A4_vehicles_vs_death_rate.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
top10_acc = state_accidents.sort_values('2024 Accidents', ascending=False).head(10)
top10_killed = state_killed.sort_values('2024 Killed', ascending=False).head(10)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].barh(top10_acc['State'], top10_acc['2024 Accidents'], color='orange')
axes[0].invert_yaxis()
axes[0].set_title('Top 10 States - Accidents (2024)')
axes[0].set_xlabel('Number of accidents')

axes[1].barh(top10_killed['State'], top10_killed['2024 Killed'], color='crimson')
axes[1].invert_yaxis()
axes[1].set_title('Top 10 States - Deaths (2024)')
axes[1].set_xlabel('Number of deaths')

plt.tight_layout()
plt.savefig(fig_path + 'A5_top10_states_accidents_deaths.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
# what % of all india deaths come from top 5 states
total_killed_2024 = state_killed['2024 Killed'].sum()
top5_killed = top10_killed.head(5)['2024 Killed'].sum()
print("Top 5 states share of total deaths:", round(top5_killed / total_killed_2024 * 100, 1), "%")
# joining the two state tables
states = pd.merge(state_accidents[['State', '2024 Accidents']],
                  state_killed[['State', '2024 Killed']], on='State')

# only taking states with at least 1000 accidents (small UTs give very odd values)
states = states[states['2024 Accidents'] >= 1000]

states['Severity'] = (states['2024 Killed'] / states['2024 Accidents'] * 100).round(1)
states = states.sort_values('Severity', ascending=False)

national_severity = round(total_killed_2024 / state_accidents['2024 Accidents'].sum() * 100, 1)
print("National average severity:", national_severity)

plt.figure(figsize=(12, 6))
colors = []
for s in states['Severity']:
    if s > national_severity:
        colors.append('crimson')
    else:
        colors.append('seagreen')
plt.bar(states['State'], states['Severity'], color=colors)
plt.axhline(national_severity, color='black', linestyle='--', label='India average')
plt.title('Deaths per 100 Accidents by State (2024)')
plt.ylabel('Deaths per 100 accidents')
plt.xticks(rotation=75)
plt.legend()
plt.savefig(fig_path + 'A6_state_severity_2024.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
rint("Most severe 5 states:")
print(states.head(5))
print()
print("Least severe 5 states:")
print(states.tail(5))
x = state_accidents['2024 Accidents']
y = state_killed['2024 Killed']

correlation = np.corrcoef(x, y)[0, 1]
print("Correlation between accidents and deaths:", round(correlation, 3))

plt.figure(figsize=(9, 6))
plt.scatter(x, y, color='steelblue')

# writing names of a few important states
for i in range(len(state_accidents)):
    if state_accidents['2024 Accidents'][i] > 30000 or state_killed['2024 Killed'][i] > 10000:
        plt.text(x[i], y[i], state_accidents['State'][i], fontsize=8)

plt.title('Accidents vs Deaths for each State (2024)')
plt.xlabel('Accidents')
plt.ylabel('Deaths')
plt.grid(alpha=0.3)
plt.savefig(fig_path + 'A7_accidents_vs_deaths_scatter.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
top_cities = city_violation.sort_values('Total', ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_cities['City'], top_cities['Total'], color='purple')
plt.title('Top 10 Cities by Road Deaths (2024)')
plt.ylabel('Deaths')
plt.xticks(rotation=45)
plt.savefig(fig_path + 'A9_top10_cities_deaths.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
world_sorted = world_deaths.sort_values('Deaths_per_100k')

colors = []
for c in world_sorted['Country']:
    if c == 'India':
        colors.append('red')
    elif c in ['World', 'South Asia']:
        colors.append('gray')
    else:
        colors.append('skyblue')

plt.figure(figsize=(10, 6))
plt.barh(world_sorted['Country'], world_sorted['Deaths_per_100k'], color=colors)
plt.title('Road Deaths per 1 Lakh People (2019)')
plt.xlabel('Deaths per 100,000 people')
plt.savefig(fig_path + 'A10_india_vs_world.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(violation['Category'], violation['2024-Killed'], color='firebrick')
axes[0].set_title('Deaths by Type of Violation (2024)')
axes[0].set_ylabel('Deaths')
axes[0].tick_params(axis='x', rotation=45)

# pie chart labels were overlapping for small values, so i used a bar chart of % share
violation['Share %'] = (violation['2024-Killed'] / violation['2024-Killed'].sum() * 100).round(1)
axes[1].bar(violation['Category'], violation['Share %'], color='salmon')
axes[1].set_title('% Share of Deaths by Violation (2024)')
axes[1].set_ylabel('% of deaths')
axes[1].tick_params(axis='x', rotation=45)
for i in range(len(violation)):
    axes[1].text(i, violation['Share %'][i] + 1, str(violation['Share %'][i]) + '%', ha='center')

plt.tight_layout()
plt.savefig(fig_path + 'B1_violation_deaths.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
 deaths per 100 accidents for each violation
violation['Severity'] = (violation['2024-Killed'] / violation['2024-Accidents'] * 100).round(1)
violation[['Category', '2024-Accidents', '2024-Killed', 'Severity']].sort_values('Severity', ascending=False)
matrix = victim_vehicle.drop(columns=['Victim', 'Total'])
values = matrix.values

plt.figure(figsize=(11, 7))
plt.imshow(values, cmap='Reds')
plt.colorbar(label='Deaths')

plt.xticks(range(len(matrix.columns)), matrix.columns, rotation=45)
plt.yticks(range(len(victim_vehicle)), victim_vehicle['Victim'])
plt.xlabel('Crime vehicle (vehicle that caused the accident)')
plt.ylabel('Victim')
plt.title('Victim vs Crime Vehicle (Deaths, 2024)')

# writing the numbers inside each box
for i in range(values.shape[0]):
    for j in range(values.shape[1]):
        if values[i, j] > 15000:
            text_color = 'white'     # white text on dark boxes
        else:
            text_color = 'black'
        plt.text(j, i, int(values[i, j]), ha='center', va='center', fontsize=7, color=text_color)

plt.savefig(fig_path + 'C2_victim_vs_crime_vehicle.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
road_user_sorted = road_user.sort_values('Persons killed 2024', ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(road_user_sorted['Road-user category'], road_user_sorted['Persons killed 2024'], color='darkcyan')
plt.title('Persons Killed by Road User Type (2024)')
plt.ylabel('Deaths')
plt.xticks(rotation=45)
plt.savefig(fig_path + 'C1_road_user_deaths.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()

total = road_user['Persons killed 2024'].sum()
road_user['Share %'] = (road_user['Persons killed 2024'] / total * 100).round(1)
road_user.sort_values('Share %', ascending=False)
helmet_killed = safety_device['No Helmet - Killed'].sum()
seatbelt_killed = safety_device['No Seat belt - killed'].sum()
two_wheeler_deaths = road_user[road_user['Road-user category'] == 'Two-wheelers']['Persons killed 2024'].values[0]

print("Deaths without helmet   :", helmet_killed)
print("Deaths without seat belt:", seatbelt_killed)
print("% of two wheeler deaths without helmet:", round(helmet_killed / two_wheeler_deaths * 100, 1), "%")

x = np.arange(2)
width = 0.35
plt.figure(figsize=(8, 5))
plt.bar(x - width/2, [safety_device['No Helmet - Killed'][0], safety_device['No Seat belt - killed'][0]], width, label='Drivers')
plt.bar(x + width/2, [safety_device['No Helmet - Killed'][1], safety_device['No Seat belt - killed'][1]], width, label='Passengers')
plt.xticks(x, ['No Helmet', 'No Seat Belt'])
plt.ylabel('Deaths')
plt.title('Deaths due to not using Safety Devices (2024)')
plt.legend()
plt.savefig(fig_path + 'C3_helmet_seatbelt.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()
x = np.arange(len(age_gender))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, age_gender['2018 - Male'], width, label='Male', color='royalblue')
plt.bar(x + width/2, age_gender['2018 - Female'], width, label='Female', color='hotpink')
plt.xticks(x, age_gender['Age-Group'])
plt.title('Road Deaths by Age Group and Gender (2018)')
plt.xlabel('Age group')
plt.ylabel('Deaths')
plt.legend()
plt.savefig(fig_path + 'C4_age_gender.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()

male = age_gender['2018 - Male'].sum()
female = age_gender['2018 - Female'].sum()
print("Male share  :", round(male / (male + female) * 100, 1), "%")
print("Female share:", round(female / (male + female) * 100, 1), "%")

age_18_45 = age_gender[age_gender['Age-Group'].isin(['18-25', '25-35', '35-45'])]
young = age_18_45['2018 - Male'].sum() + age_18_45['2018 - Female'].sum()
print("Age 18-45 share of deaths:", round(young / (male + female) * 100, 1), "%")
lic_years = ['2020', '2021', '2022', '2023', '2024']

plt.figure(figsize=(10, 5))
for i in range(len(license_type)):
    plt.plot(lic_years, license_type.loc[i, lic_years], marker='o', label=license_type['Type of license'][i])
plt.title('Accidents by Type of Driving Licence')
plt.xlabel('Year')
plt.ylabel('Accidents')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig(fig_path + 'C5_license_type.png', dpi=300, bbox_inches='tight')   # saving the figure
plt.show()

license_type
saved_figures = sorted(os.listdir(fig_path))

print("Total figures saved:", len(saved_figures))
print()
for f in saved_figures:
    print("  ", f)

'''Road deaths increased by about 26% from 2014 to 2024, even though accidents did not increase much.
About 36 people die in every 100 accidents in India.
5 states give almost half of all deaths - UP, Tamil Nadu, Maharashtra, MP and Karnataka.
Bihar, Jharkhand and Punjab have the most deadly accidents (around 80 deaths per 100), while Kerala has the least (about 8).
Causes

Over-speeding is the biggest cause (about 70% of deaths).
Mobile phone use and drunk driving are the most deadly per accident.
Hit and run and vehicle overturn have the highest death rate among collision types.
Potholes are the most deadly road condition.
High-Risk Factors

Two-wheeler riders (46%) and pedestrians (21%) are the most at risk.
Not wearing a helmet is linked to about 66% of two-wheeler deaths.
Young males (18 - 45 years) are the most affected group.'''
