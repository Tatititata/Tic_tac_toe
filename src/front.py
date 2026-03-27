from domain.model.game_field import GameField
import requests
import base64

BASE_URL = "http://127.0.0.1:5000"

def register(login, password):
    resp = requests.post(f"{BASE_URL}/auth/register", json={"login": login, "password": password})
    if resp.status_code == 201:
        print("Registered:", resp.json()["id"])
    else:
        print("Error:", resp.json()["error"])

def login(login, password):
    auth = base64.b64encode(f"{login}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    resp = requests.post(f"{BASE_URL}/auth/login", headers=headers)
    if resp.status_code == 200:
        user_id = resp.json()["id"]
        print("Logged in:", user_id)
        return user_id
    else:
        print("Login error:", resp.json()["error"])
        return None

def create_game(login, password, type='bot'):
    auth = base64.b64encode(f"{login}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    resp = requests.post(f"{BASE_URL}/game", json={"type": type}, headers=headers)
    if resp.status_code == 201:
        game = resp.json()
        print("Game created:", game["uid"])
        print(GameField.from_list(game['field']))
        return game["uid"]
    else:
        print("Error:", resp.json().get("error", resp.text))
        return None

def make_move(game_id, move, login, password):
    auth = base64.b64encode(f"{login}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    resp = requests.post(f"{BASE_URL}/{game_id}", json={"move": move}, headers=headers)
    if resp.status_code == 200:
        game = resp.json()
        print(GameField.from_list(game['field']))
        print("Status:", game["status"])
        print('Winner: ', game['winner_id'])
        return game
    else:
        print("Error:", resp.json().get("error", resp.text))
        return None

def check_available(user_login, user_password):
    auth = base64.b64encode(f"{user_login}:{user_password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    resp = requests.get(f"{BASE_URL}/games/available", headers=headers)
    if resp.status_code == 200:
        games = resp.json()
        return [[g['uid'], g['status']] for g in games]
    else:
        print("Error:", resp.json().get("error", resp.text))
        return []
    
def user_info(user_login, user_password):
    pass

def join_game(user_login, user_password, game_id):
    auth = base64.b64encode(f"{user_login}:{user_password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    resp = requests.post(f"{BASE_URL}/{game_id}/join", headers=headers)
    if resp.status_code == 200:
        game = resp.json()
        print("Game created:", game["uid"])
        print(GameField.from_list(game['field']))
        return game["uid"]
    else:
        print("Error:", resp.json().get("error", resp.text))
        return None


def front():
    print("=== Tic-Tac-Toe Console Client ===")
    user_login = None
    user_password = None
    games = []
    string = '''
    1. Register
    2. Check available games
    3. User info
    4. Play game
    5. Login
    6. Create game
    q to quit:
    '''

    while True:
        choice = input(string)
        if choice == '1':
            user_login = input("Login: ")
            user_password = input("Password: ")
            register(user_login, user_password)
        elif choice == '2':
            games = check_available(user_login, user_password)
            print(*games, sep='\n')
        elif choice == '3':
            user = user_info(user_login, user_password)
            print(user)
        elif choice == '4':
            if not games:
                games = check_available(user_login, user_password)
            for idx, g in enumerate(games):
                print(f'{idx}. {g}')
            try:
                num = int(input("Choose game number: "))
                game_id = join_game(user_login, user_password, games[num][0])
                print(game_id)
                while True:
                    move = input("Enter move (1-9) or q to quit: ")
                    if move == 'q':
                        break
                    try:
                        move = int(move)
                        if 0 < move < 10:
                            make_move(game_id, move, user_login, user_password)
                        else:
                            print("Invalid move")
                    except ValueError:
                        print("Invalid input")
            except:
                print("Invalid number")
        elif choice == 'q':
            break
        elif choice == '5':
            user_login = input("Login: ")
            user_password = input("Password: ")
            login(user_login, user_password)
        elif choice == '6':
            type = input("1 = human, 2 = bot")
            if type == '1':
                type = 'human'
            else:
                type = 'bot'
            game_id = create_game(user_login, user_password, type)
            print(game_id)
            while True:
                move = input("Enter move (1-9) or q to quit: ")
                if move == 'q':
                    break
                try:
                    move = int(move)
                    if 0 < move < 10:
                        make_move(game_id, move, user_login, user_password)
                    else:
                        print("Invalid move")
                except ValueError:
                    print("Invalid input")

if __name__ == "__main__":
    front()