
import sys, string

codes   = {}

def frequency (str) :
    freqs = {}
    for ch in str :
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs

def sortFreq (freqs) :
    letters = freqs.keys()
    tuples = []
    for let in letters :
        tuples.append((freqs[let],let))
    tuples.sort()
    return tuples

def buildTree(tuples) :
    while len(tuples) > 1 :
        leastTwo = tuple(tuples[0:2])                  # get the 2 to combine
        theRest  = tuples[2:]                          # all the others
        combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
        tuples   = theRest + [(combFreq,leastTwo)]     # add branch point to the end
        tuples.sort(key=lambda t: t[0])                                # sort it into place
    return tuples[0]            # Return the single tree inside the list

def trimTree (tree) :
     # Trim the freq counters off, leaving just the letters
    p = tree[1]                                    # ignore freq count in [0]
    if type(p) == type("") : return p              # if just a leaf, return it
    else : return (trimTree(p[0]), trimTree(p[1])) # trim left then right and recombine

def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        if not pat:
            codes[node] = '0'
        else:
            codes[node] = pat                # A leaf. set its code
    else  :                              #
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1")    # then do the right branch.

def encode (str) :
    global codes
    output = ""
    for ch in str : output += codes[ch]
    return output

def decode (tree, str) :
    output = ""
    p = tree
    for bit in str :
        if bit == '0' : p = p[0]     # Head up the left branch
        else          : p = p[1]     # or up the right branch
        if type(p) == type("") :
            output += p              # found a character. Add to output
            p = tree                 # and restart for next character
    return output

def main () :
    inputs = ["This is a testtttttttt","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","The bird is the word",""]

    for str in inputs:
        print("--------------------------------------")
        if not str:
            print("Empty String.")
            return
        print("The size of the data is: {}\n".format(sys.getsizeof(str)))
        print("The content of the data is: {}\n".format(str))
        freqs = frequency(str)

        tuples = sortFreq(freqs)
        # for key, value in tuples:
        #    print(f"{key} - {value}")
        tree = buildTree(tuples)

        tree = trimTree(tree)

        assignCodes(tree)

        small = encode(str)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof((small, 2))))
        print("The content of the encoded data is: {}\n".format(small))
        original = decode(tree, small)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(original)))
        print("The content of the encoded data is: {}\n".format(original))


if __name__ == "__main__" : main()