from sqlalchemy import text

class Schema:

    @staticmethod
    def init(engine):
        with engine.connect() as conn:
            conn.execute(text('''
                CREATE TABLE IF NOT EXISTS users(
                    uid VARCHAR(100) PRIMARY KEY,
                    login VARCHAR(100) UNIQUE NOT NULL,
                    password_hash VARCHAR (255) NOT NULL
                )''')
            )
            conn.execute(text('''
                CREATE TABLE IF NOT EXISTS games(
                    uid VARCHAR(100) PRIMARY KEY,
                    field VARCHAR[9],
                    player_o_id VARCHAR(100),
                    player_x_id VARCHAR(100),
                    winner_id VARCHAR(100),
                    status VARCHAR(50) DEFAULT 'waiting',  -- waiting, in_progress, finished
                    created_at TIMESTAMP DEFAULT NOW()
                )''')
            )
            conn.commit()

