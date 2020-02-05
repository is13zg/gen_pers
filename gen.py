from PIL import Image
import random

women_hair = ["whb.png", "whw.png", "whr.png", "whn.png"]
men_hair = ["mhb.png", "mhw.png", "mhr.png", "mhn.png"]
hats = ["hatt.png", "red-hat.png", "purplehat.png"]
things = ["bag.png", "bow.png", "mobile.png"]
shoes = ["ubrshoe.png", "ubshoes.png", "ugshoes.png"]
pants = ["ublls.png", "ubls.png", "ubs.png", "ugls.png", "uwls.png", "uws.png"]
women_shits = ["wbs.png", "wgs.png", "whs.png", "wrs.png", "wws.png", "wys.png"]
men_shits = ["mbs.png", "mgs.png", "mhs.png", "mrs.png", "mws.png", "mys.png"]

#MEN = 1
#HAIR = 0
#THING = 0
#SHOE = 0
#SHIRT = 0
#PANT = 0

ls1 = ["женщина", "мужчина"]
ls2 = ["волос нет", "волосы светлые", "волосы рыжие", "волосы черные"]
ls4 = ["головного убора нет", "шляпа классическая", "красная бейсболка", "оранжевая панама"]
ls5 = ["белая футболка", "красная футболка", "серая рубашка", "коричневая рубашка", "желтая майка", "синяя рубашка"]
ls6 = ["бежевые шорты", "синие шорты", "черные шорты", "черные брюки", "светлые брюки", "зеленые брюки",
       "красные брюки"]
ls7 = ["серая обувь", "черная обувь", "коричневая обувь"]
ls8 = ["в руках ничего нет", "в руках сумка", "в руках бутылка с водой"]




def get_txt_by_num(num):

    MEN = int(num[0])
    HAIR = int(num[1])
    THING = int(num[2])
    SHOE = int(num[3])
    SHIRT = int(num[4])
    PANT = int(num[5])
    HAT =  int(num[6])

    im1 = Image.open('tors.png')

    if MEN:
        im2 = Image.open(men_hair[HAIR])
        im3 = Image.open(men_shits[SHIRT])

    else:
        im2 = Image.open(women_hair[HAIR])
        im3 = Image.open(women_shits[SHIRT])

    im1.paste(im2.convert('RGB'), (0, 0), im2)
    im1.paste(im3.convert('RGB'), (0, 0), im3)
    im7 = Image.open(shoes[SHOE])
    im1.paste(im7.convert('RGB'), (0, 0), im7)

    if THING != 0:
        im4 = Image.open(things[THING - 1])
        im1.paste(im4.convert('RGB'), (0, 0), im4)

    if HAT != 0:
        im5 = Image.open(hats[HAT - 1])
        im1.paste(im5.convert('RGB'), (0, 0), im5)

    im6 = Image.open(pants[PANT])
    im1.paste(im6.convert('RGB'), (0, 0), im6)


    im1.save(num+'.png')




def get_num(mn, mx):
    return str(random.randint(mn, mx))


ms = set()
while True:
    if len(ms) >= 117:
        break
    st = get_num(0, 1)
    st += get_num(0, 3)
    st += get_num(0, 3)
    st += get_num(0, 2)
    st += get_num(0, 5)
    st += get_num(0, 5)
    st += get_num(0, 3)
    ms.add(st)


for x in ms:
    get_txt_by_num(x)


