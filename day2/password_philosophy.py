
with open('password_philosophy_input.txt', 'r') as infile:
    password_db = infile.read()
    password_db = password_db.split('\n')
    del password_db[-1]

    valid = 0
    invalid = 0

    for row in password_db:
        column = row.split(': ')

        policy = column[0].split(' ')
        password = column[1]

        rule = policy[0]
        char = policy[1]

        min_max = rule.split('-')

        minC = min_max[0]
        maxC = min_max[1]

        filters = [ chars for chars in password if chars == char ]

        counts = len(filters)

        if counts >= int(minC) and counts <= int(maxC):
            #valid = valid + 1 #uncomment for part 1
            pass
        else: 
            #invalid = invalid + 1
            pass
        sub_valid = 0

        if password[int(minC)-1] == char:
            sub_valid = sub_valid + 1
        if password[int(maxC)-1] == char:
            sub_valid = sub_valid + 1
        if sub_valid == 1:
            valid = valid + 1
        else:
            invalid = invalid + 1
    print(f'Valid: {valid} , Invalid: {invalid}')

