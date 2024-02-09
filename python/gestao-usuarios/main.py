from flask import Flask, url_for, render_template
from routes.home import home_route


app = Flask(__name__)

app.register_blueprint(home_route)


app.run(debug=True)
