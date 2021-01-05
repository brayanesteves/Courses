CREATE DATABASE IF NOT EXISTS `bd_importar`;

# <PRODUCTO>
CREATE TABLE IF NOT EXISTS `bd_importar`.`producto` (
    `producto_id` VARCHAR(10) NOT NULL COMMENT 'producto_id (Producto: Identificación)',
    `producto_nombre` VARCHAR(50) NOT NULL COMMENT 'producto_nombre (Producto: Nombre)',        
    PRIMARY KEY (`producto_id`)
) ENGINE='InnoDB' DEFAULT CHARSET='utf8' COLLATE='utf8_bin' COMMENT='producto (Producto)';

CREATE PROCEDURE `SP_REGISTRAR_PERSONA`(IN PNOMBRES VARCHAR(50), IN PAPELLIDOS VARCHAR(50), IN PARCHIVO TEXT)
INSERT INTO `persona`(nombre, apellido, archivo) VALUES(PNOMBRES, PAPELLIDOS, PARCHIVO)
# </PRODUCTO>