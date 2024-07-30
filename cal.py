from ics import Calendar, Event
from datetime import datetime, timedelta

# Define the timetable data
timetable = [
    {"day": "Monday", "start": "09:00", "end": "09:55", "course": "PCS-308", "location": "CR-2", "faculty": "Dr. Goutam Verma"},
    {"day": "Monday", "start": "11:00", "end": "11:55", "course": "PCS-362", "location": "LT-8", "faculty": "Dr. Abhinav Sharma"},
    {"day": "Monday", "start": "13:00", "end": "13:55", "course": "TCS-304", "location": "LT-8", "faculty": "Mr. Ajay Joshi"},
    {"day": "Tuesday", "start": "09:00", "end": "09:55", "course": "PCS-362 Lab", "location": "Aryabhat First Floor Lab", "faculty": "Lab"},
    {"day": "Tuesday", "start": "11:00", "end": "11:55", "course": "TCS-306", "location": "CR-2", "faculty": "Dr. Ashwini Kumar"},
    {"day": "Tuesday", "start": "13:00", "end": "13:55", "course": "TCS-382", "location": "LT-8", "faculty": "Mr. Nitin Bhardwaj"},
    {"day": "Wednesday", "start": "09:00", "end": "09:55", "course": "PCS-362", "location": "CR-2", "faculty": "Dr. Abhinav Sharma"},
    {"day": "Wednesday", "start": "11:00", "end": "11:55", "course": "PCS-308", "location": "LT-12", "faculty": "Dr. Goutam Verma"},
    {"day": "Wednesday", "start": "13:00", "end": "13:55", "course": "TCS-382", "location": "LT-34", "faculty": "Mr. Nitin Bhardwaj"},
    {"day": "Thursday", "start": "09:00", "end": "09:55", "course": "PCS-362", "location": "LT-8", "faculty": "Dr. Abhinav Sharma"},
    {"day": "Thursday", "start": "11:00", "end": "11:55", "course": "TCS-308 Lab", "location": "Aryabhat First Floor Lab 1", "faculty": "Lab"},
    {"day": "Thursday", "start": "13:00", "end": "13:55", "course": "TCS-304", "location": "LT-13", "faculty": "Mr. Ajay Joshi"},
    {"day": "Friday", "start": "09:00", "end": "09:55", "course": "TCS-306", "location": "CR-2", "faculty": "Dr. Ashwini Kumar"},
    {"day": "Friday", "start": "11:00", "end": "11:55", "course": "TCS-382", "location": "LT-8", "faculty": "Mr. Nitin Bhardwaj"},
    {"day": "Friday", "start": "13:00", "end": "13:55", "course": "PCS-308", "location": "LT-13", "faculty": "Dr. Goutam Verma"},
]

# Create a calendar
calendar = Calendar()

# Function to convert day name to date
def get_date_for_day(day_name):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.now()
    target_day = day_names.index(day_name)
    days_ahead = target_day - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return today + timedelta(days=days_ahead)

# Add events to the calendar
for entry in timetable:
    event = Event()
    event.name = f"{entry['course']} - {entry['location']}"
    event.description = f"Lecture by {entry['faculty']}"
    event.location = entry['location']
    
    event_start_date = get_date_for_day(entry['day'])
    event_start_time = datetime.strptime(entry['start'], "%H:%M").time()
    event_end_time = datetime.strptime(entry['end'], "%H:%M").time()
    
    event.begin = datetime.combine(event_start_date, event_start_time)
    event.end = datetime.combine(event_start_date, event_end_time)
    
    # Set event recurrence to weekly
    event.make_all_day()
    event.recurrences = [f"FREQ=WEEKLY;BYDAY={entry['day'][:2].upper()};INTERVAL=1"]

    calendar.events.add(event)

# Save the calendar to an .ics file
with open('/mnt/data/timetable.ics', 'w') as f:
    f.write(str(calendar))