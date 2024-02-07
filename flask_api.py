from flask import Flask, request, jsonify
from sim_score import sim_score, text_preprocessing

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def welcome():
    return jsonify({'you are welcome plase go the similarity route to checksentence similarity'})

@app.route('/similarity', methods=['GET','POST'])
def calculate_similarity():
    print("route is accesing")
    # Get the text inputs from the request
    text2 = request.args.get('text2')
    text1 = request.args.get('text1')
    # check if getting both texts through args
    if bool(text1) and bool(text2):
        print("Got text arguments")

        # Check if both texts are not emty
        if not text1.strip() or not text2.strip():
            return jsonify({'error': 'Please provide both texts,text field is empty now'})

        #Calculating score by passing args to a function
        similarity_score = sim_score(text1, text2)

        # Return the similarity score
        return jsonify({'similarity_score': similarity_score})
    else:
        return jsonify({'error': 'Please provide both text arguments'})

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='192.168.1.50',port='5004',debug=True)
