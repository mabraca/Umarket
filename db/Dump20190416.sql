CREATE DATABASE  IF NOT EXISTS `ubiimarket_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `ubiimarket_db`;
-- MySQL dump 10.13  Distrib 5.7.22, for Win64 (x86_64)
--
-- Host: localhost    Database: ubiimarket_db
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.38-MariaDB

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
-- Table structure for table `dt_componentes_producto`
--

DROP TABLE IF EXISTS `dt_componentes_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_componentes_producto` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla componentes de producto.',
  `dt_productos_intnumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el número del producto .',
  `dpnprecio_componente` double DEFAULT NULL COMMENT 'Este campo almacena el precio del componente del producto.',
  `dtmfecha_creacion` datetime DEFAULT NULL COMMENT 'Este campo almacena la fecha y hora  de creación del registro de los datos del componente.',
  `dtmfecha_actualizacion` datetime DEFAULT NULL COMMENT 'Este campo almacena la fecha y hora de actualización del registro.',
  PRIMARY KEY (`id`,`dt_productos_intnumero_producto`),
  KEY `fk_dt_producto_dt_componente_producto` (`dt_productos_intnumero_producto`),
  CONSTRAINT `fk_dt_producto_dt_componente_producto` FOREIGN KEY (`dt_productos_intnumero_producto`) REFERENCES `dt_productos` (`intumero_producto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_componentes_producto`
--

LOCK TABLES `dt_componentes_producto` WRITE;
/*!40000 ALTER TABLE `dt_componentes_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_componentes_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_detalle_entrada`
--

DROP TABLE IF EXISTS `dt_detalle_entrada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_detalle_entrada` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla detalle de entrada al inventario.',
  `dt_entrada_inventario_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla entrada al inventario.',
  `dt_productos_intnumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el numero del producto .',
  `dt_productos_dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa a la cual pertenece la entrada al inventario.',
  `intcantidad` int(10) DEFAULT NULL COMMENT 'Este campo almacena la cantidad de producto a ingresar.',
  `dpnprecio_unitario` double DEFAULT NULL COMMENT 'Este campo almacena el precio unitario del producto a entrar al inventario.',
  `dpnmonto_subtotal` double DEFAULT NULL COMMENT 'Este campo almacena el monto del subtotal del producto.',
  `dpnmonto` double DEFAULT NULL COMMENT 'Este campo almacena el monto del producto.',
  `intorden` int(11) DEFAULT NULL COMMENT 'Este campo almacena el orden del detalle de la entrada, es decir, el correlativo para identificar cual es el número del item.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  PRIMARY KEY (`id`,`dt_entrada_inventario_id`),
  KEY `fk_dt_entrada_inventario_dt_detalle_inventario` (`dt_entrada_inventario_id`),
  KEY `fk_dt_producto_dt_detalle_inventario` (`dt_productos_intnumero_producto`,`dt_productos_dt_empresa_id_empresa`),
  CONSTRAINT `fk_dt_entrada_inventario_dt_detalle_inventario` FOREIGN KEY (`dt_entrada_inventario_id`) REFERENCES `dt_entrada_inventario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_producto_dt_detalle_inventario` FOREIGN KEY (`dt_productos_intnumero_producto`, `dt_productos_dt_empresa_id_empresa`) REFERENCES `dt_productos` (`intumero_producto`, `dt_empresa_id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_detalle_entrada`
--

LOCK TABLES `dt_detalle_entrada` WRITE;
/*!40000 ALTER TABLE `dt_detalle_entrada` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_detalle_entrada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_detalle_factura`
--

DROP TABLE IF EXISTS `dt_detalle_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_detalle_factura` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla detalle de factura.',
  `dt_factura_strnumero_factura` varchar(15) NOT NULL COMMENT 'Este campo almacena el número de la factura.',
  `dt_pedido_id` int(11) NOT NULL,
  `dt_productos_intumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el numero del producto, el cual esta como llave foranea proveniente de la tabla producto.',
  `strnumero_serial` varchar(20) DEFAULT NULL COMMENT 'Este campo almacena el número del serial de producto.',
  `dpnmonto` double DEFAULT NULL COMMENT 'Este campo almacena el monto del producto.',
  `dpnmonto_iva` double DEFAULT NULL COMMENT 'Este campo almacena el monto del Impuesto al Valor Agredado del producto.',
  `dpnmonto_total` double DEFAULT NULL COMMENT 'Este campo almacena el monto total del producto',
  `intorden` int(11) DEFAULT NULL COMMENT 'Este campo almacena el número de orden del producto en el detalle de la factura, es decir, lleva el control de item en el detalle.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de creación del registro.',
  PRIMARY KEY (`id`,`dt_factura_strnumero_factura`,`dt_pedido_id`),
  KEY `fk_dt_factura_dt_detalle_factura` (`dt_factura_strnumero_factura`),
  KEY `fk_dt_pedido` (`dt_pedido_id`),
  KEY `fk_dt_producto_dt_detalle_factura` (`dt_productos_intumero_producto`),
  CONSTRAINT `fk_dt_factura_dt_detalle_factura` FOREIGN KEY (`dt_factura_strnumero_factura`) REFERENCES `dt_factura` (`strnumero_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_pedido` FOREIGN KEY (`dt_pedido_id`) REFERENCES `dt_pedido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_producto_dt_detalle_factura` FOREIGN KEY (`dt_productos_intumero_producto`) REFERENCES `dt_productos` (`intumero_producto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_detalle_factura`
--

LOCK TABLES `dt_detalle_factura` WRITE;
/*!40000 ALTER TABLE `dt_detalle_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_detalle_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_detalle_guia`
--

DROP TABLE IF EXISTS `dt_detalle_guia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_detalle_guia` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla detalle de guia.',
  `dt_guia_strguia_qr` varchar(60) NOT NULL COMMENT 'Este campo almacena el código de qr de la guía.',
  `strubicacion` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena la ubicación de la guía.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  PRIMARY KEY (`id`,`dt_guia_strguia_qr`),
  KEY `fk_dt_guia_dt_detalle_guia` (`dt_guia_strguia_qr`),
  CONSTRAINT `fk_dt_guia_dt_detalle_guia` FOREIGN KEY (`dt_guia_strguia_qr`) REFERENCES `dt_guia` (`strguia_qr`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_detalle_guia`
--

LOCK TABLES `dt_detalle_guia` WRITE;
/*!40000 ALTER TABLE `dt_detalle_guia` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_detalle_guia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_detalle_inventario`
--

DROP TABLE IF EXISTS `dt_detalle_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_detalle_inventario` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla detalle del inventario.',
  `strnumero_serial` varchar(20) DEFAULT NULL COMMENT 'Este campo almacena el numero de serial del producto existente en el inventario.',
  `strnumero_lote` varchar(20) DEFAULT NULL COMMENT 'Este campo almacena el número de lote del producto existente en el inventario.',
  `tb_estatus_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del estatus del producto existente en el inventario.',
  `dt_inventario_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del inventario.',
  `dt_inventario_dt_productos_intumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el número del producto existente en el inventario.',
  `dt_inventario_dt_productos_dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa a la cual pertenece el producto existente en el inventario.',
  `dpnprecio` double DEFAULT NULL COMMENT 'Este campo almacena el precio del producto existente en el inventario.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`dt_inventario_id`),
  KEY `fk_dt_detalle_inventario_dt_inventario` (`dt_inventario_id`,`dt_inventario_dt_productos_intumero_producto`,`dt_inventario_dt_productos_dt_empresa_id_empresa`),
  KEY `fk_dt_detalle_inventario_tb_estatus` (`tb_estatus_id`),
  CONSTRAINT `fk_dt_detalle_inventario_dt_inventario` FOREIGN KEY (`dt_inventario_id`, `dt_inventario_dt_productos_intumero_producto`, `dt_inventario_dt_productos_dt_empresa_id_empresa`) REFERENCES `dt_inventario` (`id`, `dt_productos_intumero_producto`, `dt_productos_dt_empresa_id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_detalle_inventario_tb_estatus` FOREIGN KEY (`tb_estatus_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_detalle_inventario`
--

LOCK TABLES `dt_detalle_inventario` WRITE;
/*!40000 ALTER TABLE `dt_detalle_inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_detalle_inventario` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `ubiimarket_db`.`tg_dt_detalle_inventario_actualizacion` AFTER UPDATE ON `dt_detalle_inventario` FOR EACH ROW
BEGIN
	UPDATE dt_detalle_inventario SET dtmfecha_actualizacion=now() WHERE id=NEW.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `dt_detalle_pedido`
--

DROP TABLE IF EXISTS `dt_detalle_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_detalle_pedido` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla detalle de pedido.',
  `dt_pedido_id` int(11) NOT NULL COMMENT 'Este campo almaena el identificador del pedido.',
  `dt_productos_intnumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el número del producto.',
  `dpnprecio_unitario` double NOT NULL COMMENT 'Este campo almacena el precio unitario del producto pedido.',
  `dpnmonto` double DEFAULT NULL COMMENT 'Este campo almacena el monto del producto.',
  `intcantidad` int(11) DEFAULT NULL COMMENT 'Este campo almacena la cantidad del producto.',
  `dpnmonto_iva` double DEFAULT NULL COMMENT 'Este campo almacena el monto del Impuesto al Valor Agregado.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`dt_pedido_id`),
  KEY `fk_detalle_pedido_dt_pedido` (`dt_pedido_id`),
  KEY `fk_dt_detalle_pedido_dt_productos` (`dt_productos_intnumero_producto`),
  CONSTRAINT `fk_detalle_pedido_dt_pedido` FOREIGN KEY (`dt_pedido_id`) REFERENCES `dt_pedido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_detalle_pedido_dt_productos` FOREIGN KEY (`dt_productos_intnumero_producto`) REFERENCES `dt_productos` (`intumero_producto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_detalle_pedido`
--

LOCK TABLES `dt_detalle_pedido` WRITE;
/*!40000 ALTER TABLE `dt_detalle_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_detalle_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_direccion_entrega`
--

DROP TABLE IF EXISTS `dt_direccion_entrega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_direccion_entrega` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla dirección de entrega.',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del usuario que registró la dirección de su entrega.',
  `strdireccion_entrega` varchar(150) NOT NULL COMMENT 'Este campo almacena la dirección de la entrega del usuario.',
  `strotros_datos` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena otros datos relacionados a la dirección, ejemplo, punto de referencia o nombres de personas por la cual debe preguntar.',
  `strcoordenadas` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena las coordenadas de localización de la entrega.',
  `tm_parroquia_tm_municipio_id` int(11) NOT NULL,
  `tm_parroquia_id` int(11) NOT NULL,
  `tm_parroquia_tm_municipio_tm_estado_id` int(11) NOT NULL,
  `tm_parroquia_tm_municipio_tm_estado_tm_pais_id` int(11) NOT NULL,
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de actualización del registro.',
  PRIMARY KEY (`id`,`tm_parroquia_tm_municipio_id`,`tm_parroquia_id`,`tm_parroquia_tm_municipio_tm_estado_id`,`tm_parroquia_tm_municipio_tm_estado_tm_pais_id`),
  KEY `fk_dt_direccion_entrega_dt_usuarios` (`dt_usuarios_id`),
  KEY `fk_direccion_entrega_tm_parroquia` (`tm_parroquia_id`,`tm_parroquia_tm_municipio_id`,`tm_parroquia_tm_municipio_tm_estado_id`,`tm_parroquia_tm_municipio_tm_estado_tm_pais_id`),
  CONSTRAINT `fk_direccion_entrega_tm_parroquia` FOREIGN KEY (`tm_parroquia_id`, `tm_parroquia_tm_municipio_id`, `tm_parroquia_tm_municipio_tm_estado_id`, `tm_parroquia_tm_municipio_tm_estado_tm_pais_id`) REFERENCES `tm_parroquia` (`id`, `tm_municipio_id`, `tm_municipio_tm_estado_id`, `tm_municipio_tm_estado_tm_pais_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_direccion_entrega_dt_usuarios` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_direccion_entrega`
--

LOCK TABLES `dt_direccion_entrega` WRITE;
/*!40000 ALTER TABLE `dt_direccion_entrega` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_direccion_entrega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_empresa`
--

DROP TABLE IF EXISTS `dt_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la empresa.',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del usuario al cual pertenece la empresa.',
  `strnombre_empresa` varchar(100) NOT NULL COMMENT 'Este campo almacena el nombre de la empresa.',
  `srtrif_empresa` varchar(10) DEFAULT NULL COMMENT 'Este campo almacena el Registro de Información Fiscal de la empresa.',
  `strdireccion` varchar(150) DEFAULT NULL COMMENT 'Este campo almacena la dirección de la empresa.',
  `strcodigo_postal` varchar(8) DEFAULT NULL COMMENT 'Este campo almacena el código postal de la empresa.',
  `strhorario_empresa` varchar(20) DEFAULT NULL COMMENT 'Este campo almacena el horario de la empresa.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro de la empresa.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización de los datos de la empresa.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `strnombre_empresa_UNIQUE` (`strnombre_empresa`),
  KEY `fk_dt_empresa_dt_usuarios` (`dt_usuarios_id`),
  CONSTRAINT `fk_dt_empresa_dt_usuarios` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_empresa`
--

LOCK TABLES `dt_empresa` WRITE;
/*!40000 ALTER TABLE `dt_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_entrada_inventario`
--

DROP TABLE IF EXISTS `dt_entrada_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_entrada_inventario` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla entrada al inventario.',
  `dt_empresa_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa a la cual se le hará entrada al inventario.',
  `datfecha_entrada` date NOT NULL COMMENT 'Este campo almacena la fecha de entrada al inventario.',
  `dpnmonto_subtotal` double DEFAULT NULL COMMENT 'Este campo almacena el monto subtotal de la entrada al inventario.',
  `dpnmonto_iva` double DEFAULT NULL COMMENT 'Este campo almacena el monto del Impuesto al Valor Agregado.',
  `dpnmonto` double DEFAULT NULL COMMENT 'Este campo almacena el monto total de la entrada al inventario.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del  registro.',
  `dtmfecha_actualización` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`dt_empresa_id`),
  KEY `dt_entrada_inventario_dt_empresa` (`dt_empresa_id`),
  CONSTRAINT `dt_entrada_inventario_dt_empresa` FOREIGN KEY (`dt_empresa_id`) REFERENCES `dt_empresa` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_entrada_inventario`
--

LOCK TABLES `dt_entrada_inventario` WRITE;
/*!40000 ALTER TABLE `dt_entrada_inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_entrada_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_eventos`
--

DROP TABLE IF EXISTS `dt_eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_eventos` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla eventos.',
  `stroperacion` varchar(10) NOT NULL COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_evento` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora del evento.',
  `strdescripcion` varchar(300) NOT NULL COMMENT 'Este campo almacena la descripción del evento',
  `strip_evento` varchar(15) NOT NULL COMMENT 'Este campo almacena la ip del evento registrado.',
  `struser_agent` varchar(250) NOT NULL COMMENT 'Este campo almacena de cual navegador web se realizó el evento.',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del usuario que realiza el evento.',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_eventos`
--

LOCK TABLES `dt_eventos` WRITE;
/*!40000 ALTER TABLE `dt_eventos` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_eventos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_factura`
--

DROP TABLE IF EXISTS `dt_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_factura` (
  `strnumero_factura` varchar(15) NOT NULL COMMENT 'Este campo almacena el número de factura.',
  `tm_moneda_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la moneda con la cual se realizo la compra.',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del usuario que realiza la compra.',
  `datfecha_factura` date DEFAULT NULL COMMENT 'Este campo almacena la fecha de la factura.',
  `intnumero_control` int(11) DEFAULT NULL COMMENT 'Este campo almacena el número de control de la factura.',
  `dt_empresa_id` int(11) DEFAULT NULL,
  `tb_estatus_id` int(11) NOT NULL,
  `dpmonto` double DEFAULT NULL COMMENT 'Este campo almacena el monto del producto a comprar.',
  `sgnmonto_iva` double DEFAULT NULL COMMENT 'Este campo almacena el monto del Impuesto al Valor Agregado de la factura.',
  `sgnmonto_total` double DEFAULT NULL COMMENT 'Este campo almacena el monto total de la factura.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación de la factura.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`strnumero_factura`,`dt_usuarios_id`),
  KEY `fk_dt_factura_tm_modena` (`tm_moneda_id`),
  KEY `fk_dt_factura_dt_usuarios_comprador` (`dt_usuarios_id`),
  KEY `fk_dt_factura_dt_empresa_ofertante` (`dt_empresa_id`),
  KEY `fk_dt_factura_tb_estatus` (`tb_estatus_id`),
  CONSTRAINT `fk_dt_factura_dt_empresa_ofertante` FOREIGN KEY (`dt_empresa_id`) REFERENCES `dt_empresa` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_factura_dt_usuarios_comprador` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_factura_tb_estatus` FOREIGN KEY (`tb_estatus_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_factura_tm_modena` FOREIGN KEY (`tm_moneda_id`) REFERENCES `tm_moneda` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_factura`
--

LOCK TABLES `dt_factura` WRITE;
/*!40000 ALTER TABLE `dt_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_guia`
--

DROP TABLE IF EXISTS `dt_guia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_guia` (
  `strguia_qr` varchar(60) NOT NULL COMMENT 'Este campo almacena el código QR de la guía.',
  `dt_pedido_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del pedido que esta relacionado a la guía.',
  `strnumero_tracking` varchar(20) NOT NULL COMMENT 'Este campo almacena el número del traking de la guía.',
  `tb_status_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del estatus.',
  `strpeso` varchar(5) DEFAULT NULL COMMENT 'Este campo almacena el peso del pedido.',
  `straltura` varchar(5) DEFAULT NULL COMMENT 'Este campo almacena la altura del pedido.',
  `blnasegurada` tinyint(4) DEFAULT '0' COMMENT 'Este campo almacena si el pedido esta asegurado.',
  `dpnmonto_asegurado` double DEFAULT NULL COMMENT 'Este campo almacena el monto de aseguramiento del pedido.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`strguia_qr`,`dt_pedido_id`),
  UNIQUE KEY `strnumero_tracking_UNIQUE` (`strnumero_tracking`),
  KEY `fk_dt_guia_dt_pedido` (`dt_pedido_id`),
  KEY `fk_dt_guia_tb_estatus` (`tb_status_id`),
  CONSTRAINT `fk_dt_guia_dt_pedido` FOREIGN KEY (`dt_pedido_id`) REFERENCES `dt_pedido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_guia_tb_estatus` FOREIGN KEY (`tb_status_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_guia`
--

LOCK TABLES `dt_guia` WRITE;
/*!40000 ALTER TABLE `dt_guia` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_guia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_instrumentos_pagos_usuario`
--

DROP TABLE IF EXISTS `dt_instrumentos_pagos_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_instrumentos_pagos_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla instrumentos de pagos.\n',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacenar el campo del identificador del usuario.',
  `strnumero_cuenta` varchar(45) NOT NULL COMMENT 'Este campo almacena el numero de cuenta, tarjeta de dédito o crédito del usuaurio.',
  `strcodigo_seguridad` varchar(3) DEFAULT NULL COMMENT 'Este campo almacena el código de seguridad de la tarjeta de débito o crétido.',
  `strfecha_vencimiento` varchar(5) DEFAULT NULL COMMENT 'Este campo almacena la fecha de vencimiento de la tarjeta de débito o crétido.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora  de creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `strnumero_cuenta_UNIQUE` (`strnumero_cuenta`),
  KEY `fk_dt_instrumentos_pagos_dt_usuario` (`dt_usuarios_id`),
  CONSTRAINT `fk_dt_instrumentos_pagos_dt_usuario` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_instrumentos_pagos_usuario`
--

LOCK TABLES `dt_instrumentos_pagos_usuario` WRITE;
/*!40000 ALTER TABLE `dt_instrumentos_pagos_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_instrumentos_pagos_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_inventario`
--

DROP TABLE IF EXISTS `dt_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_inventario` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla inventarios',
  `dt_productos_intumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el id del numero del producto de la tabla producto como llave foranea',
  `dt_productos_dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el id de la empresa a la cual pertenece el producto',
  `tb_estatus_id` int(11) NOT NULL COMMENT 'Este campo almacena el id del status de la tabla base estatus',
  `intstock` int(10) DEFAULT NULL COMMENT 'Este campo almacena el stock del articulo o la disponibilidad',
  `datfecha_inventario` date DEFAULT NULL COMMENT 'Este campo almacena  la fecha de inventario ',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creacion del registro',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`dt_productos_intumero_producto`,`dt_productos_dt_empresa_id_empresa`),
  KEY `fk_dt_inventario_dt_productos` (`dt_productos_intumero_producto`,`dt_productos_dt_empresa_id_empresa`),
  KEY `fk_st_inventario_tb_estatus` (`tb_estatus_id`),
  CONSTRAINT `fk_dt_inventario_dt_productos` FOREIGN KEY (`dt_productos_intumero_producto`, `dt_productos_dt_empresa_id_empresa`) REFERENCES `dt_productos` (`intumero_producto`, `dt_empresa_id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_st_inventario_tb_estatus` FOREIGN KEY (`tb_estatus_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_inventario`
--

LOCK TABLES `dt_inventario` WRITE;
/*!40000 ALTER TABLE `dt_inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_pedido`
--

DROP TABLE IF EXISTS `dt_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_pedido` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador, el mismo es un campo autoincrementado',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el id del usuario que realiza el pedido',
  `tb_status_id` int(11) NOT NULL COMMENT 'Este campo almacena el status del pedido',
  `dpnmonto_pedido` double NOT NULL COMMENT 'Este campo almacena el monto del pedido el cliente o usuario',
  `dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa a la cual se le realizo el pedido',
  `dpnmonto_iva` double DEFAULT NULL COMMENT 'Este campo almacena el monto del iva del pedido',
  `dpnmonto_total` double DEFAULT NULL COMMENT 'Este campo almacena el monto total del pedido.',
  `strdescripcion` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena la descripcion del pedido realizado',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`dt_usuarios_id`),
  KEY `fk_dt_pedido_dt_usuarios_comprador` (`dt_usuarios_id`),
  KEY `fk_dt_pedido_tb_estatus` (`tb_status_id`),
  KEY `fk_dt_pedido_dt_empresa` (`dt_empresa_id_empresa`),
  CONSTRAINT `fk_dt_pedido_dt_empresa` FOREIGN KEY (`dt_empresa_id_empresa`) REFERENCES `dt_empresa` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_pedido_dt_usuarios_comprador` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_pedido_tb_estatus` FOREIGN KEY (`tb_status_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_pedido`
--

LOCK TABLES `dt_pedido` WRITE;
/*!40000 ALTER TABLE `dt_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_productos`
--

DROP TABLE IF EXISTS `dt_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_productos` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla producto',
  `intumero_producto` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el número del producto',
  `dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa al cual pertenece el producto',
  `tm_unidades_medida_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la unidad de medida del producto',
  `tm_modelo_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del modelo del producto',
  `strnombre_producto` varchar(100) DEFAULT NULL COMMENT 'Este campo almacen el nombre del producto ',
  `dpnprecio_producto` double DEFAULT NULL COMMENT 'Este campo almacena el precio del prducto.',
  `tm_modelo_tm_marca_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la marca.',
  `tb_estatus_id` int(11) NOT NULL COMMENT 'Este campo almacena el identidicador del estatus del producto',
  `tm_subcategoria_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la subcategoria del producto',
  `tm_subcategoria_tm_categoria_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de  la categoria del producto.\n',
  `intcantidad` int(11) DEFAULT NULL COMMENT 'Este campo almacena la cantidad del producto.',
  `strfoto_producto` varchar(250) DEFAULT NULL,
  `tm_subcategoria_tm_categoria_tm_ramo_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del ramo del producto.',
  `dpnpunto_reorden` double DEFAULT NULL COMMENT 'Este campo almacena el punto de reorden del producto.',
  `intstock_minimo` int(11) DEFAULT NULL COMMENT 'Este campo almacena el stock minimo del producto.\n',
  `intstock_maximo` int(11) DEFAULT NULL COMMENT 'Este campo almacena el stock maximo del producto.\n',
  `dpnultimo_costo` double DEFAULT NULL COMMENT 'Este campo almacena el ultimo costo del producto.\n',
  `dtmfecha_vencimiento` date DEFAULT NULL COMMENT 'Este campo almacena la fecha de vencimiento.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de creación de actualización del registro.',
  PRIMARY KEY (`intumero_producto`,`dt_empresa_id_empresa`,`tm_modelo_id`,`tm_subcategoria_tm_categoria_tm_ramo_id`),
  UNIQUE KEY `strnumero_producto_UNIQUE` (`intumero_producto`),
  KEY `fk_dt_producto_dt_empresa` (`dt_empresa_id_empresa`),
  KEY `fk_dt_producto_tm_unidades_medida` (`tm_unidades_medida_id`),
  KEY `fk_dt_producto_tm_modelo` (`tm_modelo_id`,`tm_modelo_tm_marca_id`),
  KEY `fk_dt_producto_tb_estatus` (`tb_estatus_id`),
  KEY `fk_dt_producto_subcategoria` (`tm_subcategoria_id`,`tm_subcategoria_tm_categoria_id`),
  CONSTRAINT `fk_dt_producto_dt_empresa` FOREIGN KEY (`dt_empresa_id_empresa`) REFERENCES `dt_empresa` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_producto_subcategoria` FOREIGN KEY (`tm_subcategoria_id`, `tm_subcategoria_tm_categoria_id`) REFERENCES `tm_subcategoria` (`id`, `tm_categoria_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_producto_tb_estatus` FOREIGN KEY (`tb_estatus_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_producto_tm_modelo` FOREIGN KEY (`tm_modelo_id`, `tm_modelo_tm_marca_id`) REFERENCES `tm_modelo` (`id`, `tm_marca_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_producto_tm_unidades_medida` FOREIGN KEY (`tm_unidades_medida_id`) REFERENCES `tm_unidades_medida` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_productos`
--

LOCK TABLES `dt_productos` WRITE;
/*!40000 ALTER TABLE `dt_productos` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_rol`
--

DROP TABLE IF EXISTS `dt_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_rol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `strnombre_rol` varchar(45) NOT NULL COMMENT 'Este campo almacena el nombre del rol.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de creación del registro.',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_rol`
--

LOCK TABLES `dt_rol` WRITE;
/*!40000 ALTER TABLE `dt_rol` DISABLE KEYS */;
INSERT INTO `dt_rol` VALUES (1,'ADMINISTRADOR','2019-03-25 12:47:14'),(2,'FABRICANTE','2019-03-25 12:48:14'),(3,'PRODUCTOR','2019-03-25 12:51:25'),(4,'CLIENTE FINAL','2019-03-25 12:51:25'),(5,'REPARTIDOR','2019-04-10 00:35:27');
/*!40000 ALTER TABLE `dt_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_usuarios`
--

DROP TABLE IF EXISTS `dt_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el idnetificador de la tabla usuarios',
  `strcorreo_electronico` varchar(60) NOT NULL COMMENT 'Este campo almacena el correo electronico del usuario, el mismo servira como login para iniciar session\n',
  `strusuario` varchar(45) DEFAULT NULL,
  `strcontrasena` varchar(60) NOT NULL COMMENT 'Este campo almacena la contrasena del usuario\n',
  `strnombres` varchar(45) NOT NULL COMMENT 'Este campo almacena el nombre del usuario.',
  `strapellidos` varchar(45) NOT NULL COMMENT 'Este campo almacena los apellidos del usuario.',
  `strtelefono` varchar(15) DEFAULT NULL COMMENT 'Este campo almacena el número telefonico.',
  `tb_estatus_id` int(11) NOT NULL,
  `strcodigo_promocional` varchar(60) DEFAULT NULL,
  `token` varchar(8) DEFAULT NULL,
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `strcorreo_electronico_UNIQUE` (`strcorreo_electronico`),
  UNIQUE KEY `strusuario_UNIQUE` (`strusuario`),
  KEY `fk_dt_usuarios_tb_estatus` (`tb_estatus_id`),
  CONSTRAINT `fk_dt_usuarios_tb_estatus` FOREIGN KEY (`tb_estatus_id`) REFERENCES `tb_estatus` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_usuarios`
--

LOCK TABLES `dt_usuarios` WRITE;
/*!40000 ALTER TABLE `dt_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_usuarios_has_dt_roles`
--

DROP TABLE IF EXISTS `dt_usuarios_has_dt_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_usuarios_has_dt_roles` (
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del usuario.',
  `dt_roles_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del rol',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`dt_usuarios_id`,`dt_roles_id`),
  KEY `fk_dt_usuarios_has_dt_rol_dt_rol` (`dt_roles_id`),
  CONSTRAINT `fk_dt_usuarios_has_dt_rol_dt_rol` FOREIGN KEY (`dt_roles_id`) REFERENCES `dt_rol` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_dt_usuarios_has_dt_rol_dt_usuario` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_usuarios_has_dt_roles`
--

LOCK TABLES `dt_usuarios_has_dt_roles` WRITE;
/*!40000 ALTER TABLE `dt_usuarios_has_dt_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_usuarios_has_dt_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_valoracion_empresa`
--

DROP TABLE IF EXISTS `dt_valoracion_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_valoracion_empresa` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla valoración de la empresa.',
  `dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa a la cual se llevará el registro de valoración.',
  `blnvaloracion1` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 1 de la empresa.',
  `blnvaloracion2` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 2 de la empresa.',
  `blnvaloracion3` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 3 de la empresa.',
  `blnvaloracion4` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 4 de la empresa.',
  `blnvaloracion5` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 5 de la empresa.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora del registro de la valoración.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización de la valoración.',
  PRIMARY KEY (`id`,`dt_empresa_id_empresa`),
  KEY `fk_dt_valoracion_empresa` (`dt_empresa_id_empresa`),
  CONSTRAINT `fk_dt_valoracion_empresa` FOREIGN KEY (`dt_empresa_id_empresa`) REFERENCES `dt_empresa` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_valoracion_empresa`
--

LOCK TABLES `dt_valoracion_empresa` WRITE;
/*!40000 ALTER TABLE `dt_valoracion_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_valoracion_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_valoracion_producto`
--

DROP TABLE IF EXISTS `dt_valoracion_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_valoracion_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla valoración del producto.',
  `dt_productos_intumero_producto` int(11) NOT NULL COMMENT 'Este campo almacena el número del producto al cual será valorado.',
  `dt_productos_dt_empresa_id_empresa` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la empresa a la cual pertenece el producto.',
  `blnvaloracion1` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena  la valoración 1 del producto.',
  `blnvaloracion2` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 2 del producto.',
  `blnvaloracion3` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 3 del producto.',
  `blnvaloracion4` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 4 del producto.',
  `blnvaloracion5` tinyint(4) DEFAULT NULL COMMENT 'Este campo almacena la valoración 5 del producto.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`dt_productos_intumero_producto`,`dt_productos_dt_empresa_id_empresa`),
  KEY `fk_valoracion_producto_dt_producto` (`dt_productos_intumero_producto`,`dt_productos_dt_empresa_id_empresa`),
  CONSTRAINT `fk_valoracion_producto_dt_producto` FOREIGN KEY (`dt_productos_intumero_producto`, `dt_productos_dt_empresa_id_empresa`) REFERENCES `dt_productos` (`intumero_producto`, `dt_empresa_id_empresa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_valoracion_producto`
--

LOCK TABLES `dt_valoracion_producto` WRITE;
/*!40000 ALTER TABLE `dt_valoracion_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_valoracion_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dt_vehiculos`
--

DROP TABLE IF EXISTS `dt_vehiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dt_vehiculos` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla vehículos.',
  `dt_usuarios_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del usuario.',
  `strplaca` varchar(15) NOT NULL COMMENT 'Este campo almacena la placa del vehículo.',
  `strcolor` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena el color del vehículo.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de actualización del registro.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `strplaca_UNIQUE` (`strplaca`),
  KEY `fk_dt_vehiculos_dt_usuario` (`dt_usuarios_id`),
  CONSTRAINT `fk_dt_vehiculos_dt_usuario` FOREIGN KEY (`dt_usuarios_id`) REFERENCES `dt_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dt_vehiculos`
--

LOCK TABLES `dt_vehiculos` WRITE;
/*!40000 ALTER TABLE `dt_vehiculos` DISABLE KEYS */;
/*!40000 ALTER TABLE `dt_vehiculos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sys_log`
--

DROP TABLE IF EXISTS `sys_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(60) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `accion` varchar(15) NOT NULL,
  `sessionId` varchar(60) NOT NULL,
  `message` varchar(250) NOT NULL,
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sys_log`
--

LOCK TABLES `sys_log` WRITE;
/*!40000 ALTER TABLE `sys_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `sys_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_estatus`
--

DROP TABLE IF EXISTS `tb_estatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_estatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla estatus.',
  `intvalor` int(11) DEFAULT NULL COMMENT 'Este campo almacena el valor del status .',
  `strnombre_estatus` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena el nombre del estatus .',
  `strnombre_tabla` varchar(20) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la tabla a la cual hace referencia el estatus',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_estatus`
--

LOCK TABLES `tb_estatus` WRITE;
/*!40000 ALTER TABLE `tb_estatus` DISABLE KEYS */;
INSERT INTO `tb_estatus` VALUES (1,0,'INACTIVO','dt_usuarios','2019-03-31 07:12:33','2019-03-31 07:12:33'),(2,1,'INACTIVO','dt_usuarios','2019-03-31 07:12:52','2019-03-31 07:12:52');
/*!40000 ALTER TABLE `tb_estatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_banco`
--

DROP TABLE IF EXISTS `tm_banco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_banco` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `strcodigo_banco` varchar(4) DEFAULT NULL,
  `strnombre_banco` varchar(100) DEFAULT NULL,
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_banco`
--

LOCK TABLES `tm_banco` WRITE;
/*!40000 ALTER TABLE `tm_banco` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_banco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_categoria`
--

DROP TABLE IF EXISTS `tm_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identidicador de la tabla categoria.',
  `tm_ramo_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del ramo al cual pertenece la categoria.',
  `strnombre_categoria` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la categoria.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`tm_ramo_id`),
  KEY `fk_tm_categoria_tm_ramo` (`tm_ramo_id`),
  CONSTRAINT `fk_tm_categoria_tm_ramo` FOREIGN KEY (`tm_ramo_id`) REFERENCES `tm_ramo` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_categoria`
--

LOCK TABLES `tm_categoria` WRITE;
/*!40000 ALTER TABLE `tm_categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_ciudad`
--

DROP TABLE IF EXISTS `tm_ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_ciudad` (
  `id` int(11) NOT NULL,
  `strnombre_ciudad` varchar(100) DEFAULT NULL,
  `tm_estado_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del estado al cual pertenece la ciudad.',
  `tm_estado_tm_pais_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del país al cual pertenece la ciudad.',
  `stmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`tm_estado_id`,`tm_estado_tm_pais_id`),
  KEY `fk_tm_ciudad` (`tm_estado_id`,`tm_estado_tm_pais_id`),
  CONSTRAINT `fk_tm_ciudad` FOREIGN KEY (`tm_estado_id`, `tm_estado_tm_pais_id`) REFERENCES `tm_estado` (`id`, `tm_pais_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_ciudad`
--

LOCK TABLES `tm_ciudad` WRITE;
/*!40000 ALTER TABLE `tm_ciudad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_estado`
--

DROP TABLE IF EXISTS `tm_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_estado` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla estados.',
  `strnombre_estado` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena el nombre del estado.',
  `tm_pais_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del país al cual pertenece el estado.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`tm_pais_id`),
  KEY `fk_tm_estado_tm_pais` (`tm_pais_id`),
  CONSTRAINT `fk_tm_estado_tm_pais` FOREIGN KEY (`tm_pais_id`) REFERENCES `tm_pais` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_estado`
--

LOCK TABLES `tm_estado` WRITE;
/*!40000 ALTER TABLE `tm_estado` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_marca`
--

DROP TABLE IF EXISTS `tm_marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_marca` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla marca',
  `strnombre_marca` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la marca.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de la creación del registro de la marca.',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_marca`
--

LOCK TABLES `tm_marca` WRITE;
/*!40000 ALTER TABLE `tm_marca` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_modelo`
--

DROP TABLE IF EXISTS `tm_modelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_modelo` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla modelo.',
  `tm_marca_id` int(11) NOT NULL COMMENT 'Este campo almacena el id de la tabla marca como llave foranea.',
  `strnombre_modelo` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena el nombre del modelo.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación de los registros del modelo.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`tm_marca_id`),
  KEY `fk_tm_modelo_tm_marca` (`tm_marca_id`),
  CONSTRAINT `fk_tm_modelo_tm_marca` FOREIGN KEY (`tm_marca_id`) REFERENCES `tm_marca` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_modelo`
--

LOCK TABLES `tm_modelo` WRITE;
/*!40000 ALTER TABLE `tm_modelo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_modelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_moneda`
--

DROP TABLE IF EXISTS `tm_moneda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_moneda` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla moneda.',
  `strmoneda` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la moneda.',
  `strsiglas` varchar(4) DEFAULT NULL COMMENT 'Este campo almacena las sigles de la moneda.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `strsiglas_UNIQUE` (`strsiglas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_moneda`
--

LOCK TABLES `tm_moneda` WRITE;
/*!40000 ALTER TABLE `tm_moneda` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_moneda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_municipio`
--

DROP TABLE IF EXISTS `tm_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_municipio` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla municipio.',
  `strnombre_municipio` varchar(100) DEFAULT NULL COMMENT 'Este campo almacena el nombre del municipio.',
  `tm_estado_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del estado al cual pertenece el municipio,',
  `tm_estado_tm_pais_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del país al pertenece el municipio.',
  `tm_ciudad_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la ciudad a la cual pertenece el municipio.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`,`tm_estado_id`,`tm_estado_tm_pais_id`,`tm_ciudad_id`),
  KEY `fk_tm_municipio_tm_estado` (`tm_estado_id`,`tm_estado_tm_pais_id`),
  CONSTRAINT `fk_tm_municipio_tm_estado` FOREIGN KEY (`tm_estado_id`, `tm_estado_tm_pais_id`) REFERENCES `tm_estado` (`id`, `tm_pais_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_municipio`
--

LOCK TABLES `tm_municipio` WRITE;
/*!40000 ALTER TABLE `tm_municipio` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_pais`
--

DROP TABLE IF EXISTS `tm_pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_pais` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla país.',
  `strcodigo_pais` varchar(3) DEFAULT NULL COMMENT 'Este campo almacena el código del país.',
  `strnombre_pais` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena el nombre del país.',
  `strsiglas` varchar(3) DEFAULT NULL COMMENT 'Este campo almacena las siglas del país.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización del registro.',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_pais`
--

LOCK TABLES `tm_pais` WRITE;
/*!40000 ALTER TABLE `tm_pais` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_parroquia`
--

DROP TABLE IF EXISTS `tm_parroquia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_parroquia` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla parroquia.',
  `strnobre_parroquia` varchar(100) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la parroquia.',
  `tm_municipio_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del municipio al cual pertenece la parroquia.',
  `tm_municipio_tm_estado_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del estado al cual pertenece la parroquia.',
  `tm_municipio_tm_estado_tm_pais_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador del país al cual pertenece la parroquia.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de actualización del registro.',
  PRIMARY KEY (`id`,`tm_municipio_id`,`tm_municipio_tm_estado_id`,`tm_municipio_tm_estado_tm_pais_id`),
  KEY `fk_tm_parroquia_tm_municipio` (`tm_municipio_id`,`tm_municipio_tm_estado_id`,`tm_municipio_tm_estado_tm_pais_id`),
  CONSTRAINT `fk_tm_parroquia_tm_municipio` FOREIGN KEY (`tm_municipio_id`, `tm_municipio_tm_estado_id`, `tm_municipio_tm_estado_tm_pais_id`) REFERENCES `tm_municipio` (`id`, `tm_estado_id`, `tm_estado_tm_pais_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_parroquia`
--

LOCK TABLES `tm_parroquia` WRITE;
/*!40000 ALTER TABLE `tm_parroquia` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_parroquia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_ramo`
--

DROP TABLE IF EXISTS `tm_ramo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_ramo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla ramo.',
  `strnombre_ramo` varchar(150) DEFAULT NULL,
  `tb_estatus_id` int(11) NOT NULL,
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_ramo`
--

LOCK TABLES `tm_ramo` WRITE;
/*!40000 ALTER TABLE `tm_ramo` DISABLE KEYS */;
INSERT INTO `tm_ramo` VALUES (1,'MATERIAL, ACCESORIOS Y SUMINISTROS DE PLANTAS Y ANIMALES VIVOS',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(2,'MINERALES, TEXTILES Y MATERIALES NO COMESTIBLES DE PLANTAS Y ANIMALES',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(3,'PRODUCTOS QUIMICOS INCLUYENDO LOS BIO-QUIMICOS Y GASES INDUSTRIALES',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(4,'RESINA, COLOFONIA, CAUCHO, ESPUMA, PELICULA Y MATERIALES ELASTOMERICOS',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(5,'MATERIALES Y PRODUCTOS DE PAPEL',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(6,'COMBUSTIBLES, ADITIVOS PARA COMBUSTIBLES, LUBRICANTES Y MATERIALES ANTICORROSIVOS',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(7,'MAQUINARIA DE MINERIA Y PERFORACION DE POZOS Y ACCESORIOS',0,'2019-04-09 21:59:56','0000-00-00 00:00:00'),(8,'MAQUINARIA Y ACCESORIOS PARA AGRICULTURA, PESCA, SILVICULTURA Y FAUNA.',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(9,'MAQUINARIA Y ACCESORIOS PARA CONSTRUCCION Y EDIFICACION',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(10,'MAQUINARIA Y ACCESORIOS DE FABRICACION Y TRANSFORMACION INDUSTRIAL',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(11,'MAQUINARIA, ACCESORIOS Y SUMINISTROS PARA MANEJO, ACONDICIONAMIENTO Y ALMACENAMIENTO DE MATERIALES',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(12,'VEHICULOS COMERCIALES, MILITARES Y PARTICULARES, ACCESORIOS Y COMPONENTES',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(13,'MAQUINARIA Y ACCESORIOS PARA GENERACION Y DISTRIBUCION DE ENERGIA',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(14,'HERRAMIENTAS Y MAQUINARIA EN GENERAL',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(15,'COMPONENTES Y SUMINISTROS DE FABRICACION, ESTRUCTURAS, OBRAS Y CONSTRUCCIONES',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(16,'COMPONENTES Y SUMINISTROS DE FABRICACION',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(17,'COMPONENTES Y SUMINISTROS ELECTRONICOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(18,'SUMINISTROS, COMPONENTES Y ACCESORIOS ELECTRICOS Y DE ILUMINACION',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(19,'SISTEMAS, EQUIPOS Y COMPONENTES DE DISTRIBUCION Y ACONDICIONAMIENTO',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(20,'EQUIPO DE LABORATORIO, MEDIDA, OBSERVACION Y COMPROBACION',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(21,'EQUIPO, ACCESORIOS Y SUMINISTROS MEDICOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(22,'TELECOMUNICACIONES, RADIODIFUSION Y TECNOLOGIA DE LA INFORMACION',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(23,'EQUIPO, ACCESORIOS Y SUMINISTROS DE OFICINA',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(24,'EQUIPO Y SUMINISTROS DE IMPRENTA, FOTOGRAFICOS Y AUDIOVISUALES',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(25,'EQUIPOS Y SUMINISTROS DE DEFENSA, ORDEN PUBLICO, PROTECCION Y SEGURIDAD',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(26,'EQUIPO Y SUMINISTROS DE LIMPIEZA',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(27,'MAQUINARIA, EQUIPO Y SUMINISTROS PARA LA INDUSTRIA DE SERVICIOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(28,'EQUIPOS DEPORTIVOS, DE RECREO, SUMINISTROS Y ACCESORIOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(29,'ALIMENTOS, BEBIDAS Y TABACO',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(30,'MEDICAMENTOS Y PRODUCTOS FARMACEUTICOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(31,'MUEBLES, ACCESORIOS, ELECTRODOMESTICOS Y PRODUCTOS ELECTRONICOS DE CONSUMO',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(32,'ROPA, MALETAS Y PRODUCTOS DE TOCADOR',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(33,'PRODUCTOS PARA RELOJERIA, JOYERIA Y GEMAS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(34,'PRODUCTOS PUBLICADOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(35,'MUEBLES Y MOBILIARIOS',0,'2019-04-09 21:59:57','0000-00-00 00:00:00'),(36,'INSTRUMENTOS Y ARTES MUSICALES, JUEGOS, JUGUETES, EQUIPAMIENTO, MATERIAL, ACCESORIOS Y SUMINISTROS PARA EDUCACION',0,'2019-04-09 21:59:57','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `tm_ramo` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `ubiimarket_db`.`tg_ramo_actualizacion` AFTER UPDATE ON `tm_ramo` FOR EACH ROW
BEGIN
	UPDATE tm_ramo SET dtmfecha_actualizacion=now() WHERE id=NEW.ID;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `tm_subcategoria`
--

DROP TABLE IF EXISTS `tm_subcategoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_subcategoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Este campo almacena el identificador de la tabla subcategoria.',
  `tm_categoria_id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la categoria a la cual pertenece la subcategoria.',
  `tm_categoria_tm_ramo_id` int(11) NOT NULL,
  `strnombre_subcategoria` varchar(60) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la subcategoria.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la creación del registro.',
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha y hora de la actualización de los datos del registro.',
  PRIMARY KEY (`id`,`tm_categoria_id`,`tm_categoria_tm_ramo_id`),
  KEY `fk_subcategoria_tm_categoria` (`tm_categoria_id`,`tm_categoria_tm_ramo_id`),
  CONSTRAINT `fk_subcategoria_tm_categoria` FOREIGN KEY (`tm_categoria_id`, `tm_categoria_tm_ramo_id`) REFERENCES `tm_categoria` (`id`, `tm_ramo_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_subcategoria`
--

LOCK TABLES `tm_subcategoria` WRITE;
/*!40000 ALTER TABLE `tm_subcategoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_subcategoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tm_unidades_medida`
--

DROP TABLE IF EXISTS `tm_unidades_medida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tm_unidades_medida` (
  `id` int(11) NOT NULL COMMENT 'Este campo almacena el identificador de la tabla unidades de medidas.',
  `strnombre_medida` varchar(45) DEFAULT NULL COMMENT 'Este campo almacena el nombre de la unidad de medida.',
  `strsiglas` varchar(4) DEFAULT NULL COMMENT 'Este campo almacena las siglas de la unidad de medida.',
  `intcantidad` int(11) DEFAULT NULL COMMENT 'Este campo almacena la cantidad de la unidad de medida.',
  `dtmfecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dtmfecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Este campo almacena la fecha de la actualización de los datos de la unidad de medida.\\n',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tm_unidades_medida`
--

LOCK TABLES `tm_unidades_medida` WRITE;
/*!40000 ALTER TABLE `tm_unidades_medida` DISABLE KEYS */;
/*!40000 ALTER TABLE `tm_unidades_medida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ubiimarket_db'
--

--
-- Dumping routines for database 'ubiimarket_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-16 17:17:09
