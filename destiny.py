import asyncio
import aiodns
import sys
import re

banner = """\u001b[33;1m           
 _/_  __/'    
(/(-_) ///)(/ 
           /  \u001b[0m"""

loop = asyncio.get_event_loop()
resolver = aiodns.DNSResolver(loop=loop)

async def query(name, query_type):
	return await resolver.query(name, query_type)

def getIp(hostname):
	try:
		r = 'host=(.*?),'
		coro = query(hostname, 'A')
		result = loop.run_until_complete(coro)
		x = re.findall(r, str(result[0])) 
		return (x[0])
		
	except:
		pass

def run(hostnames):
	ips = {}

	for host in hostnames:
		host = host.replace("\n","")
		ip = getIp(host)
		
		if ip not in ips:
			ips[ip] = []

		ips[ip].append(host)

	return (ips)

def printResult(ips):
	for ip in ips:
		print(" ")
		print(f"\u001b[32m=> {ip}:\u001b[0m")
		for hosts in ips[ip]:
			print(f"- {hosts}")

def main():
	print(banner)
	hostnames = sys.stdin
	ips = run(hostnames)
	printResult(ips)
	
if __name__ == '__main__':
	main()