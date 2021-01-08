CREATE DATABASE IF NOT EXISTS `gestor`;

CREATE TABLE IF NOT EXISTS `gestor`.`t_usuarios` (
    `id_usuario` INT(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
    `fechaNacimiento` DATE NULL,
    `email` VARCHAR(245) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
    `usuario` VARCHAR(245) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
    `password` TEXT CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
    `insert` DATETIME NOT NULL DEFAULT NOW()
) ENGINE=INNODB;

INSERT INTO `gestor`.`t_usuarios`(`nombre`, `fechaNacimiento`, `email`, `usuario`, `password`, `insert`) VALUES('Roldan', '1990-04-01', 'roldan@gmail.com', 'usuario1', SHA1(123456), NOW());