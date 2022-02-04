
''' A program that calculate grade from input score
    on a ten point scale and print the grade score to student 
    indicating a grade of A or B or C or D or F by Ndubuisi Asogwa
'''
def main():
    another = 'Y' # declare and initialize a variable
    while another == 'Y':     
# Grading student's score 
        score_num = input("Enter a grade score from (0 to 100): ")
        if not (score_num.isdigit()):
            grade = 'invalid Numeric integer input'
        else:
            score = int(score_num)
            if score > 100:
                grade = 'invalid score - too large'
            elif score > 89:
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
                grade = 'invalid score - too low'
        
        print(f'Grade is ------{grade}')
        another = input('Another run (Y): ')
    print('End the program')
main()

    

   