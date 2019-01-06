
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

s = 'python\fis\tawesome\r\n'

print(clean_spaces(s))