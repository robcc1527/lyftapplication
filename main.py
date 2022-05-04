from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route("/test", methods=['POST'])


def test():
#return variable - empty string
    word_return = ''
    content = request.json
#    print(content['string_to_cut']) - print to debug code
# loop through string and changing index by 1 and mod 3 to find third char
    for index, letter in enumerate(content['string_to_cut']):
        if (index+1) % 3 == 0:
#       adding 3rd char to return variable
            word_return = word_return + letter
    return jsonify({"return_string": word_return})

#error handeling
@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500