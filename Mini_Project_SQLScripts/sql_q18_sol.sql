SELECT match_no, COUNT(booking_time) as total_fouls
FROM player_booked
GROUP BY match_no
ORDER BY total_fouls DESC
LIMIT 1;
