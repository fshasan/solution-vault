select distinct city from station where (lower(city) like 'a%a') OR (lower(city) like 'a%e') OR
(lower(city) like 'a%i') OR (lower(city) like 'a%o') OR (lower(city) like 'a%u') OR

(lower(city) like 'e%a') OR (lower(city) like 'e%e') OR
(lower(city) like 'e%i') OR (lower(city) like 'e%o') OR (lower(city) like 'e%u') OR

(lower(city) like 'i%a') OR (lower(city) like 'i%e') OR
(lower(city) like 'i%i') OR (lower(city) like 'i%o') OR (lower(city) like 'i%u') OR

(lower(city) like 'o%a') OR (lower(city) like 'o%e') OR
(lower(city) like 'o%i') OR (lower(city) like 'o%o') OR (lower(city) like 'o%u') OR

(lower(city) like 'u%a') OR (lower(city) like 'u%e') OR
(lower(city) like 'u%i') OR (lower(city) like 'u%o') OR (lower(city) like 'u%u');