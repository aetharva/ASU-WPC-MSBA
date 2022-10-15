-- continue on basic data retrieval

-- use company

select lname, gender from employee;

SELECT lname, IF(gender = "M", "Male", "Female") as gender
FROM employee;

SELECT lname, salary,
	CASE
		WHEN salary >= 1000000 THEN "seven figure"
        WHEN salary >= 100000 THEN "six figure"
        ELSE "five figure"
	END AS salary_range
	FROM employee;
    
SELECT lname, fname
	FROM employee
    WHERE salary >= 100000

-- SELECT lname, fname
	-- FROM employee
    -- WHERE salary >= 100000 AND salary <1000000;
    
    
-- SELECT lname, fname
	-- FROM employee
    -- WHERE salary BETWEEN 100000 AND 999999;
    

SELECT * FROM employee WHERE FName LIKE "G%";