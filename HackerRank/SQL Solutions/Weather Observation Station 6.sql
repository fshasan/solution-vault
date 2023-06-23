select distinct city from station where (lower(city) LIKE 'a%') OR (lower(city) LIKE 'e%') OR
(lower(city) LIKE 'i%') OR (lower(city) LIKE 'o%') OR (lower(city) LIKE 'u%');