SELECT c.name
FROM city AS c
INNER JOIN country AS coun
ON c.countrycode=coun.code
WHERE coun.continent='Africa';
