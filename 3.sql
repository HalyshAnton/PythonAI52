--вся таблиця
SELECT *
FROM ANIMALS;

--ДОБАВИТИ СТОВПЧИК ДО ІСНУЮЧОЇ ТАБЛИЦІ
--СТОВПЧИК З ДАТОЮ ВАКЦИНІЦІЇ
ALTER TABLE ANIMALS
ADD COLUMN LAST_VACCINE DATE DEFAULT '2025-10-11';


--В SELECT МОЖНУТЬ БУТИ ВИРАЗИ(МАТЕМАТИЧНІ І НЕ ТІЛЬКИ)
SELECT 10*AGE+5 AS TOTAL, AGE+ANIMAL_ID AS "AGE + ID(НАЗВА СТОВПИКА З ПРОПУСКАМИ)"
FROM ANIMALS;

SELECT LOWER(BREED) AS BREED, UPPER(COLOR) AS COLOR
FROM ANIMALS;


-- РЕГУЛЯРНІ ВИРАЗИ
-- МОВА ШАБЛОНІВ ДЛЯ STR РЯДКІВ(ПОЧИНАЄТЬСЯ З ..., МІСТИТЬ .., МІСТИ .. НЕ МЕНШЕ .. РАЗІВ, РЯДКИ ТИПУ DDDD-DD-DD)
-- _ -- ДОВІЛЬНИЙ СИМВОЛ
-- % -- ДОВІЛЬНА КІЛЬКІСТЬ ДОВІЛЬНИХ СИМВОЛІВ(ВКЛЮЧНО З 0)

-- ___   -- РЯДОК ДОВЖИНИ 3
-- А___  -- РЯДОК ДОВЖИНИ 4, ПОЧИНАЄТЬСЯ НА А
-- А%    -- ДОВІЛЬНИЙ РЯДОК ЩО ПОСИНЯЄТЬСЯ НА А
-- %А%   -- РЯДОК В ЯКОМУ Є ЛІТЕРА А

-- ЗАСТОСУВАТИ ШАБЛОН МОЖНА ЧЕРЕЗ LIKE
SELECT *
FROM ANIMALS
WHERE BREED LIKE '___';   -- ПОРОДА З 3 ЛІТЕР

SELECT *
FROM ANIMALS
WHERE COLOR LIKE '%і%';   -- КОЛІР МІСТИТЬ ЛІТЕРУ і

SELECT *
FROM ANIMALS
WHERE COLOR ILIKE '%і%';   -- ШАБЛОН НЕ ЧУТЛИВИЙ ДО РЕГІСТРУ


-- РОБОТА З ДАТОЮ
-- ЯК  ДАВНО ВАКЦИНУВАЛИСЬ
SELECT CURRENT_DATE - LAST_VACCINE
FROM ANIMALS;

-- ТЕЖ САМЕ ЧЕРЕЗ ФУНКЦІЮ AGE
SELECT AGE(LAST_VACCINE)
FROM ANIMALS;

-- ЯКОГО МІСЯЦЯ ТА ЧИСЛА ВІДБУЛАСЬ ВАКЦИНАЦІЯ
SELECT LAST_VACCINE, EXTRACT(MONTH FROM LAST_VACCINE) AS "MONTH", EXTRACT(DAY FROM LAST_VACCINE) AS "DAY"
FROM ANIMALS;

-- КОЛИ НАСТУПНА ВАКЦИНАЦІЯ(ЯКЩО ЇЇ ТРЕБА РОБИТИ РАЗ В ПІВРОКУ)
SELECT LAST_VACCINE, LAST_VACCINE + INTERVAL '6 MONTHS' AS NEXT_VACCINE
FROM ANIMALS;



--- ГРУПУВАННЯ
-- РОЗБИТТЯ ДАНИХ НА ГРУПИ ПО ОДНОМУ СТОВПЧИКУ ТА ОБРАХУНОК ПЕВНИХ ХАРАКТЕРИСТИК ПО ІНШИХ СТОВПЧИКАХ

-- КІЛЬКІСТЬ ТВАРИН КОЖНОГО ТИПУ
SELECT BREED, COUNT(*)   -- КІЛЬКІСТЬ РЯДКІВ У КОЖНІЙ ГРУПІ
FROM ANIMALS
GROUP BY BREED -- ЗГРУПУВАТИ ПО ПОРОДІ


SELECT LOWER(BREED), COUNT(*)  -- КІЛЬКІСТЬ РЯДКІВ У КОЖНІЙ ГРУПІ
FROM ANIMALS
GROUP BY LOWER(BREED) -- ЗГРУПУВАТИ ПО ПОРОДІ

-- АГРЕГАТНА ФУНКЦІЯ -- ФУНКЦІЯ ЯКА ОТРИМУЄ БАГАТО ПАРАТЕРІВ АЛЕ ПОВЕРТАЄ ОДИН РЕЗУЛЬТАТ
-- ПРИКЛАДИ: SUM, MIN, MAX, AVG, COUNT


-- ДЛЯ КОЖНОГО ТИПУ ТВАРИН ВИВЕСТИ КІЛЬКІСТЬ, МІНІМАЛЬНИЙ/МАКСИМАЛЬНІЙ/СЕРЕДНІЙ ВІК
SELECT BREED, MIN(AGE), MAX(AGE), AVG(AGE)
FROM ANIMALS
GROUP BY BREED;





