
"""
Sample
`main` is the top level module for your Flask application.
"""

# Import the Flask Framework
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
@app.route('/index')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello CMSC818G people! How\'s it going?'


@app.route('/contribute', methods=['POST'])
def contribute():
    tasks = {"message": "success"}
    return jsonify({'tasks': tasks})


@app.route('/login', methods=['POST'])
def login():
    response = None
    if request.method == 'POST':
        body = request.get_json()

        if body is not None:
            response = "Login successful!"

        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    else:
        response = "Invalid request!"
    return send_response(response)


def send_response(message):
    message_dict = {"message": message}
    return jsonify(message_dict)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(405)
def invalid_request(e):
    """Return a custom 405 error."""
    return 'Invalid request', 405


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


# [START APP]
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END app]
