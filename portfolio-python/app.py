from flask import Flask, render_template

app = Flask(__name__)    #main file   

@app.route("/")          #homepage URL
def home():              #Function for homepage
    return render_template("index.html")           #Show HTML page

if __name__ == "__main__":
    app.run(debug=True)     #Start server


# Flask → used to create your web application
# render_template → used to show HTML pages