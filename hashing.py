import hashlib
import secrets

password_gebruiker = input('Welk wachtwoord wilt u hashen zonder SALT?\n')
s = "" # GEEN SALT
db_password = password_gebruiker+s # MAAKT 1 VARIABLE VAN WACHTWOORD EN SALT
h = hashlib.md5(db_password.encode()) # HASHING
print(h.hexdigest() + "\nDit wachtwoord is niet veilig in een database, omdat er geen salt bij komt.")

password_gebruiker = input('Welk wachtwoord wilt u hashen met een vaste SALT?\n')
s = "8ld" # SALT
db_password = password_gebruiker+s # MAAKT 1 VARIABLE VAN WACHTWOORD EN SALT
h = hashlib.md5(db_password.encode()) # HASHING
print(h.hexdigest() + "\nDit wachtwoord is veiliger dan plain text maar nog niet veilig genoeg, omdat de salt het zelfde blijft.")    # PRINT HET NIEUWE WACHTWOORD UIT

password_gebruiker = input('Welk wachtwoord wilt u hashen met een random SALT?') # PASSWORD VAN DE GEBRUIKER
s = secrets.token_hex(8) # Door de SALT random te maken is het nieuwe wachtwoord veiliger.
db_password = password_gebruiker+s # MAAKT 1 VARIABLE VAN WACHTWOORD EN SALT
h = hashlib.md5(db_password.encode()) # HASHING
print(h.hexdigest() + "\nHet nieuwe wachtwoord met een random Salt.")    # PRINT HET NIEUWE WACHTWOORD UIT


