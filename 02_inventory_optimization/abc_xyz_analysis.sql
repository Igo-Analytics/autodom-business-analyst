-- ABC-XYZ анализ запчастей
SELECT 
    Запчасть,
    SUM(Продажи) AS ОбщиеПродажи,
    CASE 
        WHEN SUM(Продажи) > 1000 THEN 'A'
        WHEN SUM(Продажи) > 500 THEN 'B'
        ELSE 'C'
    END AS Категория
FROM Запчасти
GROUP BY Запчасть;
