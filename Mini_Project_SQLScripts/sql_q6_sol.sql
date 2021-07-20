SELECT COUNT(*)
FROM soccer_team
INNER JOIN (SELECT team_id FROM match_details
WHERE decided_by IN ('N')) as match_no_penalty_shootout
USING(team_id)
WHERE ABS(goal_diff) =1;