import sqlite3

class Database:
    db_name = "database.db"
    
    def __init__(self):
        sql = """create table if not exists Teacher
             (TeacherID integer,
             Teachername text,
             primary key(TeacherID))"""
        self.execute_sql(sql)
        sql = """create table if not exists Student
             (StudentID integer,
             Studentname text,
             primary key(StudentID))"""
        self.execute_sql(sql)
        
    def execute_sql(self, sql):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()

    def create_data(self):
        sql = """insert into Teacher (TeacherID, Teachername) values (1, 'Dave')"""
        self.execute_sql(sql)

if __name__ == "__main__":
    mydatabase = Database()
    mydatabase.create_data()
