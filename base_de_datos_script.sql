-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Autor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`Bodega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Bodega` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`, `nombre`),
  UNIQUE INDEX `direccion_UNIQUE` (`direccion` ASC) VISIBLE,
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`ProductoTipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ProductoTipo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE,
  UNIQUE INDEX `idtipo_producto_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Producto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `producto_tipo_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `producto_tipo_id`),
  UNIQUE INDEX `idproducto_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_producto_tipo_producto1_idx` (`producto_tipo_id` ASC) VISIBLE,
  CONSTRAINT `fk_producto_tipo_producto1`
    FOREIGN KEY (`producto_tipo_id`)
    REFERENCES `mydb`.`ProductoTipo` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`BodegaInventario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`BodegaInventario` (
  `bodega_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`bodega_id`, `producto_id`),
  INDEX `fk_bodega_inventario_producto1_idx` (`producto_id` ASC) VISIBLE,
  INDEX `fk_bodega_inventario_bodega1_idx` (`bodega_id` ASC) VISIBLE,
  CONSTRAINT `fk_bodega_has_producto_bodega1`
    FOREIGN KEY (`bodega_id`)
    REFERENCES `mydb`.`Bodega` (`id`)
    ON DELETE RESTRICT,
  CONSTRAINT `fk_bodega_has_producto_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `mydb`.`Producto` (`id`)
    ON DELETE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`Editorial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Editorial` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `usuario_id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `contraseña` VARCHAR(32) NOT NULL,
  `fecha_creacion` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`usuario_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `create_time_UNIQUE` (`fecha_creacion` ASC) VISIBLE,
  UNIQUE INDEX `usuario_id_UNIQUE` (`usuario_id` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`Informe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Informe` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id_autor` INT NOT NULL,
  `bodega_id_origen` INT NOT NULL,
  `bodega_id_destino` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_informe_bodega_idx` (`bodega_id_origen` ASC) VISIBLE,
  INDEX `fk_informe_bodega1_idx` (`bodega_id_destino` ASC) VISIBLE,
  INDEX `fk_informe_usuario1_idx` (`usuario_id_autor` ASC) VISIBLE,
  CONSTRAINT `fk_informe_bodega`
    FOREIGN KEY (`bodega_id_origen`)
    REFERENCES `mydb`.`Bodega` (`id`),
  CONSTRAINT `fk_informe_bodega1`
    FOREIGN KEY (`bodega_id_destino`)
    REFERENCES `mydb`.`Bodega` (`id`),
  CONSTRAINT `fk_informe_usuario1`
    FOREIGN KEY (`usuario_id_autor`)
    REFERENCES `mydb`.`Usuario` (`usuario_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`InformeInventario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`InformeInventario` (
  `informe_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`informe_id`, `producto_id`),
  INDEX `fk_informe_has_producto_producto1_idx` (`producto_id` ASC) VISIBLE,
  INDEX `fk_informe_has_producto_informe1_idx` (`informe_id` ASC) VISIBLE,
  CONSTRAINT `fk_informe_inventario_informe1`
    FOREIGN KEY (`informe_id`)
    REFERENCES `mydb`.`Informe` (`id`),
  CONSTRAINT `fk_informe_inventario_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `mydb`.`Producto` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`ProductoAutor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ProductoAutor` (
  `producto_id` INT NOT NULL,
  `autor_id` INT NOT NULL,
  PRIMARY KEY (`producto_id`, `autor_id`),
  INDEX `fk_producto_has_autor_autor1_idx` (`autor_id` ASC) VISIBLE,
  INDEX `fk_producto_has_autor_producto1_idx` (`producto_id` ASC) VISIBLE,
  CONSTRAINT `fk_producto_has_autor_autor1`
    FOREIGN KEY (`autor_id`)
    REFERENCES `mydb`.`Autor` (`id`),
  CONSTRAINT `fk_producto_has_autor_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `mydb`.`Producto` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydb`.`ProductoEditorial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ProductoEditorial` (
  `producto_id` INT NOT NULL,
  `editorial_id` INT NOT NULL,
  PRIMARY KEY (`producto_id`, `editorial_id`),
  INDEX `fk_producto_has_editorial_editorial1_idx` (`editorial_id` ASC) VISIBLE,
  INDEX `fk_producto_has_editorial_producto1_idx` (`producto_id` ASC) VISIBLE,
  CONSTRAINT `fk_producto_has_editorial_editorial1`
    FOREIGN KEY (`editorial_id`)
    REFERENCES `mydb`.`Editorial` (`id`),
  CONSTRAINT `fk_producto_has_editorial_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `mydb`.`Producto` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
