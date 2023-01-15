from flask import Flask,render_template,jsonify,request,json
from chat import get_response

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index_get():
        return render_template("index.html")

    @app.route("/predict",methods=["POST"])
    def predict():
        text = request.get_json()['message']
        # TODO: check if text is valid
        print("User: ")
        response = get_response(text)
        print("Bot: ",response)
        message = {"answer":response}
        return jsonify(message)
    return app

# if __name__ == "__main__":
#     app.run(debug=False)