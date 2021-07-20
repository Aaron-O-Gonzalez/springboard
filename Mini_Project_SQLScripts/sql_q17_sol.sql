 SELECT country_name, COUNT(ass_ref_id) as assistant_ref_counts
 FROM asst_referee_mast
 INNER JOIN soccer_country
 USING(country_id)
 GROUP BY country_name 
 ORDER BY assistant_ref_counts DESC
 LIMIT 1;