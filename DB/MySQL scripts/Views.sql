CREATE DATABASE IF NOT EXISTS `rental_management_system`;
USE `rental_management_system`;

-- Views

-- (1)

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `rental_management_system`.`electricity_uses_and_payments` AS
    SELECT 
        `t1`.`E_id` AS `E_id`,
        `t1`.`rentee_id` AS `rentee_id`,
        `t1`.`used_unit` AS `used_unit`,
        `t1`.`amount` AS `instant_amount`,
        `t1`.`unit_recorded_on` AS `unit_recorded_on`,
        `t2`.`unsettled_amount` AS `unsettled_amount`,
        ELECTRICITYUSEDAMOUNT(`t1`.`amount`,
                `t1`.`rentee_id`,
                `t1`.`E_id`) AS `genuine_amount`,
        `t2`.`paid_amount` AS `paid_amount`,
        `t2`.`paid_on` AS `paid_on`
    FROM
        (`rental_management_system`.`electricity_used` `t1`
        LEFT JOIN `rental_management_system`.`electricity_payment` `t2` ON ((`t1`.`E_id` = `t2`.`e_id`)));

-- (2)

CREATE VIEW `rental_management_system`.`house_not_on_rent_status` AS
    SELECT 
        r1.house_no,
        r1.rentee_id as r1_rentee_id,
        r1.rentee_name as r1_rentee_name,
        r1.left_on,
        r2.rentee_id as r2_rentee_id,
        r2.rentee_name as r2_rentee_name,
        r2.shifted_on,
        datediff(r2.shifted_on,r1.left_on) as `Not On Rent For(in days)`
    FROM rentee_details r1 JOIN rentee_details r2 ON r1.house_no = r2.house_no 
    WHERE r1.rentee_id < r2.rentee_id ORDER BY r1.rentee_id;
