from sqlalchemy import text

class Schema:

    @staticmethod
    def init(engine):
        with engine.connect() as conn:
            conn.execute(text('''
                CREATE TABLE IF NOT EXISTS users(
                    id VARCHAR(100) PRIMARY KEY,
                    login VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR (255) NOT NULL
                )''')
            )
            conn.execute(text('''
                CREATE TABLE IF NOT EXISTS games(
                    id VARCHAR(100) PRIMARY KEY,
                    field VARCHAR[9],
                    player_o_id VARCHAR(100),
                    player_x_id VARCHAR(100),
                    winner_id VARCHAR(100)
                )''')
            )
            conn.commit()

