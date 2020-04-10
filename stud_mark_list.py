class students:
    def __init__(self):
         self.stud_names_list = []
         self.stud_name_mark = []
         self.total_Marks_List = []

    def getDetails(self):
        self.name = ''
        self.marks=[]
        self.name = input("Enter Student Name:")
        self.stud_total=0
        no_of_subjects = int(input("Enter the number of subjects :"))
        print("Enter the marks :")
        for i in range(no_of_subjects):
            temp=int(input("Mark :"))
            self.marks.append(temp)
            self.stud_total+=temp
        self.stud_names_list.append(self.name)
        self.total_Marks_List.append(self.stud_total)
        self.stud_name_mark.append(self.name)
        self.stud_name_mark.append(self.marks)
        print(self.stud_name_mark)
    def displayTotal(self):
        for i,k in (self.stud_names_list):
            print("Name :",self.stud_names_list[i]," -> Total Mark Obtained :",self.total_Marks_List[i])
S = students()
while(True):
    f = input("Want to Add Student and Marks? Y or N :")
    if f == 'N':
        break
    S.getDetails()
S.displayTotal()