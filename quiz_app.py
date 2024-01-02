import sys
import random


def main():
    # TODO: your code here

    # 1. Get the command line arguments via sys.argv
    
    # 2. Open the correct file open(rf'questions\<filename>.txt)'
    
    # 3. Iterate over the file
        #for line in file:
    
    #       3.1. Parse the line (use s.split())
            
            
    #       3.2 Create a list of options
            

    #       3.3 random.shuffle(l)

    profession= sys.argv[1]
    num_qos=sys.argv[2]
    num_qos=int(num_qos)

    with open(rf'questions\{profession}.txt') as file:

        sum_correctAnswers=0
        sum_questions=0
        options_list=[]

        for line in file:

            line.strip()
            question,correct_answer,options=line.split(';')

            options_list=options.split(',')
            options_list.append(correct_answer)

            random.shuffle(options_list)

            print(question)

            for i in options_list:
                print(i)

            sum_questions+=1

            ans=int(input("Select the correct answer"))

            if(options[ans-1]==correct_answer):
                sum_correctAnswers+=1

            if(sum_questions==num_qos):
                break
            
        print(f"You answered {sum_correctAnswers}/{num_qos} correct answers")
            
    pass


if __name__ == '__main__':
    main()
