-- script that creates a table, second_table, in the current database and adds multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name varchar(256),
    score int
);
INSERT INTO second_table VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
