from aocd import data, submit

data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def is_valid_order(update, rules):
    rule_set = set(tuple(rule.split('|')) for rule in rules)
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[j], update[i]) in rule_set:
                return False
    return True

def reorder(update, rules):
    rule_set = set(tuple(rule.split('|')) for rule in rules)
    n = len(update)
    update = update[:]
    for i in range(n):
        for j in range(n - 1):
            if(update[j+1], update[j]) in rule_set:
                update[j], update[j+1] = update[j+1], update[j]
    return update

def solve(input_text):
    rules_text, updates_text = input_text.split('\n\n')
    rules = rules_text.split('\n')
    updates = [update.split(',') for update in updates_text.split('\n')]
    valid_middle_pages = []
    invalid_middle_pages = []
    for update in updates:
        if is_valid_order(update, rules):
            middle_index = len(update) // 2
            valid_middle_pages.append(int(update[middle_index]))
        else:
            corrected_update = reorder(update, rules)
            middle_index = len(corrected_update) // 2
            invalid_middle_pages.append(int(corrected_update[middle_index]))
    
    valid = sum(valid_middle_pages)
    invalid = sum(invalid_middle_pages)

    return valid, invalid

valid_ans, invalid_ans = solve(data)
print(f"p1 {valid_ans}")
print(f"p2 {invalid_ans}")
