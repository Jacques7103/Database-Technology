-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: stocks
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `stocks`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `stocks` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `stocks`;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `category` varchar(255) NOT NULL,
  `product_brand` varchar(255) NOT NULL,
  PRIMARY KEY (`category`,`product_brand`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('Refrigerator','GE'),('Refrigerator','LG'),('Refrigerator','Maytag'),('Refrigerator','Samsung'),('Refrigerator','Whirlpool'),('Television','Hisense'),('Television','LG'),('Television','Samsung'),('Television','Sony'),('Television','TCL');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refrigerator`
--

DROP TABLE IF EXISTS `refrigerator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `refrigerator` (
  `product_brand` varchar(255) DEFAULT NULL,
  `type_id` varchar(255) NOT NULL,
  `modal_price` float(255,2) DEFAULT NULL,
  `selling_price` float(255,2) DEFAULT NULL,
  `stocks` int(10) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`type_id`),
  KEY `category` (`product_brand`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refrigerator`
--

LOCK TABLES `refrigerator` WRITE;
/*!40000 ALTER TABLE `refrigerator` DISABLE KEYS */;
INSERT INTO `refrigerator` VALUES ('LG','GC-B257SGVL',741.00,849.99,8,'Linear Cooling, Door Cooling, Hygiene Filter Gen2, No Ice Tray, 913 x 1790 x 735, Refri : R600a'),('LG','GC-L22FTQBL',814.46,999.99,5,'Express Freezing, Child Lock, Moist Balance Crisper, 835 x 1787 x 734, Door Cooling'),('LG','GC-Q257CSFS',1269.92,1400.00,5,'Voice Control, Remote Control, Smart Alert, 913 x 1790 x 735, Door Cooling, Refri : R600a-62g'),('GE','GFE28GYNFS',2443.00,2549.99,3,'Fingerprint Resistant Stainless, Twinchill Evaporators, Child Lock, Advanced Water Filtration, 908 x 1791 x 921, Turbo Cool Setting'),('GE','GSS25GYPFS',1443.00,1599.99,5,'Fingerprint Resistant Stainless, External Dispenser, Advanced Water Filtration, Electronic Display, 915 x 1769 x 883, Child Lock'),('Maytag','MFW2055FRZ',2299.00,2499.99,3,'Fingerprint Resistant Stainless, Temperature-Controlled Wide-N-Fresh Deli Drawer, 765 x 1737 x 873, Exterior Dispenser'),('Maytag','MRT118FFFE',749.00,999.99,5,'PowerCold Feature, Gallon Door Storage, Bottom-Mounted Freshlock Crispers with Humidity Controls, 756 x 1610 x 797'),('Maytag','MSS25N4MKZ',1339.00,1699.99,5,'Fingerprint Resistant Stainless, Gallon Door Bins, Non-dispense layout, Humidity-Controlled Freshlock Crisper, 912 x 1769 x 854'),('GE','PVD28BYNFS',3554.00,3799.99,3,'Fingerprint Resistant Stainless, Advanced Water Filtration, Hands-free Autofill Water, 905 x 1778 x 933, Door in Door'),('Samsung','RF48A4000B4',830.00,1099.00,5,'Twin Cooling Plus, Movable Ice Maker, No Frost, Power Cool/Freeze, 890 x 1875 x 795'),('Samsung','RH64A53F1B4',1400.00,1699.00,5,'Food Showcase, SpaceMax Technology, Metal Cooling, All-around Cooling, Power Cool/Freeze, Auto Ice Maker, 776 x 1909 x 974'),('Samsung','RS62T5F01B4',1850.00,2199.99,3,'SmartView, Tuneln/Spotify, View Inside, Recipes & Meal Planner, New Bixby, Bluetooth Call, Samsung SmartThings, 974 x 1909 x 776'),('Whirlpool','WRB543CMJV',1599.00,1899.99,5,'TotalCoverage Cooling, Auto Hibernate Mode, Gallon Door Bin, Large Freezer Drawer, Fast Drink Option, 619 x 1804 x 721'),('Whirlpool','WRF555SDHV',2799.00,3099.99,3,'Exterior Ice and Water Dispenser with EveryDrop Filtration, Spillproof Shelves, Humidity-Controlled Double Crisper, 905 x 1785 x 889'),('Whirlpool','WRS325SDHZ',1799.00,2099.99,3,'Frameless Glass Shelves, Adjustable Gallon Door Bins, Exterior Ice and Water Dispenser with EveryDrop Filtration, 902 x 1769 x 854');
/*!40000 ALTER TABLE `refrigerator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `television`
--

DROP TABLE IF EXISTS `television`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `television` (
  `product_brand` varchar(255) DEFAULT NULL,
  `type_id` varchar(255) NOT NULL,
  `modal_price` float(255,2) DEFAULT NULL,
  `selling_price` float(255,2) DEFAULT NULL,
  `stocks` int(10) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`type_id`),
  KEY `category` (`product_brand`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `television`
--

LOCK TABLES `television` WRITE;
/*!40000 ALTER TABLE `television` DISABLE KEYS */;
INSERT INTO `television` VALUES ('Hisense','43A4200G',245.63,309.99,10,'43 Inch, Processor : Quad-Core, Full HD, Sound : DTS Virtual-X'),('LG','50UQ9000PSD',499.00,700.00,10,'50 Inch, 4K Resolution, ThinQ AI & WebOS, Active HDR'),('TCL','55A8',784.97,1099.99,9,'55 Inch, 4K Resolution, Dolby Audio, Google Assistant, 60 Hz, T-Cast, HDR10 Decoding'),('Hisense','65U6H',899.94,1099.99,5,'65 Inch, 4K Resolution, Full Array Local Dimming, Bezeless Design'),('Hisense','75A6500H',1116.97,1399.99,5,'75 Inch, 4K resolution, Ambient Light Adaptive, Sound : DTS Virtual-X'),('TCL','75P735',1148.76,1499.99,5,'75 Inch, Resolution : 3840 x 2160, 60 Hz, HDR10, Hands-Free Voice Control, Dolby Atmos, MMEC'),('LG','75QNED86SQA',2792.69,3099.99,3,'75 Inch, 4K Resolution, Dolby Atmos, 100% Color Consistency & Color Volume'),('LG','75UQ8050PSB',1103.76,1399.99,5,'75 Inch, 4K Resolution, ThinQ AI & WebOS, Active HDR'),('TCL','85P725',2552.31,2899.99,3,'85 Inch, Resolution : 3840 x 2160, Dolby Atmos, Hands-Free Voice Control 2.0, AiPQ Engine'),('Sony','A80K',1659.35,1899.99,3,'55 Inch, Resolution : 3840 x 2160, Cognitive Processor XR, 120 FPS, Auto Genre Picture Mode'),('Samsung','QA43LS03BAKXXD',680.54,999.99,5,'43 Inch, Resolution : 3840 x 2160, Quantum Processor 4K, Matte Display'),('Samsung','QA55LS03RAKPXD',1085.00,1299.99,5,'55 Inch, Resolution : 3840 x 2160, Quantum HDR+, Seamless Connection'),('Samsung','QA55LS03TAKXXD',1180.45,1399.99,5,'55 Inch, Resolution : 3840 x 2160, Quantum Processor 4K, Frame-look Design'),('Sony','X90J',893.47,1249.99,5,'55 Inch, Resolution : 3840 x 2160, XR Clarity, 120 FPS, 3D Surround Upscaling, Dolby Atmos, Acoustic Auto Calibration'),('Sony','X90K',957.26,1299.99,5,'55 Inch, Resolution : 3840 x 2160, Acoustic Multi-Audio, 3D Surround Upscaling, Ambient Optimization');
/*!40000 ALTER TABLE `television` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `occupation` enum('Auditor','Marketing','Storekeeper') DEFAULT NULL,
  `user_id` int(3) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `worker` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Chi','asd','Marketing',101),('Jopras','asd','Auditor',102),('Xynn','asd','Storekeeper',100);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `worker`
--

DROP TABLE IF EXISTS `worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `worker` (
  `user_id` int(3) NOT NULL AUTO_INCREMENT,
  `occupation` enum('Auditor','Marketing','Storekeeper') NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`occupation`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `worker`
--

LOCK TABLES `worker` WRITE;
/*!40000 ALTER TABLE `worker` DISABLE KEYS */;
INSERT INTO `worker` VALUES (100,'Storekeeper','Ferdinand','Jacques'),(101,'Marketing','Leonardo','Richie'),(102,'Auditor','Jonathan','Prasetyo');
/*!40000 ALTER TABLE `worker` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-27 14:34:16
