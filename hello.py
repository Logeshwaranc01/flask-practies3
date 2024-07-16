from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>Hello </h1>"

@app.route('/Hi')
def hello1():
    return "<h1>Hello Logesh!</h1>"

@app.route('/c')
def hello2():
    return "<h1>Hello Logesh! How are you?</h1>"


if __name__=='__main__':
    app.run(debug=True)

