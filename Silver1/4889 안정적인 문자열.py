# Input & Calculate
count = 0
score = 0
answer = []
while(True):
    # Input
    test = list(input()) # Input as list
    if test[0] == '-':
        break
    count += 1

    # Calculate
    idx_last = len(test) - 1 # Get the final index of the string
    idx = 0
    # Delete pairs
    while(idx != idx_last):
        if test[idx] == '{' and test[idx+1] == '}':
            test.pop(idx+1)
            test.pop(idx)
            idx_last = len(test) - 1
            idx = 0
            if idx_last == -1:
                break
        else:
            idx += 1
    
    # Calculate Answer
    score = 0
    test_len = len(test)
    
    for i in range(0, int(test_len/2)):
        if test[i*2] != '{':
            score += 1
        if test[i*2+1] != '}':
            score += 1
    answer.append(score)

# Output
for i in range(0, count):
    print(str(i+1)+'. ' + str(answer[i]))
