-- MySQL dump 10.14  Distrib 5.5.31-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: cmdbtest
-- ------------------------------------------------------
-- Server version	5.5.31-MariaDB-log

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('0725f9e44b59');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `idc_id` int(11) NOT NULL,
  `power` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_cabinet_idc_id` (`idc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (1,'A11-22',0,'450');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(50) NOT NULL,
  `superior` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idc`
--

DROP TABLE IF EXISTS `idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `idc_name` varchar(30) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `user_interface` varchar(50) NOT NULL,
  `user_phone` varchar(20) NOT NULL,
  `rel_cabinet_num` int(11) NOT NULL,
  `pack_cabinet_num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_idc_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (1,'shubei','oom','zhaowei','123','guishi@163.com','xiaohong','12345678912',12,15),(2,'jxq','酒仙桥','北京','12315011401','guishi@163.com','frank','12345678912',12,15);
/*!40000 ALTER TABLE `idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_info`
--

DROP TABLE IF EXISTS `ip_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ip_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) NOT NULL,
  `mac` varchar(20) NOT NULL,
  `device` varchar(20) NOT NULL,
  `serve_id` int(11) NOT NULL,
  `swich_id` int(11) NOT NULL,
  `swich_port` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_ip_info_serve_id` (`serve_id`),
  KEY `ix_ip_info_swich_id` (`swich_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_info`
--

LOCK TABLES `ip_info` WRITE;
/*!40000 ALTER TABLE `ip_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacture`
--

DROP TABLE IF EXISTS `manufacture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manufacture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacture`
--

LOCK TABLES `manufacture` WRITE;
/*!40000 ALTER TABLE `manufacture` DISABLE KEYS */;
/*!40000 ALTER TABLE `manufacture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `power`
--

DROP TABLE IF EXISTS `power`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `power` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_power` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `power`
--

LOCK TABLES `power` WRITE;
/*!40000 ALTER TABLE `power` DISABLE KEYS */;
INSERT INTO `power` VALUES (1,'160'),(2,'250'),(3,'450'),(4,'480');
/*!40000 ALTER TABLE `power` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(20) NOT NULL,
  `pid` int(11) NOT NULL,
  `module_letter` varchar(10) NOT NULL,
  `dev_interface` varchar(100) DEFAULT NULL,
  `op_interface` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raid`
--

DROP TABLE IF EXISTS `raid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raid`
--

LOCK TABLES `raid` WRITE;
/*!40000 ALTER TABLE `raid` DISABLE KEYS */;
/*!40000 ALTER TABLE `raid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raidtype`
--

DROP TABLE IF EXISTS `raidtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `raidtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raidtype`
--

LOCK TABLES `raidtype` WRITE;
/*!40000 ALTER TABLE `raidtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `raidtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier` int(11) DEFAULT NULL,
  `manufactures` varchar(50) NOT NULL,
  `manufacture_date` date DEFAULT NULL,
  `server_type` varchar(20) DEFAULT NULL,
  `st` varchar(60) DEFAULT NULL,
  `assets_no` varchar(60) DEFAULT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `cabinet_id` int(11) DEFAULT NULL,
  `cabinet_pos` varchar(10) DEFAULT NULL,
  `expire` date DEFAULT NULL,
  `ups` int(11) DEFAULT NULL,
  `parter` varchar(50) DEFAULT NULL,
  `parter_type` varchar(50) DEFAULT NULL,
  `server_up_time` date DEFAULT NULL,
  `os_type` varchar(20) DEFAULT NULL,
  `os_version` varchar(10) DEFAULT NULL,
  `hostname` varchar(32) NOT NULL,
  `inner_ip` varchar(32) NOT NULL,
  `mac_address` varchar(32) DEFAULT NULL,
  `ip_info` varchar(300) DEFAULT NULL,
  `server_cpu` varchar(250) DEFAULT NULL,
  `server_disk` varchar(250) DEFAULT NULL,
  `server_mem` varchar(250) DEFAULT NULL,
  `raid` varchar(10) DEFAULT NULL,
  `raid_card_type` varchar(50) DEFAULT NULL,
  `remote_card` varchar(32) DEFAULT NULL,
  `remote_cardip` varchar(32) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `remark` text,
  `last_op_time` time DEFAULT NULL,
  `last_op_people` int(11) DEFAULT NULL,
  `monitor_mail_group` varchar(32) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `server_purpose` int(11) DEFAULT NULL,
  `trouble_resolve` int(11) DEFAULT NULL,
  `op_interface_other` int(11) DEFAULT NULL,
  `dev_interface` int(11) DEFAULT NULL,
  `check_update_time` time DEFAULT NULL,
  `vm_status` int(11) NOT NULL,
  `power` int(11) DEFAULT NULL,
  `host` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_server_host` (`host`),
  KEY `ix_server_hostname` (`hostname`),
  KEY `ix_server_idc_id` (`idc_id`),
  KEY `ix_server_inner_ip` (`inner_ip`),
  KEY `ix_server_manufactures` (`manufactures`),
  KEY `ix_server_server_purpose` (`server_purpose`),
  KEY `ix_server_service_id` (`service_id`),
  KEY `ix_server_st` (`st`),
  KEY `ix_server_status` (`status`),
  KEY `ix_server_supplier` (`supplier`),
  KEY `ix_server_vm_status` (`vm_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servertype`
--

DROP TABLE IF EXISTS `servertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `manufactures_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_servertype_manufactures_id` (`manufactures_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servertype`
--

LOCK TABLES `servertype` WRITE;
/*!40000 ALTER TABLE `servertype` DISABLE KEYS */;
/*!40000 ALTER TABLE `servertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `switch`
--

DROP TABLE IF EXISTS `switch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `switch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `switch_name` varchar(50) NOT NULL,
  `switch_type` varchar(50) NOT NULL,
  `manager_ip` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `cabinet_id` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `expire` date DEFAULT NULL,
  `remark` text,
  `manufacturers` int(11) DEFAULT NULL,
  `last_op_time` time DEFAULT NULL,
  `last_op_people` int(11) DEFAULT NULL,
  `switch_port_nums` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_switch_cabinet_id` (`cabinet_id`),
  KEY `ix_switch_idc_id` (`idc_id`),
  KEY `ix_switch_status` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `switch`
--

LOCK TABLES `switch` WRITE;
/*!40000 ALTER TABLE `switch` DISABLE KEYS */;
/*!40000 ALTER TABLE `switch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `deparment_id` int(11) DEFAULT NULL,
  `is_leader` int(11) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_user_deparment_id` (`deparment_id`),
  KEY `ix_user_is_leader` (`is_leader`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-20 18:29:43
