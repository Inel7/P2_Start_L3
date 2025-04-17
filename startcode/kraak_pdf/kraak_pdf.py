import pikepdf
from tqdm import tqdm

passwords = []
for lijn in open("woorden.txt"):
    passwords.append(lijn.strip())

#probeer elk mogelijk wachtwoord
for password in tqdm(passwords):
    try:
        #probeer pdf te decrypteren
        pikepdf.open("hacking.pdf",password=password)
        # als we hier komen is het wachtwoord succesvol gevonden (geen error)
        print("wachtwoord gevonden: ", password)
        break
    except pikepdf._core.PasswordError:
        #fout wachtwoord, doe niets
        pass
