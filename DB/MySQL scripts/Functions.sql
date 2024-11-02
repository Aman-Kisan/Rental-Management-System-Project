CREATE DATABASE IF NOT EXISTS `rental_management_system`;
USE `rental_management_system`;

-- Functions
-- (1)

DELIMITER // 
DROP FUNCTION IF EXISTS `ElectricityUsedAmount`//
CREATE FUNCTION `ElectricityUsedAmount`(amount FLOAT,r_id INT,e_id INT) RETURNS float
    COMMENT 'returns the actual amount for electricity by setteling the unsettled amount'
BEGIN
	DECLARE used_amount FLOAT;
    DECLARE U_amount FLOAT;
    SET U_amount = (SELECT unsettled_amount FROM `electricity_used` t1 LEFT JOIN `electricity_payment`
    t2 ON t1.E_id=t2.e_id WHERE rentee_id=r_id AND t1.E_id < e_id ORDER BY t1.E_id DESC LIMIT 1);
    IF U_amount IS NULL THEN
		SET U_amount = 0;
	END IF;
    SET used_amount = amount + U_amount;
    RETURN (used_amount);
END//

-- (2) 
DROP FUNCTION IF EXISTS `ElectricityUsageStatus`//
CREATE FUNCTION `ElectricityUsageStatus`(used_unit FLOAT) RETURNS varchar(6)
    DETERMINISTIC
    COMMENT 'Returns LOW , MEDIUM , HIGH according to units used'
BEGIN
	DECLARE usage_status VARCHAR(6);
    
    IF used_unit <=250 THEN 
		SET usage_status = 'LOW';
	ELSEIF (250 < used_unit AND used_unit<=500) THEN
		SET usage_status = 'MEDIUM';
	ELSEIF 500 < used_unit THEN
			SET usage_status = 'HIGH';
	END IF;
    
    -- return the usage_status
RETURN(usage_status);
END//


--(3)
DROP IF EXISTS `FetchRenteeID`//
CREATE FUNCTION `FetchRenteeID`(R_name VARCHAR(50)) RETURNS int
    DETERMINISTIC
    COMMENT 'returns the rentee_id for the given rentee_name'
BEGIN
		RETURN(SELECT rentee_id FROM `rentee_details` WHERE rentee_name=R_name);
END//

DELIMITER ;