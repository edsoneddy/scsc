import sys
import re
def pro_inp(inp_txt):
    lns = inp_txt.split('\n')
    wrds = []
    cur_wrd = ""
    for ln in lns:
        ln = ln.strip()
        if ln.endswith('-'):
            cur_wrd += ln[:-1]
        else:
            cur_wrd += ln
            wrds.extend(re.sub(r'[^\w-]', ' ', cur_wrd).split())
            cur_wrd = ""
    unq_wrds = set(wrd.lower() for wrd in wrds)
    srt_wrds = sorted(unq_wrds)
    return srt_wrds
def main():
    inp_txt = sys.stdin.read()
    out_wrds = pro_inp(inp_txt)
    for wrd in out_wrds:
        print(wrd)
if __name__ == "__main__":
    main()