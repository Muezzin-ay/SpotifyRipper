import urllib.request
import re
pattern = r'loading="eager" src="([^ ]*)"'

#do not know why, but it works
req = urllib.request.urlopen('https://open.spotify.com/track/1qsexgIQui6hZ8tAGoEg4G').read().decode('utf-8').encode('cp850','replace').decode('cp850')


result = re.findall(pattern,req)
print(result)