

import datetime
# Store speaker details and lecture schedules

speakers = {}
lectures = []
# Function to add a speaker

def add_speaker():
    name = input("Enter speaker name: ")
    topic = input("Enter topic of expertise: ")
    email = input("Enter speaker email: ")
    if email in speakers:
        print("❌ Speaker already exists.\n")
    else:
        speakers[email] = {
            'name': name,
            'topic': topic,
            'email': email
        }
        print(f"✅ Speaker '{name}' added successfully.\n")
# Function to schedule a guest lecture

def schedule_lecture():
    email = input("Enter speaker email to schedule: ")
    if email not in speakers:
        print("❌ Speaker not found. Please add the speaker first.\n")
        return
    date_str = input("Enter lecture date and time (YYYY-MM-DD HH:MM): ")
    try:
        lecture_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        lecture = {
            'speaker_email': email,
            'datetime': lecture_datetime
        }
        lectures.append(lecture)
        print("✅ Lecture scheduled successfully.\n")
    except ValueError:
        print("❌ Invalid date format.\n")
        
# Function to view all scheduled lectures
def view_lectures():
    if not lectures:
        print("📭 No lectures scheduled yet.\n")
        return
    print("\n📅 Scheduled Guest Lectures:")
    for i, lecture in enumerate(lectures, 1):
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"{i}. {speaker['name']} ({speaker['topic']}) on {dt}")
    print()

# Function to send reminders (simulated)
def send_reminders():
    now = datetime.datetime.now()
    upcoming = [
        l for l in lectures
        if 0 <= (l['datetime'] - now).days <= 1
    ]
    if not upcoming:
        print("📭 No upcoming lectures within 1 day.\n")
        return
    print("🔔 Sending reminders for upcoming lectures:\n")
    for lecture in upcoming:
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"Reminder sent to {speaker['name']} ({speaker['email']}) for lecture on {dt}")
    print()

# Main menu loop
def main():
    while True:
        print("=== Guest Lecture Scheduler ===")
        print("1. Add Speaker")
        print("2. Schedule Guest Lecture")
        print("3. View Scheduled Lectures")
        print("4. Send Event Reminders")
        print("5. Exit")  
        choice = input("Enter your choice (1-5): ")
        print()
        if choice == '1':
            add_speaker()
        elif choice == '2':
            schedule_lecture()
        elif choice == '3':
            view_lectures()
        elif choice == '4':
            send_reminders()
        elif choice == '5':
            print("👋 Exiting Guest Lecture Scheduler. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.\n")

# Run the program
main()

import datetime

# Store speaker details and lecture schedules
speakers = {}
lectures = []

# Function to add a speaker
def add_speaker():
    name = input("Enter speaker name: ")
    topic = input("Enter topic of expertise: ")
    email = input("Enter speaker email: ")
    
    if email in speakers:
        print("❌ Speaker already exists.\n")
    else:
        speakers[email] = {
            'name': name,
            'topic': topic,
            'email': email
        }
        print(f"✅ Speaker '{name}' added successfully.\n")

# Function to schedule a guest lecture
def schedule_lecture():
    email = input("Enter speaker email to schedule: ")
    if email not in speakers:
        print("❌ Speaker not found. Please add the speaker first.\n")
        return
    
    date_str = input("Enter lecture date and time (YYYY-MM-DD HH:MM): ")
    try:
        lecture_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        lecture = {
            'speaker_email': email,
            'datetime': lecture_datetime
        }
        lectures.append(lecture)
        print("✅ Lecture scheduled successfully.\n")
    except ValueError:
        print("❌ Invalid date format.\n")

# Function to view all scheduled lectures
def view_lectures():
    if not lectures:
        print("📭 No lectures scheduled yet.\n")
        return

    print("\n📅 Scheduled Guest Lectures:")
    for i, lecture in enumerate(lectures, 1):
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"{i}. {speaker['name']} ({speaker['topic']}) on {dt}")
    print()

# Function to send reminders (simulated)
def send_reminders():
    now = datetime.datetime.now()
    upcoming = [
        l for l in lectures
        if 0 <= (l['datetime'] - now).days <= 1
    ]
    if not upcoming:
        print("📭 No upcoming lectures within 1 day.\n")
        return

    print("🔔 Sending reminders for upcoming lectures:\n")
    for lecture in upcoming:
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"Reminder sent to {speaker['name']} ({speaker['email']}) for lecture on {dt}")
    print()

# Main menu loop
def main():
    while True:
        print("=== Guest Lecture Scheduler ===")
        print("1. Add Speaker")
        print("2. Schedule Guest Lecture")
        print("3. View Scheduled Lectures")
        print("4. Send Event Reminders")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        print()
        
        if choice == '1':
            add_speaker()
        elif choice == '2':
            schedule_lecture()
        elif choice == '3':
            view_lectures()
        elif choice == '4':
            send_reminders()
        elif choice == '5':
            print("👋 Exiting Guest Lecture Scheduler. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.\n")

# Run the program
main()
import datetime

