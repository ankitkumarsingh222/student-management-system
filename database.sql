CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(30) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    phone VARCHAR(20),
    department VARCHAR(100),
    year INT,
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students
(roll_no, name, email, phone, department, year, address)
VALUES
('ECE001', 'Rahul Kumar', 'rahul@example.com', '9876543210', 'Electronics and Communication', 4, 'Bengaluru')
ON DUPLICATE KEY UPDATE roll_no = roll_no;
