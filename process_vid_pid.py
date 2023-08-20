import re
last_vid = None
with open('usb.ids') as f:
  for line in f:
    if len(line)==0:
      continue
    if line[0] != '\t':
      m = re.findall(r'([0-9A-Fa-f]+)\s+.*', line)
      if len(m) == 1:
        last_vid = m[0]
    if line[0] == '\t':
      dat = line.strip().split()
      print('v'+last_vid.upper() + 'p' + dat[0].upper()+'d'+'\t'+' '.join(dat[1:]))

