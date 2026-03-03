# Implement the keyword encoding and decoding for the Latin alphabet. The keyword cipher uses a keyword to rearrange the letters in the alphabet. You should add the provided keyword at the beginning of the alphabet. A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet. The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.
#
# Encryption:
#
# The keyword is "Crypto"
#
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:
#
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"
#
# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"


class Cipher:

    def __init__(self, keyword):
        self.keyword = keyword
        self.plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyword_upper = keyword.upper()
        result_upper_text = "".join(dict.fromkeys(keyword_upper))
        tail = ""
        for ch in self.plain:
            if ch not in result_upper_text:
                tail += ch
        self.cipher = result_upper_text + tail

    def encode(self, data):
        pass
        # TODO: please add your code here

    def decode(self, data):
        pass
        # TODO: please add your code here