import random
from faker import Faker

fake = Faker()

def random_gpa():
    return round(random.uniform(2.0, 4.0), 2)

def random_budget():
    return round(random.uniform(5_000_000, 10_000_000), 2)

def random_salary():
    return round(random.uniform(50_000, 150_000), 2)

def random_year(start=1950, end=2022):
    return random.randint(start, end)

def scholarships():
    return 'General, Merit, Need-Based'

def random_phone():
    return fake.phone_number()

def random_email():
    return fake.email()

def random_location():
    return "Shenzhen"

# Open a single file for writing all the INSERT statements
with open("insert_statements.sql", "w") as f:
    
    # Professors
    professors = []
    for i in range(200):
        stmt = f"""INSERT INTO Professor (InstructorID, Name, Gender, Email, Title, SchoolName, Office, TeachingAssignments, Publications, Year, Salary, EducationBackground, ResearchField)
VALUES ('P{i}', '{fake.name()}', '{random.choice(["Male", "Female"])}', '{random_email()}', '{fake.job()}', 'School_{random.randint(0, 9)}', '{fake.street_address()}', '{fake.sentence()}', '{fake.text(50)}', {random_year()}, {random_salary()}, '{fake.text(50)}', '{fake.word()}');"""
        professors.append(stmt)
    f.write("\n".join(professors) + "\n")

    # Students
    students = []
    for i in range(10000):
        stmt = f"""INSERT INTO Student (StudentID, Name, Email, Gender, Year, MajorName, GPA, SchoolName, CollegeName, TuitionFees, Scholarships, FinancialAids, HonorsRewards, Nation, PhoneNumbers, MailingAddress, EmergencyContact, GraduateStatus)
VALUES ('S{i}', '{fake.name()}', '{random_email()}', '{random.choice(["Male", "Female"])}', {random.randint(1, 5)}, 'Major_{random.randint(0, 29)}', {random_gpa()}, 'School_{random.randint(0, 9)}', 'College_{random.randint(0, 9)}', {round(random.uniform(5000, 50000), 2)}, '{scholarships()}', 'None', 'None', 'China', '{random_phone()}', '{fake.address()}', '{fake.name()}', 'Undergraduate');"""
        students.append(stmt)
    f.write("\n".join(students) + "\n")

    # PhD Students
    phd_students = []
    for i in range(1000):
        stmt = f"""INSERT INTO PhDStudent (StudentID, Salary, TeachingAssistant, Supervisor, Lab, ResearchField, EducationBackground)
VALUES ('S{i}', {random_salary()}, '{fake.name()}', '{fake.name()}', 'Lab_{random.randint(0, 9)}', '{fake.word()}', '{fake.text(50)}');"""
        phd_students.append(stmt)
    f.write("\n".join(phd_students) + "\n")

    # Courses
    courses = []
    for i in range(500):
        stmt = f"""INSERT INTO Course (CourseID, Name, Career, Credits, Section, Component, Schedule, Year, InstructorID, TA, GradeDistribution, Quota, Location)
VALUES ('C{i}', '{fake.word()}', '{random.choice(["Undergraduate", "Graduate"])}', {random.randint(3, 5)}, 'Section_{random.randint(1, 10)}', '{fake.word()}', '{fake.text(30)}', {random_year()}, 'P{random.randint(0, 19)}', 'S{random.randint(0, 9)}', {round(random.uniform(60, 100), 2)}, {random.randint(30, 100)}, '{random_location()}');"""
        courses.append(stmt)
    f.write("\n".join(courses) + "\n")

    # Enrolls
    enrolls = []
    for i in range(50000):
        stmt = f"""INSERT INTO Enrolls (StudentID, CourseID, Grade)
VALUES ('S{random.randint(0, 49)}', 'C{random.randint(0, 19)}', {round(random.uniform(0, 100), 2)});"""
        enrolls.append(stmt)
    f.write("\n".join(enrolls) + "\n")

    # Labs
    labs = []
    for i in range(35):
        stmt = f"""INSERT INTO Lab (LabID, Name, InstructorID, StudentID, Funding, PhoneNumber, Email, Address, Fields, Subject)
VALUES ('L{i}', '{fake.word()}', 'P{random.randint(0, 19)}', 'S{random.randint(0, 49)}', {random_budget()}, '{random_phone()}', '{random_email()}', '{fake.address()}', '{fake.text(50)}', '{fake.word()}');"""
        labs.append(stmt)
    f.write("\n".join(labs) + "\n")

    # Supervises
    supervises = []
    for i in range(2000):
        stmt = f"""INSERT INTO Supervises (InstructorID, LabID)
VALUES ('P{random.randint(0, 19)}', 'L{i}');"""
        supervises.append(stmt)
    f.write("\n".join(supervises) + "\n")

    # Club Activity
    club_activities = []
    for i in range(20):
        stmt = f"""INSERT INTO ClubActivity (StudentID, ClubName)
VALUES ('S{random.randint(0, 49)}', 'Club_{random.randint(0, 9)}');"""
        club_activities.append(stmt)
    f.write("\n".join(club_activities) + "\n")

    # College Tutor
    college_tutors = []
    for i in range(100):
        stmt = f"""INSERT INTO CollegeTutor (StudentID, CollegeFlatFloor)
VALUES ('S{random.randint(0, 49)}', '{fake.word()}');"""
        college_tutors.append(stmt)
    f.write("\n".join(college_tutors) + "\n")

    # College Tutoring
    college_tutoring = []
    for i in range(1000):
        stmt = f"""INSERT INTO CollegeTutoring (StudentID, CollegeName)
VALUES ('S{random.randint(0, 49)}', 'College_{random.randint(0, 9)}');"""
        college_tutoring.append(stmt)
    f.write("\n".join(college_tutoring) + "\n")

    # Clubs
    clubs = []
    for i in range(50):
        stmt = f"""INSERT INTO Club (ClubID, ClubName, President, ClubMembers, Budget)
VALUES ('C{i}', 'Club_{i}', '{fake.name()}', '{fake.name()},{fake.name()}', {random_budget()});"""
        clubs.append(stmt)
    f.write("\n".join(clubs) + "\n")

print("SQL insert statements for all entities have been saved into 'insert_statements.sql'.")
