# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=unused-import
# pylint: disable=no-member

# models.py
import flask_sqlalchemy
from app import db


class Usps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))

    def __init__(self, a):
        self.address = a

    def __repr__(self):
        return "<Usps address: %s>" % self.address
