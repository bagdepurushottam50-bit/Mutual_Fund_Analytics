
-- 1. Total Records
SELECT COUNT(*) FROM fact_nav;

-- 2. Average NAV
SELECT AVG(NAV) AS avg_nav FROM fact_nav;

-- 3. Maximum NAV
SELECT MAX(NAV) AS max_nav FROM fact_nav;

-- 4. Minimum NAV
SELECT MIN(NAV) AS min_nav FROM fact_nav;

-- 5. Top 10 NAV Funds
SELECT Scheme_Name, NAV
FROM fact_nav
ORDER BY NAV DESC
LIMIT 10;

-- 6. Unique Schemes
SELECT COUNT(DISTINCT Scheme_Code)
FROM fact_nav;

-- 7. NAV Greater Than 100
SELECT *
FROM fact_nav
WHERE NAV > 100;

-- 8. Scheme Wise Average NAV
SELECT Scheme_Name, AVG(NAV)
FROM fact_nav
GROUP BY Scheme_Name;

-- 9. Latest Date
SELECT MAX(Date)
FROM fact_nav;

-- 10. Records Per Date
SELECT Date, COUNT(*)
FROM fact_nav
GROUP BY Date;
