SELECT COUNT(*) as goalkeeper_team_captains_count FROM
(SELECT player_id, player_name
FROM player_mast
INNER JOIN match_captain
ON match_captain.player_captain = player_mast.player_id
WHERE player_mast.posi_to_play IN ('GK')) as goalkeeper_captains;