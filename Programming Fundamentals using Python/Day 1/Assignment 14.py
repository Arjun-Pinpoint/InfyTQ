'''
JIT University offering degree courses to students has decided to provide scholarship based on the following details:
Branch of study	Score (%)	Scholarship %	Remarks
Arts	Score is at least 90	50	The student is eligible only for one scholarship% even if both the score conditions are valid for the given branch of study. In such cases, students are eligible for the highest scholarship% applicable among the two.
Arts	Score is an odd number	5	
Engineering	Score is more than 85	50	
Engineering	Score is divisible by 7	5	
If there are 500 students who have joined the university, write a pseudo
code to calculate and display the final fees to be paid by each student.
You may accept the branch of study, score and course fee as inputs for each
student and calculate the final fees to be paid by each student based on
formulae given below:
Scholarship amount=course fee * (scholarship%)
Final fee= course fee - scholarship amount
'''
end-if
for (Counter=1, Counter<=500, Counter=Counter+1)
input Branch_Of_Study,Score,Course_Fee
Scholarship=0
if(Branch_Of_Study=="Arts") then
if(Score>=90)then
Scholarship=50
else if(Score %2==0) then
Scholarship=5
end-if
else if(Branch_Of_Study=="Engineering") then
if(Score>85) then
Scholarship=50
else if(Score%7==0) then
Scholarship=5
end-if
end-if
Scholarship_Amount=Course_Fee*Scholarship/100
Final_Fee=Course_Fee - Scholarship_Amount
display Final_Fee
end-for
