alphabet = 'abcdefghijklmnopqrstuvwxyz'

def binaryconverter(x):
    L1=[]
    for k in range(len(x)):
        L=[]
        for i in range(0,len(x[k])-1):
            if x[k][i].isalpha() and x[k][i+1].isalpha():
                L.append(1)
            if x[k][i].isalpha() and not x[k][i+1].isalpha():
                L.append(0)
        if x[k][-1].isalpha():
            L.append(1)
        L1.append(L)
    return L1

def length(region):
    length = 1   
    for term in region:
        if term == "None":
            length = length*2
    return length

def partof(term,expanded_regions):
    Truth = True
    overlying_regions = []
    for region in expanded_regions:
        for i in range(0,len(term)):
            if region[i] == "None":
                Truth = True
            elif term[i] != region[i]:
                Truth = False
                break
        if Truth and (region == term):
            Truth = False
        elif Truth:
            overlying_regions.append(region)
    return [overlying_regions,Truth]

def termcombiner(l):
    n = len(l[0])
    for i in range(0,n): # i iterates over the indexes of each minterm
        n1 = len(l)
        for j in range(0,n1): # j iterates over whole list l which has all minterms possible till computing a particular i.
            # creating copy of element l[j]
            p = []
            for element in l[j]:
                p.append(element)
            # deepcopy complete
            if p[i] != "None":
                p[i] = (0,1)[p[i]==0] # swapping 1 to 0 and 0 to 1 for ith element of term.
                if (p in l):
                    p[i] = "None"
                    if p not in l:
                        l.append(p)
    l1 = []
    for term in l:
        k = term
        if not(partof(k,l)[1]) and ("None" in k):
            l1.append(k)
    return l1

def constituents(expanded_region):
    n = len(expanded_region)
    c = []
    c.append(expanded_region)
    for i in range(n):
        if expanded_region[i] == "None":
            c_copy = []
            for element in c:
                c_copy.append(element)
            for j in range(len(c_copy)):
                term = c_copy[j]
                term1 = []
                for element in term:
                    term1.append(element)
                term1[i] = 0
                c.append(term1)
                term2 = []
                for element in term:
                    term2.append(element)
                term2[i]= 1
                c.append(term2)
                c.remove(term)
    return c

def largest_region(regions):
    lsize = 0
    lregion = []
    for region in regions:
        if lsize< length(region):
            lsize = length(region)
            lregion = region
    return lregion
            

def helperf(true,dc):
    l = true + dc
    if len(l) == 0:
        return l
    trueterms = binaryconverter(true)
    legalterms = binaryconverter(l)
    expanded_regions = termcombiner(legalterms)
    copytrueterms = binaryconverter(true)
    expanded_terms = []
    final_terms = []
    cterms = []
    for term in trueterms:
        regions = partof(term,expanded_regions)[0]
        expanded_terms.append(regions)
        cterms.append(regions)
    for i in range(len(copytrueterms)):
        term =copytrueterms[i]
        regions = cterms[i]
        if term in trueterms:
            if "None" not in largest_region(regions):
                final_terms.append(regions[0])
                trueterms.remove(term)
            elif len(regions) == 1:
                region = largest_region(regions)
                final_terms.append(region)
                ac = []
                bc = []
                for j in range(len(trueterms)):
                    if trueterms[j] in constituents(region):
                        ac.append(trueterms[j])
                        bc.append(expanded_terms[j])
                for k in ac:
                    try:
                        trueterms.remove(k)
                    except ValueError:
                        pass
                for t in bc:
                    try:
                        expanded_terms.remove(t)
                    except ValueError:
                        pass
    copytrueterms = []
    for elements in trueterms:
        copytrueterms.append(elements)
    for i in range(len(copytrueterms)):
        term =copytrueterms[i]
        regions = expanded_terms[i]
        if term in trueterms:
            if "None" not in largest_region(regions):
                final_terms.append(regions[0])
                trueterms.remove(term)
            else:
                region = largest_region(regions)
                final_terms.append(region)
                ac = []
                bc = []
                for j in range(len(trueterms)):
                    if trueterms[j] in constituents(region):
                        ac.append(trueterms[j])
                        bc.append(expanded_terms[j])
                for k in ac:
                    try:
                        trueterms.remove(k)
                    except ValueError:
                        pass
                for t in bc:
                    try:
                        expanded_terms.remove(t)
                    except ValueError:
                        pass
    return final_terms

def alphabet_converter(expandedterms):
    alphabet_terms = []
    for j in range(0,len(expandedterms)):
        alphabet_term = ""
        for i in range(0,len(expandedterms[j])):
            if expandedterms[j][i] == 1:
                alphabet_term = alphabet_term + alphabet[i]
            elif expandedterms[j][i] == 0:
                alphabet_term = alphabet_term + alphabet[i]+"'"
        if alphabet_term == "":
            alphabet_term = "None"
        alphabet_terms.append(alphabet_term)
    return alphabet_terms

def opt_function_reduce(func_TRUE, func_DC):
    optimized_minterms = helperf(func_TRUE,func_DC)
    return alphabet_converter(optimized_minterms)

print(opt_function_reduce(["a'b'c", "a'bc", "a'bc'", "ab'c'"],["abc'"]))

        


