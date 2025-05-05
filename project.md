# CSC 3170 Group Project

# CSC 3170 Group

# April 2025

# 1 Introduction

# 1.1 company

Chinese University of Shenzhen, Hong Kong

# 1.1.1 requirement

human resource management

# 1.1.2 entities, attributes, and relationships

# Entity

1. School
- Name
- Location
- Website
- Dean
- Establishment Year
- School average GPA
- Scholarships
2. Student
- StudentID
- Name
- E-mail
- Gender
- Year
- Major
- GPA
---
# School

# College

# Tuition fees

# Scholarships

# Financial Aids

# Honors and Rewards

# Nation

# Phone Numbers

# Mailing Address

# Emergency Contact

# Graduate Status

# Professor

# InstructorID

# Name

# Gender

# E-mail

# Title

# School

# Office

# Teaching Assignments

# Publications

# Year

# Salary

# Education Background

# Research Field

# Ph.D Student

# StudentID

# Salary

# Teaching Assistant

# Supervisor

# Lab

# Research Field

# Education Background

# Course
---
# 6. Major

- (a) Name
- (b) School
- (c) School Package
- (d) Establishment Year

# 7. Lab

- (a) LabID
- (b) Instructor
- (c) Student
- (d) Funding
- (e) Phone Number
- (f) E-mail
- (g) Address
- (h) Fields
- (i) Subject

# 8. College

- (a) Name
- (b) College descriptions
- (c) Office
- (d) Budget
- (e) Location
---
# Entities and Their Attributes

|Entity|Attributes|
|---|---|
|School|Name, Location, Website, Dean, Establishment Year, School average GPA, Scholarships|
|Student|StudentID, Name, E-mail, Gender, Year, Major, GPA, School, College, Tuition fees, Scholarships, Financial Aids, Honors and Rewards, Nation, Phone Numbers, Mailing Address, Emergency Contact, Graduate Status|
|Professor|InstructorID, Name, Gender, E-mail, Title, School, Office, Teaching Assignments, Publications, Year, Salary, Education Background, Research Field|
|Ph.D Student|StudentID, Salary, Teaching Assistant, Supervisor, Lab, Research Field, Education Background|
|Course|CourseID, Course Name, Career, Credits, Section, Component, Schedule (course timing), Year, Instructor, TA, Grade distribution, Quota, Location|
|Major|Name, School, School Package, Establishment Year|
|Lab|LabID, Instructor, Student, Funding, Phone Number, E-mail, Address, Fields, Subject|
|College|Name, College descriptions, Office, Budget, Location, Dean, Establishment Year, Warden|
|College Tutor|StudentID, College+flat+floor (shaw C7)|
|Club/Activity|ClubID, Club Name, President, Club members, Budget|

Table 1: Entities and Their Attributes
---
# 1.2 Relevant Entities

# 1.2.1 Relationships

- School-Has-Major (1:N)
- Student-Enrolls-Course (M:N)
- Professor-Teaches-Course (1:N)
- Lab-SupervisedBy-Professor (1:N)

# 1.2.2 Constrains

- Grade ∈ [0, 100]
- Student.Major references Major.Name
- Ph.D Student IS A Student

# 1.3 E-R Diagram

| | | | |College| | |
|---|---|---|---|---|---|---|
| | |Name| | | | |
| |Major|Has|School|School|Professor|InstructorID|
| | | |Dean|Teaches| |Supervises|
|StudentID|Student|Enrolls|Course| |Lab| |
| | |Constraints:| | | | |
| | |- Grade ∈ [0, 100]| | | | |
|- Student.Major references Major.Name| | | | | | |
| | |- Ph.D Student IS A Student| | | | |
| |Ph.D Student| | | | |Club/Activity|

# 1.4 Relational Schemas

# 1.4.1 1. Professor

|InstructorID|(Primary Key)|
|---|---|
|Name|(Non-key attribute)|
|SchoolName|(Foreign Key to School.Name)|

