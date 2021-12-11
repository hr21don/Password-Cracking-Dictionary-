import hashlib

"""
Method 1: Provide a input and output the hexadecimal equivalent of the encoded value.

"""
# initializing string
str2hash = "qwerty"
  
# encoding qwerty using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
  
# printing the equivalent hexadecimal value.
print "The hexadecimal equivalent of hash is : ", end =""
print result.hexdigest()


"""
# Method 2: Simple MD5 hash cracker

Tested on passwrd= '011584wb'
passwrd_hash= '5378a9d21949ae0ef0956ef7f5284e9d'
"""
HASH = '5378a9d21949ae0ef0956ef7f5284e9d'
PASSLIST = [
        '011584wb',
        '0148068885',
        '040191flo',
        'password',
        '0508rabbit88'
        '10393Ravens52'
        '1234567Ks123'
        '12qwaszx'
        '12qwaszx'
        '3634819zhang'
        '804139aq'
]

def main():
        for word in PASSLIST:
                guess = hashlib.md5(word.encode('utf-8')).hexdigest()
                if guess.upper() == HASH or guess.lower() == HASH:
                        print f'[+] Password has been found: {word}'
                        exit(0)
                else:
                        print f'[-] Guess: {word} incorrect... {guess}'
        print f'Password not found in wordlist...'
if __name__ == '__main__':
        main()

"""
Method 3: WordList
Check to see if the hash is included in md5, sha1, sha224, sha256, sha384, sha512.
"""
def passCrack(inputPass):
    
    #file=open(filename,errors="ignore")
    try:
        passFile = open("wordlist.txt", "r", encoding="utf-8")
    except:
        print " Oh oh... We could not find the file. Is it the end?"

    for password in passFile:
        
        enc_Passwrd = password.encode("utf-8")
       
        digest = hashlib.md5(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha1(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha512(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha384(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha224(enc_Passwrd.strip()).hexdigest().lower()
        
        if digest == inputPass:
            print "Password has been found: " + password
            
if __name__ == '__main__':
    #md5 hash
    passCrack("3c9b1a779c22025e758dc0d187517ccd")
    


"""
Method 4: Coming Soon! 
"""

