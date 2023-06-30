-- Lists all cities by state
SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id;