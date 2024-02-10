import random

class LiuQianLoongYearMagic:
    def __init__(self):
        self.slogan = "见证奇迹的时刻"
        self.cards = []
        self.under_butt_card = ''

    def get_random_length_card(self, length=4):
        suits = ['♠', '♥', '♦', '♣']
        ranks = [str(i) for i in range(2, 11)] + list('JQKA')
        cards = [suit+str(rank) for suit in suits for rank in ranks]
        cards += ['🃏大', '🃏小']
        self.cards = random.sample(cards, length)
        return self.cards

    def split_cards(self):
        self.cards += self.cards
        return self.cards

    def change_cards_index_by_text(self, text: str):
        for i in range(len(text)):
            self.cards.append(self.cards.pop(0))
        return self.cards

    def change_cards_index_by_area(self, north_or_south: str):
        north_or_south = int(north_or_south)
        if north_or_south > 3 or north_or_south < 1:
            raise ValueError('地域输入不正确')
        return self.insert_card(north_or_south)

    def insert_card(self, cards_num=3):
        top_card = self.cards[:cards_num]
        bottom_card = self.cards[cards_num:]
        center_card_index = random.randint(1, len(self.cards)-cards_num-1)
        self.cards = bottom_card[:center_card_index] + top_card + bottom_card[center_card_index:]
        return self.cards

    def hide_your_first_card(self):
        self.under_butt_card = self.cards.pop(0)
        return self.cards

    def throw_card_by_gender(self, gender: int):
        if gender > 3 or gender < 1:
            raise ValueError('性别输入不正确')
        self.cards = self.cards[gender:]
        return self.cards

if __name__ == '__main__':
    magic = LiuQianLoongYearMagic()
    print("1.抽4张卡牌:", magic.get_random_length_card(4))
    print("2.撕开卡牌:", magic.split_cards())
    name = input("\033[33m您的姓名:\033[0m")
    print("3.按名字换牌后:", magic.change_cards_index_by_text(name))
    print("4.将上面三张牌穿插在中间后:", magic.insert_card(3))
    print("5.将首张牌藏在你的屁屁底下:", magic.hide_your_first_card())
    north_or_south = input("\033[33m您是南方人，还是北方人（1.南方, 2.北方, 3.未知）:\033[0m")
    print("6.按南北换牌:", magic.change_cards_index_by_area(north_or_south))
    gender = input("\033[33m您的性别（1.男, 2.女, 3.不男不女）:\033[0m")
    print("7.按男女丢牌:", magic.throw_card_by_gender(1))
    print("\033[34m-----"+magic.slogan+"-----\033[0m")
    print("8.按七字真言换牌后:", magic.change_cards_index_by_text(magic.slogan))
    while len(magic.cards) > 1:
        print("好运留下来")
        magic.cards.append(magic.cards.pop(0))
        print("保洁阿姨对不起")
        magic.cards.pop(0)
    print("\033[32m最后剩下的牌是:", magic.cards[0], " 你屁屁底下的牌是:", magic.under_butt_card+'\033[0m')
