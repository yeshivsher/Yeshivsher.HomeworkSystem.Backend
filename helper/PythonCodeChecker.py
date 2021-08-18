import ast
import sys
import random

result = False

class PythonCodeChecker(str):

    def default(str):
        print('\nstr\n')
        print(str)

        sys.argv = ['1']
        exec(str)
        return result

    def compareTwoDicsAsGrade(dic1, dic2):
        counterForGradeInTests = 0

        for key in dic1:
            try:
                if dic1[key] == dic2[key]:
                    counterForGradeInTests = counterForGradeInTests + 10
            except:
                print('\nBugs.\n')

        return counterForGradeInTests

    def int(strOfFile):
        examSolutionOutput = {}

        try:
            for n in range(10):
                sys.argv = [n]
                exec(strOfFile)

                examSolutionOutput[n] = result
        except:
            print('\nPython file contains bugs.\n')

        return examSolutionOutput
    
    def float(strOfFile):
        examSolutionOutput = {}

        try:
            for n in range(10):
                arg = round(random.uniform(0, 1), 1)
                arg = arg + n
                
                sys.argv = [arg]
                exec(strOfFile)

                examSolutionOutput[n] = result
        except:
            print('\nPython file contains bugs.\n')

        return examSolutionOutput
    
    def string(strOfFile):
        examSolutionOutput = {}

        try:
            for n in range(10):
                arg = str(round(random.uniform(0, 1), n))
                
                sys.argv = [arg]
                exec(strOfFile)

                examSolutionOutput[n] = result
        except:
            print('\nPython file contains bugs.\n')

        return examSolutionOutput
