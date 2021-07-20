SELECT venue_id, venue_name
FROM soccer_venue
INNER JOIN (SELECT venue_id, decided_by
			FROM match_mast
            WHERE decided_by IN ('P')) as venues_shootout
USING (venue_id);