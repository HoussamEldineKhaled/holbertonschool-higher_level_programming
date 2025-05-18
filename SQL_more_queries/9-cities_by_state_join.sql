-- cities by state
SELECT cities.id, cities.name, states.name
FROM cities, states
INNER JOIN states ON cities.states_id = states.id
ORDER BY cities.id ASC;
