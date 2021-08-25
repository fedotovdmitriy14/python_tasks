ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")

import re

def travel(r, zipcode):
    if zipcode == '':
        return ':/'
    r = r.split(',')
    no_result = zipcode + ':/'
    zipcode = zipcode.split()
    result = []
    result2 = '/'
    counter = 0
    final_code = ''
    for i in r:
        i = i.split()
        if i[-1] == zipcode[1] and i[-2] == zipcode[0]:
            if counter == 0:
                result += (zipcode)
                result += (':')
                counter += 1
            result += i[1:-2]
            result += ','
            result2 += " " + i[0] + ','
    result = ' '.join(str(item) for item in result)
    if len(result) == 0:
        return no_result
    else: 
        final_code = result + result2
        final_code = final_code.replace(' ,/ ', '/')
        final_code = final_code.replace(' : ', ':')
        final_code = final_code.replace(', ', ',')
        final_code = final_code.replace(' ,', ',')
        final_code = final_code.rstrip(',')
        return final_code
    
        


print(travel(ad, "AA 45522"))


import re

# print(len(re.findall('AA 45522', ad)))


# a = ['st', 'sg']
# b = 'a'
# print(b + ' '.join(str(item) for item in a))