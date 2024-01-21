-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: humpT
-- ------------------------------------------------------
-- Server version	11.2.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `responses`
--

DROP TABLE IF EXISTS `responses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `responses` (
  `question` text DEFAULT NULL,
  `answer` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `responses`
--

LOCK TABLES `responses` WRITE;
/*!40000 ALTER TABLE `responses` DISABLE KEYS */;
INSERT INTO `responses` VALUES ('dd','ss'),('ssa','2345'),('is anything else?','lol'),('1234','23456789'),('hello','world');
/*!40000 ALTER TABLE `responses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sendnow_message`
--

DROP TABLE IF EXISTS `sendnow_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sendnow_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sendnow_message`
--

LOCK TABLES `sendnow_message` WRITE;
/*!40000 ALTER TABLE `sendnow_message` DISABLE KEYS */;
INSERT INTO `sendnow_message` VALUES (1,'Every Tuesday, indulge in our truffle-infused dishes at a special price.'),(2,'Get a free espresso shot with any dessert, available every Monday.'),(3,'Celebrate our Risotto Week with a new flavor introduced daily.'),(4,'Discover a different antipasti every week with our Chef\'s Selection.'),(5,'End your week sweetly with a buy-one-get-one offer on all desserts.'),(6,'Book a romantic dinner for two and enjoy a complimentary bottle of Prosecco.'),(7,'Experience our Cheese Lovers\' menu with a variety of Italian cheeses.'),(8,'Weekday happy hour with half-price appetizers and drink specials from 3-5 PM.'),(9,'Celebrate with us and the birthday guest eats for free! (ID required)'),(10,'Dine with the sounds of live opera on the last Saturday of each month.'),(11,'Weekly specials featuring ingredients from the local farmer\'s market.'),(12,'Dive into our seafood Saturdays with a curated selection of seafood dishes.'),(13,'Join our interactive pizza-making class – perfect for groups and families.'),(14,'Introducing a new dessert each month inspired by Italian cinema.'),(15,'Solo diners get a complimentary glass of wine with their meal on Wednesdays.'),(16,'Unwind with our aperitivo selections from 4 PM onwards, every Thursday.'),(17,'Gluten-free pasta and pizza now available every day.'),(18,'Seniors enjoy a 20% discount every Wednesday.'),(19,'Build your own lasagna with various ingredients, available on Mondays.'),(20,'Start the week with our fresh mozzarella dishes at a discount.');
/*!40000 ALTER TABLE `sendnow_message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-19 18:14:52
