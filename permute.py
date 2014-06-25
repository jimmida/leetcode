x = []

def permute(s, prefix):
  if len(s) == 0:
    x.append(prefix)
  for (i,c) in enumerate(s):
    permute(s[0:i]+s[i+1:], prefix+c)