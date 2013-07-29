import requests, sys, time
from time import gmtime, strftime

# configurations
rec_id= ''
tkn = ''
email = ''
domain = ''
sub_name= ''


def get_current_ip():
	r = requests.get('http://api.externalip.net/ip')
	ip = r.text
	return(ip)

def update_ip(rec_id,tkn,email,domain,sub_name,new_ip):
	params = { 'a':'rec_edit', 'tkn': tkn, 'id': rec_id, 'email': email, 'z': domain, 'type':'A', 'name':sub_name, 'content': new_ip, 'service_mode': '1', 'ttl': '1' } 
	r = requests.get('https://www.cloudflare.com/api_json.html', params = params)
	if r.json()['result'] == 'success':
		return True
	else:
		return False

while True:

	current_ip = get_current_ip()
	with open('old_ip.txt', 'r') as f:
		old_ip = f.readline()

	if old_ip == current_ip:
		print("IP-Address not changed - " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	else:	
		if update_ip(rec_id=rec_id, tkn=tkn, email=email, domain=domain, sub_name=sub_name, new_ip=current_ip):
			with open('old_ip.txt', 'w') as f:
				f.write(current_ip)
			print("IP-Address successfully updated!" + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
		else:
			print("A Problem occured!" + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	time.sleep(10)

