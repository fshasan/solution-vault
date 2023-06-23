select distinct city from station where (lower(city) like '%a') OR (lower(city) like '%e') OR 
(lower(city) like '%i') OR (lower(city) like '%o') OR (lower(city) like '%u')