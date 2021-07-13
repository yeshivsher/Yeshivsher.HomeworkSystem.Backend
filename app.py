#!/usr/bin/env python
from config import app
from controllers.teacher_controller import teacherApi
from controllers.classes_controller import classesApi
from controllers.student_controller import studentApi
from controllers.homework_controller import homeworkApi

# register the api
app.register_blueprint(teacherApi)
app.register_blueprint(classesApi)
app.register_blueprint(studentApi)
app.register_blueprint(homeworkApi)

if __name__ == '__main__':
    ''' run application '''
    app.run(port=5000)
