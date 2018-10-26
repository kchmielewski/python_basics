import sys


class Cipher:
    def __init__(self):
        self.mod = 26
        self.alphabetUpper = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(self.mod)))
        self.alphabetLower = dict(zip("abcdefghijklmnopqrstuvwxyz", range(self.mod)))

        self.alphabet2Upper = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.alphabet2Lower = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))

        self.swap = dict(zip(
            [ord("ą"), ord("ć"), ord("ę"), ord("ł"), ord("ń"), ord("ó"), ord("ś"), ord("ź"), ord("ż"),
             ord("Ą"), ord("Ć"), ord("Ę"), ord("Ł"), ord("Ń"), ord("Ó"), ord("Ś"), ord("Ż"), ord("Ź")],
            ["a", "c", "e", "l", "n", "o", "s", "z", "z", "A", "C", "E", "L", "N", "O", "S", "Z", "Z"]))

    @staticmethod
    def nwd(a, mod):
        while mod:
            a, mod = mod, a % mod
        return a

    @staticmethod
    def removeEmptyLines(text):
        text2 = text.split('\n')
        text = []
        for sth in text2:
            if sth != '':
                text.append(sth)
        text = '\n'.join(text)
        return text

    def findReverseA(self, a):
        for a2 in range(26):
            if self.nwd(a2, self.mod) == 1 and a * a2 % 26 == 1:
                return a2


class Ceasar(Cipher):
    def encoding(self, public, key):
        encrypted = ""
        public = self.removeEmptyLines(public)
        for letter in public:
            letter = letter.translate(self.swap)
            if letter.isalpha():
                if letter.isupper():
                    encrypted += self.alphabet2Upper[(self.alphabetUpper[letter.translate(self.swap)] + key) % self.mod]
                else:
                    encrypted += self.alphabet2Lower[(self.alphabetLower[letter.translate(self.swap)] + key) % self.mod]
            else:
                encrypted += letter

        with open("crypto.txt", "w", encoding="utf-8") as crypto, open("extra.txt", "w", encoding="utf-8") as extra:
            crypto.write(encrypted)
            for letter in public.strip()[:3]:
                if letter.isalpha():
                    extra.write(letter)

    def decrypting(self, text, key):
        decrypted = ""
        text = self.removeEmptyLines(text)

        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    decrypted += self.alphabet2Upper[(self.alphabetUpper[letter.translate(self.swap)] - key) % self.mod]
                else:
                    decrypted += self.alphabet2Lower[(self.alphabetLower[letter.translate(self.swap)] - key) % self.mod]
            else:
                decrypted += letter

        with open("decrypt.txt", "w", encoding="utf-8") as decrypt:
            decrypt.write(decrypted)

    def cryptoanalysisPublic(self, helper, encrypted):
        i = 0
        encrypted = self.removeEmptyLines(encrypted)

        try:
            text = helper[0]
        except IndexError:
            raise IndexError("File extra.txt is empty!")

        while text != encrypted[0]:
            i += 1

            if helper[0].isupper():
                text = self.alphabet2Upper[(self.alphabetUpper[helper[0].translate(self.swap)] + i) % self.mod]
            else:
                text = self.alphabet2Lower[(self.alphabetLower[helper[0].translate(self.swap)] + i) % self.mod]

        with open("key-new.txt", "w", encoding="utf-8") as keynew:
            keynew.write(str(i))
            self.decrypting(encrypted,i)

    def cryptoanalysisCryptogram(self, encrypted):
        text = ""
        encrypted = self.removeEmptyLines(encrypted)

        with open("decrypt.txt", "w", encoding="utf-8") as decrypt:
            for i in range(26):
                for letter in encrypted:
                    if letter.isalpha():
                        if letter.isupper():
                            text += self.alphabet2Upper[(self.alphabetUpper[letter.translate(self.swap)] - i) % self.mod]
                        else:
                            text += self.alphabet2Lower[(self.alphabetLower[letter.translate(self.swap)] - i) % self.mod]
                    else:
                        text += letter
                decrypt.write(text + "\n")
                text = ""


