with open("input.txt") as f:
    memory = [int(x) for x in f.read().split(',')]

# Part 1
nums = memory.copy()
nums[1] = 12            # Restore codes to values from before the fire
nums[2] = 2             #
code_length = 4
opcodes = list(nums[i:i+code_length] for i in range(0,len(nums), code_length))
for code in opcodes:
    print(80*"=")
    print(nums)
    print("Read in opcode {}".format(code))
    if code[0] == 99:
        print("Code 99: End of program.")
        break
    elif code[0] == 1:
        print("Adding {} and {} into memory at {}".format(nums[code[1]],
                                                          nums[code[2]],
                                                          code[3]))
        nums[code[3]] = nums[code[1]] + nums[code[2]]
    elif code[0] == 2:
        print("Multiplying {} and {} into memory at {}".format(nums[code[1]],
                                                          nums[code[2]],
                                                          code[3]))
        nums[code[3]] = nums[code[1]] * nums[code[2]]
    else:
        print("Something went wrong, opcode unknown. Exiting...")
        exit()

print(80*'~')
print(nums)



# Part 2
nums = memory.copy()
noun = 0
verb = 0
for n in range(0,100):
    for v in range(0,100):
        nums[1] = n
        nums[2] = v
        opcodes = list(nums[i:i+code_length] for i in range(0,len(nums), code_length))
        for code in opcodes:
            if code[0] == 99:
                break
            elif code[0] == 1:
                nums[code[3]] = nums[code[1]] + nums[code[2]]
            elif code[0] == 2:
                nums[code[3]] = nums[code[1]] * nums[code[2]]
            else:
                print("Found wrong opcode: {}".format(code[0]))
                print("Something went wrong, opcode unknown. Exiting...")
                exit()
        if nums[0] == 19690720:
            noun = n
            verb = v
            break
        else:
            nums = memory.copy()
    if nums[0] == 19690720:
        break

print(100*noun+verb)
