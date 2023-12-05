with open("data.txt") as data:
    num_sum = 0
    for line in data:
        number = ""
        for char in line:
            if char.isnumeric():
                number += str(char)
        calibration_value = str(number[:1]) + str(number[-1:])
        num_sum += int(calibration_value)
    print(num_sum)
