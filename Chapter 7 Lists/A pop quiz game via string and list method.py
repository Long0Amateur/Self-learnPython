# A pop quiz game via string and list method


question =['What is the capital of France?',
            'Which state has only one neighbor?']

answer =['Paris','Maine']

num_right = 0
for i in range(len(question)):
    guess = input(question[i])
    if guess.lower() == answer[i].lower():
        print('Correct')
        num_right+=1
    else:
        print('Wrong. The answer is',answer[i])
    print('You have',num_right,'out of',num_right,'right.')
