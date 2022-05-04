CREATE VIEW grouped_meeting_joins AS
SELECT m.id AS meeting_id,
       m.name AS meeting_name,
	   COUNT(m.id) AS times_meeting_joined
FROM meetings m
JOIN meeting_joins mj ON mj.meeting_id = m.id
GROUP BY m.id