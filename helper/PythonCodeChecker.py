import ast
import sys

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

    def int(str):
        examSolutionOutput = {}

        try:
            for n in range(10):
                sys.argv = [n]
                exec(str)

                examSolutionOutput[n] = result
        except:
            print('\nPython file contains bugs.\n')

        return examSolutionOutput
    
    def float(str):
        examSolutionOutput = {}

        try:
            for n in range(10):
                sys.argv = [n]
                exec(str)

                examSolutionOutput[n] = result
        except:
            print('\nPython file contains bugs.\n')

        return examSolutionOutput
    
    def string(str):
        examSolutionOutput = {}

        try:
            for n in range(10):
                sys.argv = [n]
                exec(str)

                examSolutionOutput[n] = result
        except:
            print('\nPython file contains bugs.\n')

        return examSolutionOutput
