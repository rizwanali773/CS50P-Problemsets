# StudyPulse 🧠📘

#### [Video Demo](https://youtu.be/x2kcZqMXWv8)

## CS50P Final Project

**StudyPulse** is a command-line Python application that helps students track their daily study habits and provides smart analysis with personalized feedback. Instead of being just a simple tracker, StudyPulse analyzes patterns in study time, subjects, moods, and consistency to encourage better study habits.

This project is designed specifically to meet the requirements of **CS50’s Introduction to Programming with Python (CS50P)**.

---

## 🎯 Project Motivation

Many students study regularly but fail to understand:

* Which subjects they neglect
* Whether they are consistent
* If they are overworking or burning out

StudyPulse solves this problem by turning raw study logs into **meaningful insights**.

---

## 🛠️ Features

* 📅 Log daily study sessions (date, subject, time, mood)
* 💾 Persistent storage using a JSON file
* 📊 Automatic analysis of study data
* 🧠 Personalized feedback and suggestions
* 🔥 Study streak detection
* 📆 Weekly report using command-line arguments

---

## 🧩 Concepts Used (CS50 Checklist)

* Functions and modular design
* Loops and conditionals
* Lists and dictionaries
* File handling (JSON)
* Error handling with try/except
* Command-line arguments (`sys.argv`)
* Clean, readable, and well-commented code

---

## 🚀 How to Run the Project

### 1️⃣ Run the main program

```bash
python project.py
```

You will see an interactive menu:

* Add Study Log
* View Summary
* Exit

---

### 2️⃣ Generate Weekly Report

```bash
python project.py --weekly-report
```

This command displays a summary of the last 7 days including:

* Total study time
* Active study days
* Productivity score

---

## 📂 File Structure

```
project.py          # Main application file
study_data.json     # Data file (auto-created)
README.md           # Project documentation
```

---

## 🧪 Sample Input

```
Date: 2025-12-15
Subject: Python
Time: 90
Mood: tired
```

## 📤 Sample Output

```
📊 Study Summary
🔥 Most studied subject: Python
⚠️ Least studied subject: Physics

🧠 Personalized Feedback
😴 You felt tired often. Consider taking proper breaks.
```

---

## 🔮 Future Improvements

* Graphical charts (ASCII or GUI)
* Export weekly report as a text file
* Reminder system for missed study days
* More advanced productivity scoring

---

## 👨‍💻 Author

**Mohammd Adnan Ali**
B. Tech. - CSE(IoT) - '28, India
CS50 Python Student

---

## ✅ Academic Honesty

This project is my own original work, created for the CS50 Python course, following all academic honesty guidelines.

---

⭐ *Study smart, not just hard!*