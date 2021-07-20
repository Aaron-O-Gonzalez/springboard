SELECT referee_name, COUNT(booking_time) as total_bookings
FROM referee_mast
INNER JOIN match_mast
USING(referee_id)
INNER JOIN player_booked
USING(match_no)
GROUP BY referee_name
ORDER BY total_bookings DESC
LIMIT 1;