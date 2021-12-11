# Password-Cracking-Tutorial

## What is Password cracking?
In a general sense, password cracking is the process of using an application program to identify and recover passwords from a computer or network resource.

## What does this mean?

With this information, malicious actors can undertake a range of criminal activities where they can gain unauthorised access to restricted resources for identity theft and fraud. 

## What makes a strong password?
Password crackers can decipher passwords in a matter of days or hours, depending on how weak or strong the password is.  To make a password stronger and more difficult to uncover, a plaintext password should adhere to the following 6 rules!

### 1. Be at least 12 characters long:
*  The shorter a password is, the easier and faster it will be cracked.

### 2. Combine letters and a variety of characters.
*  Using numbers and special characters, such as periods and commas, increases the number of possible combinations.

### 3. Avoid reusing a password. 
* If a password is cracked, then a person with malicious intent could use that same password to easily access other password-protected accounts the victim owns.

### 4. Pay attention to password strength indicators.
* Some password-protected systems include a password strength meter, which is a scale that tells users when they have created a strong password.

### 5. Avoid easy-to-guess phrases and common passwords.

* Weak passwords can be a name, a pet's name or a birthdate -- something personally identifiable. Short and easily predictable patterns, like 123456, password or qwerty, also are weak passwords.

### 6. Use encryption (2FA).

* Enable 2 Factor Autentication to secure your passwords on all your accounts. 
* Take advantage of password creation tools and managers. 


##  Password cracking attacks

You might have two choices either a dictionary attack or brute force attack. 

So whats faster?

Well, a dictionary attack is much faster than a brute force attack where success is determined by the password list size. 

## Password dictionaries + leaked passwords by skullsecurity.org

* John the Ripper	
* Cain & Abel	
* Conficker worm	
* 500 worst passwords	
* 370 Banned Twitter passwords

Resource can be found here Wiki(2021).https://wiki.skullsecurity.org/index.php/Passwords#Password_dictionaries. Date Accessed:11/12/21

## Resources (Password creation tools + managers)

DashLane(2021). https://www.dashlane.com/features/password-generator . Date Accessed: 11/12/21
Howsecureismypasssword(2021). https://howsecureismypassword.net/ . Date Accessed: 11/12/21
Diceware(2021). https://diceware.dmuth.org/ . Date Accessed: 11/12/21

## Lets Build our own || I/O + Testing 

## Input

```
"""
Method 1: Provide a input and output the hexadecimal equivalent of the encoded value.

"""
# initializing string
str2hash = "qwerty"
  
# encoding qwerty using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())

```
## Output

Heres what the example output should look like

* The hexadecimal equivalent of hash is : d8578edf8458ce06fbc5bb76a58c5ca4

## Input

```
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
                        print(f'[+] Password has been found: {word}')
                        exit(0)
                else:
                        print(f'[-] Guess: {word} incorrect... {guess}')
        print(f'Password not found in wordlist...')
if __name__ == '__main__':
        main()

```
## Output

Heres what the example output should look like 

* [+] Password has been found: 011584wb

## Input

```
"""
Method 3: WordList 
Check to see if the hash is included in md5, sha1, sha224, sha256, sha384, sha512.
"""
def passCrack(inputPass):
    
    #file=open(filename,errors="ignore")
    try:
        passFile = open("wordlist.txt", "r", encoding="utf-8")
    except:
        print(" Oh oh... We could not find the file. Is it the end?")

    for password in passFile:
        
        enc_Passwrd = password.encode("utf-8")
       
        digest = hashlib.md5(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha1(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha512(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha384(enc_Passwrd.strip()).hexdigest().lower()
##        digest = hashlib.sha224(enc_Passwrd.strip()).hexdigest().lower()
        
        if digest == inputPass:
            print("Password has been found: " + password)
            
if __name__ == '__main__':
    #md5 hash
    passCrack("3c9b1a779c22025e758dc0d187517ccd")
```
## Output

Heres what the example output should look like 
* Password has been found: bahamut24ritter

![Capture](https://user-images.githubusercontent.com/91548582/145674386-7786b9bd-3aab-45aa-8c40-732f9eb30c82.PNG)


