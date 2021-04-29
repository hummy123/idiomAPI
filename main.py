from flask import Flask, request, jsonify
from idiom_inference import inference
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return """<html>
    <form method="POST" action="/predict">
    <label>Sentence:</label><br>
    <input type="text" name="sentence"><br>
    <input type="submit" value="Submit">
    </form>
    </html>"""

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print(request.form)
    sentence = request.form['sentence']
    print(sentence)
    idiom = inference(sentence)
    print(idiom)
    idDef = defineAnswer(idiom)
    return jsonify(prediction=idiom, definition=idDef)

def defineAnswer(idiom):
    if idiom == "none":
        return "No idioms detected."
    elif idiom == "It's raining cats and dogs.":
        return "When it is raining cats and dogs, the rain is pouring down very heaily."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)


