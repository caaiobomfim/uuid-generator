from flask import Flask, render_template, request, flash
import uuid

app = Flask(__name__)
app.secret_key = "x5gm96658CBG1"

@app.route('/', methods=["POST", "GET"])
def index(): 
    option = request.form.get('select-uuid')
    if option == "uuid1":
        flash(uuid.uuid1())
    if option == "uuid4":
        flash(uuid.uuid4())
    return render_template('index.html')

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')