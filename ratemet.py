from flask import Flask, request
from flask_restful import Resource, Api
from senti_classifier import senti_classifier
import math

app = Flask(__name__)
api = Api(app)


swear_words = []
with open('swear/bad_words.txt') as fh:
    for line in fh:
        word = line.rstrip()
        swear_words.append(word)
@app.after_request
def after(response):
    # todo with response
    print response.status
    print response.headers
    print response.get_data()
    return response
    
class returnSentiment(Resource):
    def get(self):
        return """
        Please post a json string in the following way:
        {"sentences":["on a long and frosty morning.","I asid hello"]}
        """
    def post(self):
        json_data = request.get_json(force=True)
        print json_data
        if 'sentences' not in json_data:
            return "Nope"
        sentences = json_data['sentences']
        swear_score = 0
        percentage = 0
        for swear in swear_words:
            for single_sentence in sentences:
                if swear in single_sentence:
                    swear_score +=1
        if swear_score:
            gloop = str(sentences)
            words = gloop.split(' ')
            print len(words)
            percentage = (float(swear_score) / len(words)) *100.0
            # Avert all ye eyes gentle folk, thar be monsters
            percentage = float("{:.2f}".format(percentage)) 
            # so dirty. I know there is a decimal module
            # but, this a hack day and writing this comment
            # took longer than this hack



        pos_score, neg_score = senti_classifier.polarity_scores(sentences)
        print sentences
        print pos_score, neg_score
        return {'positive_score': pos_score, 'negative_score': neg_score, 'swear_count': swear_score, 'swear_percentage': percentage}


api.add_resource(returnSentiment, '/')
if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=80,debug=True)
    app.run(debug=True)
