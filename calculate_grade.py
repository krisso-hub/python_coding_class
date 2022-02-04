''' A program that calculate grade from input score
    on a ten point scale and print the grade score to student 
    indicating a grade of A or B or C or D or F by Ndubuisi Asogwa
'''
# Grading student's score 
score_num = input("Enter a grade score from (0 to 100): ")
if score_num.isdigit():
    score = int(score_num)
    if score > 100:
        print('invalid score - too large')
        grade = 'invalid'
    elif score > 89:
        print('your score - {grade}')
        grade = 'A'
    elif score > 79:
        grade = 'B'
    elif score > 69:
        grade = 'C'
    elif score > 59:
        grade = 'D'
    elif score >= 0:
        grade = 'F'
    
    else:
        print('invalid score - too small, your score must be positive')
        grade = 'invalid'
else:
    print('Invalid score - your score must a digit from 0 -100 integer')
    grade = 'invalid'
print(f'Grade is ------{grade}')

    

   