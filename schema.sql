CREATE TABLE IF NOT EXISTS Competencies (
competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
date_entered TEXT,
active INTEGER DEFAULT (1));

CREATE TABLE IF NOT EXISTS Users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
last_name TEXT NOT NULL,
first_name TEXT NOT NULL,
manager INTEGER DEFAULT (0),
phone TEXT,
email TEXT NOT NULL UNIQUE,
password NOT NULL,
hire_date TEXT,
date_entered TEXT,
active DEFAULT (1));

CREATE TABLE IF NOT EXISTS Assessments (
assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
competency_id INTEGER NOT NULL,
date_entered TEXT,
active INTEGER DEFAULT (1),
FOREIGN KEY (competency_id)
    REFERENCES Competencies (competency_id)
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
result_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
assessment_id INTEGER NOT NULL,
score INTEGER NOT NULL,
date_taken TEXT NOT NULL,
manager_id INTEGER,
date_entered TEXT,
active INTEGER DEFAULT (1),
FOREIGN KEY (user_id)
    REFERENCES Users (user_id),
FOREIGN KEY (assessment_id)
    REFERENCES Assessments (assessment_id),
FOREIGN KEY (manager_id)
    REFERENCES Users (user_id));