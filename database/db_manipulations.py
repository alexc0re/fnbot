
from database.db_connection import DataBaseConnection

from fnAPI.fn_api import log
class UsersDB:

    def __init__(self):
        self.db_connection = DataBaseConnection("users.db")


    def update_order_number(self, user_id, username):
        query = "UPDATE users SET username = ? WHERE user_id = ?"
        self.db_connection.execute(query, username, user_id)
        self.db_connection.connection.commit()


    def process_user(self, user_id, username):
        if self.check_user_in_db(user_id):
            self.update_order_number(user_id, username)
        else:
            self.create_user_in_db(user_id, username)



    def create_user_in_db(self, user_id, username):
        if self.check_user_in_db(user_id) is False:
            self.db_connection.execute(
                f"INSERT INTO users (user_id, username) VALUES (?, ?)",
                user_id, username)

            self.db_connection.connection.commit()





    def check_user_in_db(self, user_id):
        query = "SELECT COUNT(*) FROM users WHERE user_id = ?"
        row = self.db_connection.fetchone(query, user_id)
        if row[0] == 0:
            print("User not found")
            return False
        else:
            print("User found")
            return True


    def get_user_order_number(self, user_id):
        query = "SELECT username FROM users WHERE user_id = ?"
        row = self.db_connection.fetchone(query, user_id)
        log.info(f'Username: {row}')
        log.info(type(row))

        return str(row[0])




if __name__ == '__main__':
    db = UsersDB()
    db.get_user_order_number('317014717')




