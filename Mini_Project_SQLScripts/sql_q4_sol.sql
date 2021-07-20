SELECT play_schedule, COUNT(*) as substitutions
FROM player_in_out
GROUP BY play_schedule;