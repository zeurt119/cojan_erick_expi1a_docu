-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.41 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for cojan_erick_expi1a_docu
DROP DATABASE IF EXISTS `cojan_erick_expi1a_docu`;
CREATE DATABASE IF NOT EXISTS `cojan_erick_expi1a_docu` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cojan_erick_expi1a_docu`;

-- Dumping structure for table cojan_erick_expi1a_docu.t_personnes
DROP TABLE IF EXISTS `t_personnes`;
CREATE TABLE IF NOT EXISTS `t_personnes` (
  `ENo` int NOT NULL,
  `ENom` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `EJob` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `EChef` int DEFAULT NULL,
  `EDebut` date DEFAULT NULL,
  `Esal` double DEFAULT NULL,
  `ECom` double DEFAULT NULL,
  `DNo` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- Dumping data for table cojan_erick_expi1a_docu.t_personnes: ~15 rows (approximately)
INSERT INTO `t_personnes` (`ENo`, `ENom`, `EJob`, `EChef`, `EDebut`, `Esal`, `ECom`, `DNo`) VALUES
	(7369, 'Dupond', 'Ouvrier', 7902, '1998-02-05', 1800, NULL, 20),
	(7499, 'Jurt', 'Vendeur', 7698, '1995-03-25', 1852.2, NULL, 30),
	(7521, 'Durand', 'Vendeur', 7698, '1997-02-15', 1447.03125, 300, 30),
	(7566, 'Cartier', 'Manager', 7839, '1995-05-31', 2975, 500, 20),
	(7654, 'Martin', 'Vendeur', 7698, '1995-04-23', 1447.03125, NULL, 30),
	(7698, 'Blanc', 'Manager', 7839, '1994-05-28', 4658.5, 14000, 30),
	(7782, 'Clarion', 'Manager', 7839, '1993-06-11', 3630.000000000001, NULL, 10),
	(7788, 'Noir', 'Analyste', 7566, '1991-12-12', 6050.000000000001, NULL, 20),
	(7839, 'Stoll', 'Président', NULL, '1991-02-15', 1500, NULL, 10),
	(7844, 'Gelli', 'Vendeur', 7698, '1996-06-30', 1273.3875, NULL, 30),
	(7876, 'Volery', 'Ouvrier', 7788, '1993-09-05', 950, NULL, 20),
	(7900, 'Jan', 'Ouvrier', 7698, '1991-10-13', 3630.000000000001, 0, 30),
	(7902, 'Moulin', 'Analyste', 7566, '1992-10-11', 2450, NULL, 20),
	(7934, 'Tripet', 'Ouvrier', 7782, '1994-08-01', 1300, NULL, 10),
	(8001, 'Schmidt', 'Manager', 7566, NULL, 2500, NULL, 100);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
