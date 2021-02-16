def numKeypadSolutions(wordlist, keypads):
    # Write your code here
    # reduce wordlist to set
    words = [frozenset(w) for w in wordlist]
    # find all the sub strings of keypads with the begining letter
    sub_strings = []
    for k in keypads:
        sub = [k[0]]
        for c in k[1:]:
            sub += [c + i for i in sub]
        sub = [frozenset(i) for i in sub]
        sub_strings.append(sub)
    print(len(sub_strings))
    
    ans = []
    for j in sub_strings:
        count = 0
        for w in words:
            if w in j:
                count += 1
        ans.append(count)
    return ans


wordlist = ['APPLE', 'PLEAS', 'PLEASE']
keypads = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']
numKeypadSolutions(wordlist, keypads)
