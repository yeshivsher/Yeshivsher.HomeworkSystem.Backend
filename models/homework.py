#!/usr/bin/env python
from models.student import Student
from flask import Flask, jsonify, request
from config import db
import yaml
import os
import datetime


class Homework(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'homework'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fileData = db.Column('FileData', db.LargeBinary(length=(2**32)-1), nullable=False)
    name = db.Column('Name', db.String(45), nullable=False)
    classId = db.Column('ClassId', db.Integer, nullable=False)
    status = db.Column('Status', db.Integer, nullable=False,default='לא הוגש')
    date = db.Column('Date',db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    grade = db.Column('Grade', db.Integer, nullable=True)
    studentId = db.Column('StudentId', db.Integer, nullable=False)
    isFileExist = db.Column('IsFileExist', db.Boolean, nullable=False, default=0)

    # def __init__(self, fileData, name, classId):
    #     self.fileData = fileData
    #     self.name = name
    #     self.classId = classId
