import fileinput

def compress(s):
    p = s[0]
    n = 0
    out = []
    for c in s:
        if c == p:
            n += 1
        else:
            if n == 1:
                out.append(p)
            else:
                out.append(''.join((str(n), p)))
            n = 1
            p = c
    if n == 1:
        out.append(p)
    else:
        out.append(''.join((str(n), p)))
    return ''.join(out)

def run(fname):
    for line in open(fname):
        print(compress(line.strip()))
       
run("compress.in")