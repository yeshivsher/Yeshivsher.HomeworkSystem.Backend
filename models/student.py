#!/usr/bin/env python
from flask import Flask, jsonify, request
from config import db
import yaml
import os


class Student(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Name', db.String(), nullable=False)
    lastName = db.Column('LastName', db.String(45), nullable=False)
    password = db.Column('Password', db.String(45), nullable=False)
    mail = db.Column('Mail', db.String(45), nullable=False)
    classIds = db.Column('ClassIds', db.String(45), nullable=False)

    # def __init__(self, name, lastName, password, classIds, mail):
    #     self.name = name
    #     self.lastName = lastName
    #     self.password = password
    #     self.classIds = classIds
    #     self.mail = mail
