CREATE DATABASE IF NOT EXISTS `bd_grafico`;

# <PRODUCTO>
CREATE TABLE IF NOT EXISTS `bd_grafico`.`producto` (
    `id` INT(255) NOT NULL AUTO_INCREMENT COMMENT 'id (Identificación)',
    `producto_nombre` VARCHAR(50) NOT NULL COMMENT 'producto_nombre (Producto: Nombre)',
    `producto_stock` VARCHAR(50) NOT NULL COMMENT 'producto_stock (Producto: Stock)',
    PRIMARY KEY (`id`)
) ENGINE='InnoDB' DEFAULT CHARSET='utf8' COLLATE='utf8_bin' COMMENT='producto (Producto)';

INSERT INTO `bd_grafico`.`producto` VALUES(NULL, 'GASEOSA', 20);
INSERT INTO `bd_grafico`.`producto` VALUES(NULL, 'CHOCOLATES', 5);
INSERT INTO `bd_grafico`.`producto` VALUES(NULL, 'YOGURT', 10);
INSERT INTO `bd_grafico`.`producto` VALUES(NULL, 'SNACK', 3);
INSERT INTO `bd_grafico`.`producto` VALUES(NULL, 'ACEITE', 5);

CREATE PROCEDURE `SP_DATOSGRAFICOS_BAR`()
SELECT * FROM `producto`
# </PRODUCTO>

# <VENTA>
CREATE TABLE IF NOT EXISTS `bd_grafico`.`venta` (
    `venta_id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'venta_id (Venta: Identificación)',
    `producto_id` INT(11) NOT NULL COMMENT 'producto_id (Producto: Identificación)',
    `venta_cantidad` INT(255) NOT NULL COMMENT 'producto_stock (Producto: Stock)',
    `venta_feregistro` DATE NOT NULL COMMENT 'venta_feregistro (Venta: Fecha de Registro)',
    PRIMARY KEY (`venta_id`)
) ENGINE='InnoDB' DEFAULT CHARSET='utf8' COLLATE='utf8_bin' COMMENT='venta (Venta)';

INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 1, 10, "2019-05-05");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 1, 2,  "2020-05-11");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 6, 3,  "2020-05-22");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 8, 5,  "2020-05-22");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 8, 3,  "2020-05-22");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 4, 15, "2020-05-22");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 5, 15, "2020-05-22");
INSERT INTO `bd_grafico`.`venta` VALUES(NULL, 2, 30, "2019-05-22");

CREATE PROCEDURE `SP_DATOSGRAFICOS_PARAMETRO`(IN FECHAINICIO VARCHAR(10), IN FECHAFIN VARCHAR(10))
SELECT `producto`.`producto_nombre`, SUM(`venta`.`venta_cantidad`) AS `CANTIDAD` FROM `venta` INNER JOIN `producto` ON `venta`.`producto_id` = `producto`.`id` WHERE YEAR(`venta`.`venta_feregistro`) BETWEEN FECHAINICIO AND FECHAFIN GROUP BY `producto`.`id`
# </VENTA>