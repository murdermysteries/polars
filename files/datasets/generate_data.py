"""
Data Generation Script for "Death at the Aurora Theater" Murder Mystery
This script generates synthetic datasets for the murder mystery scenario.
"""

import pandas as pd
import polars as pl
import random
import string
from datetime import datetime, timedelta
from faker import Faker

# Set random seed for reproducibility
random.seed(42)
fake = Faker()
Faker.seed(42)

# Constants
CASE_DATE = "2025-03-15"  # Date of the murder
CASE_ID = "AURORA-2025-03-15"  # Unique case ID for the murder

def generate_case_id(length=10):
    """Generate a random alphanumeric case ID"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_random_date(start_year=2023, end_date=None):
    """Generate a random date between start_year and end_date"""
    if end_date is None:
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    start_date = datetime(start_year, 1, 1)
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_random_datetime(start_year=2023, end_date=None, specific_date=None):
    """Generate a random datetime with time"""
    if specific_date:
        # Use the specific date but random time
        base_date = datetime.strptime(specific_date, "%Y-%m-%d")
        hours = random.randint(9, 23)  # Theater hours
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        return base_date.replace(hour=hours, minute=minutes, second=seconds).strftime("%Y-%m-%d %H:%M:%S")
    else:
        # Completely random date and time
        date_str = generate_random_date(start_year, end_date)
        base_date = datetime.strptime(date_str, "%Y-%m-%d")
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        return base_date.replace(hour=hours, minute=minutes, second=seconds).strftime("%Y-%m-%d %H:%M:%S")

def generate_member_id(length=8):
    """Generate a random member ID"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Generate Police Records
def generate_police_records(num_records=100):
    """Generate synthetic police records"""
    squads = ["homicide", "narcotics", "cybercrime", "fraud", "burglary", "organized crime"]
    locations = ["Aurora Theater", "Downtown Park", "Riverside Mall", "Central Station", "Eastside Alley", "West End Club"]
    
    # Make sure our murder case is included
    data = {
        "case_id": [CASE_ID] + [generate_case_id() for _ in range(num_records-1)],
        "squad": ["homicide"] + [random.choice(squads) for _ in range(num_records-1)],
        "date": [CASE_DATE] + [generate_random_date() for _ in range(num_records-1)],
        "location": ["Aurora Theater"] + [random.choice(locations) for _ in range(num_records-1)],
        "type": ["murder"] + [random.choice(["theft", "assault", "vandalism", "fraud", "murder", "drug offense"]) for _ in range(num_records-1)]
    }
    
    return pl.DataFrame(data)

# Generate Witness Reports
def generate_witness_reports(case_ids, num_reports=150):
    """Generate synthetic witness reports"""
    
    def generate_testimony():
        observations = [
            "I saw a suspicious person near the stage.",
            "There was a loud noise before people started running.",
            "Someone was arguing loudly moments before it happened.",
            "I noticed someone rushing backstage right after the performance.",
            "I noticed broken glass and heard shouting.",
            "There was a strange person watching the actors all evening."
        ]
        actions = [
            "They looked nervous and kept checking over their shoulder.",
            "They dropped something and quickly picked it up.",
            "They ran off when the commotion started.",
            "They were wearing dark clothes and avoided eye contact.",
            "They seemed to be waiting for someone.",
            "They spoke briefly with another person and left."
        ]
        return f"{random.choice(observations)} {random.choice(actions)}"
    
    # Create specific testimonies for our murder case
    specific_testimonies = [
        "I saw the lighting technician arguing with the victim earlier in the day. They seemed very angry.",
        "The stage manager was acting strangely all evening, constantly checking the time.",
        "I noticed the costume designer had access to the victim's dressing room multiple times.",
        "The sound engineer was the last person I saw talking to the victim before the performance.",
        "The director and the victim had a heated argument about creative differences during rehearsal."
    ]
    
    # Generate data with specific testimonies for our case
    data = {
        "case_id": [CASE_ID] * 5 + [random.choice(case_ids) for _ in range(num_reports-5)],
        "witness_name": [fake.name() for _ in range(num_reports)],
        "testimony": specific_testimonies + [generate_testimony() for _ in range(num_reports-5)]
    }
    
    return pl.DataFrame(data)

