# Backend - Full Stack Trivia API 
## Introduction
This project is a Trivia API form Udacity,you are able to add questions, search through the question ,delete questions ,get questions that have the same category ,get all category,get all questions and play quizz 
## Getting Started
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
## Error Handling
Errors are returned as JSON objects in the following format
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
## Endpoints
#### GET /categories
- *General*:
    -Returns a list of all categories(id,type) and success value
- *sample*:`curl http://127.0.0.1:5000/categories`
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
- *Sample*: `curl http://127.0.0.1:5000/questions`
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
- *Sample*: `curl -X DELETE http://127.0.0.1:5000/questions/2`
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
- *Sample*: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Test add question1", "answer":"test answer ", "category":"2","difficulty":3}'`
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
- *Sample*:`curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"search":"Where"}'`
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
- *Sample*:`curl http://127.0.0.1:5000/categories/2/questions`
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
- *Sample*:`curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":"2","previous_questions":27}'`
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
