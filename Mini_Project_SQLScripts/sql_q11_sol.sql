WITH country_details AS 
(SELECT country_id, country_name
FROM soccer_country
WHERE country_name IN ('England'))

SELECT player_name, jersey_no, playing_club
FROM player_mast
INNER JOIN country_details
ON country_details.country_id = player_mast.team_id
WHERE posi_to_play IN ('GK');