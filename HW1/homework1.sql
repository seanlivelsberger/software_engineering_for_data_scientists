.open 'class.db'

SELECT
video_id
,category_id
,'us' AS language
	FROM
	USvideos
UNION ALL
SELECT
video_id
,category_id
,'de' AS language
	FROM
	DEvideos
UNION ALL
SELECT
video_id
,category_id
,'gb' AS language
	FROM
	GBvideos
UNION ALL
SELECT
video_id
,category_id
,'ca' AS language
	FROM
	CAvideos
UNION ALL
SELECT
video_id
,category_id
,'fr' AS language
	FROM
	FRvideos;
