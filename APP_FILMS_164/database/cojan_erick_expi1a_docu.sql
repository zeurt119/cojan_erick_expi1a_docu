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

drop database if exist cojan_erick_expi1a_docu;
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
  `commentaire` text,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table cojan_erick_expi1a_docu.t_client: ~10 rows (approximately)
INSERT INTO `t_client` (`id_client`, `nom`, `prenom`, `entreprise`, `email`, `telephone`, `commentaire`) VALUES
	(1, 'Dupont', 'Pierre', 'Dupont SARL', 'pierre.dupont@example.com', '0791234567', 'Client fidèle depuis 2 ans.'),
	(2, 'Durand', 'Marie', 'Durand & Fils', 'marie.durand@example.com', '0789876543', 'Demande des documents régulièrement.'),
	(3, 'Morel', 'Antoine', 'AM Informatique', 'antoine.morel@example.com', '0773334455', 'Souhaite recevoir un rapport mensuel.'),
	(4, 'Giraud', 'Lucie', 'Transport Giraud', 'lucie.giraud@example.com', '0761122334', 'Ravi des services.'),
	(5, 'Lemoine', 'Pauline', 'PL Conseil', 'pauline.lemoine@example.com', '0759988776', 'Besoin de factures trimestrielles.'),
	(6, 'Fernandez', 'Carlos', 'Carlos Dépannage', 'carlos.fernandez@example.com', '0745566778', 'Client récent.'),
	(7, 'Nguyen', 'Thierry', 'Thierry Énergies', 'thierry.nguyen@example.com', '0793344556', 'Demande des documents techniques.'),
	(8, 'Schmidt', 'Elise', 'Schmidt & Co', 'elise.schmidt@example.com', '0786655443', 'À relancer pour les validations.'),
	(9, 'Lopez', 'Hugo', 'HL Design', 'hugo.lopez@example.com', '0779988776', 'Actif sur plusieurs projets.'),
	(10, 'Meier', 'Nina', 'Meier Architectes', 'nina.meier@example.com', '0767788990', 'Demande des mises à jour fréquentes.');

-- Dumping structure for table cojan_erick_expi1a_docu.t_docclients
DROP TABLE IF EXISTS `t_docclients`;
CREATE TABLE IF NOT EXISTS `t_docclients` (
  `id_doc` int NOT NULL AUTO_INCREMENT,
  `id_client` int NOT NULL,
  `id_utilisateur` int NOT NULL,
  `titre` varchar(150) DEFAULT NULL,
  `contenu` text,
  `date_ajout` date DEFAULT NULL,
  `chemin_fichier` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_doc`),
  KEY `id_client` (`id_client`),
  KEY `id_utilisateur` (`id_utilisateur`),
  CONSTRAINT `t_docclients_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `t_client` (`id_client`),
  CONSTRAINT `t_docclients_ibfk_2` FOREIGN KEY (`id_utilisateur`) REFERENCES `t_utilisateur` (`id_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table cojan_erick_expi1a_docu.t_docclients: ~10 rows (approximately)
INSERT INTO `t_docclients` (`id_doc`, `id_client`, `id_utilisateur`, `titre`, `contenu`, `date_ajout`) VALUES
	(1, 1, 1, 'Contrat 2023', 'Contenu du contrat signé en 2023', '2023-01-15'),
	(2, 2, 2, 'Facture Janvier', 'Facture pour le mois de janvier', '2023-02-01'),
	(3, 3, 3, 'Rapport mensuel', 'Rapport mensuel des activités', '2023-03-10'),
	(4, 4, 4, 'Accusé de réception', 'Confirmation de réception des documents', '2023-04-05'),
	(5, 5, 5, 'Plan de projet', 'Plan détaillé du projet 2024', '2024-01-20'),
	(6, 6, 6, 'Note technique', 'Note sur les spécificités techniques du service', '2024-02-18'),
	(7, 7, 7, 'Certificat', 'Certificat de conformité délivré', '2024-03-22'),
	(8, 8, 8, 'Historique des échanges', 'Résumé des communications par mail', '2024-04-15'),
	(9, 9, 9, 'Planning de maintenance', 'Planning prévu pour 2024', '2024-05-01'),
	(10, 10, 10, 'Lettre de remerciement', 'Lettre envoyée suite à une collaboration réussie', '2024-05-15');

-- Dumping structure for table cojan_erick_expi1a_docu.t_utilisateur
DROP TABLE IF EXISTS `t_utilisateur`;
CREATE TABLE IF NOT EXISTS `t_utilisateur` (
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table cojan_erick_expi1a_docu.t_utilisateur: ~10 rows (approximately)
INSERT INTO `t_utilisateur` (`id_utilisateur`, `nom`, `prenom`, `email`) VALUES
	(1, 'Durand', 'Alice', 'alice.durand@example.com'),
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
