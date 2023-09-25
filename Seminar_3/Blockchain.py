import sys
import datetime
import hashlib

# hash('apple') = 1324654czxczxczdvzjkhfkjsdhf
# hash('banan') = asfdsf6+s46df4ds4f5sdff

#Classes
class Block(object):
    #Properties
    block_no = 0
    data = "G"
    next = None
    hash = None
    previous_hash = 0x0
    timestamp=0

    def __init__(self, data, block_no,timestamp): #Input arguments
        self.data = data
        self.block_no = block_no
        self.timestamp = datetime.datetime.now()

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.block_no).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8')
        )
        return h.hexdigest()

    def str(self):
        return "--------------"+"\nBLOCK HASH: " + str(self.hash()) + "\nBLOCK NO: " + str(self.block_no) + "\nBLOCK DATA: " + self.data + "\nTIME STAMP: " + str(self.timestamp) +"\n--------------"


class Blockchain(object):

    diff = 20
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    chain = []
    chain.append(Block("РќР°С‡Р°Р»Рѕ РіРѕР»РѕСЃРѕРІР°РЅРёСЏ", 1,0))

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block = self.block.next

    def mine(self, block):
        self.chain.append(block)


def main():
    menu()


def menu():


    print("\n\n***** Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ РІ СЃРёСЃС‚РµРјСѓ РіРѕР»РѕСЃРѕРІР°РЅРёСЏ РЅР° РѕСЃРЅРѕРІРµ Р±Р»РѕРєС‡РµР№РЅР° *****")
    print()

    choice = input("""
                      A: Р’С…РѕРґ
                      B: Р’С‹С…РѕРґ
                      РџРѕР¶Р°Р»СѓР№СЃС‚Р°, РІС‹Р±РµСЂРёС‚Рµ РІР°С€Рµ РґРµР№СЃС‚РІРёРµ: """)

    if choice == "A" or choice == "a":
        login()

    elif choice == "B" or choice == "b":
        print("\n********* Р’С‹ РІС‹С€Р»Рё РёР· СЃРёСЃС‚РµРјС‹ **********")
        sys.exit()

    else:
        print("РќР°РґРѕ РЅР°РїРёСЃР°С‚СЊ РёРјРµРЅРЅРѕ РёР»Рё A РёР»Рё B Р°РЅРіР»РёР№СЃРєРёРјРё Р±СѓРєРІР°РјРё")
        print("РџРѕРїСЂРѕР±СѓР№С‚Рµ РµС‰Рµ")
        menu()


def login():
    print("\n\n************** Р’С‹ РІРѕС€Р»Рё РЅР° СЃС‚СЂР°РЅРёС†Сѓ Р°РІС‚РѕСЂРёР·Р°С†РёРё ***************")
    print()

    id=input("\n Р’РІРµРґРёС‚Рµ РІР°С€ СѓРЅРёРєР°Р»СЊРЅС‹Р№ С†РёС„СЂРѕРІРѕР№ РЅРѕРјРµСЂ:")


    if id == "1234": #Default ID
        vote()

    else:
        print("Р’С‹ РІРІРµР»Рё РЅРµСЃСѓС‰РµСЃС‚РІСѓСЋС‰РёР№ С†РёС„СЂРѕРІРѕР№ РЅРѕРјРµСЂ")
        print("РџРѕРїСЂРѕР±СѓР№С‚Рµ РµС‰Рµ")
        menu()

def vote():
    print("\n\n************* Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ РЅР° СЃС‚СЂР°РЅРёС†Сѓ РіРѕР»РѕСЃРѕРІР°РЅРёСЏ ***************")
    print()

    yvote = input("\n Р—Р° РєРѕРіРѕ РІС‹ С…РѕС‚РёС‚Рµ РѕС‚РґР°С‚СЊ СЃРІРѕР№ РіРѕР»РѕСЃ:\n"
               "A. РРѕСЃРёС„ РџСЂРёРіРѕР¶РёРЅ\n"
               "B. Р•РІРіРµРЅРёР№ РџСЂРёРіРѕР¶РёРЅ\n"
               "РЎРґРµР»Р°Р№С‚Рµ СЃРІРѕР№ РІС‹Р±РѕСЂ:")


    if yvote == "A" or yvote == "a" or yvote == "B" or yvote == "b":
        if yvote == "A" or yvote == "a":
            vote_name = "РРѕСЃРёС„ РџСЂРёРіРѕР¶РёРЅ"
        else:
            vote_name = "Р•РІРіРµРЅРёР№ РџСЂРёРіРѕР¶РёРЅ"

        print("\n--------------")
        print("Р’Р°С€ РіРѕР»РѕСЃ СѓС‡С‚РµРЅ. РџРѕРґРѕР¶РґРёС‚Рµ РїРѕРєР° РґСЂСѓРіРёРµ СѓР·Р»С‹ СЃРѕРµРґРёРЅСЏС‚СЃСЏ....")
        print("--------------")
        print("РўРµРєСѓС‰РёР№ Р±Р»РѕРєС‡РµР№РЅ :")

        blockchain = Blockchain()

        block = Block(vote_name, len(blockchain.chain)+1,datetime.datetime.now())
        blockchain.mine(block)

        for id in range(len(blockchain.chain)):
            print(blockchain.chain[id].str()) #Prints blockchain details

        print("Р”Р»РёРЅР° С†РµРїРё: ")
        print(len(blockchain.chain)) # Prints blockchain length

        print("\n--------------")
        print("\n РЎРїР°СЃРёР±Рѕ, РІС‹ СѓСЃРїРµС€РЅРѕ РїСЂРѕРіРѕР»РѕСЃРѕРІР°Р»Рё Рё РІР°С€ СЂРµР·СѓР»СЊС‚Р°С‚ Р±С‹Р» РґРѕР±Р°РІР»РµРЅ РІ Р±Р»РѕРєС‡РµР№РЅ.")
        print("\n Р’С‹ РїРµСЂРµРЅР°РїСЂР°РІР»СЏРµС‚РµСЃСЊ РЅР° РґРѕРјР°С€РЅСЋСЋ СЃС‚СЂР°РЅРёС†Сѓ.")

        menu()

    else:
        print("Р’С‹ РІРІРµР»Рё РЅРµРєРѕСЂСЂРµРєС‚РЅС‹Р№ РІР°СЂРёР°РЅС‚ РіРѕР»РѕСЃРѕРІР°РЅРёСЏ")
        print("РџРѕРїСЂРѕР±СѓР№С‚Рµ РµС‰Рµ")
        vote()


main()