---
# 1.4.2 2. Major

|Name|(Primary Key)|
|---|---|
|SchoolName|(Foreign Key to School.Name)|

# 1.4.3 3. Course

|CourseID|(Primary Key)|
|---|---|
|Name|(Non-key attribute)|
|InstructorID|(Foreign Key to Instructor.ID)|
|TA|(Foreign Key to PhDStudent.ID)|

# 1.4.4 4. Student

|StudentID|(Primary Key)|
|---|---|
|MajorName|(Foreign Key to Major.Name)|
|SchoolName|(Foreign Key to School.Name)|
|CollegeName|(Foreign Key to College.Name)|

# 1.4.5 5. Enrolls (Student-Course Relationship)

|StudentID|(Foreign Key to Student.StudentID)|
|---|---|
|CourseID|(Foreign Key to Course.CourseID)|
|Composite Primary Key:|(StudentID, CourseID)|
|Grade|Check: 0 ≤ Grade ≤ 100|

# 1.4.6 6. Lab

|LabID|(Primary Key)|
|---|---|
|Name|(Non-key attribute)|
|InstructorID|(Foreign Key to Professor.InstructorID)|
|StudentID|(Foreign Key to Student.StudentID)|

# 1.4.7 7. Supervises (Professor-Lab Relationship)

|InstructorID|(Foreign Key to Professor.InstructorID)|
|---|---|
|LabID|(Foreign Key to Lab.LabID)|
|Composite Primary Key:|(InstructorID, LabID)|

# 1.4.8 8. PhDStudent (ISA Student)

StudentID
(Primary Key, Foreign Key to Student.StudentID)

# 1.4.9 9. ClubActivity (Multivalued Attribute for Student)

|StudentID|(Foreign Key to PhDStudent.StudentID)|
|---|---|
|ClubName|(Multivalued attribute component)|
|Composite Primary Key:|(StudentID, ClubName)|

---
# 1.4.10 College

CollegeName
(Primary Key)

# 1.4.11 College Tutor

|StudentID|(Primary Key, Foreign Key to Student.StudentID)|
|---|---|
|College+flat+floor|(Multivalued attribute component)|

# 1.4.12 College Tutoring (College-College Tutor Relationship)

|StudentID|(Primary Key, Foreign Key to Student.StudentID)|
|---|---|
|CollegeName|(Primary Key, Foreign Key to College.Name)|

# 1.4.13 Justification for Normalization

- Primary Keys: All tables define a primary key (PK), ensuring entity integrity.
- Foreign Keys: Relationships are enforced through foreign keys (FK).
- Functional Dependencies:
- All non-key attributes fully depend on the primary key.
- No transitive dependencies exist between non-key attributes.
- Multivalued Dependencies:
- The table ClubActivity resolves the multivalued attribute "Club/Activity" for PhDStudent.
- BCNF Compliance: Each determinant is a candidate key.
- Constraints:
- Enrolls.Grade includes a domain constraint (0 ≤ Grade ≤ 100).
- The ISA hierarchy (PhDStudent inherits StudentID via FK) is preserved.
---
# Customers

|PK|customer id|int NOT NULL|
|---|---|---|
| |customer name|char(50) NOT NULL|

# Orders

|1:N|PK|order id|int NOT NULL|
|---|---|---|---|
|customer id|FK1|customer id|int NOT NULL|
| |order date|date NOT NULL| |

# 1.5 sample SQL used for practical daily operations and activities

# enrollment of new students:

INSERT INTO Student (StudentID, Name, E-mail, Gender, Year, Major, GPA, School, College, Tuition fees, Scholarships, Financial Aids, Honors and Rewards, Nation, Phone Numbers, Mailing Address, Emergency Contact, Graduate Status)
VALUES
(125090021, 'Zengz', '125090021@link.cuhk.edu.cn', 'Female', 2025, 'None', 'SME', 'Ling', 125000, 0, 10000, 'None', 'China', '13308254153', 'Shenzhen', '110', 'Undergraduate'),
(125090024, 'Cengz', '125090024@link.cuhk.edu.cn', 'Male', 2025, 'None', 'SSE', 'Muse', 115000, 0, 115000, 'None', 'India', '13303424153', 'New Delhi', '120', 'Graduate');
---
# Enrollment of New Students

