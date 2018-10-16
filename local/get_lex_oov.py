import sys

if len(sys.argv) != 3:
    print('usage: python get_lex_oov.py <G2P output lexicon with 3 columns>  <output lexicon.txt in 2 columns>')
    sys.exit()


fin = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'a')

for l in fin:
  arr = l.split("\t")
  if not arr[2].strip()=="":
    fo.write(arr[0] + "  " + arr[2]);

fin.close()
fo.close()
