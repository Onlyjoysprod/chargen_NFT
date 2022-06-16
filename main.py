import os
from tkinter import *
import itertools
from PIL import Image
from random import shuffle, randint
import pandas as pd

VERSION = 0.01

backgrounds_count = len(os.listdir(path='0-backs'))
backgrounds_spec_count = len(os.listdir(path='1-backs_spec'))
cryptos_count = len(os.listdir(path='2-cryptos_spec'))
skins_count = len(os.listdir(path='3-skins'))
clothes_count = len(os.listdir(path='4-clothes'))
faces_count = len(os.listdir(path='5-faces'))
glasses_count = len(os.listdir(path='6-glasses_spec'))
heads_count = len(os.listdir(path='7-heads'))
shadows_count = len(os.listdir(path='8-shadow'))
total_chars = backgrounds_count * clothes_count * faces_count * heads_count * shadows_count

data = {'Number': [],
        'NFT name': [],
        'Background': [],
        'Crypto': [],
        'Body skin': [],
        'Outfit': [],
        'Face': [],
        'Glasses': [],
        'Head': []}

data_name_dict = {'Background': ['Brown', 'Turquoise', 'Blue', 'Purple', 'Pink', 'Green Carpet', 'Red Carpet', 'Space',
                                 'Sakura', 'Crosses'],
                  'Crypto': ['None', 'BTC', 'ETH', 'XRP'],
                  'Body skin': ['White', 'Brown', 'Gray', 'Yellow', 'Dark', 'Green', 'Pink'],
                  'Outfit': ['Red Shirt', 'Swimming Trunks', 'Black Shirt', 'Pants', 'White Shirt', "Mage's Cloak",
                             'Priest', 'Goth', 'Samurai', 'Green Shirt'],
                  'Face': ['Suspicious', 'Sly', 'Calm', 'Surprised'],
                  'Glasses': ['None', 'Brown Glasses', 'Swimming Mask', 'Monocle', 'Laser Glasses', 'Eye Patch',
                              'Band', 'White Glasses', 'Cool Glasses', 'Sleep Mask'],
                  'Head': ['Straw Hat', 'Cap', 'Afro', 'Viking', 'Foil Hat', 'Iroquois', 'Tail', 'Bully',
                           'Japanese Biker', 'Bald', 'Emo', 'Reed Hat']
                  }


def generate():
    back = [el for el in range(backgrounds_count)]
    back_spec = [el for el in range(backgrounds_spec_count)]
    crypto_spec = [el for el in range(cryptos_count)]
    skin = [el for el in range(skins_count)]
    clothes = [el for el in range(clothes_count)]
    faces = [el for el in range(faces_count)]
    glasses = [el for el in range(glasses_count)]
    head = [el for el in range(heads_count)]
    shadow = [el for el in range(shadows_count)]

    char_shuffle = [el for el in range(total_chars)]
    shuffle(char_shuffle)

    counts_arrays = [back, clothes, faces, head, shadow]
    spec_count_arrays = [back_spec, crypto_spec, skin, glasses]

    counter = 0
    """
    filename indexes
    0-number, 1-back, 2-crypto, 3-skin, 4-clothes, 5-face, 6-glasses, 7-head
    """
    filename_list = [0, 0, 0, 0, 0, 0, 0, 0]
    for el in itertools.product(*counts_arrays):
        print(f'{el} - {counter}')
        filename_list[0] = counter

        img_first = Image.open(f"back.jpg", 'r')
        img_back = Image.open(f"0-backs/{el[0]}.png", 'r')
        filename_list[1] = el[0]

        # random skin chose
        randomiser = randint(0, skins_count - 1)
        img_skin = Image.open(f'3-skins/{randomiser}.png', 'r')
        filename_list[3] = randomiser

        img_clothes = Image.open(f'4-clothes/{el[1]}.png', 'r')
        filename_list[4] = el[1]

        img_faces = Image.open(f'5-faces/{el[2]}.png', 'r')
        filename_list[5] = el[2]

        img_head = Image.open(f'7-heads/{el[3]}.png', 'r')
        filename_list[7] = el[3]

        img_shadow = Image.open(f'8-shadow/{el[4]}.png', 'r')

        img_first.paste(img_back, (0, 0), mask=img_back)
        # --back_spec
        randomiser = randint(1, 10)
        if randomiser == 1:
            rand_back = randint(0, backgrounds_spec_count - 1)
            img_back_spec = Image.open(f"1-backs_spec/{rand_back}.png", 'r')
            img_first.paste(img_back_spec, (0, 0), mask=img_back_spec)
            filename_list[1] = backgrounds_count + rand_back

        # --crypto_spec
        randomiser = randint(1, 25)
        if randomiser == 1:
            rand_crypto = randint(0, cryptos_count - 1)
            crypto_spec = Image.open(f"2-cryptos_spec/{rand_crypto}.png", 'r')
            img_first.paste(crypto_spec, (0, 0), mask=crypto_spec)
            filename_list[2] = rand_crypto + 1
        else:
            filename_list[2] = 0
        img_first.paste(img_skin, (0, 0), mask=img_skin)
        img_first.paste(img_clothes, (0, 0), mask=img_clothes)
        img_first.paste(img_faces, (0, 0), mask=img_faces)
        # --glasses_spec
        randomiser = randint(1, 3)
        if randomiser == 1:
            rand_glasses = randint(0, glasses_count - 1)
            glasses_spec = Image.open(f"6-glasses_spec/{rand_glasses}.png", 'r')
            img_first.paste(glasses_spec, (0, 0), mask=glasses_spec)
            filename_list[6] = rand_glasses + 1
        else:
            filename_list[6] = 0
        img_first.paste(img_head, (0, 0), mask=img_head)
        img_first.paste(img_shadow, (0, 0), mask=img_shadow)

        data['Number'].append(char_shuffle[counter] + 1)

        data['NFT name'].append(f'Pillguy #{char_shuffle[counter] + 1}')
        data['Background'].append(data_name_dict['Background'][filename_list[1]])
        data['Crypto'].append(data_name_dict['Crypto'][filename_list[2]])
        data['Body skin'].append(data_name_dict['Body skin'][filename_list[3]])
        data['Outfit'].append(data_name_dict['Outfit'][filename_list[4]])
        data['Face'].append(data_name_dict['Face'][filename_list[5]])
        data['Glasses'].append(data_name_dict['Glasses'][filename_list[6]])
        data['Head'].append(data_name_dict['Head'][filename_list[7]])

        img_first.save(f'./characters/{char_shuffle[counter] + 1}.png', format="png")
        img_first.close()

        counter += 1

    metadata = pd.DataFrame(data)
    metadata.to_excel('./metadata.xlsx', sheet_name='Metadata', index=False)

    window.destroy()
    qt = Tk()
    qt.geometry('200x120')
    qt.title('Готово!')
    qt_txt = Label(qt, text="Generation\ncomplite!", font=('Times', 15))
    knpk = Button(qt, text='OK', command=qt.destroy, width=15)
    qt_txt.pack()
    knpk.pack()


window = Tk()
window.title(f'CharGen v{VERSION}')
window.geometry('')

btn = Button(window, text="Generate", command=generate, padx=5, pady=5)
btn.grid(column=1, row=4)

lbl_heads = Label(window, text=f'Total characters: {total_chars}', padx=5, pady=5)
lbl_heads.grid(column=0, row=5)
lbl_empty = Label(window, text='Press Generate to start', padx=5, pady=5)
lbl_empty.grid(column=2, row=5)

window.mainloop()
