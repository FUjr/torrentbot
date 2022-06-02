import re
input = 'details.php?group_id=28223&torrent_id=3'
rex = r'.*torrent_id=(\d{2,5})'
print(re.search(rex,input).group(1))