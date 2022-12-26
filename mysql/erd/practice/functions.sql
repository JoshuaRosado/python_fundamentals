-- MYSQL Functions--  

-- >>>>>Text<<<<<<<

-- CONCAT()
-- SELECT CONCAT(' Mr. ', '',first_name, ' ' ,  last_name) AS full_name FROM users;
-- CONCAT_WS() ====WHITE SPACE
-- SELECT CONCAT_WS('  ' ,  first_name ,  last_name , 'NBA') AS full_name FROM users;
-- LENGTH()
-- SELECT LENGTH(last_name) AS last_len FROM users;
-- LOWER()
-- SELECT LOWER(first_name) AS first_lowercase FROM users;

-- >>>>>Date<<<<<<<<<
-- HOUR()
-- SELECT HOUR(joined_datetime) AS date_hour FROM users;
-- DAYNAME()
-- SELECT DAYNAME(joined_datetime) AS date_hour FROM users;
-- MONTH()
-- SELECT MONTH(joined_datetime) AS date_hour FROM users;
-- NOW()
-- SELECT NOW(joined_datetime) AS date_hour FROM users;
-- DATE_FORMAT()
-- SELECT DATE_FORMAT(joined_datetime, '%W %M %e, %Y') AS date_hour FROM users;


