CREATE DATABASE IF NOT EXISTS `bd_persona`;

# <PERSONA>
CREATE TABLE IF NOT EXISTS `bd_persona`.`persona` (
    `id` INT(255) NOT NULL AUTO_INCREMENT COMMENT 'id (Identificación)',
    `nombre` VARCHAR(50) NOT NULL COMMENT 'nombre (Nombre)',
    `apellido` VARCHAR(50) NOT NULL COMMENT 'apellido (Apellido)',
    `archivo` TEXT NOT NULL COMMENT 'archivo (Archivo)',    
    PRIMARY KEY (`id`)
) ENGINE='InnoDB' DEFAULT CHARSET='utf8' COLLATE='utf8_bin' COMMENT='persona (Persona)';

CREATE PROCEDURE `SP_REGISTRAR_PERSONA`(IN PNOMBRES VARCHAR(50), IN PAPELLIDOS VARCHAR(50), IN PARCHIVO TEXT)
INSERT INTO `persona`(nombre, apellido, archivo) VALUES(PNOMBRES, PAPELLIDOS, PARCHIVO)
# </PERSONA>