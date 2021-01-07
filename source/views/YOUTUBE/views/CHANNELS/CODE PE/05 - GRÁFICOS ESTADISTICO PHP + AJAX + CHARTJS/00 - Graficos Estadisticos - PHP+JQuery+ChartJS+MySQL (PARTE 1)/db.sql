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