select distinct city from station where not ((lower(city) like '%a') OR
(lower(city) like '%e') OR
(lower(city) like '%i') OR
(lower(city) like '%o') OR
(lower(city) like '%u') OR
(lower(city) like '%A') OR
(lower(city) like '%E') OR
(lower(city) like '%I') OR
(lower(city) like '%O') OR
(lower(city) like '%U')) ;