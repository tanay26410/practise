#kmp algorithim
def KMPSearch(s:str, p:str):
    M = len(p)
    N = len(s)
 
    # create lps[] that will hold the longest prefix suffix
    # values for ptern
    lps = [0]*M
    j = 0 # index for p[]
 #no changes 
 
    # Preprocess the ptern (calculate lps[] array)
    computeLPSArray(p, M, lps)
 
    i = 0 # index for s[]
    while i < N:
        if p[j] == s[i]:
            i += 1
            j += 1
 
        if j == M:

            j = lps[j-1]
            return True
        # mismatch after j matches
        elif i < N and p[j] != s[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False
 
def computeLPSArray(p, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if p[i]== p[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
print('No changes')