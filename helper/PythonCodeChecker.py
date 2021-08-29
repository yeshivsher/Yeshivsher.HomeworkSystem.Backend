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
                return 0

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
            return 0

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
            return 0

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
            return 0

        return examSolutionOutput

    def list_int(strOfFile):
        examSolutionOutput = {}

        try:
            lastN = 0
            for n in range(1, 11):
                arg = []
                for j in range(lastN * 10, n * 10):
                    arg.append(j)

                sys.argv = [str(arg)]
                exec(strOfFile)

                examSolutionOutput[n] = result

                lastN = n
        except:
            print('\nPython file contains bugs.\n')
            return 0

        return examSolutionOutput

    def list_float(strOfFile):
        examSolutionOutput = {}

        try:
            lastN = 0
            for n in range(1, 11):
                arg = []
                for j in range(lastN * 10, n * 10):
                    arg.append(j + 0.2)

                sys.argv = [str(arg)]
                exec(strOfFile)

                examSolutionOutput[n] = result

                lastN = n
        except:
            print('\nPython file contains bugs.\n')
            return 0

        return examSolutionOutput

    def list_string(strOfFile):
        examSolutionOutput = {}

        try:
            lastN = 0
            for n in range(1, 11):
                arg = []
                for j in range(lastN * 10, n * 10):
                    arg.append(str(j))

                sys.argv = [str(arg)]
                exec(strOfFile)

                examSolutionOutput[n] = result

                lastN = n
        except:
            print('\nPython file contains bugs.\n')
            return 0

        return examSolutionOutput
    
    
    def dic_int(strOfFile):
        examSolutionOutput = {}

        try:
            lastN = 0
            for n in range(1, 11):
                arg = {}
                for j in range(lastN * 10, n * 10):
                    arg[j]= j * j

                sys.argv = [str(arg)]
                exec(strOfFile)

                examSolutionOutput[n] = result
                print(examSolutionOutput)

                lastN = n
        except:
            print('\nPython file contains bugs.\n')
            return 0
            
        return examSolutionOutput
           
    def dic_float(strOfFile):
        examSolutionOutput = {}

        try:
            lastN = 0
            for n in range(1, 11):
                arg = {}
                for j in range(lastN * 10, n * 10):
                    j = j + 0.1
                    arg[j]= j * j

                sys.argv = [str(arg)]
                exec(strOfFile)

                examSolutionOutput[n] = result

                lastN = n
        except:
            print('\nPython file contains bugs.\n')
            return 0

        return examSolutionOutput

    def dic_string(strOfFile):
        examSolutionOutput = {}

        try:
            lastN = 0
            for n in range(1, 11):
                arg = {}
                for j in range(lastN * 10, n * 10):
                    arg[j] = str(j)+ str(n)

                sys.argv = [str(arg)]
                exec(strOfFile)

                examSolutionOutput[n] = result

                lastN = n
        except:
            print('\nPython file contains bugs.\n')
            return 0

        return examSolutionOutput
