# Polars Murder Mysteries

The goal is to develop a series of murder mysteries (in a cozy crime novel style) that help to learn the features of the polars package for data analysis.

The murder mysteries should be hosted in an online notebook environment. Candidates are Google Colab or sth like Jupyterlite (see [here](https://jtp.io/jupytercon-2023-jupyterlite/files/index.html#1)) or Marimo. It's necessary to have Polars pre-installed and to be able to load static files (the notebooks).

The project is inspired by SQL Murder Mysteries: <https://mystery.knightlab.com/>

## Naming Ideas 

for a project that eventually spans multiple data analysis languages

* Database Detectives
* Dataframe Detectives
* Dataset Detectives

## Cases based on Claude

Death at the Aurora Theater

- police record database
    - type: murder
    - location: theater
    - date: yesterday (relative date vs. user date?)
    - => case id
- Witness Reports
    - case id
    - witness name
    - testimony
    => saw crime from different angles 
- stage access
    - date
    - location
    - member id
- staff database
    - member id
    - staff name
    - staff role
- ticket database: not needed, full fake data
- theater review archives for different actors: not needed, full fake data


## Polars Material

* Cheatsheet as PDF: <https://franzdiebold.github.io/polars-cheat-sheet/Polars_cheat_sheet.pdf>
* Overview of Polars vs Pandas: <https://www.rhosignal.com/posts/polars-pandas-cheatsheet/>
* Getting started with Polars: <https://docs.pola.rs/user-guide/getting-started/>

## Prompts with ChatGPT

> I want to create exercises for learning the "polars" library for data analysis based on fictious data-driven murder mysteries. Every mystery can be solved by analysing dataframes and joining them to find subsets of interest (e.g. a list of license plates that were seen at a certain time and a database of the owners of the respective cars). I want to develop small, slightly whimsical murder mysteries in the style of cozy crime novels. They should use polar bears as protagonists.
> Please help me brainstorm 10 ideas for such murder mysteries. For each idea, also suggest potential cases for dataframes that have data linked to the respective case. 

Here are 10 whimsical murder mystery ideas featuring polar bears, each tied to potential dataframes for analysis:

---

### 1. **The Case of the Missing Iceberg**
**Plot**: A polar bear scientist claims their research iceberg was stolen overnight, disrupting an important experiment. 
**Dataframes**: 
- **Iceberg Tracker**: Timestamps, GPS coordinates, and iceberg IDs.
- **Research Logs**: Iceberg ID, experiment details, and assigned scientists.
- **Weather Records**: Timestamp, wind speeds, and currents.

---

### 2. **The Midnight Fish Heist**
**Plot**: The Grand Fish Feast preparation is halted when the storage catches are raided.
**Dataframes**:
- **Storage Inventory**: Fish type, quantity, storage ID, and timestamps.
- **Surveillance Logs**: Timestamped entries for storage areas.
- **Guest List**: Invitees and access badges.

---

### 3. **The Case of the Poisoned Snowcone**
**Plot**: A polar bear chef collapses after tasting a snowcone at a festival.
**Dataframes**:
- **Vendor Sales**: Vendor names, timestamps, and items sold.
- **Ingredient Deliveries**: Delivery time, source, and ingredient type.
- **Hospital Records**: Timestamps and symptoms.

---

### 4. **The Vanishing Sleigh**
**Plot**: A polar bear sleigh racer reports their sled missing hours before a race.
**Dataframes**:
- **Garage Logs**: Timestamped access to sled garages.
- **Competitor Registrations**: Racer names and sled details.
- **Maintenance Records**: Sled IDs and repair histories.

---

### 5. **The Frozen Fish Feud**
**Plot**: A polar bear elder accuses a rival clan of stealing fishing rights on a sacred glacier pond.
**Dataframes**:
- **Fishing Permits**: Bear names, permit IDs, and locations.
- **Catch Logs**: Fisher name, species, and catch timestamps.
- **Glacier Patrol Reports**: Patrol times and observations.

---

### 6. **The Artic Art Caper**
**Plot**: A rare ice sculpture is discovered to be a forgery during a high-profile auction.
**Dataframes**:
- **Sculpture Registry**: IDs, creators, and appraisal values.
- **Auction Records**: Buyer and bid data.
- **Authentication Logs**: Timestamped verifications of sculptures.

---

### 7. **The Blizzard Burglary**
**Plot**: During a fierce snowstorm, a polar bear entrepreneur reports stolen tech equipment.
**Dataframes**:
- **Tech Inventory**: Item names, serial numbers, and owners.
- **Storm Tracker**: Timestamps, snow intensities, and wind speeds.
- **Witness Statements**: Sightings with timestamps and descriptions.

---

### 8. **The Paw Print Puzzle**
**Plot**: A polar bear cub finds unusual paw prints near their den and suspects foul play.
**Dataframes**:
- **Paw Print Database**: Shape, size, and bear IDs.
- **Territory Maps**: Bear IDs and assigned areas.
- **Ranger Reports**: Timestamped patrol observations.

---

### 9. **The Glacier Gala Scandal**
**Plot**: A prized fish dish at a gala dinner is found sabotaged with non-native species.
**Dataframes**:
- **Menu Plans**: Dish details and assigned chefs.
- **Supply Logs**: Source and delivery of ingredients.
- **Guest Interactions**: Guest names, seatings, and conversations.

---

### 10. **The Case of the Singing Iceberg**
**Plot**: An iceberg choir’s lead singer goes missing on performance night, replaced by an imposter.
**Dataframes**:
- **Choir Roster**: Singer IDs and parts sung.
- **Attendance Logs**: Arrival times for rehearsal and performance.
- **Transport Records**: Vehicles used and driver IDs.

---

Would you like to expand on any of these ideas or brainstorm more specific dataframe structures?

> Please develop the first case ("The Case of the Missing Iceberg") into a full mystery including:

> - an introduction to the reader
> - an overview of the tables for the reader
> - a culprit with a motive
> - polars code to create the different dataframes. there should be at least 100 potential suspects in the tables to avoid brute-force attempts.
> - a function where the reader can suggest a suspect and the function verifies whether the suspect is indeed the culprit

> (NOTE TO SELF: The script below does not really offer any logic why a specific suspect is indeed the culprit. Will require some additional prompting to generate code that captures this.) Worked on related topic for pandas murder mysteries: <C:\Users\maxal\OneDrive\Desktop\Dropbox\python\pandas_murder_mystery>

```python
# The Case of the Missing Iceberg
# Introduction:
# Late one evening, Dr. Ursula Polar, a renowned glaciologist, discovers her research iceberg (ID: "GLC-042") has vanished from its designated GPS coordinates. This iceberg was crucial to her climate study, and its disappearance threatens months of work. 
# Can you help solve the mystery by analyzing the provided data tables?

import polars as pl
import random
import pandas as pd
from datetime import datetime, timedelta
from faker import Faker

# Overview of Tables:
# 1. Iceberg Tracker: Logs GPS coordinates and movements of icebergs ("iceberg_tracker").
# 2. Research Logs: Records which scientist was working on which iceberg ("research_logs").
# 3. Weather Records: Contains environmental data for the relevant timestamps ("weather_records").
# 4. Witness Statements: Lists polar bears and their observations near the iceberg's location ("witness_statements").

# Data Preparation
random.seed(42)
fake = Faker()


def generate_random_datetime(start_date, end_date, n):
    return [
        start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        for _ in range(n)
    ]

# 1. Iceberg Tracker
diceberg_ids = [f"GLC-{i:03d}" for i in range(50)]
diceberg_tracker_data = {
    "timestamp": generate_random_datetime(datetime(2023, 1, 1), datetime(2023, 12, 31), 1000),
    "iceberg_id": [random.choice(diceberg_ids) for _ in range(1000)],
    "gps_latitude": [random.uniform(-90.0, -60.0) for _ in range(1000)],
    "gps_longitude": [random.uniform(0.0, 180.0) for _ in range(1000)],
}
diceberg_tracker = pl.DataFrame(diceberg_tracker_data)

# 2. Research Logs
scientists = [fake.name() for _ in range(100)]
research_logs_data = {
    "iceberg_id": random.choices(diceberg_ids, k=200),
    "scientist": random.choices(scientists, k=200),
    "experiment": [random.choice(["Melt Rate", "Core Sampling", "Salinity Testing"]) for _ in range(200)],
}
research_logs = pl.DataFrame(research_logs_data)

# 3. Weather Records
weather_records_data = {
    "timestamp": generate_random_datetime(datetime(2023, 1, 1), datetime(2023, 12, 31), 1000),
    "wind_speed": [random.uniform(0.0, 30.0) for _ in range(1000)],
    "current_direction": [random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"]) for _ in range(1000)],
    "temperature": [random.uniform(-40.0, 0.0) for _ in range(1000)],
}
weather_records = pl.DataFrame(weather_records_data)

# 4. Witness Statements
polar_bears = [fake.first_name() for _ in range(150)]
witness_statements_data = {
    "bear_id": random.choices(polar_bears, k=300),
    "observation_time": generate_random_datetime(datetime(2023, 1, 1), datetime(2023, 12, 31), 300),
    "description": [
        random.choice(["Saw movement", "Heard strange noises", "Noticed unusual tracks", "Saw nothing"])
        for _ in range(300)
    ],
}
witness_statements = pl.DataFrame(witness_statements_data)

# Culprit Details:
culprit = "Scientist_42"
motive = "Scientist_42 wanted to sabotage Dr. Ursula's study to promote their rival research."

# Verification Function
def verify_culprit(suspect):
    if suspect == culprit:
        return "Correct! Scientist_42 sabotaged the study by towing the iceberg away."
    return "Incorrect. Keep analyzing the data!"

# Polars Code to Inspect Data
print("\nIceberg Tracker:\n", diceberg_tracker.head(5))
print("\nResearch Logs:\n", research_logs.head(5))
print("\nWeather Records:\n", weather_records.head(5))
print("\nWitness Statements:\n", witness_statements.head(5))
```