#TODO: learn a little more about validation and testing- answer was achieved but code is sloppy. Specifically about exception handling
#Would also want to break out each individual data test rather than have one huge function

def passport_valid_test(data):
    
    if 'cid' in data.keys() and len(data.keys()) == 8:
        return True
    elif 'cid' not in data.keys() and len(data.keys()) == 7:
        return True
    else:
        return False

def passport_data_validation(data):
    eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
    try:
        assert len(data['eyr']) ==4
        assert 2020 <= int(data['eyr']) <= 2030


        assert len(data['byr']) ==4
        assert 1920 <= int(data['byr']) <= 2002

        assert len(data['iyr']) ==4
        assert 2010 <= int(data['iyr']) <= 2020

    #     height tests
        assert data['hgt'][-2:] == 'cm' or data['hgt'][-2:] == 'in'
        if data['hgt'][-2:]=='cm':
            assert 150 <= int(data['hgt'][:-2]) <= 193
        elif data['hgt'][-2:]=='in':
            assert 59 <= int(data['hgt'][:-2]) <= 76

    #     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        assert data['hcl'][0]=='#' and data['hcl'][1:].isalnum()

    #         ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        assert data['ecl'] in eye_colors
    #     pid (Passport ID) - a nine-digit number, including leading zeroes.
        assert len(str(data['pid']))==9
        return True
    except AssertionError as msg:  
#         print(msg)
        return False
    
  
#Assuming a string as input, saved under 'passports'

passport_entry = passports.split('\n\n')

# build the passport database
passport_db = dict()
for i,entry in enumerate(passport_entry):
    split_entry = entry.replace('\n',' ').split()
    passport_db[i]=  {x.split(':')[0] : x.split(':')[1] for x in split_entry}

#Run through each entry and validate the data:
data_validated = 0 
valid_passport = 0
for entry in passport_db:
    data = passport_db[entry]
    is_valid = passport_valid_test(data)
    if is_valid:
        valid_passport += 1
        try:
            assert passport_data_validation(data)
            data_validated += 1
        except AssertionError as msg:  
            pass
    else:
        continue
    
    
print(f'''Q1. Valid Passport Count - {valid_passport} ''')
print(f'''Q2. Data Validated Passport Count - {data_validated} ''')

