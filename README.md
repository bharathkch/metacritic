# metacritic
# Assignment

## Pre Requisites
* Python 3.7.7 installed (A virtual environment is preferred)
* Install the dependencies
    ```bash
    pip install -r requirements.txt

    ```
## Usage

* Configure the flask app

** The host and port number of the Flask application can be configured in "config/.env"
> The application runs on localhost and port:5000 by default

* Run the Flask Application
    ```bash
    <path_to_app>/parse_metacritic.py
    ```

* Perform a health check using the "/ping" endpoint. You should see a "OK" message.
    ```bash
    curl http://localhost:5000/ping
    
      OK
    ```
    
## Available API's

API | Description
--- | ---
`GET /ping` | A default API added by ASR. Returns string 'OK'. Used for basic healthcheck.
`GET /games` | Returns the list of games with title and score.
`GET /games/<title of the game>` | Fetches the game based on the title in the request and returns the game object(tile and score) if found. Else, error message.
 
 
### Examples

* Retrieve all the games
    ```bash
    curl -sS  http://localhost:5000/games | python -m json.tool
  
    [
    {
        "title": "The Last of Us Part II",
        "score": "94"
    },
    {
        "title": "Ghost of Tsushima",
        "score": "83"
    },
    {
        "title": "Beyond Blue",
        "score": "75"
    },
    {
        "title": "Those Who Remain",
        "score": "49"
    },
    {
        "title": "Pistol Whip",
        "score": "92"
    },
    {
        "title": "Cuphead",
        "score": "87"
    }
    ]
    ```

* Retrieve a particular game
    ```bash
    curl -sS http://localhost:5000/games/Those%20Who%20Remain | python -m json.tool
    
  {
    "title": "Those Who Remain",
    "score": "49"
  }
 
    ```
    
* Invalid Game
    ```bash
    curl -sS http://localhost:5000/games/Some%20Ramdom%20Game | python -m json.tool
    
   {
    "Error": "A game with title  'Some Ramdom Game' Not found"
   }

    ```
    
## Unit Testing

* Execute Unit Tests
    ```bash
    
  pytest . -s --debug

