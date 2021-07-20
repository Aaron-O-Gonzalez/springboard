WITH max_penalty_shootout AS (SELECT match_no, penalty_score
FROM match_details
ORDER BY penalty_score DESC
LIMIT 1)

SELECT match_no, country_name
FROM goal_details
INNER JOIN max_penalty_shootout
USING (match_no)
INNER JOIN soccer_country
ON goal_details.team_id = soccer_country.country_id;