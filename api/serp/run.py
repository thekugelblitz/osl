import sys
import hspl

#query = "indias cheap web hosting"
query = sys.argv[1]
#url = "hostingspell.com"
url = sys.argv[2]

h = hspl.Hspl()
result = h.check(query, url)
print(result)
h.close_browser()