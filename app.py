from flask import Flask, render_template, request, redirect, url_for
import pickle
import helper

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        if q1 and q2:
            query = helper.query_point_creator(q1, q2)
            prediction = model.predict(query)[0]
            result = 'Duplicate' if prediction else 'Not Duplicate'
            return redirect(url_for('index', result=result))
    
    result = request.args.get('result')
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