|Student ID|Name|Email|Gender|Graduation Year|Major|School|Scholarship|Salary|Phone|Location|Office|Education Level|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|125090823|Shir|125090823@link.cuhk.edu.cn|Female|2025|None|SDS|Diligentia|150000|13535348162|Shanghai|110|UnderGraduate|
|125090833|Zhengkr|125090833@link.cuhk.edu.cn|Female|2025|None|SSE|Ling|95000|13395283945|New York|911|Graduate|
|125090336|Leo|125090336@link.cuhk.edu.cn|Male|2025|None|SDS|Diligentia|95000|13345254153|Shenzhen|110|Phd|

# Enrollment of New Professor

|Instructor ID|Name|Gender|Email|Title|School|Office|Teaching Assignments|Publications|Year|Salary|Education Background|Research Field|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|012533|Liu Jianing|Male|Liujianing001@link.cuhk.edu.cn|Associate Professor|SDS|TA101|None|None|2025|1000000|CUHK - CUHK - CUHK|Computer Science|

# Choose a Major in Year Two

UPDATE Student SET major = 'Data Science and Big Data Technology' WHERE student_id IN (125090336, 125090833, 125090823);

# Update Course Grade Distribution

UPDATE Course SET Grade distribution = 0.4 WHERE CourseID = MAT1001, AND enrollment_year = 202501;

# Enrollment of New Courses

|Course ID|Course Name|Career|Credits|Section|Component|Schedule|Year|Instructor|TA|Grade Distribution|Quota|Location|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|MAT1001|Calculas|Undergraduate|3|L01|Lecture|2025|Liu Jianing|Ceng Ziyu|202501|None|100|TA101|
|CSC1001|Python|Undergraduate|3|L01|Lecture|2025|Zeng Zuo|Wan Yi|202501|None|120|TB310|
|ECO3121|Econometrics|Graduate|3|L03|Lecture|2025|Zheng Kuoru|Ru Kezheng|202502|None|200|TC110|
|MAT5012|Calculas|Phd|3|L02|Tutorial|2025|Liu Jianing|Qu Toushi|202501|None|20|TA120|

# Update Student Average GPA

UPDATE Students SET grade = CASE WHEN student_id = 125090024 THEN 3.65 WHEN student_id = 125090336 THEN 3.80 WHEN student_id = 125090021 THEN 3.20 ELSE grade END;
---
# SQL Queries

# 1. Queries

# 1.1 Query the SDS student who admitted in 2023:

SELECT  COUNT (*)  AS     student_count
FROM  Student
WHERE  enrollment_year    = 2023
AND  School    = ’ SDS ’;

# 1.2 Query the student number in Ling college:

SELECT  COUNT (*)  AS     student_count
FROM  Student
WHERE  College  =  ’ Ling ’;

# 1.3 Query the ratio of male and female students in SDS:

SELECT
SUM ( CASE WHEN  gender  =    ’ Female ’   THEN  1  ELSE  0 END ) AS female_count ,
SUM ( CASE WHEN  gender  =    ’ Male ’  THEN 1   ELSE  0  END ) AS male_count ,
COUNT (*)  AS  total ,
ROUND (
SUM ( CASE  WHEN gender    = ’ Female ’ THEN   1.0    ELSE  0 END )  /
NULLIF ( SUM ( CASE  WHEN  gender    =  ’ Male ’ THEN  1.0  ELSE  0  END ) ,  0) ,
2
)  AS female_to_male_ratio
FROM  Student
WHERE  School    = ’ SDS ’;

# 1.4 Sample SQL of an analytic or data mining nature

