from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello world!'

@app.route('/dojo')

def dojo():
    return 'Dojo!!!'



@app.route('/say/<string:name>')

def hello(name):
    return render_template('hello.html', name = name)


@app.route('/repeat/<int:num>/<str>')

def repeat(num, str):
    return str * num




if __name__=="__main__":
    
    app.run(debug=True)
    

    
    
    