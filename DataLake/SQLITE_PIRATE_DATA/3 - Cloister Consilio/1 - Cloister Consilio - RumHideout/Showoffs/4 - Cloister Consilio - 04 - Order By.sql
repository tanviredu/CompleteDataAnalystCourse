SELECT BELONGSTO,
       COUNT(*) AS BARRELS 
FROM RUMHIDEOUT 
GROUP BY BELONGSTO
ORDER BY BARRELS ASC