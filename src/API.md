# API Contract

## 1. User Registration
Creates a new user.

- **URL:** /auth/register
- **Method:** POST
- **Headers:**
    - Content-Type: application/json
- **Request Body:**
    json
    {
        "login": "string",
        "password": "string"
    }
    - **Success Response (201 Created):**
    json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000"
    }
    - **Error (400 Bad Request):**
    json
    {
        "error": "login and password required"
    }
    - **Error (409 Conflict):**
    json
    {
        "error": "login already exists"
    }
    
## 2. User Login
Authenticates a user.

- **URL:** /auth/login
- **Method:** POST
- **Headers:**
    - Content-Type: application/json
- **Request Body:**
    json
    {
        "login": "string",
        "password": "string"
    }
- **Success Response (200 OK):**
    json
    {
        "refresh_token": "string",
        "access_token": "string"
    }
- **Error (401 Unauthorized):**
    json
    {
        "error": "invalid credentials"
    }
- **Error (401 Unauthorized):**
    json
    {
        "error": "Invalid or expired token"
    }
    
## 3. Create Game
Creates a new game.

- **URL:** /game
- **Method:** POST
- **Headers:**
    - Authorization: Bearer <access_token>
- **Request Body:**
    json
    {
        "type": "bot" | "human"
    }
- **Success Response (201 Created):**
    json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "field": "         ",
        "status": "waiting" | "in_progress"
    }
- **Error (401 Unauthorized):**
    json
    {
        "error": "authorization required"
    }
    
## 4. Make a Move
Makes a move in an existing game.

- **URL:** /game/{id}
- **Method:** POST
- **Headers:**
    - Authorization: Basic <base64(login:password)>
- **Request Body:**
    json
    {
        "move": 4
    }
- **Success Response (200 OK):**
    json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "field": "X  O  X O ",
        "status": "in_progress" | "finished",
        "winner": "user_id" | null
    }
- **Error (400 Bad Request):**
    json
    {
        "error": "invalid move"
    }
- **Error (401 Unauthorized):**
    json
    {
        "error": "authorization required"
    }
- **Error (404 Not Found):**
    json
    {
        "error": "game not found"
    }
    
## 5. Get Game Status
Returns current game state.

- **URL:** /game/{id}
- **Method:** GET
- **Headers:**
    - Authorization: Basic <base64(login:password)>
- **Request Body:** none
- **Success Response (200 OK):**
    json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "field": "X  O  X O ",
        "status": "waiting" | "in_progress" | "finished" | "draw",
        "player_x": "user_id",
        "player_o": "user_id" | null,
        "winner": "user_id" | null
    }
    
## 6. Get Available Games
Returns list of games waiting for opponent.

- **URL:** /games/available
- **Method:** GET
- **Headers:**
    - Authorization: Basic <base64(login:password)>
- **Request Body:** none
- **Success Response (200 OK):**
    json
    [
        {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "player_x": "user_id",
            "created_at": "2025-03-25T10:00:00"
        }
    ]
    
## 7. Join Game
Joins an existing game waiting for opponent.

- **URL:** /{id}/join
- **Method:** POST
- **Headers:**
    - Authorization: Basic <base64(login:password)>
- **Request Body:** none
- **Success Response (200 OK):**
    json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "field": "         ",
        "status": "in_progress"
    }
- **Error (404 Not Found):**
    json
    {
        "error": "game not found"
    }
- **Error (409 Conflict):**
    json
    {
    }
    
## 8. Get Game History
Returns completed games for authenticated user.

- **URL:** /games/history
- **Method:** GET
- **Headers:**
    - Authorization: Basic <base64(login:password)>
- **Request Body:** none
- **Success Response (200 OK):**
    json
    [
        {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "opponent": "user_id",
            "result": "win" | "loss" | "draw",
            "created_at": "2025-03-25T10:00:00"
        }
    ]
    
## 9. Get Leaderboard
Returns top N players by win ratio.

- **URL:** /leaderboard?limit=10
- **Method:** GET
- **Headers:**
    - Authorization: Basic <base64(login:password)>
- **Request Body:** none
- **Query Parameters:**
  - limit (optional, default: 10, max: 100)
  
- **Success Response (200 OK):**
    json
    [
        {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "login": "alice",
            "wins": 15,
            "losses": 3,
            "draws": 2,
            "ratio": 5.0
        }
    ]
