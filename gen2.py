from PIL import Image
import random
import pprint

# количества генерируемых
NN = 99
# среднее кол-во картинок с одинаковым параметром
ser = 16.5
# допустимое отклонение от идеала
kr = 5

# папка для сохранения
rpath = "results"

# папка с картинками
spath = "imgsrc"

# цвета волос фиолетовый, синий, рыжий, белый, коричнеавый, черный
hats = ["v1.png", "v2.png", "v3.png", "v4.png", "v5.png", "v6.png"]

# головы с разными эмоциями: плачет, удивление, злой, испуган , смех, обычный
hair = ["h1.png", "h2.png", "h3.png", "h4.png", "h5.png", "h6.png", ]

# вещи в руке: сумка, бутылка, телефон, кубик рубик, ничего, книга
things = ["bag.png", "bow.png", "mobile.png", "cube.png", "no_pict.png", "book.png"]

# штаны: хаки, серые, черные, краснын, коричневые, бордовый
pants = ["sht1.png", "sht2.png", "sht3.png", "sht4.png", "sht5.png", "sht6.png"]

# рубашки: зеленая, голубая, желатая, розовая, хаки, красный
shits = ["rub1.png", "rub2.png", "rub3.png", "rub4.png", "rub5.png", "rub6.png"]

# Тут считает сколько различных штанов каждого типа было сгенерировано
pnts = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
shts = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
hrs = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
thngs = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
mnts = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}


# обнуление словарей для подсчета различных параметров
def zerod():
    pnts["0"] = 0
    pnts["1"] = 0
    pnts["2"] = 0
    pnts["3"] = 0
    pnts["4"] = 0
    pnts["5"] = 0

    shts["0"] = 0
    shts["1"] = 0
    shts["2"] = 0
    shts["3"] = 0
    shts["4"] = 0
    shts["5"] = 0

    hrs["0"] = 0
    hrs["1"] = 0
    hrs["2"] = 0
    hrs["3"] = 0
    hrs["4"] = 0
    hrs["5"] = 0

    thngs["0"] = 0
    thngs["1"] = 0
    thngs["2"] = 0
    thngs["3"] = 0
    thngs["4"] = 0
    thngs["5"] = 0

    mnts["0"] = 0
    mnts["1"] = 0
    mnts["2"] = 0
    mnts["3"] = 0
    mnts["4"] = 0
    mnts["5"] = 0


# MEN = 1
# HAIR = 0
# THING = 0
# SHOE = 0
# SHIRT = 0
# PANT = 0

# по номеру возвращает картинку и считает кол-во для проверки
def sc(num):
    EMOC = int(num[0])
    HAIR_CLR = int(num[1])
    THING = int(num[2])
    SHIRT = int(num[4])
    PANT = int(num[3])

    pnts[str(PANT)] += 1
    shts[str(SHIRT)] += 1
    hrs[str(HAIR_CLR)] += 1
    thngs[str(THING)] += 1
    mnts[str(EMOC)] += 1


# сохраняет картинку по номеру
def get_txt_by_num(num):
    EMOC = int(num[0])
    HAIR_CLR = int(num[1])
    THING = int(num[2])
    SHIRT = int(num[4])
    PANT = int(num[3])

    im1 = Image.open(spath + "/" + 'tors3.png')
    im2 = Image.open(spath + "/" + hair[EMOC])
    im3 = Image.open(spath + "/" + shits[SHIRT])
    im4 = Image.open(spath + "/" + things[THING])
    im5 = Image.open(spath + "/" + hats[HAIR_CLR])
    im6 = Image.open(spath + "/" + pants[PANT])

    im1.paste(im2.convert('RGB'), (0, 0), im2)
    im1.paste(im3.convert('RGB'), (0, 0), im3)
    im1.paste(im4.convert('RGB'), (0, 0), im4)
    im1.paste(im5.convert('RGB'), (0, 0), im5)
    im1.paste(im6.convert('RGB'), (0, 0), im6)

    im1.save(rpath + "/" + num + '.png')


def get_num(mn, mx):
    return str(random.randint(mn, mx))


povtor = True

while povtor:
    ms = set()
    zerod()
    while True:
        if len(ms) >= NN:
            break
        st = get_num(0, 5)
        st += get_num(0, 5)
        st += get_num(0, 5)
        st += get_num(0, 5)
        st += get_num(0, 5)
        if st not in ms:
            ms.add(st)
    for x in ms:
        sc(x)

    c = 0

    for x in pnts.values():
        if abs(x - ser) >= kr:
            c = 1
    for x in shts.values():
        if abs(x - ser) >= kr:
            c = 1

    for x in hrs.values():
        if abs(x - ser) >= kr:
            c = 1

    for x in thngs.values():
        if abs(x - ser) >= kr:
            c = 1

    for x in mnts.values():
        if abs(x - ser) >= kr:
            c = 1
    if c == 0:
        break

for x in ms:
    print(x)
    get_txt_by_num(x)

pprint.pprint(pnts)
pprint.pprint(shts)
pprint.pprint(hrs)
pprint.pprint(thngs)
pprint.pprint(mnts)
