from aocd import data, submit

def is_valid_order(update, rules):
    rule_set = set(tuple(rule.split('|')) for rule in rules)
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[j], update[i]) in rule_set:
                return False
    return True

def solve(input_text):
    rules_text, updates_text = input_text.split('\n\n')
    rules = rules_text.split('\n')
    updates = [update.split(',') for update in updates_text.split('\n')]
    valid_middle_pages = []
    for update in updates:
        if is_valid_order(update, rules):
            middle_index = len(update) // 2
            valid_middle_pages.append(int(update[middle_index]))
        else:
            print(update)
    return sum(valid_middle_pages)

ans = solve(data)
#submit(ans)
print(ans)
