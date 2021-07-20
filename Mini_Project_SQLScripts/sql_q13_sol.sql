SELECT player_name, posi_to_play
FROM player_mast
INNER JOIN goal_details
USING (player_id)
WHERE posi_to_play IN ('DF');