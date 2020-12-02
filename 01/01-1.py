from utils import read_txt_as_int

EXPENSE_REPORT_FILEPATH = 'expense_report.txt'

expenses = read_txt_as_int(EXPENSE_REPORT_FILEPATH)

print(expenses)
expenses = sorted(expenses) # sort in ascending order
print(expenses)

sum_2020 = tuple() # this will hold the found values

for cur_expense in expenses: # starting with smallest number
    i = len(expenses) - 1 # end of list
    while i >= 0:
        cur_sum = cur_expense + expenses[i]
        print(cur_sum)
        if cur_sum == 2020:
            # found them
            sum_2020 = (cur_expense, expenses[i])
            break
        elif cur_sum < 2020:
            # stop adding from the tail and start with the next number at the head,
            # the sums can only get smaller if we continue
            break
        else:
            # if sum > 2020, keep going
            i -= 1

    if sum_2020:
        break

print(sum_2020)
# final answer
print(sum_2020[0] * sum_2020[1])
