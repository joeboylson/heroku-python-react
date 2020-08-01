import os
from flask import Flask, request, redirect, url_for, render_template, send_file, send_from_directory, Blueprint


app = Flask(__name__, template_folder='./dist')


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

# Heroku sets "PYTHON_ENV" to "PRODUCTION"
IS_PRODUCTION = os.environ.get('PYTHON_ENV') == 'PRODUCTION'
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


@app.route('/')
def index ():
  ''' GET - returns "index.html" '''

  if (IS_PRODUCTION):
    return render_template('index.html')
  else:
    return "DEVELOPMENT"


# --- NOTE: webpack config proxy is set up to reroute any "/api/..." requests to this backend.
# --- It's advised that you prefix any new routes with "/api" (ex: "/api/users")

# --------------------------------------------------------------------------------
# START THE APP
# --------------------------------------------------------------------------------

if __name__ == '__main__':
  print('::: {}'.format(PORT))
  app.run(debug=DEBUG, host='0.0.0.0', port=PORT)