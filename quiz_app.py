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
            
    #profession= sys.argv[1]
    #num_qos=int(sys.argv[2])
    profession= sys.argv[0]
    num_qos=sys.argv[1]
    num_qos=int(num_qos)

    with open(rf'questions\{profession}.txt') as file:
        sum=0
        for line in range(num_qos+1):
            question,answer=line.split('?')
            nothing,correct_answer,options=answer.split(';')
            options_list=options.split(',')
            random.shuffle(options_list)
            file.write(line)
            ans=int(sys.argv)
            if(ans==1):
                sum+=1
            
        print(f"You answered {sum}/{num_qos} correct answers")

            
    pass


if __name__ == '__main__':
    main()
