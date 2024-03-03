-- 코드를 입력하세요
-- 2022-10-16에 대여중인 건 START_DATE <
-- 한 CAR_ID가 여러번 대여된 경우가 있음..
-- 한 CAR_ID에 대해 대여중이 있으면 대여가능은 없어야함
-- 일단 나중에 좀 더 풀어보자고..


SELECT CAR_ID,
    IF(START_DATE <= "2022-10-16" AND "2022-10-16" <= END_DATE, "대여중", "대여 가능") AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
