SELECT COUNT(*) as bookings_during_stoppage_time
FROM player_booked
WHERE play_schedule IN ('ST');