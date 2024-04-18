from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('pyhtml.html',mensaje=mensaje)

if __name__ : '__main__':
     app.run(debug=True)