import ast

def compute(codes, int_code): # RDD, 4, 1234
    pointer = True # True = Front, False = Rear
    for code in codes: # R D D
        if code == 'R':
            if pointer: # if Front
                pointer = False
            else:
                pointer = True
        else:   # 만약 삭제 연산일 경우
            if int_code: # 비어 있지 않을 경우
                if pointer: # 앞을 가리킬 경우
                    int_code.pop(0)
                else:
                    int_code.pop(-1)
            else: # 비어 있는 경우
                return [], False
    if int_code and pointer == False:
        int_code.reverse()
    return int_code, True

test_case = int(input())

results = []
corrects= []

for i in range(test_case):
    codes = list(input()) # RDD
    seq_len = int(input()) # 4
    int_code = ast.literal_eval(input()) # 1, 2, 3, 4
    
    result, correct = compute(codes, int_code)
    results.append(result)
    corrects.append(correct)

for i in range(test_case):
    if corrects[i]:
        print(results[i])
    else:
        print('error')
