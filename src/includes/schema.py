import settings

from includes.db import Db

class Schema:

	def CreateDatabase():

		return Db.ExecuteQuery(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci",None,True,True)

	def CreateTables():
		
		#####################################################################################################
		query = """
			CREATE TABLE IF NOT EXISTS service_logs (
				log_id VARCHAR(45) PRIMARY KEY NOT NULL,
				service VARCHAR(45) NOT NULL,
				endpoint VARCHAR(150) NOT NULL,
				request LONGTEXT DEFAULT NULL,
				response LONGTEXT NOT NULL,
				reviewed BOOLEAN DEFAULT '0',
				date DATETIME NOT NULL
			) ENGINE=INNODB;
		"""

		if not Db.ExecuteQuery(query,None,True):
			return False

		Db.ExecuteQuery("ALTER TABLE service_logs ADD INDEX service (service);",None,True)
		Db.ExecuteQuery("ALTER TABLE service_logs ADD INDEX endpoint (endpoint);",None,True)
		Db.ExecuteQuery("ALTER TABLE service_logs ADD INDEX reviewed (reviewed);",None,True)
		Db.ExecuteQuery("ALTER TABLE service_logs ADD INDEX date (date);",None,True)
		#####################################################################################################

		#####################################################################################################
		query = """
			CREATE TABLE IF NOT EXISTS exception_logs (
				log_id VARCHAR(45) PRIMARY KEY NOT NULL,
				service VARCHAR(45) NOT NULL,
				method VARCHAR(150) NOT NULL,
				exception LONGTEXT DEFAULT NULL,
				comments LONGTEXT DEFAULT NULL,
				payload JSON DEFAULT NULL,
				reviewed BOOLEAN DEFAULT '0',
				date DATETIME NOT NULL
			) ENGINE=INNODB;
		"""

		if not Db.ExecuteQuery(query,None,True):
			return False

		Db.ExecuteQuery("ALTER TABLE exception_logs ADD INDEX service (service);",None,True)
		Db.ExecuteQuery("ALTER TABLE exception_logs ADD INDEX method (method);",None,True)
		Db.ExecuteQuery("ALTER TABLE exception_logs ADD INDEX reviewed (reviewed);",None,True)
		Db.ExecuteQuery("ALTER TABLE exception_logs ADD INDEX date (date);",None,True)
		#####################################################################################################

		return True