# Ulster University — Student & Visitor Check-In System

A simple command-line Python application that manages check-ins for students and visitors at Ulster University. Built as part of a student representative consultation project to support front-desk operations.

---

## What It Does

- Greets the user and generates a unique **Visit ID** for the session
- Routes to a **Student** or **Visitor** flow based on the user's input
- **Students** — validates registration number, collects name and course, and confirms check-in
- **Visitors** — collects name, displays a staff list, captures host selection, and returns availability status

---

## Requirements

- Python 3.8 or higher
- No third-party libraries — uses only the built-in `random` module

---

## How To Run

```bash
# Clone the repository
git clone https://github.com/Iheanacho-Innocent/ulster-checkin-system.git

cd ulster-checkin-system

python visitor_checkin.py
```

---

## Example Output

**Student check-in:**
```
Welcome To Ulster University
You can clock in with this system
Visit ID: 4823
Are you a visitor or a Student? student
Kindly input your student registration number: 10045
Dear Student, Welcome to school...
Kindly type your full name: Innocent Iheanacho
What is your course of study: MSc Data Analytics
Thank you, Innocent! You have been checked in successfully.
```

**Visitor check-in:**
```
Welcome To Ulster University
You can clock in with this system
Visit ID: 7341
Are you a visitor or a Student? visitor
Welcome to our esteemed institution
Please input your full name: John Smith
Please who is hosting you? Choose from the list:
1 - Dr James
2 - Dr Emeka
3 - Prof Thomas
Enter the number of your host: 2
You can walk to his office, he is available.
```


## Author
**Innocent Emeka Iheanacho**
MSc International Business with Data Analytics — Ulster University
[LinkedIn](https://www.linkedin.com/in/iheanacho-innocent-emeka/) | [GitHub](https://github.com/Iheanacho-Innocent)
