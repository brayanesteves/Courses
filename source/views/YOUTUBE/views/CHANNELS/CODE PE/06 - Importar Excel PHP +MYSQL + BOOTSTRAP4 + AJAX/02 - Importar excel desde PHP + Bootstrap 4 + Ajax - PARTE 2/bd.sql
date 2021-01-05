CREATE DATABASE IF NOT EXISTS `bd_importar`;

# <PRODUCTO>
CREATE TABLE IF NOT EXISTS `bd_importar`.`producto` (
    `producto_id` VARCHAR(10) NOT NULL COMMENT 'producto_id (Producto: Identificación)',
    `producto_nombre` VARCHAR(50) NOT NULL COMMENT 'producto_nombre (Producto: Nombre)',        
    PRIMARY KEY (`producto_id`)
) ENGINE='InnoDB' DEFAULT CHARSET='utf8' COLLATE='utf8_bin' COMMENT='producto (Producto)';

CREATE PROCEDURE `PA_REGISTRAR_PRODUCTO_EXCEL`(IN IDPRODUCTO VARCHAR(10), IN PRODUCTO VARCHAR(50))
INSERT INTO `producto`(producto_id, producto_nombre) VALUES(IDPRODUCTO, PRODUCTO)
# </PRODUCTO>