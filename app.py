from flask import Flask , render_template, request,redirect, flash , url_for

app=Flask(__name__)
app.config['SECRET_KEY']='736b228b517671fd9e5d8ba243c78a84'

@app.route('/')
def home():
    return render_template('#')

@app.route('/round1')
def round1():
    return render_template('#')

@app.route('/round2')
def round2():
    return render_template('#')

@app.route('/results')
def results():
    return render_template('#')


if __name__ =='__main__':
    app.run(debug=True)

