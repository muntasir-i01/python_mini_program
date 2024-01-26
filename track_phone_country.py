import phonenumbers

from phonenumbers import geocoder

phone_number = phonenumbers.parse("+917188886660")

print(geocoder.description_for_number(phone_number, 'en'))
