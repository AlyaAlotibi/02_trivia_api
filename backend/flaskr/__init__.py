import os
from flask import (Flask,
 request, abort,
  jsonify)
from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_question(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  question = [question.format() for question in selection]
  current_questions = question[start:end]

  return current_questions
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TO1: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)

  '''
  @TO1: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
  '''
  @TO1: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def available_categories():
    categories = Category.query.order_by(Category.id).all()

    if len(Category.query.all()) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'categories':  {category.id: category.type for category in categories}
    })

  '''
  @TO1: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def retrieve_questions():
    selection = Question.query.order_by(Question.id).all()
    current_question = paginate_question(request, selection)
    categories = Category.query.order_by(Category.id).all()
    for s in selection:
      for c in categories:
        if int(s.category)==c.id:
         category=c.type
    if len(current_question) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_question,
      'totalQuestions': len(Question.query.all()),
       'categories':  {category.id: category.type for category in categories}
      ,'currentCategory':category
    })
  '''
  @TO1: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    deletedQ=Question.query.filter(Question.id==question_id).one_or_none()
    if deletedQ is None:
      abort(422)
    try:
      deletedQ.delete()
      selection = Question.query.order_by(Question.id).all()
      current_question = paginate_question(request, selection)
      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions':current_question,
        'totalQuestions': len(selection)
      })
    except:
      abort(422)

    
  '''
  @TO1: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.
  '''
  @app.route('/questions', methods=['POST'])
  def post_question():
    body=request.get_json()
    new_question =body.get('question',None)
    new_answer = body.get('answer',None)
    new_category = body.get('category',None)
    new_difficulty = body.get('difficulty',None)
    try:
      questions=Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty)
      questions.insert()
      return jsonify({
        'success': True,
        'created': questions.id,
        'questions':questions.question,
        'answer':questions.answer,
        'category':questions.category,
        'difficulty':questions.difficulty
        
       })
    except:
      abort(422)

  '''
  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TO1: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def get_questions():
    body = request.get_json()
    search = body.get('search', None)
    try:
      question=Question.query.filter(Question.question.ilike('%{}%'.format(search))).all()

      categories = Category.query.order_by(Category.id).all()
      for s in question:
         for c in categories:
          if int(s.category)==c.id:
             category1=c.type
      return jsonify({
      'success': True,
      'questions': [q.format() for q in question],
      'totalQuestions': len(Question.query.all())
      ,'currentCategory':category1
      })
    except:
      abort(404)
  '''
  @To1: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def retrieve_by_category(category_id):
    try:
      categories = Category.query.filter(Category.id==category_id).all()
      questions=Question.query.filter(Question.category==str(category_id)).all()
      for s in questions:
         for c in categories:
          if int(s.category)==c.id:
             category1=c.type
      
      return jsonify({
        'success': True,
        'question':[question.format() for question in questions],
         'totalQuestions': len(questions),
         'currentCategory':category1
         })
    except:
      abort(404)
    

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def quizzes():
   body = request.get_json()
   previous_questions = body.get('previous_questions')
   print(previous_questions)
   category = body.get('quiz_category')
   print(category)
   if ((category is None) or (previous_questions is None)):
      abort(400)
   if (int(category) == 0):
      questions = Question.query.all()
   else:
      questions = Question.query.filter_by(category=str(category)).all()

   random.shuffle(questions)

   Current_Question = None
   for question in questions:
      found = False
      for previous_id in range(previous_questions):
        if question.id == previous_id:
          pre_questions=question.id
          break
        else:
          Current_Question = question
          found = True
          pre_questions=question.id

      if found:
        break

   if Current_Question is None:
        return jsonify({
            'success': False,
            'message':'I hope you enjoined the quiz'
        })

   return  jsonify({
              'success': True,
              'previous questions':[pre for pre in range(pre_questions)]
              ,'question': Current_Question.format()
            })
    

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400
  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405
  return app

    