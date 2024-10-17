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
        LEFT JOIN `rental_management_system`.`electricity_payment` `t2` ON ((`t1`.`E_id` = `t2`.`e_id`)))