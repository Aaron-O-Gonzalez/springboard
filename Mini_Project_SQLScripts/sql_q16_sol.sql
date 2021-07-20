WITH venue_details AS(
SELECT venue_name, match_no, referee_id 
FROM soccer_venue
INNER JOIN match_mast
USING(venue_id))

SELECT venue_name, referee_name, COUNT(match_no) as number_of_matches 
FROM referee_mast
INNER JOIN venue_details
USING(referee_id)
GROUP BY referee_name, venue_name;  