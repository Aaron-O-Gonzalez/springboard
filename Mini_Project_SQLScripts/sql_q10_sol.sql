WITH country_details AS 
(SELECT country_name, country_id 
FROM soccer_country
WHERE country_name IN ('England'))

SELECT * FROM player_mast
INNER JOIN country_details
ON country_details.country_id = player_mast.team_id
WHERE playing_club IN ('Liverpool');