# Generate Stage Access Logs
def generate_stage_access_logs(num_logs=200):
    """Generate synthetic stage access logs"""
    locations = [
        "main stage", "backstage", "lighting grid", "prop room", "dressing room", "sound booth", "orchestra pit"
    ]
    directions = ["entering", "leaving"]
    
    # Generate random employee IDs
    employee_ids = [generate_member_id() for _ in range(20)]
    
    # Include our murderer's movements
    murderer_id = employee_ids[0]  # First ID is our murderer
    victim_id = employee_ids[1]    # Second ID is our victim
    
    # Create specific access logs for murder day
    murder_day_logs = [
        # Murderer's movements
        {"date": f"{CASE_DATE} 18:30:45", "location": "backstage", "member_id": murderer_id, "direction": "entering"},
        {"date": f"{CASE_DATE} 19:15:22", "location": "lighting grid", "member_id": murderer_id, "direction": "entering"},
        {"date": f"{CASE_DATE} 19:45:10", "location": "lighting grid", "member_id": murderer_id, "direction": "leaving"},
        {"date": f"{CASE_DATE} 19:46:33", "location": "dressing room", "member_id": murderer_id, "direction": "entering"},
        {"date": f"{CASE_DATE} 19:52:18", "location": "dressing room", "member_id": murderer_id, "direction": "leaving"},
        {"date": f"{CASE_DATE} 21:30:05", "location": "backstage", "member_id": murderer_id, "direction": "leaving"},
        
        # Victim's movements
        {"date": f"{CASE_DATE} 17:45:12", "location": "dressing room", "member_id": victim_id, "direction": "entering"},
        {"date": f"{CASE_DATE} 18:30:33", "location": "dressing room", "member_id": victim_id, "direction": "leaving"},
        {"date": f"{CASE_DATE} 18:35:47", "location": "main stage", "member_id": victim_id, "direction": "entering"},
        {"date": f"{CASE_DATE} 20:15:22", "location": "main stage", "member_id": victim_id, "direction": "leaving"},
        {"date": f"{CASE_DATE} 20:20:18", "location": "dressing room", "member_id": victim_id, "direction": "entering"}
        # No exit log for victim - they were found dead in the dressing room
    ]
    
    # Generate random access logs
    random_logs = []
    for _ in range(num_logs - len(murder_day_logs)):
        # 20% chance of being on murder day, 80% other days
        if random.random() < 0.2:
            date = generate_random_datetime(specific_date=CASE_DATE)
        else:
            date = generate_random_datetime()
            
        random_logs.append({
            "date": date,
            "location": random.choice(locations),
            "member_id": random.choice(employee_ids),
            "direction": random.choice(directions)
        })
    
    # Combine specific and random logs
    all_logs = murder_day_logs + random_logs
    
    # Convert to DataFrame
    return pl.DataFrame(all_logs)

# Generate Staff Database
def generate_staff_database(employee_ids):
    """Generate synthetic staff database"""
    roles = [
        "Stage Manager", "Lighting Technician", "Sound Engineer", "Set Designer", "Costume Designer",
        "Actor", "Director", "Props Master", "Makeup Artist", "Usher", "Box Office Clerk",
        "Production Assistant", "Choreographer", "Dramaturg", "Front of House Manager"
    ]
    
    # Make sure our murderer is the lighting technician and victim is the lead actor
    murderer_id = employee_ids[0]
    victim_id = employee_ids[1]
    
    data = {
        "employee_id": employee_ids,
        "employee_name": [fake.name() for _ in range(len(employee_ids))],
        "employee_role": ["Lighting Technician", "Lead Actor"] + [random.choice(roles) for _ in range(len(employee_ids)-2)]
    }
    
    return pl.DataFrame(data)

# Main function to generate all datasets
def generate_all_datasets():
    """Generate all datasets for the murder mystery"""
    # Generate police records
    police_records = generate_police_records(100)
    police_records.write_csv("police_records.csv")
    
    # Get case IDs for witness reports
    case_ids = police_records["case_id"].to_list()
    
    # Generate witness reports
    witness_reports = generate_witness_reports(case_ids, 150)
    witness_reports.write_csv("witness_reports.csv")
    
    # Generate stage access logs
    stage_access = generate_stage_access_logs(200)
    stage_access.write_csv("stage_access.csv")
    
    # Get employee IDs from stage access logs
    employee_ids = stage_access["member_id"].unique().to_list()
    
    # Generate staff database
    staff_database = generate_staff_database(employee_ids)
    staff_database.write_csv("staff_database.csv")
    
    # Return the murderer and victim information for verification
    murderer_id = employee_ids[0]
    murderer_info = staff_database.filter(pl.col("employee_id") == murderer_id)
    victim_id = employee_ids[1]
    victim_info = staff_database.filter(pl.col("employee_id") == victim_id)
    
    return {
        "murderer_id": murderer_id,
        "murderer_name": murderer_info["employee_name"][0],
        "murderer_role": murderer_info["employee_role"][0],
        "victim_id": victim_id,
        "victim_name": victim_info["employee_name"][0],
        "victim_role": victim_info["employee_role"][0],
        "case_id": CASE_ID,
        "case_date": CASE_DATE
    }

if __name__ == "__main__":
    print("Starting data generation...")
    try:
        # Generate all datasets
        result = generate_all_datasets()
        print("Datasets generated successfully!")
        print(f"Murderer: {result['murderer_name']} ({result['murderer_role']})")
        print(f"Victim: {result['victim_name']} ({result['victim_role']})")
        
        # Print current directory and files
        import os
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in current directory: {os.listdir('.')}")
    except Exception as e:
        print(f"Error generating datasets: {e}")
