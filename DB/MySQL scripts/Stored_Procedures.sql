CREATE DATABASE IF NOT EXISTS `rental_management_system`;
USE `rental_management_system`;

-- Stored Procedures
-- (1)

DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `FetchElectricityUseAmount`(IN R_name VARCHAR(50),OUT Total_amount FLOAT,OUT Number_Of_Months INT,OUT P_unit FLOAT,OUT C_unit FLOAT,OUT U_amount FLOAT)
	COMMENT 'To fetch the unpaid total electricity used amount by the rentee '
BEGIN
	DECLARE R_id INT;
	DECLARE SUM_AMOUNT FLOAT;
	
	SELECT rentee_id INTO R_id FROM `rentee_details` WHERE rentee_name = R_name;
	SELECT unsettled_amount INTO U_amount FROM electricity_payment WHERE e_id IN(SELECT E_id FROM electricity_used WHERE rentee_id = R_id) ORDER BY payment_id DESC LIMIT 1;
	SELECT COUNT(amount) INTO Number_Of_Months FROM electricity_used WHERE E_id NOT IN(SELECT e_id FROM electricity_payment) AND rentee_id=R_id;
	SELECT SUM(amount) INTO Total_amount FROM electricity_used WHERE E_id NOT IN(SELECT e_id FROM electricity_payment) AND rentee_id=R_id;
	-- SELECT U_amount;
	SELECT FLOOR(previous_unit) INTO P_unit FROM electricity_used WHERE E_id NOT IN (SELECT e_id FROM electricity_payment) AND rentee_id=R_id LIMIT 1;
	SELECT FLOOR(current_unit) INTO C_unit FROM electricity_used WHERE E_id NOT IN (SELECT e_id FROM electricity_payment) AND rentee_id=R_id ORDER BY E_id DESC LIMIT 1;
	
	SET Total_amount = Total_amount + U_amount;	
    SELECT P_unit,C_unit,Number_Of_Months,U_amount,Total_amount-U_amount,Total_amount;
END//

-- (2)
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertNewRentee`(IN R_name VARCHAR(50),IN shift_date DATE,IN ADV VARCHAR(3),IN house_number INT)
    COMMENT 'Inserting information of new rentee'
BEGIN
	INSERT INTO `rentee_details`(rentee_name,shifted_on,advance_given,house_no) VALUES(R_name,shift_date,ADV,house_number);
END//

-- (3)
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateElectricityUsed`(IN r_name VARCHAR(50),IN c_unit FLOAT,IN price_per_unit FLOAT,IN recorded_on DATE)
    COMMENT 'to update the electricity used table'
BEGIN
	DECLARE R_id INT;
    DECLARE temp_r_id INT;
    DECLARE p_unit FLOAT;
    DECLARE used_unit FLOAT;
    
    SET p_unit = NULL;
    SELECT rentee_id INTO R_id FROM `rentee_details` WHERE rentee_name=r_name;
    SELECT FLOOR(current_unit) INTO p_unit FROM `electricity_used` WHERE rentee_id=R_id ORDER BY E_id DESC LIMIT 1;
    
    IF p_unit=NULL THEN 
		SELECT rentee_id INTO temp_r_id FROM `rentee_details` WHERE house_no IN 
        (SELECT house_no FROM `rentee_details` WHERE rentee_id=R_id) ORDER BY rentee_id DESC LIMIT 1 OFFSET 1;
		SELECT FLOOR(current_unit) INTO p_unit FROM `electricity_used` WHERE rentee_id = temp_r_id ORDER BY E_id DESC LIMIT 1;
    END IF;
	
    SET c_unit = FLOOR(c_unit);
    INSERT INTO `electricity_used`(rentee_id,previous_unit,current_unit,used_unit,amount,unit_recorded_on)
    VALUES(R_id,p_unit,c_unit,(c_unit-p_unit),(c_unit-p_unit)*price_per_unit,recorded_on);
    
END//

-- (4)
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateRentalPayment`(IN R_name VARCHAR(50),IN Paid_on DATE,IN Payment_type VARCHAR(45))
    COMMENT 'For updating the rent payment'
BEGIN
	DECLARE R_id INT;
	SELECT rentee_id INTO R_id FROM `rentee_details` WHERE rentee_name=R_name;
    INSERT INTO `rental_payments`(rentee_id,paid_on,payment_type) VALUES(R_id,Paid_on,Payment_type); 
END//

-- (5)
CREATE PROCEDURE `UpdateRenteeDetails` (IN R_name VARCHAR(50),IN date_of_leave DATE)
COMMENT 'To update the rentee house leaving date in rentee_details table'
BEGIN
	UPDATE `rentee_details` SET `left_on` = date_of_leave WHERE rentee_id = FetchRenteeID(R_name);
END//

--(6)
CREATE PROCEDURE `NoOfMonthsStayed`(IN R_Name VARCHAR(50),OUT NoOfMonthsStayed INT)
    COMMENT 'Returns the Number of months rentee has stayed till date or left date'
BEGIN
	 DECLARE ShiftedOn DATE;
     DECLARE LeftOn DATE;
     DECLARE NoOfDays INT;
     DECLARE NoOfMonths FLOAT;
SELECT 
    shifted_on, left_on
INTO ShiftedOn , LeftOn FROM
    rentee_details
WHERE
    rentee_id = FetchRenteeID(R_Name);
     IF LeftOn IS NULL THEN SET LeftOn = CURDATE();
     END IF;
SELECT DATEDIFF(LeftOn, ShiftedOn) INTO NoOfDays;
	 SET NoOfMonths = ROUND(NoOfDays / 30.417,2);
	 IF NoOfMonths - FLOOR(NoOfMonths) <= 0.35 THEN 
  		SET NoOfMonthsStayed = FLOOR(NoOfMonths);
      ELSE 
 		SET NoOfMonthsStayed = CEIL(NoOfMonths);
      END IF;

SELECT NoOfMonthsStayed,NoOfDays;
END//

DELIMITER ;