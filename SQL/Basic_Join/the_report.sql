SELECT CASE WHEN G.grade>=8 THEN S.name ELSE Null END, G.grade, S.marks
FROM students AS S
INNER JOIN grades AS G
ON S.marks >= G.min_mark AND S.marks <= G.max_mark
ORDER BY G.grade DESC, S.name;
