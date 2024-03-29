# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=wrong-import-position
# pylint: disable=anomalous-backslash-in-string
# pylint: disable=missing-module-docstring
# pylint: disable=no-member
# pylint: disable=invalid-envvar-default
# pylint: disable=inconsistent-return-statements


import os
import re
from os.path import join, dirname
import flask
import flask_sqlalchemy
import flask_socketio
from dotenv import load_dotenv

ADDRESSES_RECEIVED_CHANNEL = "addresses received"

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database_uri = os.environ["DATABASE_URL"]

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
import models

db.create_all()
db.session.commit()


def emit_all_addresses(channel):
    all_addresses = [
        db_address.address for db_address in db.session.query(models.Usps).all()
    ]

    socketio.emit(channel, {"allAddresses": all_addresses})


users_total = []


@socketio.on("connect")
def on_connect():
    users_total.append("connect")
    userTotal = len(users_total)
    socketio.emit("connected", {"test": userTotal})

    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    return users_total


@socketio.on("disconnect")
def on_disconnect():
    connectSucc = "connect"
    users_total.remove(connectSucc)
    userTotal = len(users_total)
    socketio.emit("disconnected", {"test": userTotal})
    return users_total


@socketio.on("new address input")
def on_new_address(data):

    db.session.add(models.Usps(data["address"]))

    if data["address"] == "!! about":
        text = "Bot: Welcome to Text+ "
        db.session.add(models.Usps(text))
        return text

    if data["address"] == "!! help":
        text = "Bot: Use different commands to explore (!! about, !! help, !! funtranslate)"
        db.session.add(models.Usps(text))
        return text

    info = data["address"]
    db.session.commit()

    url = re.findall("(?P<url>https?://[^\s]+)", info)
    if url:
        click = url
        socketio.emit("new data", {"test": click})
        return click

    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)


@socketio.on("new username")
def on_new_name(data):

    db.session.add(models.Usps(data["address"]))
    db.session.commit()

    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)


@app.route("/")
def index():
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")


if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
