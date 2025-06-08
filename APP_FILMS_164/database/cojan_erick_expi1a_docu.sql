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

-- Dumping structure for table cojan_erick_expi1a_docu.t_client
DROP TABLE IF EXISTS `t_client`;
CREATE TABLE IF NOT EXISTS `t_client` (
  `id_client` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) DEFAULT NULL,
  `entreprise` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table cojan_erick_expi1a_docu.t_client: ~10 rows (approximately)
INSERT INTO `t_client` (`id_client`, `nom`, `prenom`, `entreprise`, `email`, `telephone`) VALUES
	(1, 'Dupont', 'Pierre', 'Dupont SARL', 'pierre.dupont@example.com', '0791234567'),
	(2, 'Durand', 'Marie', 'Durand & Fils', 'marie.durand@example.com', '0789876543'),
	(3, 'Morel', 'Antoine', 'AM Informatique', 'antoine.morel@example.com', '0773334455'),
	(4, 'Giraud', 'Lucie', 'Transport Giraud', 'lucie.giraud@example.com', '0761122334'),
	(5, 'Lemoine', 'Pauline', 'PL Conseil', 'pauline.lemoine@example.com', '0759988776'),
	(6, 'Fernandez', 'Carlos', 'Carlos Dépannage', 'carlos.fernandez@example.com', '0745566778'),
	(7, 'Nguyen', 'Thierry', 'Thierry Énergies', 'thierry.nguyen@example.com', '0793344556'),
	(8, 'Schmidt', 'Elise', 'Schmidt & Co', 'elise.schmidt@example.com', '0786655443'),
	(9, 'Lopez', 'Hugo', 'HL Design', 'hugo.lopez@example.com', '0779988776'),
	(10, 'Meier', 'Nina', 'Meier Architectes', 'nina.meier@example.com', '0767788990');

-- Dumping structure for table cojan_erick_expi1a_docu.t_docclients
DROP TABLE IF EXISTS `t_docclients`;
CREATE TABLE IF NOT EXISTS `t_docclients` (
  `id_doc` int NOT NULL AUTO_INCREMENT,
  `titre` varchar(150) DEFAULT NULL,
  `contenu` text,
  `date_ajout` date DEFAULT NULL,
  `entreprise` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_doc`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table cojan_erick_expi1a_docu.t_docclients: ~10 rows (approximately)
INSERT INTO `t_docclients` (`id_doc`, `titre`, `contenu`, `date_ajout`, `entreprise`) VALUES
	(2, 'Facture fevrier', 'Facture pour le mois de fevrier', '2024-02-01', 'Durand & Fils'),
	(3, 'Rapport annuel', 'Rapport annuel des activités', '2024-03-10', 'AN Informatique'),
	(4, 'Accusé de réception', 'Confirmation de réception des documents', '2023-04-05', 'Transport Giraud'),
	(5, 'Plan de projet', 'Plan détaillé du projet 2024', '2024-01-20', 'PL Conseil'),
	(6, 'Note technique', 'Note sur les spécificités techniques du service', '2024-02-18', 'Carlos Dépannage'),
	(7, 'Certificat', 'Certificat de conformité délivré', '2024-03-22', 'Thierry Énergies'),
	(8, 'Historique des échanges', 'Résumé des communications par mail', '2024-04-15', 'Schmidt & Co'),
	(9, 'Planning de maintenance', 'Planning prévu pour 2024', '2024-05-01', 'HL Design'),
	(10, 'Lettre de remerciement', 'Lettre envoyée suite à une collaboration réussie', '2024-05-15', 'Meier Architectes'),
	(17, 'Facture rosa ', 'la facture pour le site a rosa ', '2025-03-10', 'zrtdev');

-- Dumping structure for table cojan_erick_expi1a_docu.t_utilisateur
DROP TABLE IF EXISTS `t_utilisateur`;
CREATE TABLE IF NOT EXISTS `t_utilisateur` (
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table cojan_erick_expi1a_docu.t_utilisateur: ~9 rows (approximately)
INSERT INTO `t_utilisateur` (`id_utilisateur`, `nom`, `prenom`, `email`) VALUES
	(2, 'Martin', 'Jean', 'jean.martin@example.com'),
	(3, 'Bernard', 'Sophie', 'sophie.bernard@example.com'),
	(4, 'Petit', 'Luc', 'luc.petit@example.com'),
	(5, 'Robert', 'Claire', 'claire.robert@example.com'),
	(6, 'Leroy', 'Nicolas', 'nicolas.leroy@example.com'),
	(7, 'Moreau', 'Camille', 'camille.moreau@example.com'),
	(8, 'Simon', 'Julien', 'julien.simon@example.com'),
	(9, 'Michel', 'Laura', 'laura.michel@example.com'),
	(10, 'Garcia', 'Paul', 'paul.garcia@example.com');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
