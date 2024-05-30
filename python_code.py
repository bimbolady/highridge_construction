

# Here's a python program to facilitate the weekly payments of workers at Highridge Construction Company

import random

# Function to generate random names
def generate_name():
    first_names = ['Chinedu', 'Adebambo', 'Adeola', 'Kareemat', 'Barakat', 'Dolapo', 'Boluwatife', 'Oluwaseun']
    last_names = ['Okon', 'Aderibigbe', 'Adesina', 'Akindele', 'Olasupo', 'Olasupo', 'Kendrick', 'Ogunyoye']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random salaries (within the range of 5000 to 35000)
def generate_salary():
    return random.randint(5000, 35000)

# Function to generate random gender
def generate_gender():
    return random.choice(['Male', 'Female'])

# Generate list of workers with their names, salary, and gender
workers = []
for _ in range(400):
    name = generate_name()
    salary = generate_salary()
    gender = generate_gender()
    workers.append({'name': name, 'salary': salary, 'gender': gender})

for worker in workers:
    print(worker)

# Next is a code to generate payment slips and implement conditional statements

for worker in workers:
    name = worker['name']
    salary = worker['salary']
    gender = worker['gender']
    employee_level = ""

    try:
        if 10000 < salary < 20000:
            employee_level = "A1"
        if 7500 < salary < 30000 and gender == "Female":
            employee_level = "A5-F"

        # Payment slip (printing for the sake of example)
        print(f"Name: {name}, Salary: {salary}, Gender: {gender}, Employee Level: {employee_level}")

    except Exception as e:
        print(f"Error processing payment slip for {name}: {e}")