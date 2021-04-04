import argparse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

parser = argparse.ArgumentParser( formatter_class=argparse.RawDescriptionHelpFormatter,
description=("""
Examples:
.
.
.
"""))

parser.add_argument("-f", action='store', type=str,  default="", dest="file",  help="file with urls")
parser.add_argument("-v", action='store', type=int,  default=0, dest="verbose",  help="verbose, default off (=0)")
args = parser.parse_args()
verbose = args.verbose

def MakeReqs(url):

	##URL
	try:
		ReqNoHeader = requests.get(url, allow_redirects=False, verify=False, stream=True)
		SizeNoHeader = ReqNoHeader.headers['Content-length']
		CodeNoHeader = ReqNoHeader.status_code
	except:
		try:
			response = requests.get(url, allow_redirects=False, verify=False)
			SizeNoHeader = len(response.content)
			CodeNoHeader = response.status_code
		except:
			CodeNoHeader = 0
			SizeNoHeader = 0
			if verbose:
				print ("req error")

	## localhost-Header
	try:
		ReqLocalhostHeader = requests.get(url, allow_redirects=False, verify=False, stream=True, headers={'Host': 'localhost'})
		SizeLocalhostHeader = ReqLocalhostHeader.headers['Content-length']
		CodeLocalhostHeader = ReqLocalhostHeader.status_code
	except:
		try:
			response = requests.get(url, allow_redirects=False, verify=False, headers={'Host': 'localhost'})
			SizeLocalhostHeader = len(response.content)
			CodeLocalhostHeader = response.status_code
		except:
			SizeLocalhostHeader = 0
			CodeLocalhostHeader = 0
			if verbose:
				print ("req error")

	## 127.0.0.1-Header
	try:
		ReqIPv4 = requests.get(url, allow_redirects=False, verify=False, stream=True, headers={'Host': '127.0.0.1'})
		SizeIPv4 = ReqIPv4.headers['Content-length']
		CodeIPv4 = ReqIPv4.status_code
	except:
		try:
			response = requests.get(url, allow_redirects=False, verify=False, headers={'Host': '127.0.0.1'})
			SizeIPv4 = len(response.content)
			CodeIPv4 = response.status_code
		except:
			SizeIPv4 = 0
			CodeIPv4 = 0
			if verbose:
				print ("req error")

	## [::1]-Header
	try:
		ReqIPv6 = requests.get(url, allow_redirects=False, verify=False, stream=True, headers={'Host': '[::1]'})
		SizeIPv6 = ReqIPv6.headers['Content-length']
		CodeIPv6 = ReqIPv6.status_code
	except:
		try:
			response = requests.get(url, allow_redirects=False, verify=False, headers={'Host': '[::1]'})
			SizeIPv6 = len(response.content)
			CodeIPv6 = response.status_code
		except:
			SizeIPv6 = 0
			CodeIPv6 = 0
			if verbose:
				print ("req error")

	return(SizeNoHeader, CodeNoHeader, SizeLocalhostHeader, CodeLocalhostHeader, SizeIPv4, CodeIPv4, SizeIPv6, CodeIPv6)


if args.file == "":
	print ("please add a file with urls, with  -f /path/to/file.txt")
	exit()

with open(args.file,'r') as f:
	urls = f.read().splitlines()

for i in range(len(urls)):
	SizeNoHeader, CodeNoHeader, SizeLocalhostHeader, CodeLocalhostHeader, SizeIPv4, CodeIPv4, SizeIPv6, CodeIPv6 = MakeReqs(urls[i])

	#check for diffrent sizes
	if ((SizeNoHeader != SizeLocalhostHeader or SizeNoHeader != SizeIPv4 or SizeNoHeader != SizeIPv6) and (CodeLocalhostHeader not in(400,401,403) or CodeIPv4 not in(400,401,403) or CodeIPv6 not in(400, 401, 403))):
		print (urls[i],";",CodeNoHeader,";",SizeNoHeader,";",CodeLocalhostHeader,";",SizeLocalhostHeader,";",CodeIPv4,";",SizeIPv4,";",CodeIPv6,";",SizeIPv6)
	else:
		if verbose:
			print ("all good no ssrf")
