from flask import Flask, request
from flask_restful import Resource, Api
from senti_classifier import senti_classifier

app = Flask(__name__)
api = Api(app)

class returnSentiment(Resource):
    def get(self):
        return {"Error":"Please post a string of data"}
    def post(self):
        gloop = request.form['data']
        sentences = gloop.split('.')

        pos_score, neg_score = senti_classifier.polarity_scores(sentences)
        print sentences
        print pos_score, neg_score
        return {'positive_score': pos_score, 'negative_score': neg_score}


api.add_resource(returnSentiment, '/')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)
