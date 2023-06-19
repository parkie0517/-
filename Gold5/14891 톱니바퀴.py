def spin(wheel, direction):
    if direction == 1:  # Clockwise
        temp = wheel.pop()
        wheel.insert(0, temp)
    else:               # Cuonterclockwise
        temp = wheel.pop(0)
        wheel.append(temp)
    
    return wheel

# Input the wheel information
wheel_1 = []
temp = str(input())
for i in range(0, 8):
    wheel_1.append(int(temp[i]))

wheel_2 = []
temp = str(input())
for i in range(0, 8):
    wheel_2.append(int(temp[i]))

wheel_3 = []
temp = str(input())
for i in range(0, 8):
    wheel_3.append(int(temp[i]))

wheel_4 = []
temp = str(input())
for i in range(0, 8):
    wheel_4.append(int(temp[i]))

# Input the number K
K = int(input())
task = []
for i in range(0, K):
    wheel, instruction = input().split()
    wheel = int(wheel)
    instruction = int(instruction)

    if wheel_1[2] != wheel_2[6]:
        diff_12 = True
    else:
        diff_12 = False

    if wheel_2[2] != wheel_3[6]:
        diff_23 = True
    else:
        diff_23 = False

    if wheel_3[2] != wheel_4[6]:
        diff_34 = True
    else:
        diff_34 = False

    
    if wheel == 1:      # If the selected wheel is 1
        wheel_1 = spin(wheel_1, instruction)
        if diff_12 == True:
            wheel_2 = spin(wheel_2, instruction*-1)
            if diff_23 == True:
                wheel_3 = spin(wheel_3, instruction)
                if diff_34 == True:
                    wheel_4 = spin(wheel_4, instruction*-1)
    elif wheel == 2:    # If the selected wheel is 2
        wheel_2 = spin(wheel_2, instruction)
        if diff_12 == True:
            wheel_1 = spin(wheel_1, instruction*-1)
        if diff_23 == True:
            wheel_3 = spin(wheel_3, instruction*-1)
            if diff_34 == True:
                wheel_4 = spin(wheel_4, instruction)
    elif wheel == 3:    # If the selected wheel is 3
        wheel_3 = spin(wheel_3, instruction)
        if diff_23 == True:
            wheel_2 = spin(wheel_2, instruction*-1)
            if diff_12 == True:
                wheel_1 = spin(wheel_1, instruction)
        if diff_34 == True:
            wheel_4 = spin(wheel_4, instruction*-1)
    else:
        wheel_4 = spin(wheel_4, instruction)
        if diff_34 == True:
            wheel_3 = spin(wheel_3, instruction*-1)
            if diff_23 == True:
                wheel_2 = spin(wheel_2, instruction)
                if diff_12 == True:
                    wheel_1 = spin(wheel_1, instruction*-1)

score = 0
if wheel_1[0] == 1:
    score += 1
if wheel_2[0] == 1:
    score += 2
if wheel_3[0] == 1:
    score += 4
if wheel_4[0] == 1:
    score += 8

print(score)