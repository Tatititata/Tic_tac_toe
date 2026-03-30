import requests
users = {}

class GameField:

    @classmethod
    def from_list(cls, l:list | str):
        obj = cls()
        for idx, sign in enumerate(l):
            if sign != ' ':
                obj.place_sign(idx, sign)
        return obj
    
    def place_sign(self, pos, sign):
        if 0 <= pos < len(self._field) and self._field[pos] == ' ' and sign in 'XO':
            self._field[pos] = sign
            return True
        else:
            return False

    def __init__(self):
        self._field = [' '] * 9

    def __str__(self):
        TOP = '╔═══╦═══╦═══╗\n'
        DIV = '╠═══╬═══╬═══╣\n'
        BOT = '╚═══╩═══╩═══╝\n'
        f = self._field         
        line1 = f'║ {f[0]} ║ {f[1]} ║ {f[2]} ║\n'
        line2 = f'║ {f[3]} ║ {f[4]} ║ {f[5]} ║\n'
        line3 = f'║ {f[6]} ║ {f[7]} ║ {f[8]} ║\n'
        return  TOP + line1 + DIV + line2 + DIV + line3 + BOT



BASE_URL = "http://127.0.0.1:5000"

def register(login, password):
    resp = requests.post(f"{BASE_URL}/auth/register", json={"login": login, "password": password})
    if resp.status_code == 201:
        print("Registered:", resp.json()["uid"])
    else:
        print("Error:", resp.json()["error"])

def login(login, password):
    resp = requests.post(f"{BASE_URL}/auth/login", json={"login": login, "password": password})
    if resp.status_code == 201:
        resp = resp.json()
        access_token = resp['access_token']
        refresh_token = resp['refresh_token']
        users[login] = [access_token, refresh_token]
        print("Logged in:", login)
    else:
        print("Login error:", resp.json())


def refresh_token(user_login):
    token = users.get(user_login, [0, 0])[1]
    resp = requests.post(f"{BASE_URL}/auth/refresh", json={"refresh_token": token})
    if resp.status_code == 201:
        resp = resp.json()
        access_token = resp['access_token']
        refresh_token = resp['refresh_token']
        users[user_login] = [access_token, refresh_token]
        print("Logged in:", user_login)
    else:
        print("Login error:", resp.json()["error"])


def create_game(access_token, type='bot'):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.post(f"{BASE_URL}/game", json={"type": type}, headers=headers)
    if resp.status_code == 201:
        game = resp.json()
        print("Game created:", game["uid"], "status: ", game['status'])
        print(GameField.from_list(game['field']))
        return game["uid"]
    else:
        print("Error:", resp.json().get("error", resp.text))
        return None

def make_move(game_id, move, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
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
    
def me(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(f"{BASE_URL}/user/me", headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        # print("Error:", resp.json())
        print(resp.text)
        return []
    
def check_available(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(f"{BASE_URL}/games/available", headers=headers)
    if resp.status_code == 200:
        games = resp.json()
        return [[g['uid'], g['status']] for g in games]
    else:
        # print("Error:", resp.json())
        print(resp.text)
        return []

def game_history(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(f"{BASE_URL}/games/history", headers=headers)
    if resp.status_code == 200:
        games = resp.json()
        return [[g['uid'], g['winner_id'], g['status']] for g in games]
    else:
        # print("Error:", resp.json())
        print(resp.text)
        return []


def user_info(access_token, uid):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(f"{BASE_URL}/user/{uid}", headers=headers)
    if resp.status_code == 200:
        user = resp.json()
        print(f'User id: {user["uid"]}, user login: {user["login"]}')
    else:
        print("Error:", resp.json().get("error", resp.text))

def join_game(access_token, game_id):
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.post(f"{BASE_URL}/{game_id}/join", headers=headers)
    if resp.status_code == 200:
        game = resp.json()
        print("Joined game:", game["uid"], game['status'])
        print(GameField.from_list(game['field']))
        return game["uid"]
    else:
        print("Error:", resp.json().get("error", resp.text))
        return None

def play_game(game_id, access_token):
    while True:
        move = input("Enter move (1-9) or q to quit: ")
        if move == 'q':
            break
        try:
            move = int(move)
            if 0 < move < 10:
                make_move(game_id, move, access_token)
            else:
                print("Invalid move")
        except ValueError:
            print("Invalid input")


def front():
    print("=== Tic-Tac-Toe Console Client ===")

    user_login = None
    user_password = None
    string = '''
    1. Register
    2. Check available games
    3. User info
    4. Play game
    5. Login
    6. Create game
    7. Refresh tokens
    8. Game history
    9. About me
    
    q to quit:
    '''

    while True:
        choice = input(string)
        if choice == '1':
            user_login = input("Login: ")
            user_password = input("Password: ")
            register(user_login, user_password)
        elif choice == '2':
            games = check_available(users.get(user_login, [0, 0])[0])
            print(*games, sep='\n')
        elif choice == '4':
            games = check_available(users.get(user_login, [0, 0])[0])
            if games:
                for idx, g in enumerate(games):
                    print(f'{idx}. {g}')
                try:
                    num = int(input("Choose game number: "))
                    # game_id = join_game(user_login, user_password, 'f51d0e64-2413-4737-b12b-e6170e8e8a01')
                    game_id = join_game(users.get(user_login, [0, 0])[0], games[num][0])
                    print(game_id)
                    
                    # play_game('f51d0e64-2413-4737-b12b-e6170e8e8a01', user_login, user_password)
                    play_game(game_id, users.get(user_login, [0, 0])[0])
                except:
                    print("Invalid number")
            else:
                print('No games available')
        elif choice == 'q':
            break
        elif choice == '5':
            user_login = input("Login: ")
            user_password = input("Password: ")
            login(user_login, user_password)

        elif choice == '6':
            type = input("1 = human, 2 = bot: ")
            if type == '1':
                type = 'human'
            else:
                type = 'bot'
            game_id = create_game(users.get(user_login, [0, 0])[0], type)
            play_game(game_id, users.get(user_login, [0, 0])[0])

        elif choice == '3':
            uid = input("enter user id: ")
            user_info(users.get(user_login, [0, 0])[0], uid)

        elif choice == '7':
            refresh_token(user_login)
        elif choice == '0':
            print(*users.items(), sep='\n')
        elif choice == '8':
            print(*game_history(users.get(user_login, [0, 0])[0]), sep='\n')
        elif choice == '9':
            print(me(users.get(user_login, [0, 0])[0]), sep='\n')

if __name__ == "__main__":
    front()