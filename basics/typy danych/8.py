'''Dany jest napis: s = 'qwerty123!@#'

Wyświetl napis pisany wielkimi literami. Skorzystaj z metody upper.
Usuń z napisu literę e. Skorzystaj z metody replace.
Sprawdź czy znak '@' znajduje się w napisie. Skorzystaj z operatora in.
'''

s = "qwerty123!@#"

s=s.replace("e","")
print(s.upper())

if "@" in s:
    print("Małpa jest w napisie")
else:
    print("Małpy nie ma")