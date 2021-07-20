WITH country_details AS 
(SELECT country_id, country_name
FROM soccer_country
WHERE country_name IN ('Germany')),

german_group_stage AS (SELECT play_stage, team_id, country_name, player_gk
FROM match_details
INNER JOIN country_details
ON match_details.team_id = country_details.country_id)

SELECT DISTINCT player_name, jersey_no, posi_to_play
FROM player_mast
INNER JOIN german_group_stage
ON german_group_stage.team_id = player_mast.team_id AND german_group_stage.player_gk = player_mast.player_id
WHERE posi_to_play IN ('GK') AND play_stage IN ('G');