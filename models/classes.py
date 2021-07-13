#!/usr/bin/env python
from flask import Flask, jsonify, request
from config import db
import yaml
import os


class Classes(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    className = db.Column('ClassName', db.String(45), nullable=False)
    credits = db.Column('Credits', db.Integer, nullable=False)

    # def __init__(self, name, className, credits):
    #     self.name = name
    #     self.className = className
    #     self.credits = credits
