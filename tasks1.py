class Onlinecourse:
    def __init__(self,course,name,reg_num):
        self.course =course
        self.name = name
        self.reg_numn = reg_num

general = Onlinecourse('mathematics',"ma'awiya jibrin","0001")
print(f"my course of study is :{general.course} and my name is:{general.name} and my matric_num is:{general.reg_numn}")
        