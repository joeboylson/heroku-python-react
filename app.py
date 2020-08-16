import os
import json
from flask import Flask, request, jsonify, redirect, url_for, render_template, send_file, send_from_directory, Blueprint
from datastore.schema import Session, User


app = Flask(__name__, template_folder='./dist')
session = Session()


# host static files at "/api/static"
static_folder = Blueprint('static', __name__, static_url_path='/api/static', static_folder='./static')
app.register_blueprint(static_folder)


# host dist at ""
dist_folder = Blueprint('dist', __name__, static_url_path='', static_folder='./dist')
app.register_blueprint(dist_folder)


# --------------------------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------------------------

DOWNLOAD_DIRECTORY = "static/images"
DIST_DIRECTORY = "dist"

# Heroku sets "NODE_ENV" to "production"
IS_PRODUCTION = os.environ.get('NODE_ENV') == 'production'
DEBUG = True if not IS_PRODUCTION else False
PORT = 5000 if not IS_PRODUCTION else os.environ.get('PORT')

# --------------------------------------------------------------------------------
# FUNCTIONS
# --------------------------------------------------------------------------------

# --- add in your functions here
# --- or remove this section and import another file

# --------------------------------------------------------------------------------
# ROUTES
# --------------------------------------------------------------------------------


class Response():
  def __init__(self, success=False, data=None, error=None, message=None):
    self.success = success 
    self.data = data 
    self.error = error 
    self.message = message 

  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


@app.route('/')
def index():
  ''' GET - returns "index.html" '''

  if (IS_PRODUCTION):
    return render_template('index.html')
  else:
    return "DEVELOPMENT"


# --- NOTE: webpack config proxy is set up to reroute any "/api/..." requests to this backend.
# --- It's advised that you prefix any new routes with "/api"

@app.route('/api/createUser', methods=['POST'])
def create_user():
  data = request.json
  response = Response()

  try:
    row = User(name=data['name'])
    session.add(row)
    session.commit()
    session.refresh(row) # refresh to get the added record
    response = Response(success=True, data={'id': row.id, 'name': row.name})
  except Exception as e:
      response = Response(error=e)
  finally:
      session.close()

  return response.to_json()


@app.route('/api/fetchAllUsers', methods=['GET'])
def fetch_all_users():
  response = Response()

  try:
    users = session.query(User).all()
    data = [{'id': row.id, 'name': row.name} for row in users]
    response = Response(success=True, data=data)
  except Exception as e:
      response = Response(error=e)
  finally:
      session.close()

  return response.to_json()


# --------------------------------------------------------------------------------
# START THE APP
# --------------------------------------------------------------------------------

if __name__ == '__main__':
  print('::: {}'.format(PORT))
  app.run(debug=DEBUG, host='0.0.0.0', port=PORT)