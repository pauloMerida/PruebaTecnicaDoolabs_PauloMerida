CREATE DATABASE DOOLABS;

USE DOOLABS;

CREATE TABLE persons (
id int auto_increment PRIMARY KEY,
name VARCHAR(100) NOT NULL
);
CREATE TABLE positions (
id int auto_increment PRIMARY KEY,
name VARCHAR(50) NOT NULL,
bonus DECIMAL(10,2) NOT NULL
);
CREATE TABLE employees (
id int auto_increment PRIMARY KEY,
person_id INT UNIQUE NOT NULL,
position_id INT NOT NULL,
salary DECIMAL(10,2) NOT NULL,
hire_date DATE NOT NULL,
FOREIGN KEY (person_id) REFERENCES persons(id),
FOREIGN KEY (position_id) REFERENCES positions(id)
);


CREATE TABLE employee_supervision (
supervisor_id INT NOT NULL,
employee_id INT NOT NULL,
PRIMARY KEY (supervisor_id, employee_id),
FOREIGN KEY (supervisor_id) REFERENCES employees(id),
FOREIGN KEY (employee_id) REFERENCES employees(id)
);

INSERT INTO persons (name) VALUES
('Carlos Ramírez'),
('María Fernández'),
('Luis Gómez'),
('Ana Torres'),
('Pedro López'),
('Laura Méndez'),
('Jorge Ruiz'),
('Sofía Herrera'),
('Fernando Díaz'),
('Isabel Navarro');
INSERT INTO positions (name, bonus) VALUES
('Gerente General', 15000.00),
('Director de Finanzas', 12000.00),
('Director de Recursos Humanos', 10000.00),
('Supervisor de Ventas', 7000.00),
('Analista Financiero', 5000.00),
('Especialista en RRHH', 4000.00),
('Vendedor Senior', 3000.00),
('Vendedor Junior', 2000.00),
('Asistente Administrativo', 1000.00),
('Recepcionista', 500.00);
INSERT INTO employees (person_id, position_id, salary, hire_date)
VALUES
(1, 1, 90000.00, '2010-05-15'),
(2, 2, 75000.00, '2012-08-10'),
(3, 3, 72000.00, '2015-04-22'),
(4, 4, 60000.00, '2016-09-30'),
(5, 5, 50000.00, '2017-11-15'),
(6, 6, 45000.00, '2018-07-05'),
(7, 7, 40000.00, '2019-10-12'),
(8, 8, 35000.00, '2020-03-18'),
(9, 9, 30000.00, '2021-06-25'),
(10, 10, 28000.00, '2022-01-14');
INSERT INTO employee_supervision (supervisor_id, employee_id)
VALUES
(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (4, 8), (5, 9),
(6, 10);