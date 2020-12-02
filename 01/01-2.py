from utils import read_txt_as_int

EXPENSE_REPORT_FILEPATH = 'expense_report.txt'

expenses = read_txt_as_int(EXPENSE_REPORT_FILEPATH)

print(expenses)
expenses = sorted(expenses) # sort in ascending order
print(expenses)

sum_2020 = tuple() # this will hold the found values

"""
A nested for loop would be easier to write, but would result in a lot of
unnecessary iterations. I wanted to find something that would be more efficient.
"""

for i, first_num in enumerate(expenses): # starting with smallest number
    print(f'FIRST: {first_num}')
    j = len(expenses) - 1 # end of list
    while j >= 0:
        second_num = expenses[j]
        print(f'SECOND: {second_num}')
        cur_sum = first_num + second_num
        if cur_sum < 2020:
            # if it were >= 2020, we are already too big for a third number
            for k, third_num in enumerate(expenses, start=i+1):
                print(first_num, second_num, third_num)
                cur_sum = first_num + second_num + third_num
                if cur_sum == 2020:
                    # found them
                    sum_2020 = (first_num, second_num, third_num)
                    break
                elif cur_sum > 2020:
                    # too big, stop and go to the next second number
                    break
        j -= 1

        if sum_2020:
            break

    if sum_2020:
        break

print(sum_2020)
# final answer
print(sum_2020[0] * sum_2020[1] * sum_2020[2])