class Affine(Cipher):
    def encoding(self, public, a, b):
        encrypted = ""

        public = self.removeEmptyLines(public)
        a2 = self.findReverseA(a)

        if self.nwd(a, self.mod) != 1 or a * a2 % 26 != 1:
            raise ValueError("Wrong key!")
        else:
            for letter in public:
                if letter.isalpha():
                    if letter.isupper():
                        encrypted += self.alphabet2Upper[((self.alphabetUpper[letter.translate(self.swap)] * a) + b) % self.mod]
                    else:
                        encrypted += self.alphabet2Lower[((self.alphabetLower[letter.translate(self.swap)] * a) + b) % self.mod]
                else:
                    encrypted += letter

        with open("crypto.txt", "w", encoding="utf-8") as crypto, open("extra.txt", "w", encoding="utf-8") as extra:
            crypto.write(encrypted)
            for letter in public.strip()[:3]:
                if letter.isalpha():
                    extra.write(letter)

    def decrypting(self, text, a, b):
        a2 = self.findReverseA(a)
        b2 = -a2 * b
        decrypted = ""
        text = self.removeEmptyLines(text)

        if self.nwd(a, self.mod) != 1 or a * a2 % 26 != 1:
            raise ValueError("Wrong key!")
        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    decrypted += self.alphabet2Upper[(self.alphabetUpper[letter.translate(self.swap)] * a2 + b2) % self.mod]
                else:
                    decrypted += self.alphabet2Lower[(self.alphabetLower[letter.translate(self.swap)] * a2 + b2) % self.mod]
            else:
                decrypted += letter

        with open("decrypt.txt", "w", encoding="utf-8") as decrypt:
            decrypt.write(decrypted)

    def cryptoanalysisPublic(self, helper, encrypted):
        encrypted = self.removeEmptyLines(encrypted)

        encr1 = encrypted[0]
        encr2 = encrypted[1]

        for a in range(1, self.mod + 1):
            if a % 2 != 0 and a != 13:
                for b in range(1, self.mod + 1):
                    if helper[0].isupper():
                        decr1 = self.alphabet2Upper[(self.alphabetUpper[helper[0].translate(self.swap)] * a + b) % self.mod]
                    else:
                        decr1 = self.alphabet2Lower[(self.alphabetLower[helper[0].translate(self.swap)] * a + b) % self.mod]

                    if helper[1].isupper():
                        decr2 = self.alphabet2Upper[(self.alphabetUpper[helper[1].translate(self.swap)] * a + b) % self.mod]
                    else:
                        decr2 = self.alphabet2Lower[(self.alphabetLower[helper[1].translate(self.swap)] * a + b) % self.mod]

                    if decr1 == encr1 and decr2 == encr2:
                        with open("key-new.txt", "w", encoding="utf-8") as keynew:
                            keynew.write("{} {}".format(a, b))
                            self.decrypting(encrypted, a, b)
                            return

    def cryptoanalysisCryptogram(self, text):
        decrypted = ""
        text = self.removeEmptyLines(text)

        with open("decrypt.txt", "w", encoding="utf-8") as decrypt:
            for a in range(1, self.mod + 1):
                if a % 2 != 0 and a != 13:
                    for b in range(1, self.mod + 1):
                        for letter in text:
                            if letter.isalpha():
                                if letter.isupper():
                                    decrypted += self.alphabet2Upper[(self.alphabetUpper[letter.translate(self.swap)] * a + b) % self.mod]
                                else:
                                    decrypted += self.alphabet2Lower[(self.alphabetLower[letter.translate(self.swap)] * a + b) % self.mod]
                            else:
                                decrypted += letter

                        decrypt.write(decrypted + "\n")
                        decrypted = ""


if "-e" in sys.argv and "-c" in sys.argv:

    ceasar = Ceasar()
    with open("plain.txt", "r", encoding="utf-8") as plain, open("key.txt", "r", encoding="utf-8") as key:
        keys = key.read().split(" ")
        a = int(keys[0])
        if a > 26 or a < 1:
            raise AttributeError("Invalid key!")

        ceasar.encoding(plain.read(), a)

elif "-e" in sys.argv and "-a" in sys.argv:

    aff = Affine()
    with open("key.txt", "r", encoding="utf-8") as key, open("plain.txt", "r", encoding="utf-8") as plain:
        keys = key.read().split(" ")
        a, b = int(keys[0]), int(keys[1])
        if a > 26 or b > 26 or a < 1 or b < 1:
            raise AttributeError("Invalid key!")

        aff.encoding(plain.read(), a, b)

elif "-d" in sys.argv and "-c" in sys.argv:

    ceasar = Ceasar()
    with open("crypto.txt", "r", encoding="utf-8") as crypto, open("key.txt", "r", encoding="utf-8") as key:
        keys = key.read().split(" ")
        a = int(keys[0])
        if a > 26 or a < 1:
            raise AttributeError("Invalid key!")
        ceasar.decrypting(crypto.read(), a)

elif "-d" in sys.argv and "-a" in sys.argv:

    aff = Affine()
    with open("key.txt", "r", encoding="utf-8") as key, open("crypto.txt", "r", encoding="utf-8") as crypto:
        keys = key.read().split(" ")
        a, b = int(keys[0]), int(keys[1])
        if a > 26 or b > 26 or a < 1 or b < 1:
            raise AttributeError("Invalid key!")

        aff.decrypting(crypto.read(), a, b)

elif "-j" in sys.argv and "-c" in sys.argv:

    ceasar = Ceasar()
    with open("extra.txt", "r", encoding="utf-8") as extra, open("crypto.txt", "r", encoding="utf-8") as crypto:
        ceasar.cryptoanalysisPublic(extra.read(), crypto.read())

elif "-j" in sys.argv and "-a" in sys.argv:

    aff = Affine()
    with open("extra.txt", "r", encoding="utf-8") as extra, open("crypto.txt", "r", encoding="utf-8") as crypto:
        aff.cryptoanalysisPublic(extra.read(), crypto.read())

elif "-k" in sys.argv and "-c" in sys.argv:

    ceasar = Ceasar()
    with open("crypto.txt", "r", encoding="utf-8") as crypto:
        ceasar.cryptoanalysisCryptogram(crypto.read())

elif "-k" in sys.argv and "-a" in sys.argv:

    aff = Affine()
    with open("crypto.txt", "r", encoding="utf-8") as crypto:
        aff.cryptoanalysisCryptogram(crypto.read())

else:
    raise AttributeError(
        "Invalid parameters! \n Available parameters: \n -c (Ceasar cipher), \n -a (Affine cipher), \n -e (encoding), "
        "\n -d (decoding), \n -j (cryptoanalysis with text), \n -k (cryptoanalisis - cryptogram)")
