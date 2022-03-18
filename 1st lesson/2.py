total_secunds = int(input('Input time in seconds: '))
hours = total_secunds // 3600
minutes = (total_secunds - hours * 3600) // 60
seconds = total_secunds - (hours * 3600 + minutes * 60)
print('time in hour : minuts : seconds is ',hours,minutes,seconds, sep=':')