import sqlite3
import pandas as pd


def create_dataframe(db_path):
	conn = sqlite3.connect(db_path)
	df = pd.read_sql_query("""SELECT
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
		FRvideos;""", conn)
	conn.close()
	return df
	
	
def test_create_dataframe(df):
	columns = list(df)
	row_count = len(df)
	key_check_row_count = len(df[['video_id','language']].drop_duplicates())
	if (row_count >= 10 
			and set(columns) == set(['video_id', 'category_id', 'language']) 
			and row_count == key_check_row_count):
		return True
	else:
		return False

# print set([1,4,2]) #== set([1,2,4])
	
print(test_create_dataframe(create_dataframe("/Users/slivelsberger/Documents/Personal/software_engineering_for_data_scientists/HW2/class.db")))
