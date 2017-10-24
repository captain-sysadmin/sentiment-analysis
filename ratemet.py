from flask import Flask, request
from flask_restful import Resource, Api
from senti_classifier import senti_classifier
import json

app = Flask(__name__)
api = Api(app)

class returnSentiment(Resource):
    def get(self):
        return """
        Please post a json string in the following way:
        {"sentences":["on a long and frosty morning.","I asid hello"]}
        """
    def post(self):
        json_data = request.get_json(force=True)
        #gloop = request.form['data']
        #sentences = gloop.split('.')
        print json_data
        if 'sentences' not in json_data:
            return "Nope"
        sentences = json_data['sentences']


        pos_score, neg_score = senti_classifier.polarity_scores(sentences)
        print sentences
        print pos_score, neg_score
        return {'positive_score': pos_score, 'negative_score': neg_score}


api.add_resource(returnSentiment, '/')
if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=80,debug=True)
    app.run(debug=True)