# Store speaker details and lecture schedules
speakers = {}
lectures = []

# Function to add a speaker
def add_speaker():
    name = input("Enter speaker name: ")
    topic = input("Enter topic of expertise: ")
    email = input("Enter speaker email: ")
    
    if email in speakers:
        print("❌ Speaker already exists.\n")
    else:
        speakers[email] = {
            'name': name,
            'topic': topic,
            'email': email
        }
        print(f"✅ Speaker '{name}' added successfully.\n")

# Function to schedule a guest lecture
def schedule_lecture():
    email = input("Enter speaker email to schedule: ")
    if email not in speakers:
        print("❌ Speaker not found. Please add the speaker first.\n")
        return
    
    date_str = input("Enter lecture date and time (YYYY-MM-DD HH:MM): ")
    try:
        lecture_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        lecture = {
            'speaker_email': email,
            'datetime': lecture_datetime
        }
        lectures.append(lecture)
        print("✅ Lecture scheduled successfully.\n")
    except ValueError:
        print("❌ Invalid date format.\n")

# Function to view all scheduled lectures
def view_lectures():
    if not lectures:
        print("📭 No lectures scheduled yet.\n")
        return

    print("\n📅 Scheduled Guest Lectures:")
    for i, lecture in enumerate(lectures, 1):
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"{i}. {speaker['name']} ({speaker['topic']}) on {dt}")
    print()

# Function to send reminders (simulated)
def send_reminders():
    now = datetime.datetime.now()
    upcoming = [
        l for l in lectures
        if 0 <= (l['datetime'] - now).days <= 1
    ]
    if not upcoming:
        print("📭 No upcoming lectures within 1 day.\n")
        return

    print("🔔 Sending reminders for upcoming lectures:\n")
    for lecture in upcoming:
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"Reminder sent to {speaker['name']} ({speaker['email']}) for lecture on {dt}")
    print()

# Main menu loop
def main():
    while True:
        print("=== Guest Lecture Scheduler ===")
        print("1. Add Speaker")
        print("2. Schedule Guest Lecture")
        print("3. View Scheduled Lectures")
        print("4. Send Event Reminders")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        print()
        
        if choice == '1':
            add_speaker()
        elif choice == '2':
            schedule_lecture()
        elif choice == '3':
            view_lectures()
        elif choice == '4':
            send_reminders()
        elif choice == '5':
            print("👋 Exiting Guest Lecture Scheduler. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.\n")

# Run the program
main()
import datetime

# Store speaker details and lecture schedules
speakers = {}
lectures = []

# Function to add a speaker
def add_speaker():
    name = input("Enter speaker name: ")
    topic = input("Enter topic of expertise: ")
    email = input("Enter speaker email: ")
    
    if email in speakers:
        print("❌ Speaker already exists.\n")
    else:
        speakers[email] = {
            'name': name,
            'topic': topic,
            'email': email
        }
        print(f"✅ Speaker '{name}' added successfully.\n")

# Function to schedule a guest lecture
def schedule_lecture():
    email = input("Enter speaker email to schedule: ")
    if email not in speakers:
        print("❌ Speaker not found. Please add the speaker first.\n")
        return
    
    date_str = input("Enter lecture date and time (YYYY-MM-DD HH:MM): ")
    try:
        lecture_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        lecture = {
            'speaker_email': email,
            'datetime': lecture_datetime
        }
        lectures.append(lecture)
        print("✅ Lecture scheduled successfully.\n")
    except ValueError:
        print("❌ Invalid date format.\n")

# Function to view all scheduled lectures
def view_lectures():
    if not lectures:
        print("📭 No lectures scheduled yet.\n")
        return

    print("\n📅 Scheduled Guest Lectures:")
    for i, lecture in enumerate(lectures, 1):
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"{i}. {speaker['name']} ({speaker['topic']}) on {dt}")
    print()

# Function to send reminders (simulated)
def send_reminders():
    now = datetime.datetime.now()
    upcoming = [
        l for l in lectures
        if 0 <= (l['datetime'] - now).days <= 1
    ]
    if not upcoming:
        print("📭 No upcoming lectures within 1 day.\n")
        return

    print("🔔 Sending reminders for upcoming lectures:\n")
    for lecture in upcoming:
        speaker = speakers[lecture['speaker_email']]
        dt = lecture['datetime'].strftime("%Y-%m-%d %H:%M")
        print(f"Reminder sent to {speaker['name']} ({speaker['email']}) for lecture on {dt}")
    print()

# Main menu loop
def main():
    while True:
        print("=== Guest Lecture Scheduler ===")
        print("1. Add Speaker")
        print("2. Schedule Guest Lecture")
        print("3. View Scheduled Lectures")
        print("4. Send Event Reminders")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        print()
        
        if choice == '1':
            add_speaker()
        elif choice == '2':
            schedule_lecture()
        elif choice == '3':
            view_lectures()
        elif choice == '4':
            send_reminders()
        elif choice == '5':
            print("👋 Exiting Guest Lecture Scheduler. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.\n")

# Run the program
main()
