-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: pizzas
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.21.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Address` (
  `address_id` int NOT NULL AUTO_INCREMENT,
  `street` varchar(255) NOT NULL,
  `town` varchar(255) NOT NULL,
  `postcode` varchar(6) NOT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `address_id` int NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DeliveryDriver`
--

DROP TABLE IF EXISTS `DeliveryDriver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DeliveryDriver` (
  `driver_id` int NOT NULL AUTO_INCREMENT,
  `operating_area` varchar(6) NOT NULL,
  `on_task` tinyint(1) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`driver_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DeliveryDriver`
--

LOCK TABLES `DeliveryDriver` WRITE;
/*!40000 ALTER TABLE `DeliveryDriver` DISABLE KEYS */;
INSERT INTO `DeliveryDriver` VALUES (1,'6226GJ',0,'Christof'),(2,'4202MS',0,'Peter'),(3,'5683CG',0,'Tom'),(4,'6221AG',0,'Pietro'),(5,'5701BG',0,'Enrique');
/*!40000 ALTER TABLE `DeliveryDriver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dessert`
--

DROP TABLE IF EXISTS `Dessert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dessert` (
  `dessert_id` int NOT NULL AUTO_INCREMENT,
  `dessert_name` varchar(255) NOT NULL,
  `dessert_price_euros` int NOT NULL,
  `dessert_price_cents` int NOT NULL,
  PRIMARY KEY (`dessert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dessert`
--

LOCK TABLES `Dessert` WRITE;
/*!40000 ALTER TABLE `Dessert` DISABLE KEYS */;
INSERT INTO `Dessert` VALUES (1,'Tiramisu',5,0),(2,'Cheesecake',6,50),(3,'Twin Cannoli',5,0),(4,'Lorem Ipsum Cupcake',6,90),(5,'Banana Waffle',5,50),(6,'Nutella Banana',6,50),(7,'Apple Crumble',7,0),(8,'Ice Cream',5,0),(9,'Rice Pudding',4,0),(10,'Protein Shake Ice',24,7);
/*!40000 ALTER TABLE `Dessert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DessertMapping`
--

DROP TABLE IF EXISTS `DessertMapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DessertMapping` (
  `dessert_map_id` int NOT NULL AUTO_INCREMENT,
  `purchase_id` int NOT NULL,
  `dessert_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`dessert_map_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DessertMapping`
--

LOCK TABLES `DessertMapping` WRITE;
/*!40000 ALTER TABLE `DessertMapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `DessertMapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Drink`
--

DROP TABLE IF EXISTS `Drink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Drink` (
  `drink_id` int NOT NULL AUTO_INCREMENT,
  `drink_name` varchar(255) NOT NULL,
  `drink_price_euros` int NOT NULL,
  `drink_price_cents` int NOT NULL,
  PRIMARY KEY (`drink_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Drink`
--

LOCK TABLES `Drink` WRITE;
/*!40000 ALTER TABLE `Drink` DISABLE KEYS */;
INSERT INTO `Drink` VALUES (1,'Water',2,0),(2,'Coke',3,0),(3,'Fanta',3,0),(4,'Sprite',3,0),(5,'Red Bull',4,50),(6,'Ice Tea',3,50),(7,'Bitter Lemon',3,0),(8,'Paulaner Weissbier',5,0),(9,'Glenfinnan 12 Years Old',25,50),(10,'Veuve Clicquot Ponsardin',99,90);
/*!40000 ALTER TABLE `Drink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DrinkMapping`
--

DROP TABLE IF EXISTS `DrinkMapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DrinkMapping` (
  `drink_map_id` int NOT NULL AUTO_INCREMENT,
  `drink_id` int NOT NULL,
  `purchase_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`drink_map_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DrinkMapping`
--

LOCK TABLES `DrinkMapping` WRITE;
/*!40000 ALTER TABLE `DrinkMapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `DrinkMapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pizza`
--

DROP TABLE IF EXISTS `Pizza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pizza` (
  `pizza_id` int NOT NULL AUTO_INCREMENT,
  `pizza_name` varchar(255) NOT NULL,
  `pizza_price_euros` int NOT NULL,
  `pizza_price_cents` int NOT NULL,
  PRIMARY KEY (`pizza_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pizza`
--

LOCK TABLES `Pizza` WRITE;
/*!40000 ALTER TABLE `Pizza` DISABLE KEYS */;
INSERT INTO `Pizza` VALUES (1,'Margherita',5,0),(2,'Tuna',6,50),(3,'Pepperoni',7,0),(4,'Vegetaria',6,0),(5,'Salami',8,50),(6,'Chicken',7,50),(7,'Hawaii',5,0),(8,'Dutch Herbs',4,20),(9,'Lover',6,90),(10,'Calzone',5,0);
/*!40000 ALTER TABLE `Pizza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PizzaMapping`
--

DROP TABLE IF EXISTS `PizzaMapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PizzaMapping` (
  `pizza_map_id` int NOT NULL AUTO_INCREMENT,
  `purchase_id` int NOT NULL,
  `pizza_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`pizza_map_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PizzaMapping`
--

LOCK TABLES `PizzaMapping` WRITE;
/*!40000 ALTER TABLE `PizzaMapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `PizzaMapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Purchase`
--

DROP TABLE IF EXISTS `Purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Purchase` (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `purchased_at` datetime NOT NULL,
  `customer_id` int NOT NULL,
  `delivery_driver_id` int DEFAULT NULL,
  PRIMARY KEY (`purchase_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Purchase`
--

LOCK TABLES `Purchase` WRITE;
/*!40000 ALTER TABLE `Purchase` DISABLE KEYS */;
/*!40000 ALTER TABLE `Purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Topping`
--

DROP TABLE IF EXISTS `Topping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Topping` (
  `topping_id` int NOT NULL AUTO_INCREMENT,
  `topping_name` varchar(255) NOT NULL,
  `vegetarian` tinyint(1) NOT NULL,
  PRIMARY KEY (`topping_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Topping`
--

LOCK TABLES `Topping` WRITE;
/*!40000 ALTER TABLE `Topping` DISABLE KEYS */;
INSERT INTO `Topping` VALUES (1,'Cheese',1),(2,'Tuna',0),(3,'Pineapple',1),(4,'Bacon',0),(5,'Tomato',1),(6,'Purple Haze',1),(7,'Chicken',0),(8,'Salami',0),(9,'Blue Pills',1),(10,'Mozzarella',1),(11,'Basil',1),(12,'Pepperoni',0);
/*!40000 ALTER TABLE `Topping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ToppingMapping`
--

DROP TABLE IF EXISTS `ToppingMapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ToppingMapping` (
  `topping_map_id` int NOT NULL AUTO_INCREMENT,
  `pizza_id` int NOT NULL,
  `topping_id` int NOT NULL,
  PRIMARY KEY (`topping_map_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ToppingMapping`
--

LOCK TABLES `ToppingMapping` WRITE;
/*!40000 ALTER TABLE `ToppingMapping` DISABLE KEYS */;
INSERT INTO `ToppingMapping` VALUES (1,1,1),(2,2,2),(3,2,1),(4,3,12),(5,4,5),(6,4,11),(7,5,8),(8,6,7),(9,6,1),(10,7,3),(11,7,4),(12,8,6),(13,8,1),(14,9,9),(15,10,1),(16,10,5),(17,10,11),(18,10,4);
/*!40000 ALTER TABLE `ToppingMapping` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-02 11:52:43
