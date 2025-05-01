import mysql.connector
from datetime import datetime
import time

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="passrod",
    database="database_name"
)

mycursor = db.cursor()

# ========================================================================
# ========================================================================

# === Create tables and add basic values ===

def create_databases():
    mycursor.execute("""
            CREATE TABLE Hospital (
                Hospital_Id INT PRIMARY KEY AUTO_INCREMENT,
                Hospital_Name VARCHAR(100) NOT NULL,
                Bed_Count SMALLINT UNSIGNED
                )
    """)

    mycursor.execute("""
            CREATE TABLE Doctor (
                Doctor_Id INT PRIMARY KEY AUTO_INCREMENT,
                Doctor_Name VARCHAR(50),
                Hospital_Id SMALLINT NOT NULL,
                Joining_At DATE NOT NULL,
                Speciality VARCHAR(50),
                Salary INT NOT NULL,
                Experience INT NULL
                )
    """)

    db.commit()


def insert_values():

    mycursor.execute("INSERT INTO Hospital (Hospital_Name, Bed_Count) VALUES (%s, %s)", ('Mayo Clinic', 200))
    mycursor.execute("INSERT INTO Hospital (Hospital_Name, Bed_Count) VALUES (%s, %s)", ('Cleveland Clinic', 400))
    mycursor.execute("INSERT INTO Hospital (Hospital_Name, Bed_Count) VALUES (%s, %s)", ('Johns Hopkins', 1000))
    mycursor.execute("INSERT INTO Hospital (Hospital_Name, Bed_Count) VALUES (%s, %s)", ('UCLA Medical Center', 1500))

    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('David', '1', '2005-2-10', 'Pediatric', '40000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('Michael', '1', '2018-07-23', 'Oncologist', '20000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('Susan', '2', '2016-05-19', 'Garnacologist', '25000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('Robert', '2', '2017-12-28', 'Pediatric ', '28000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('Linda', '3', '2004-06-04', 'Garnacologist', '42000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('William', '3', '2012-09-11', 'Dermatologist', '30000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('Richard', '4', '2014-08-21', 'Garnacologist', '32000', None))
    mycursor.execute("INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_At, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s)", ('Karen', '4', '2011-10-17', 'Radiologist', '30000', None))

    db.commit()

# ========================================================================
# ========================================================================

# === Question 2 ===
# Fetch Hospital and Doctor Information using hospital Id and doctor Id:

def get_hospital_details(hospital_id):
    mycursor.execute("SELECT * FROM Hospital WHERE Hospital_Id = %s", (hospital_id,))
    hospital = mycursor.fetchall()[0]
    print("\nPrinting Hospital record\n"
          f"Hospital Id: {hospital[0]}\n"
          f"Hospital Name: {hospital[1]}\n"
          f"Bed Count: {hospital[2]}")

def get_doctor_details(doctor_id):
    mycursor.execute("SELECT * FROM Doctor WHERE Doctor_Id = %s", (doctor_id,))
    doctor = mycursor.fetchall()[0]
    print("\nPrinting Doctor record\n"
          f"Doctor Id: {doctor[0]}\n"
          f"Doctor Name: {doctor[1]}\n"
          f"Hospital Id: {doctor[2]}\n"
          f"Joining Date: {doctor[3]}\n"
          f"Specialty: {doctor[4]}\n"
          f"Salary: {doctor[5]}\n"
          f"Experience: {doctor[6]}")


# print("Question 2: Read given hospital and doctor details")
#get_hospital_details(3)
#get_doctor_details(105)

# ========================================================================
# ========================================================================

# === Question 3 ===
# Get the list Of doctors as per the given specialty and salary:

def get_specialist_doctors_list(speciality, salary):
    mycursor.execute("SELECT * FROM  Doctor WHERE Speciality = %s AND Salary > %s", (speciality, salary))
    doctors = mycursor.fetchall()
    for doctor in doctors:
        get_doctor_details(doctor[0])

# print("\nPrinting doctors whose specialty is Garnacologist and salary greater than 30000")
#get_specialist_doctors_list("Garnacologist", 30000)


# ========================================================================
# ========================================================================

# === Question 4 ===
# Get a list of doctors from a given hospital:

def get_doctors(hospital_id):
    mycursor.execute("SELECT * FROM Doctor WHERE Hospital_Id = %s", (hospital_id,))
    hospitals = mycursor.fetchall()
    for hospital in hospitals:
        get_hospital_details(hospital[2])

# get_doctors(2)

# ========================================================================
# ========================================================================

# === Question 5 ===
# Update doctor experience in years:

def update_doctor_experience(doctor_id):
    mycursor.execute("SELECT * FROM Doctor WHERE Doctor_Id = %s", (doctor_id,))
    doctor = mycursor.fetchall()

    doctor_joining_year = doctor[0][3].year
    current_year = datetime.today().year
    experience = current_year - doctor_joining_year

    mycursor.execute("UPDATE Doctor SET Experience = %s WHERE Doctor_Id = %s", (experience, doctor_id))
    get_doctor_details(doctor_id)


# update_doctor_experience(101)
