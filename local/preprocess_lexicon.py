import sys

if len(sys.argv) != 4:
    print('usage: python get_lex_oov.py <input raw lexicon file> <reference clean legitimate word list like hunspell> <filtered lexicon for ASR>')
    sys.exit(1)

fin = open(sys.argv[1], 'r')
fdic = open(sys.argv[2], 'r')
fo = open(sys.argv[3], 'w')

dictl = []
for l in fdic:
  dictl.append(l.strip())

for ln in fin:
  word = ln.split()[0]
#  if not arr[2].strip()=="":
  if word in dictl:
    fo.write(ln);
fdic.close()
fin.close()
fo.close()
