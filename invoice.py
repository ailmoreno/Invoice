from collections import defaultdict
from datetime import datetime

def parse_time(time_str):
    """Convert time string (e.g., '8 AM') to datetime object."""
    return datetime.strptime(time_str, "%I:%M %p")

def calculate_hours(start, end):
    """Calculate the difference in hours between start and end time and round to one decimal place."""
    hours = (parse_time(end) - parse_time(start)).seconds / 3600
    return round(hours, 1)

def add_project(records, project_name, start, end):
    """Add project hours to the records, summing up hours for similar projects."""
    hours = calculate_hours(start, end)
    records[project_name] += hours

def display_summary(records):
    """Print the total billable hours for each project."""
    print("\nFinal Output:")
    for project, total_hours in records.items():
        print(f"{project}: {total_hours} hours")
    
    print("\nTotal Output:")
    total_hours_all_projects = sum(records.values())
    print(f"Total Hours: {total_hours_all_projects} hours")

if __name__ == "__main__":
    records = defaultdict(float)
    
    while True:
        project_name = input("Enter project name (or type 'stop' to finish): ")
        if project_name.lower() == 'stop':
            break
        start_time = input("Enter start time (e.g., 8:00 AM): ")
        end_time = input("Enter end time (e.g., 9:15 AM): ")
        add_project(records, project_name, start_time, end_time)
    
    display_summary(records)
