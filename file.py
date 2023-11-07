import string


class SubstitutionCipher:
    """SubstitutionCipher class.

    SubstitutionCipher encrypts message m into cipher-text c and
    decrypts cipher-text c to message m
    """

    def __init__(self, symbol_space, key, output_symbol_space=None) -> None:
        """Create SubstitutionCipher

        :param symbol_space: Symbol space for which the symbols of the plain text messages come from.
        :param key: The key to be applied to the encrypt and decrypt functions. This give the number of shifts across the symbol space.
        :return: encrypted cipher text.
        """

        self.symbol_space = symbol_space
        self.key = key
        if output_symbol_space is None:
            self.output_symbol_space = symbol_space
        else:
            self.output_symbol_space = output_symbol_space

        # A map of an plain text symbol to its encrypted equivalent    
        self.encrypt_symbol_map = {}

        # A map of an cipher text symbol to its unencrypted equivalent 
        self.decrypt_symbol_map = {}

        # TASK - complete code to initialise the map
        # for i in range(len(self.symbol_space)):
        #     # map the  ENCRYPT symbol to output symbol space
        #     # self.encrypt_symbol_map[self.symbol_space[i]] = self.output_symbol_space[]
        #     pass

        # for i in range(len(self.output_symbol_space)):
        #     # map the  DECRYPT symbol to  symbol space
        #     # self.decrypt_symbol_map[self.output_symbol_space[i]] = self.symbol_space[]
        #     pass


    def encrypt(self, plain_text):
        """Encrypt plaintext message to cipher-text

        implements encryption function 𝐸𝑛(𝑥) = (𝑥 + 𝑛) 𝑚𝑜𝑑 𝐿

        :param plain_text: The unencrypted message to be encrypted by cipher.
        :return: encrypted cipher text.
        """
        cipher_txt = ''
        for char in plain_text:
            if char in self.symbol_space:
                enc = self.encrypt_symbol_map[char]
                cipher_txt += enc
            else:
                cipher_txt += char
        return cipher_txt

    def decrypt(self, cipher_txt):
        """Decrypt cipher-text message to plaintext

        implements decryption function D𝑛(𝑥) = (𝑥 - 𝑛) 𝑚𝑜𝑑 𝐿

        :param cipher_txt: The encrypted cipher_txt to be decrypted by cipher.
        :return: unencrypted plain text.
        """
        decrypt_txt = ""
        for char in cipher_txt:
            if char in self.output_symbol_space:
                temp = self.decrypt_symbol_map[char]
            else:
                temp = char
            decrypt_txt += temp
        return decrypt_txt

    def get_symbol_space(self):
        """return the symbol space of the cipher"""
        return self.symbol_space

    def get_key(self):
        """return the key of the cipher"""
        return self.key


#  Use SubstitutionCipher to encrypt 'when in doubt, use bruteforce.' with a key of 16
# TASK - create a SubstitutionCipher from the lower case alphabet symbol space with the key of 16
# s1 = SubstitutionCipher(symbol_space=,key=)

# TASK - encrypt the given text and print it
# c = 

# TASK - verify decryption
# m_ = 
# print(f"'{c}' decrypted to '{m_}'")


# TASK - carry out brute force decryption of PHHW PH DIWHU WKH WRJD SDUWB, provide the Key
