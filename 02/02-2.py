from utils import read_txt_as_str

PASSWORDS_FILEPATH = 'password_policies.txt'

policies = read_txt_as_str(PASSWORDS_FILEPATH)
print(policies)

valid_passwords = 0

def parse_policy(policy):
    positions, policy_char, password = policy.split(' ')

    positions = tuple(positions.split('-'))
    policy_char = policy_char[0]

    return int(positions[0]), int(positions[1]), policy_char, password

for policy in policies:
    # get policy components
    first_position, second_position, policy_char, password = parse_policy(policy)

    if len(password) < first_position: # there are not enough characters in password to check
        first_position = False
    elif password[first_position - 1] != policy_char:
        first_position = False
    else:
        first_position = True

    if len(password) < second_position:  # there are not enough characters in password to check
        second_position = False
    elif password[second_position - 1] != policy_char:
        second_position = False
    else:
        second_position = True

    if first_position != second_position: # XOR, or only one is True
        valid_passwords += 1

print(valid_passwords)