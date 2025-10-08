-- СТВОРЕННЯ ТАБЛИЦІ

CREATE TABLE ANIMALS (
	-- SERIAL -- ЧИСЛО АВТОМАТИЧНО ЗБІЛЬШУЄТЬСЯ НА 1
	-- PRIMARY KEY -- ВКАЗУЄМО ЩО ДАНИЙ СТОВПЧИК ЦЕ УНІКАЛЬНА ID(ПЕРВИННИЙ КЛЮЧ)
	ANIMAL_ID SERIAL PRIMARY KEY,
	
	-- НАЗВА СТОВПЧИКІВ ТА ЇХ ТИП ДАНИХ
	BREED VARCHAR(20),  -- ТИП ТЕКСТ НЕ БІЛЬШЕ 20 СИМВОЛІВ
	AGE INT,
	COLOR VARCHAR(40)  
);


-- ДОБАВИТИ ДАНІ В ТАБЛИЦЮ
INSERT INTO ANIMALS (
	-- ПЕРЕРАХУНОК СТОВПЧИКІВ ЯКІ ВИ ДОБАВИТЕ
	BREED,
	AGE,
	COLOR
)
VALUES 
	('КІТ', 2, 'РУДИЙ'),
	('ПЕС', 6, 'СІРИЙ')
