# Backend - Full Stack Trivia API 
## Introduction
This project is a Trivia API form Udacity,you are able to add questions, search through the question ,delete questions ,get questions that have the same category ,get all category,get all questions and play quizz 
## Getting Started
#### Installing Dependencies
### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

#### Base URL
The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 
#### Authentication
This version of the application does not require authentication or API keys
#### Backend
From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
#### Frontend

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Error Handling
Errors are returned as JSON objects in the following format
- success: False.
- error: error code number.
- message: error message string giving description about the kind of error.
```
{
  "error": 400,
  "message": "bad request",
  "success": false
}

```
The API will return four error types when requests fail:
1. 404: resource not found
2. 422: unprocessable
3. 400: bad request
4. 405: method not allowed
#### example of error 
if the user inter `curl http://127.0.0.1:5000/quizzes -X GET`
- Response body:
```
{
  "error": 405,
  "message": "method not allowed",
  "success": false
}
```
## Endpoints
#### GET /categories
- *General*:
    -Returns a list of all categories(id,type) and success value
    - Request Arguments: None
- *sample*:`curl http://127.0.0.1:5000/categories`
- Response body:
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
#### GET /questions
- *General*:
    - Returns a list of questions objects,categories,current categories success value and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
    - Request Arguments: Page's number *optional*
- *Sample*: `curl http://127.0.0.1:5000/questions`
- Response body:
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": "Art",
  "questions": [
    {
      "answer": "this is an answer",
      "category": "2",
      "difficulty": 5,
      "id": 1,
      "question": "this is a question"
    },
    {
      "answer": "this is an answer",
      "category": "2",
      "difficulty": 5,
      "id": 2,
      "question": "this is a question"
    }],
  "success": true,
  "totalQuestions": 2
}
```
#### DELETE /questions/<int:question_id>
- *General*:
    - Returns id of deleted question a list of questions objects,success value and total number of questions
    - Request Arguments: question_id *required*
- *Sample*: `curl -X DELETE http://127.0.0.1:5000/questions/2`
- Response body:
```
{
  "deleted": 2,
  "questions": [
    {
      "answer": "this is an answer",
      "category": "2",
      "difficulty": 5,
      "id": 1,
      "question": "this is a question"
    }],
  "success": true,
  "totalQuestions": 1
}
```
#### POST /questions 
- *General*:
    - Creates a new question using the submitted question, answer,category and difficulty. Returns the id of the created question ID,question, success value, category, answer and difficulty.
    -  Request Arguments: a key/value object whit the following {
        - question: (type:string) containing the question itself.
        - answer: (type:string) containing answer's of the question.
        - category: (type:string) ID of category.
        - difficulty:(type:integer) difficulty level.
    }
- *Sample*: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Test add question1", "answer":"test answer ", "category":"2","difficulty":3}'`
- Response body:
```
{
  "answer": "test answer",
  "category": "2",
  "created": 50,
  "difficulty": 3,
  "questions": "Test add question1",
  "success": true
}
```
#### POST /questions/search
- *General*:
    - search about specific question. Returns the currentCategory,a list of questions objects,success value and total number of questions.
    - Request Arguments:search which is string to search about specific questions string. 
- *Sample*:`curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"search":"Where"}'`
- Response body:
```
{
  "currentCategory": "Geography",
  "questions": [
    {
      "answer": "North",
      "category": "3",
      "difficulty": 1,
      "id": 52,
      "question": "Where is USA?"
    }
  ],
  "success": true,
  "totalQuestions": 48
}
```
#### GET /categories/<int:category_id>/questions
- *General*:
    - Get questions based on category. Returns the currentCategory,a list of questions objects,success value and total number of questions. 
    - Request Arguments:category_id: category id field.
- *Sample*:`curl http://127.0.0.1:5000/categories/2/questions`
- Response body:
```
{
  "currentCategory": "Art",
  "question": [
    {
      "answer": "this is an answer",
      "category": "2",
      "difficulty": 5,
      "id": 1,
      "question": "this is a question"
    },
    {
      "answer": "Auguste Rodin",
      "category": "2",
      "difficulty": 2,
      "id": 27,
      "question": "Who created the famous sculpture 'The Thinker'"
    },
    {
      "answer": "Mark Haddon",
      "category": "2",
      "difficulty": 2,
      "id": 28,
      "question": "Who wrote the Curious Incident of the Dog in the Night Time?"
    },
    {
      "answer": "Vincent van Gogh",
      "category": "2",
      "difficulty": 2,
      "id": 29,
      "question": " Which artist cut off the lobe of his own ear and later shot himself?"
    },
    {
      "answer": "Jeff Koons",
      "category": "2",
      "difficulty": 2,
      "id": 30,
      "question": "What artist sold a balloon dog for $58.4 million?"
    },
    {
      "answer": "Amsterdam",
      "category": "2",
      "difficulty": 2,
      "id": 31,
      "question": "In which city would you find The Van Gogh Museum?"
    },
    {
      "answer": "Louvre",
      "category": "2",
      "difficulty": 2,
      "id": 32,
      "question": " The Mona Lisa by Leonardo da Vinci is on display in which Paris museum?"
    },
    {
  ],
  "success": true,
  "totalQuestions": 7
}
```
#### POST /quizzes
- *General*:
    -  a POST endpoint to get questions to play the quiz.you need to pass quiz_category and previous_questions.Returns a list of previous questions,a random question objects and success value . 
    - Request Arguments:category_id: question's category id field inter as string .previous_quesion:inter as integer
- *Sample*:`curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":"2","previous_questions":27}'`
- Response body:
```
{
  "previous questions": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27
  ],
  "question": {
    "answer": "Mark Haddon",
      "category": "2",
      "difficulty": 2,
      "id": 28,
      "question": "Who wrote the Curious Incident of the Dog in the Night Time?"
  },
  "success": true
}
```
when you set previous questions=0 that means the quiz end 
```
{
  "message": "I hope you enjoined the quiz",
  "success": false
}
```
