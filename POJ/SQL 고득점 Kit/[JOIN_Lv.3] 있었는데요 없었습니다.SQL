-- 보호 시작일보다 입양일이 더 빠른 경우
-- JOIN 후 비교
SELECT ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS JOIN ANIMAL_OUTS USING(ANIMAL_ID)
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME ASC