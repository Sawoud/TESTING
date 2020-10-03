################################################################IMPORTS
from flask import Flask

############################################################### App Declrations
app = Flask(__name__)


######################################################## PAGES

@app.route("/")
def index():
    print("grh")
    return "car"

@app.route("/page")
def page():
    print("game")
    import main
    return main.main()


if __name__ == '__main__':
#    db.create_all()
#    make_table()
    app.run(debug=True)
