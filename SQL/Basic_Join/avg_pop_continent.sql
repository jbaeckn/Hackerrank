SELECT CO.continent, FLOOR(AVG(CI.population))
FROM Country as CO
INNER JOIN City as CI
ON CO.code=CI.countrycode
GROUP BY CO.continent;
