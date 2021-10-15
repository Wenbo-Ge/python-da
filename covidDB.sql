-- -----------------------------------------------------
-- Schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `coviddata` ;
CREATE SCHEMA IF NOT EXISTS `coviddata` DEFAULT CHARACTER SET utf8mb4 ;
USE `coviddata` ;

-- -----------------------------------------------------
-- Table `coviddata`.`covidnumber`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `coviddata`.`covidnumber` (
  `pruid` INT,
  `prname` VARCHAR(50) ,
  `prnameFR` VARCHAR(50),
  `date` DATE,
  `numconf` INT,
  `numprob` INT,
  `numdeath` INT,
  `numtotal` INT,
  `numtoday` INT,
  `ratetotal` VARCHAR(50))
ENGINE = InnoDB;

SET SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE USER IF NOT EXISTS 'cst8333'@'localhost' IDENTIFIED BY '8333';
GRANT ALL ON `coviddata`.* TO 'cst8333'@'localhost';