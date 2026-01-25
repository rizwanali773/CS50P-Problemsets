import json
import sys
from datetime import datetime, timedelta

DATA_FILE = "study_data.json"


# -------------------- MAIN --------------------
def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--weekly-report":
        generate_weekly_report()
    else:
        show_menu()


# -------------------- MENU --------------------
def show_menu():
    while True:
        print("\n📘 StudyPulse Menu")
        print("1. Add Study Log")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_study_log()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Goodbye! Keep studying smart.")
            break
        else:
            print("❌ Invalid choice. Try again.")


# -------------------- ADD STUDY LOG --------------------
def add_study_log():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        datetime.strptime(date, "%Y-%m-%d")  # validation

        subject = input("Enter subject: ").strip().title()
        time_spent = int(input("Time studied (minutes): ").strip())
        mood = input("Mood (happy / tired / neutral): ").strip().lower()

        entry = {
            "date": date,
            "subject": subject,
            "time": time_spent,
            "mood": mood
        }

        save_to_file(entry)
        print("✅ Study log saved successfully!")

    except ValueError:
        print("❌ Invalid input. Please try again.")


# -------------------- FILE HANDLING --------------------
def save_to_file(entry):
    data = load_data()
    data.append(entry)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# -------------------- SUMMARY --------------------
def view_summary():
    data = load_data()

    if not data:
        print("⚠️ No study data available.")
        return

    analyze_data(data)


# -------------------- ANALYSIS --------------------
def analyze_data(data):
    subject_time = {}
    mood_count = {}

    for entry in data:
        subject = entry["subject"]
        time_spent = entry["time"]
        mood = entry["mood"]

        subject_time[subject] = subject_time.get(subject, 0) + time_spent
        mood_count[mood] = mood_count.get(mood, 0) + 1

    best_subject = max(subject_time, key=subject_time.get)
    weak_subject = min(subject_time, key=subject_time.get)

    print("\n📊 Study Summary")
    print(f"🔥 Most studied subject: {best_subject}")
    print(f"⚠️ Least studied subject: {weak_subject}")

    generate_feedback(subject_time, mood_count)


# -------------------- FEEDBACK --------------------
def generate_feedback(subject_time, mood_count):
    print("\n🧠 Personalized Feedback")

    weak_subject = min(subject_time, key=subject_time.get)
    if subject_time[weak_subject] < 60:
        print(f"📌 You are neglecting {weak_subject}. Try studying it tomorrow.")

    if mood_count.get("tired", 0) >= 3:
        print("😴 You felt tired often. Consider taking proper breaks.")

    streak = calculate_streak()
    if streak >= 5:
        print(f"🔥 Amazing! You have a {streak}-day study streak!")


# -------------------- STUDY STREAK --------------------
def calculate_streak():
    data = load_data()
    dates = sorted({entry["date"] for entry in data})

    streak = 0
    today = datetime.today().date()

    for i in range(len(dates)):
        if today - timedelta(days=i) == datetime.strptime(dates[-1 - i], "%Y-%m-%d").date():
            streak += 1
        else:
            break

    return streak


# -------------------- WEEKLY REPORT --------------------
def generate_weekly_report():
    data = load_data()
    if not data:
        print("⚠️ No data for weekly report.")
        return

    last_week = datetime.today() - timedelta(days=7)
    weekly_data = [
        entry for entry in data
        if datetime.strptime(entry["date"], "%Y-%m-%d") >= last_week
    ]

    total_time = sum(entry["time"] for entry in weekly_data)
    days = len({entry["date"] for entry in weekly_data})
    productivity_score = min(100, total_time // 5)

    print("\n📅 Weekly Study Report")
    print(f"⏱️ Total study time: {total_time} minutes")
    print(f"📆 Active days: {days}")
    print(f"⭐ Productivity Score: {productivity_score}/100")


# -------------------- RUN --------------------
if __name__ == "__main__":
    main()