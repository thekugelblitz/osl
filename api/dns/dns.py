import json
import sys
import dns.resolver

dmain_name = sys.argv[1]
qtype = sys.argv[2] #'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA'
dns_server_ips = ['1.1.1.1', '8.26.56.26', '8.8.8.8','208.67.222.222', '9.9.9.9','64.6.64.6']
dns_server_names = ['Cloudflare DNS Servers','Comodo Secure DNS', 'Google', 'OpenDNS', 'Quad9', 'Verisign Public DNS']

response = []
j=0
for i in dns_server_ips:
    res = {}
    dns.resolver.namesrvers = i
    answer = dns.resolver.resolve(dmain_name, qtype, raise_on_no_answer=False)
    if answer.rrset is not None:
        record_list = []
        for k in answer.rrset:
            record_list.append(str(k).strip())
    res['records'] = record_list
    response.append(res)
    j=j+1

print(json.dumps(response))