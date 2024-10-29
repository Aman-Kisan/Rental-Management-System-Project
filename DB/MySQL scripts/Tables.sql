CREATE DATABASE IF NOT EXISTS `rental_management_system`;
USE `rental_management_system`;

-- Tables
-- (1)
CREATE TABLE IF NOT EXISTS `electric_slab_price` (
  `slab_length` INT NOT NULL,
  `amount` FLOAT NOT NULL COMMENT 'Stores the price per unit of slab corresponding to it.');

-- (2) 
CREATE TABLE IF NOT EXISTS `rentee_details` (
  `rentee_id` INT NOT NULL AUTO_INCREMENT,
  `rentee_name` VARCHAR(50) NULL,
  `house_no` INT NOT NULL,
  `shifted_on` DATE NULL,
  `left_on` DATE NULL,
  `advance_given` VARCHAR(3) NULL,
  `rent_amount` FLOAT NULL DEFAULT 6000,
  PRIMARY KEY (`rentee_id`));

-- (3)
CREATE TABLE IF NOT EXISTS `rental_payments` (
  `payment_id` INT(2) NOT NULL AUTO_INCREMENT,
  `rentee_id` INT NOT NULL,
  `paid_on` DATE NOT NULL,
  `payment_type` VARCHAR(45) NULL DEFAULT 'Monthly Payment',
  PRIMARY KEY (`payment_id`),
  INDEX `rental_payment_rentee_id_idx` (`rentee_id` ASC) VISIBLE,
  CONSTRAINT `rentee_details.rentee_id to rental_payment_rentee_id`
    FOREIGN KEY (`rentee_id`)
    REFERENCES `rentee_details` (`rentee_id`)
ON DELETE CASCADE ON UPDATE RESTRICT);

-- (4)
CREATE TABLE IF NOT EXISTS `electricity_used` (
  `E_id` INT NOT NULL AUTO_INCREMENT,
  `rentee_id` INT NOT NULL,
  `previous_unit` FLOAT NOT NULL COMMENT 'Stores the last unit recorded.',
  `current_unit` FLOAT NOT NULL COMMENT 'Stores the current unit recorded',
  `used_unit` FLOAT NOT NULL COMMENT 'It stores the unit used for the month, which is produced by the difference between \'previous_unit\' and \'current_unit\'.',
  `amount` FLOAT NOT NULL,
  `paid_amount` FLOAT NOT NULL COMMENT 'Amount paid or given by the rentee',
  `unit_recorded_on` DATE NOT NULL COMMENT 'Amount to be returned to the rentee, which is produced by the difference between the \'amount\' and \'paid_amount\'',
  PRIMARY KEY (`E_id`),
  INDEX `rentees_detail.rentee_id to electricity_use_payment.rentee__idx` (`rentee_id` ASC) VISIBLE,
  CONSTRAINT `rentee_details.rentee_id to electricity_used.rentee_id`
    FOREIGN KEY (`rentee_id`)
    REFERENCES `rentee_details` (`rentee_id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT);

-- (5)
CREATE TABLE IF NOT EXISTS `electricity_payment` (
  `payment_id` INT NOT NULL AUTO_INCREMENT,
  `e_id` INT NOT NULL,
  `paid_amount` FLOAT NOT NULL,
  `paid_on` DATE NOT NULL,
  `unsettled_amount` FLOAT NOT NULL,
  PRIMARY KEY (`payment_id`),
  INDEX `electricity_used.E_id to electricity_payment.e_id_idx` (`e_id` ASC) VISIBLE,
  CONSTRAINT `electricity_used.E_id to electricity_payment.e_id`
    FOREIGN KEY (`e_id`)
    REFERENCES `electricity_used` (`E_id`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT);