# 1.4.1 Find one student(125090021)’s GPA ranking in his/her Major

SELECT  COUNT (*)    +  1  AS rank
FROM  Student
WHERE  Major  = ( SELECT    Major    FROM Student     WHERE StudentID =       ’ 125090021 ’)
AND  GPA >  ( SELECT    GPA FROM   Student   WHERE   StudentID     = ’ 125090021 ’)

# 1.4.2 Query the average GPA of undergraduate students whose Mailing Address is Shenzhen

SELECT  AVG ( GPA )
FROM  Student
WHERE  [ Mailing Address ]    LIKE    ’% Shenzhen % ’
AND  [ Graduate    Status ] =     ’ Undergraduate ’

# 1.4.3 Analysis for trend of average GPA for student enrolled in different year

SELECT
Year ,
AVG ( GPA ) AS Avg_GPA
FROM
Student
GROUP  BY
---
# Yearly trend of professors being hired

SELECT
Year AS employed_year,
COUNT(*) AS new_professors
FROM professors
GROUP BY Year
ORDER BY Year;

# Trends on the number of newly opened courses each year

SELECT [Year], COUNT([CourseID]) AS NewCourseCount
FROM Course
GROUP BY [Year]
ORDER BY [Year];

# Calculate the support score as a proportion of all students in School SDS, who entered the university within the last 3 years, are from Shenzhen, and have a GPA ≥ 3.7

SELECT
COUNT(*) * 1.0 /
(SELECT COUNT(*) FROM Student WHERE School = 'SDS' AND Year >= strftime('%Y', 'now') - 3) AS SupportScore
FROM Student
WHERE School = 'SDS'
AND [Mailing Address] LIKE '%Shenzhen%'
AND GPA >= 3.7
AND Year >= strftime('%Y', 'now') - 3;

# 2 LLM-Enhanced Database Query Generation and Optimization

This section describes our approach to enhancing database query functionality by leveraging a Large Language Model (LLM). The goal is to allow users to input natural language queries that the system then translates into optimized SQL commands and provides query improvement suggestions.

# 2.1 Natural Language to SQL Query Conversion

To lower the barrier for users and simplify complex query construction, we incorporate a module that converts natural language descriptions into SQL queries. The main features include:

- User Input: Users can describe their data retrieval needs in everyday language (e.g., “List all students with a GPA higher than 3.0 enrolled in the Computer Science course”).
- LLM Processing: The system leverages an LLM (e.g., via an API from OpenAI or a fine-tuned local model) to translate the natural language description into a corresponding SQL query.
---
# 2.2 Automatic Optimization and Query Refinement

In addition to generating SQL queries, our module also provides optimization recommendations to improve performance. This includes:

- Indexing Suggestions: Based on the SQL query and the database schema, the system automatically suggests which columns should be indexed or hashed to enhance query speed.
- Query Rewriting: The LLM analyzes existing SQL queries for potential performance pitfalls (such as unnecessary Cartesian products or inefficient joins) and suggests rewritten, optimized versions.
- Risk Detection: The module identifies common issues like overly complex nested queries and provides actionable recommendations for simplification.

# 2.3 Implementation and Demonstration

For practical demonstration and evaluation, the following steps are performed:

1. Interface Demo: Develop a simple interactive front-end where a user inputs a natural language query, and the system displays both the generated SQL query and the resulting dataset.
2. Optimization Comparison: Present a case study showing a sample SQL query before and after LLM-based optimization, together with performance metrics such as execution time and resource utilization.
3. Documentation: Provide a detailed description of the LLM integration process, including prompt design, example collection, and testing methodologies, illustrating the benefits of the approach.

Integrating LLM capabilities not only modernizes our system but also significantly reduces the complexity for end-users, making our database interface more intuitive and robust. This module is a key innovation in our project, addressing both usability and performance optimization, which aligns with our project’s overall goal of delivering a state-of-the-art database solution.