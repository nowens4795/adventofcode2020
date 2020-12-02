from utils import read_txt_as_str

PASSWORDS_FILEPATH = 'password_policies.txt'

policies = read_txt_as_str(PASSWORDS_FILEPATH)
print(policies)

valid_passwords = 0

def parse_policy(policy):
    allowed_range, policy_char, password = policy.split(' ')

    allowed_range = tuple(allowed_range.split('-'))
    policy_char = policy_char[0]

    return int(allowed_range[0]), int(allowed_range[1]), policy_char, password

for policy in policies:
    # get policy components
    min_range, max_range, policy_char, password = parse_policy(policy)

    char_instances = 0
    for i in password:
        if char_instances > max_range:
            # no point in continuing, we have hit our max
            break

        if i == policy_char:
            # increment count of instances
            char_instances += 1

    if min_range <= char_instances <= max_range:
        valid_passwords += 1

print(valid_passwords)