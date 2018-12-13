from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello():
 for x in range(1,20):
 	print(x)
 return "backend running."

if __name__ == "__main__":
 app.run()