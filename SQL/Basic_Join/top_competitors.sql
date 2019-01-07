SELECT S.hacker_id, H.name
FROM submissions AS S
INNER JOIN challenges AS C ON S.challenge_id=C.challenge_id
INNER JOIN difficulty AS D ON C.difficulty_level=D.difficulty_level
INNER JOIN hackers AS H ON S.hacker_id=H.hacker_id
WHERE S.score=D.score
GROUP BY S.hacker_id, H.name
HAVING COUNT(S.hacker_id)>1
ORDER BY COUNT(S.hacker_id) DESC, S.hacker_id;
