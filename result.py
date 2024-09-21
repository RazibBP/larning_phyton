class Result_sheet:
    def __init__(self,subject,result,grade):
        self.result =result
        self.grade = grade
        self.subject = subject

    def Result(self):
        print("Subject: ",self.subject," ","Marks:",self.result, " " , "GRADE :",self.grade)


#s2 = Result_sheet("bangla",70,"A")
#s2.Result()