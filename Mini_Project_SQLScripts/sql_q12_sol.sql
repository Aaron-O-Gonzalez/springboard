WITH country_details AS
(SELECT country_id, country_name
FROM soccer_country)

SELECT COUNT(goal_id) as total_goals, posi_to_play, country_name
FROM player_mast
INNER JOIN goal_details
USING (player_id)
INNER JOIN country_details
ON country_details.country_id = player_mast.team_id
GROUP BY posi_to_play, country_name;