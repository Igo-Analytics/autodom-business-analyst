-- Анализ KPI дилерских центров
WITH SalesData AS (
    SELECT 
        ДЦ,
        SUM(Выручка) AS ОбщаяВыручка,
        COUNT(*) AS КоличествоСделок
    FROM Продажи
    WHERE Год = 2024
    GROUP BY ДЦ
)
SELECT 
    ДЦ,
    ОбщаяВыручка,
    КоличествоСделок,
    ОбщаяВыручка / КоличествоСделок AS СреднийЧек,
    RANK() OVER(ORDER BY ОбщаяВыручка DESC) AS Ранг
FROM SalesData
ORDER BY ОбщаяВыручка DESC;
