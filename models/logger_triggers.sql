CREATE TRIGGER IF NOT EXISTS logger_user_delete
AFTER DELETE
ON user
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("BORRAR", "USUARIO", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_user_insert
AFTER INSERT
ON user
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("INSERTAR", "USUARIO", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_user_update
AFTER UPDATE
ON user
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("ACTUALIZAR", "USUARIO", date(julianday('now')),
	time(julianday('now')) ); 
END;
-----------------------------

CREATE TRIGGER IF NOT EXISTS logger_harvest_delete
AFTER DELETE
ON harvest
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("BORRAR", "COSECHA", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_harvest_insert
AFTER INSERT
ON harvest
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("INSERTAR", "COSECHA", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_harvest_update
AFTER UPDATE
ON harvest
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("ACTUALIZAR", "COSECHA", date(julianday('now')),
	time(julianday('now')) ); 
END;

--------------------------------------
CREATE TRIGGER IF NOT EXISTS logger_productor_delete
AFTER DELETE
ON productor
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("BORRAR", "RECOLECTOR", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_productor_insert
AFTER INSERT
ON productor
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("INSERTAR", "RECOLECTOR", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_productor_update
AFTER UPDATE
ON productor
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("ACTUALIZAR", "RECOLECTOR", date(julianday('now')),
	time(julianday('now')) ); 
END;

-------------------------------------------
CREATE TRIGGER IF NOT EXISTS logger_productor_type_delete
AFTER DELETE
ON productor_type
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("BORRAR", "TIPO RECOLECTOR", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_productor_type_insert
AFTER INSERT
ON productor_type
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("INSERTAR", "TIPO RECOLECTOR", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_productor_type_update
AFTER UPDATE
ON productor_type
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("ACTUALIZAR", "TIPO RECOLECTOR", date(julianday('now')),
	time(julianday('now')) ); 
END;

-------------------------------------------------------
CREATE TRIGGER IF NOT EXISTS logger_purchase_delete
AFTER DELETE
ON purchase
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("BORRAR", "COMPRAS", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_purchase_insert
AFTER INSERT
ON purchase
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("INSERTAR", "COMPRAS", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_purchase_update
AFTER UPDATE
ON purchase
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("ACTUALIZAR", "COMPRAS", date(julianday('now')),
	time(julianday('now')) ); 
END;

----------------------------------
CREATE TRIGGER IF NOT EXISTS logger_user_rol_delete
AFTER DELETE
ON user_rol
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("BORRAR", "ROL USUARIO", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_user_rol_insert
AFTER INSERT
ON user_rol
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("INSERTAR", "ROL USUARIO", date(julianday('now')),
	time(julianday('now')) ); 
END;

CREATE TRIGGER IF NOT EXISTS logger_user_rol_update
AFTER UPDATE
ON user_rol
BEGIN
	INSERT INTO logger (event, module, date, time)
	VALUES ("ACTUALIZAR", "ROL USUARIO", date(julianday('now')),
	time(julianday('now')) ); 
END;