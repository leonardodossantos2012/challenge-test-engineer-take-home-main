import sqlite3

class Database:
    def __init__(self, db_name="test_results.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        """Creates a table in the database to store test results."""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                image_id TEXT, 
                defect_detected BOOLEAN,
                with_defect BOOLEAN,
                low_lighting BOOLEAN
            )
        ''')
        self.conn.commit()

    def log_result(self, image_id, defect_detected, with_defect, low_lighting):
        """Logs the test result in the database."""
        self.conn.execute('''
            INSERT INTO results (image_id, defect_detected, with_defect, low_lighting) VALUES (?, ?, ?, ?)
        ''', (image_id, defect_detected, with_defect, low_lighting))
        self.conn.commit()

    def close(self):
        """Closes the database connection."""
        self.conn.close()
