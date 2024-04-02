from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "hello world-- This is My first Flask Project"

@app.route("/second")
def head2():
    return "second page"

@app.route("/third")
def head3():
    return "third Page"

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)