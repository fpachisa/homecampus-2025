'''
Created on Oct 10, 2011

Module: DivideWholeNumber
Generates "Divison of whole number by proper fraction" problems for Primary 6

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
from random import randint
from Utils import LcmGcf
from decimal import Decimal

class DivideWholeNumber:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        self.ProblemType = {"easy":[self.GenerateProblemType1(),self.GenerateProblemTypeMCQ1(),],
                            }
        try:
            return random.choice(self.ProblemType[level])
        except KeyError:
            return random.choice(random.choice(self.ProblemType.values()))
        #return self.GenerateProblemTypeMCQ1()                    
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemTypeMCQ1"],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemTypeMCQ1()],
                                    }
        
        #Creating one more problem type so it creates a list and not a list of lists
        self.ProblemTypes = []
        
        for i in self.ProblemType.values():
            for k in i:
                self.ProblemTypes.append(k)
                
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(random.choice(self.GenerateProblemType.values()))
        else:
            if LastProblemID in self.ProblemTypes:
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if LastProblemID in v][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return random.choice(self.GenerateProblemType[NextProblemKey])
            else:
                return random.choice(random.choice(self.GenerateProblemType.values()))
        return self.GenerateProblemTypeMCQ1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        ''' 6 &divide; 3/10 '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.denominator = random.choice([2,3,4,5,6,7,8,9,10,11,12])
        self.numerator = randint(1,self.denominator-1)
        self.number = randint(1,10)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+str(self.number)+"&nbsp;</td>"
        self.problem = self.problem + "<td> &divide; &nbsp;</td>"   
        self.problem = self.problem + "<td style='text-align:center; padding-top:3px'><u>&nbsp;"+str(self.numerator)+"&nbsp;</u><br>"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.problem = self.problem + "<table class='FractionsTable' style='font-size:0.8em;color:black'>"
        self.problem = self.problem + "<tr><td>(Type your answer as: If&nbsp;</td>"
        self.problem = self.problem + "<td style='padding-top:3px'><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1/2. And if&nbsp;</td>"
        self.problem = self.problem + "<td>1</td>"
        self.problem = self.problem + "<td style='padding-top:3px'><u>&nbsp;1&nbsp;</u><br>&nbsp;2</td>"
        self.problem = self.problem + "<td>&nbsp;then type as 1 1/2)</td>"
        self.problem = self.problem + "</tr></table>" 
        
        self.AnswerDenominator = self.numerator
        self.AnswerNumerator = self.number * self.denominator
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator
        self.answer = str(self.answer1)+"/"+str(self.answer2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.number,self.numerator,self.denominator,self.AnswerNumerator,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':1,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}
    
    def ExplainType1(self,problem,answer1,answer2,number,numerator,denominator,AnswerNumerator,AnswerDenominator):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        gcf = LcmGcf.LcmGcf().find_gcf(int(self.answer1), int(self.answer2))
        '''Adding the simplified fraction if possible'''
        if gcf!=1 or self.answer2==1:
            self.SimpleAnswer1 = int(answer1)/gcf
            self.SimpleAnswer2 = int(answer2)/gcf
            if self.SimpleAnswer2!=1:
                temp = "<td style='text-align:center; padding-left:0px; padding-right:0px'><u>&nbsp;"+str(self.SimpleAnswer1)+"&nbsp;</u><br>"+str(self.SimpleAnswer2)+"</td>"
                self.answer_text = self.answer_text + temp
            else:
                temp = "<td style='text-align:left; padding-left:0px; padding-right:0px'>"+str(self.SimpleAnswer1)+"</td>"
                self.answer_text = self.answer_text + temp
        else:
            temp = "<td style='text-align:center; padding-left:0px; padding-right:0px'><u>&nbsp;"+str(answer1)+"&nbsp;</u><br>"+str(answer2)+"</td>"
            self.answer_text = self.answer_text + temp

        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:left'><b><i>Step 1:</i></b>&nbsp;&nbsp;&nbsp; Change <font color='red'><b>&divide;</b></font> to <font color='red'><b>&times;</b></font>.</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'><b><i>Step 2:</i></b>&nbsp;&nbsp;&nbsp; Invert the fraction.</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'><b><i>Step 3:</i></b>&nbsp;&nbsp;&nbsp; Simplify the expression.</td></tr></table><br>"
        self.solution_text = self.solution_text + "<table><tr><td style='text-align:right; vertical-align:middle; padding-right:0px'>"+str(number)+"<font color='red'><b>&nbsp; &divide;&nbsp;</b></font></td><td style='padding-top:7px; padding-left:0px; padding-right:0px'><u>&nbsp;"+str(numerator)+"&nbsp;</u><br>"+str(denominator)+"</td>"
        self.solution_text = self.solution_text + "<td style='vertical-align:middle'>=</td><td style='text-align:right; vertical-align:middle; padding-left:0px; padding-right:0px'>"+str(number)+"<font color='red'><b>&nbsp; &times;&nbsp;</b></font></td><td style='padding-top:7px; padding-left:0px; padding-right:0px;'><u>&nbsp;"+str(denominator)+"&nbsp;</u><br>"+str(numerator)+"</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='vertical-align:middle'>=</td>"
        self.solution_text = self.solution_text + temp
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + '<br><br><img src="/images/explanation/hint.png" /> <a href="/Learn/Primary-Grade-6/Fractions/Dividing-Whole-Number-by-Proper-Fraction" alt="click for a detailed explanation" title="click for a detailed explanation" target="new"><font style="color:yellow; font-style:oblique; font-size:0.8em;" >Click here for a detailed explanation</font></a>'
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
       
        return self.explain
                    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]        
        except IndexError:
            pass
        try:
            '''self.value1 = str(self.answer1[0])+"/"+str(self.answer1[1])
            self.value2 = str(self.answer2[0])+"/"+str(self.answer2[1])
            self.value3 = str(self.answer3[0])+"/"+str(self.answer3[1])
            self.value4 = str(self.answer4[0])+"/"+str(self.answer4[1])'''
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type,'CheckAnswerType':CheckAnswerType,'grade':6,
                "complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemTypeMCQ1(self):
        ''' 6 &divide; 3/10 '''
        self.complexity_level = "easy"
        self.HCScore = 3
        self.denominator = random.choice([2,3,4,5,6,7,8,9,10,11,12])
        self.numerator = randint(1,self.denominator-1)
        self.number = randint(1,10)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+str(self.number)+"&nbsp;</td>"
        self.problem = self.problem + "<td> &divide; &nbsp;</td>"   
        
        self.problem = self.problem + "<td style='text-align:center'><u>&nbsp;"+str(self.numerator)+"&nbsp;</u><br>"+str(self.denominator)+"</td>"
        self.problem = self.problem + "<td>&nbsp;=</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.AnswerDenominator = self.numerator
        self.AnswerNumerator = self.number * self.denominator
        
        gcf = LcmGcf.LcmGcf().find_gcf(self.AnswerNumerator, self.AnswerDenominator)

        '''Simplifying the fraction if possible'''
        self.SimpleAnswerNumerator = self.AnswerNumerator/gcf
        self.SimpleAnswerDenominator = self.AnswerDenominator/gcf
        
        self.answer1 = self.AnswerNumerator
        self.answer2 = self.AnswerDenominator 
        
        self.SimpleAnswer1 = self.SimpleAnswerNumerator
        self.SimpleAnswer2 = self.SimpleAnswerDenominator
        self.answer = [0,self.SimpleAnswer1,self.SimpleAnswer2]
        
        self.wrongAnswers = []
        '''generating 5 wrong answers and making sure any of it is not equal to the correct answer'''
        i = 0
        while i!=3:
            self.WrongNumerator = randint(1,12)
            self.WrongDenominator = randint(2,12)
            if(Decimal(self.WrongNumerator)/Decimal(self.WrongDenominator)!=Decimal(self.SimpleAnswer1)/Decimal(self.SimpleAnswer2)):
                i = i+1
                self.wrongAnswers.append([0,self.WrongNumerator,self.WrongDenominator])
        self.wrongAnswers.append([0,self.SimpleAnswerNumerator+1,self.AnswerDenominator+1])
        self.wrongAnswers.append([0,self.SimpleAnswerNumerator,self.SimpleAnswerDenominator+1])
                
        self.template = "FractionMCQTypeProblems.html"
        self.problem_type = "ProblemTypeMCQ1"
        self.CheckAnswerType = 2
        self.grade = 6
                
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer1,self.answer2,self.number,self.numerator,self.denominator,self.AnswerNumerator,self.AnswerDenominator)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)
          
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        if CheckAnswerType==2:
            answer=str(answer)
            return answer==InputAnswer
        else:
            try:
                AnswerNumerator = str(answer).partition("/")[0]
                AnswerDenominator = str(answer).partition("/")[2]

                if " " in str(InputAnswer):             
                    InputMixed = int(str(InputAnswer).partition(" ")[0])
                    RemainingInput = str(InputAnswer).partition(" ")[2]
                    InputDenominator = int(str(RemainingInput).partition("/")[2])
                    InputNumerator = int(str(RemainingInput).partition("/")[0])+InputMixed*InputDenominator
                elif "/" in str(InputAnswer):
                    InputMixed = 0
                    InputNumerator = int(str(InputAnswer).partition("/")[0])
                    InputDenominator = int(str(InputAnswer).partition("/")[2])
                else:
                    InputNumerator = int(str(InputAnswer))
                    InputDenominator = 1
                if InputDenominator == 0:
                    return False
                else:
                    return Decimal(AnswerNumerator)/Decimal(AnswerDenominator)==Decimal(InputNumerator)/Decimal(InputDenominator)
            except ValueError:
                return False