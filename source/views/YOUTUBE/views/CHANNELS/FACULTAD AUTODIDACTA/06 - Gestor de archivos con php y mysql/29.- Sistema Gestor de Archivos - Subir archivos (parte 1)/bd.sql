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

CREATE TABLE IF NOT EXISTS `gestor`.`t_categorias` (
    `id_categoria` INT(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_usuario` INT(255) NOT NULL,
    `nombre` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
    `fechaInsert` DATETIME NOT NULL DEFAULT NOW()
) ENGINE=INNODB;

# LLAVE FORANEA DE `id_usuario`
ALTER TABLE `gestor`.`t_categorias`
ADD INDEX `fkCategoriaUsuario_idx`(`id_usuario` ASC);

ALTER TABLE `gestor`.`t_categorias`
ADD CONSTRAINT `fkCategoriaUsuario`
    FOREIGN KEY(`id_usuario`)
    REFERENCES `gestor`.`t_usuarios`(`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

CREATE TABLE IF NOT EXISTS `gestor`.`t_archivos` (
    `id_archivo` INT(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_categoria` INT(255) NOT NULL,
    `nombre` INT(255) NOT NULL,
    `tipo` VARCHAR(255) NOT NULL,
    `fecha` DATETIME NOT NULL DEFAULT NOW(),
    `ruta` TEXT NOT NULL        
) ENGINE=INNODB;

# LLAVE FORANEA DE `t_archivos` => `id_categoria`
ALTER TABLE `gestor`.`t_archivos`
ADD INDEX `fkArchivosCategorias_idx`(`id_categoria` ASC);

ALTER TABLE `gestor`.`t_archivos`
ADD CONSTRAINT `fkArchivosCategorias`
    FOREIGN KEY(`id_categoria`)
    REFERENCES `gestor`.`t_categorias`(`id_categoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

# AGREGAR NUEVO CAMPO
ALTER TABLE `gestor`.`t_archivos`
ADD COLUMN `id_usuario` INT NOT NULL AFTER `id_archivo`;

# LLAVE FORANEA DE `t_archivos` => `id_usuario`
ALTER TABLE `gestor`.`t_archivos`
ADD INDEX `fkUsuariosArchivos_idx`(`id_usuario` ASC);

ALTER TABLE `gestor`.`t_archivos`
ADD CONSTRAINT `fkUsuariosArchivos`
    FOREIGN KEY(`id_usuario`)
    REFERENCES `gestor`.`t_categorias`(`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;