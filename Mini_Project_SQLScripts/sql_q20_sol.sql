WITH firsthalf_substitutions AS
(SELECT player_id
FROM player_in_out
WHERE in_out IN ('I') AND play_half IN (1) AND play_schedule IN ('NT'))


SELECT player_name, player_id 
FROM player_mast
INNER JOIN firsthalf_substitutions
USING(player_id);