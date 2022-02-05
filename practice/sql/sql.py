import psycopg2

def create_db():
	
	conn = psycopg2.connect(dbname = "postgres")
	conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
	cursor = conn.cursor()
	database = "create database appi"
	cursor.execute(database)
	print("database created succesfully")
	conn.close()
	
if __name__ == "__main__":
	create_db()

