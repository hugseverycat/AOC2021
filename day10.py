from statistics import median

filename = 'puzzle_input/day10.txt'
#filename = 'puzzle_input/test_input.txt'

my_input = []

with open(filename) as file:
    for line in file:
        my_input.append(line.strip())

corruption_score = 0
incomplete_scores = []

for this_line in my_input:
    brackets = []
    corrupted = False
    for c in this_line:
        if c in ('[', '(', '{', '<'):
            # If it is an opening bracket, add it to the list
            brackets.append(c)
        else:
            # If it is a closing bracket, take the most recent
            # opening bracket and see if it pairs with the closing
            # bracket
            
            compare_c = brackets.pop()
            
            # If the brackets don't pair up, this line is corrupt
            if c == ']' and compare_c != '[':
                corrupted = True
                break
            elif c == '>' and compare_c != '<':
                corrupted = True
                break
            elif c == ')' and compare_c != '(':
                corrupted = True
                break
            elif c == '}' and compare_c != '{':
                corrupted = True
                break

    if corrupted:
        if c == ')':
            corruption_score += 3
        elif c == ']':
            corruption_score += 57
        elif c == '}':
            corruption_score += 1197
        elif c == '>':
            corruption_score += 25137
            
    elif not corrupted:  # This line is incomplete
        score = 0
        while True:
            try:
                # Since we only ever added opening brackets to the list
                # and we removed opening brackets that have a valid pair
                # all we are left with is opening brackets that need a closer.
                # So we'll go through and evaluate their scores, starting with
                # the most recent.
                c = brackets.pop()
                if c == '(':
                    score = score * 5 + 1
                elif c == '[':
                    score = score * 5 + 2
                elif c == '{':
                    score = score * 5 + 3
                else:
                    score = score * 5 + 4
            except IndexError:
                # When there are no more brackets, store the score and move on
                # to the next line in our input
                incomplete_scores.append(score)
                break
                
incomplete_scores.sort()

print("Part 1:", corruption_score)
print("Part 2:", incomplete_scores[median(range(0, len(incomplete_scores)))])

