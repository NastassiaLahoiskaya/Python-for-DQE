import sqlite3


class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             news_msg TEXT, 
                             location TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS advertising 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             adv_message TEXT, 
                             actual_until TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS quiz 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             answer TEXT, 
                             conclusion TEXT)''')
        self.conn.commit()

    def insert_news(self, news):
        self.cursor.execute("INSERT INTO news (news_msg, location) VALUES (?, ?)", (news.news_msg, news.location))
        self.conn.commit()

    def insert_advertising(self, advertising):
        self.cursor.execute("INSERT INTO advertising (adv_message, actual_until) VALUES (?, ?)",
                            (advertising.adv_message, advertising.actual_until))
        self.conn.commit()

    def insert_quiz(self, quiz):
        self.cursor.execute("INSERT INTO quiz (answer, conclusion) VALUES (?, ?)", (quiz.answer, quiz.conclusion[0]))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def selecting_all_tables(self):

        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM news;")
        result = cursor.fetchall()
        print('"News" table:', result)
        cursor.execute("SELECT * FROM advertising;")
        result = cursor.fetchall()
        print('"Advertising" table:', result)
        cursor.execute("SELECT * FROM quiz;")
        result = cursor.fetchall()
        print('"Quiz" table:', result)

        cursor.close()
        conn.close()
