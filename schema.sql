SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `rdam`;

CREATE SCHEMA IF NOT EXISTS `rdam` DEFAULT CHARACTER SET utf8;
USE `rdam`;

CREATE TABLE School (
    SchoolName VARCHAR(100) PRIMARY KEY,
    Location VARCHAR(100),
    Website VARCHAR(100),
    Dean VARCHAR(100),
    EstablishmentYear INT,
    SchoolAvgGPA DECIMAL(3,2),
    Scholarships VARCHAR(255)
);

CREATE TABLE College (
    CollegeName VARCHAR(100) PRIMARY KEY,
    Description TEXT,
    Office VARCHAR(100),
    Budget DECIMAL(12,2),
    Location VARCHAR(100),
    Dean VARCHAR(100),
    EstablishmentYear INT,
    Warden VARCHAR(100)
);

CREATE TABLE Major (
    MajorName VARCHAR(100) PRIMARY KEY,
    SchoolName VARCHAR(100),
    SchoolPackage TEXT,
    EstablishmentYear INT,
    FOREIGN KEY (SchoolName) REFERENCES School(SchoolName)
);

CREATE TABLE Professor (
    InstructorID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Gender VARCHAR(10),
    Email VARCHAR(100),
    Title VARCHAR(100),
    SchoolName VARCHAR(100),
    Office VARCHAR(100),
    TeachingAssignments TEXT,
    Publications TEXT,
    Year INT,
    Salary DECIMAL(12,2),
    EducationBackground TEXT,
    ResearchField VARCHAR(100),
    FOREIGN KEY (SchoolName) REFERENCES School(SchoolName)
);

CREATE TABLE Student (
    StudentID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Gender VARCHAR(10),
    Year INT,
    MajorName VARCHAR(100),
    GPA DECIMAL(3,2),
    SchoolName VARCHAR(100),
    CollegeName VARCHAR(100),
    TuitionFees DECIMAL(12,2),
    Scholarships VARCHAR(255),
    FinancialAids VARCHAR(255),
    HonorsRewards VARCHAR(255),
    Nation VARCHAR(50),
    PhoneNumbers VARCHAR(50),
    MailingAddress VARCHAR(255),
    EmergencyContact VARCHAR(100),
    GraduateStatus VARCHAR(50),
    FOREIGN KEY (MajorName) REFERENCES Major(MajorName),
    FOREIGN KEY (SchoolName) REFERENCES School(SchoolName),
    FOREIGN KEY (CollegeName) REFERENCES College(CollegeName)
);

CREATE TABLE PhDStudent (
    StudentID VARCHAR(20) PRIMARY KEY,
    Salary DECIMAL(12,2),
    TeachingAssistant VARCHAR(100),
    Supervisor VARCHAR(100),
    Lab VARCHAR(100),
    ResearchField VARCHAR(100),
    EducationBackground TEXT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Course (
    CourseID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Career VARCHAR(50),
    Credits INT,
    Section VARCHAR(10),
    Component VARCHAR(50),
    Schedule VARCHAR(100),
    Year INT,
    InstructorID VARCHAR(20),
    TA VARCHAR(100),
    GradeDistribution DECIMAL(3,2),
    Quota INT,
    Location VARCHAR(100),
    FOREIGN KEY (InstructorID) REFERENCES Professor(InstructorID),
    FOREIGN KEY (TA) REFERENCES PhDstudent(StudentID)
);

CREATE TABLE Enrolls (
    StudentID VARCHAR(20),
    CourseID VARCHAR(20),
    Grade DECIMAL(5,2) CHECK (Grade >= 0 AND Grade <= 100),
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

CREATE TABLE Lab (
    LabID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    InstructorID VARCHAR(20),
    StudentID VARCHAR(20),
    Funding DECIMAL(12,2),
    PhoneNumber VARCHAR(50),
    Email VARCHAR(100),
    Address VARCHAR(255),
    Fields VARCHAR(255),
    Subject VARCHAR(100),
    FOREIGN KEY (InstructorID) REFERENCES Professor(InstructorID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Supervises (
    InstructorID VARCHAR(20),
    LabID VARCHAR(20),
    PRIMARY KEY (InstructorID, LabID),
    FOREIGN KEY (InstructorID) REFERENCES Professor(InstructorID),
    FOREIGN KEY (LabID) REFERENCES Lab(LabID)
);

CREATE TABLE ClubActivity (
    StudentID VARCHAR(20),
    ClubName VARCHAR(100),
    PRIMARY KEY (StudentID, ClubName),
    FOREIGN KEY (StudentID) REFERENCES PhDStudent(StudentID)
);

CREATE TABLE CollegeTutor (
    StudentID VARCHAR(20) PRIMARY KEY,
    CollegeFlatFloor VARCHAR(100),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE CollegeTutoring (
    StudentID VARCHAR(20),
    CollegeName VARCHAR(100),
    PRIMARY KEY (StudentID, CollegeName),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CollegeName) REFERENCES College(CollegeName)
);

CREATE TABLE Club (
    ClubID VARCHAR(20) PRIMARY KEY,
    ClubName VARCHAR(100),
    President VARCHAR(100),
    ClubMembers TEXT,
    Budget DECIMAL(12,2)
);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;