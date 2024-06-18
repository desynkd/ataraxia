# conda env : serendibScops


import pygame
import pygame_gui
import myfunctions as ataraxia

pygame.init()

pygame.display.set_caption('Ataraxia')

window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
# if you need, have a variable current screen to remember which screen you are on

manager = pygame_gui.UIManager((800, 600), theme_path="style.json")

# ------UI ELEMENTS-----
# Main Menu
labelMain_vKeyword = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((150, 200), (250, 50)),
    text='Enter keyword for Vigenere Table',
    manager=manager
)

textMain_vKeyword = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((400, 200), (200, 50)),
    manager=manager
)

labelMain_keyword = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((150, 260), (250, 50)),
    text='Enter keyword for Encryption',
    manager=manager
)

textMain_keyword = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((400, 260), (200, 50)),
    manager=manager
)

buttonMain_encrypt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400, 320), (90, 50)),
    text='Encrypt', manager=manager
)

buttonMain_decrypt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((510, 320), (90, 50)),
    text='Decrypt', manager=manager
)

# Shared UI
buttonShared_return = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (50, 50)),
    text='Back', manager=manager, visible=False
)

# Encryption Screen
buttonEncrypt_encrypt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400, 340), (90, 50)),
    text='Encrypt', manager=manager, visible=False
)

labelEncrypt_plaintext = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((400, 100), (250, 50)),
    text='Enter plaintext',
    manager=manager, visible=False
)

textEncrypt_plaintext = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((400, 160), (200, 50)),
    manager=manager, visible=False
)

labelEncrypt_ciphertext = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((400, 220), (250, 50)),
    text='Ciphertext',
    manager=manager, visible=False
)

textBoxEncrypt_ciphertext = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((400, 280), (250, 50)),
    html_text='',
    manager=manager, visible=False
)

# Decryption Screen
buttonDecrypt_decrypt = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400, 340), (90, 50)),
    text='Decrypt', manager=manager, visible=False
)

labelDecrypt_ciphertext = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((400, 100), (250, 50)),
    text='Enter ciphertext',
    manager=manager, visible=False
)

textDecrypt_ciphertext = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((400, 160), (200, 50)),
    manager=manager, visible=False
)

labelDecrypt_plaintext = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((400, 220), (250, 50)),
    text='Plaintext',
    manager=manager, visible=False
)

textBoxDecrypt_plaintext = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((400, 280), (250, 50)),
    html_text='',
    manager=manager, visible=False
)


# ------GLOBAL FUNCTIONS-----
vTable = None
vDict = None
vKeyword = None
keyword = None
plaintext = None
ciphertext = None


# ------CUSTOM FUNCTIONS-----
def hideMainScreen():
    buttonMain_encrypt.hide()
    buttonMain_decrypt.hide()
    textMain_keyword.hide()
    textMain_vKeyword.hide()
    labelMain_keyword.hide()
    labelMain_vKeyword.hide()
    buttonShared_return.show()

def showMainScreen():
    buttonMain_encrypt.show()
    buttonMain_decrypt.show()
    textMain_keyword.show()
    textMain_vKeyword.show()
    labelMain_keyword.show()
    labelMain_vKeyword.show()
    buttonShared_return.hide()

def showEncryptScreen():
    buttonEncrypt_encrypt.show()
    textEncrypt_plaintext.show()
    labelEncrypt_plaintext.show()
    textBoxEncrypt_ciphertext.show()
    labelEncrypt_ciphertext.show()

def hideEncryptScreen():
    buttonEncrypt_encrypt.hide()
    textEncrypt_plaintext.hide()
    labelEncrypt_plaintext.hide()
    textBoxEncrypt_ciphertext.hide()
    labelEncrypt_ciphertext.hide()

def showDecryptScreen():
    buttonDecrypt_decrypt.show()
    textDecrypt_ciphertext.show()
    labelDecrypt_ciphertext.show()
    textBoxDecrypt_plaintext.show()
    labelDecrypt_plaintext.show()

def hideDecryptScreen():
    buttonDecrypt_decrypt.hide()
    textDecrypt_ciphertext.hide()
    labelDecrypt_ciphertext.hide()
    textBoxDecrypt_plaintext.hide()
    labelDecrypt_plaintext.hide()

def getMainMenuInputs():
    global vKeyword, keyword
    vKeyword = textMain_vKeyword.get_text()
    keyword = textMain_keyword.get_text()

def initializeAtaraxia(inpKeyword):
    global vTable, vDict
    vTable = ataraxia.createVigenereTable(inpKeyword)
    vDict = ataraxia.createDict(vTable[0])

def getEncryptionInputs():
    global plaintext
    plaintext = textEncrypt_plaintext.get_text()

def showEncryptionOutputs():
    global plaintext, ciphertext, keyword, vTable, vDict 
    ciphertext = ataraxia.encrypt(plaintext, keyword, vTable, vDict)
    textBoxEncrypt_ciphertext.set_text(ciphertext)

def getDecryptionInputs():
    global ciphertext
    ciphertext = textDecrypt_ciphertext.get_text()

def showDecryptionOutputs():
    global plaintext, ciphertext, keyword, vTable, vDict 
    plaintext = ataraxia.decrypt(ciphertext, keyword, vTable, vDict)
    textBoxDecrypt_plaintext.set_text(plaintext)


    
# ------MAIN PYGAME-----
clock = pygame.time.Clock()
is_running = True


while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # click to navigate to encryption
            if event.ui_element == buttonMain_encrypt:
                getMainMenuInputs() # get inputs
                initializeAtaraxia(vKeyword) # create viginere table                
                hideMainScreen() # hide ui and show new ui
                showEncryptScreen()


            # click to navigate to decryption
            if event.ui_element == buttonMain_decrypt:
                getMainMenuInputs() # get inputs
                initializeAtaraxia(vKeyword) # create viginere table                
                hideMainScreen() # hide ui and show new ui
                showDecryptScreen()

            # click return to main menu
            if event.ui_element == buttonShared_return:
                showMainScreen()
                hideEncryptScreen()
                hideDecryptScreen()

            # click to encrypt
            if event.ui_element == buttonEncrypt_encrypt:
                getEncryptionInputs()
                showEncryptionOutputs()

            # click to decrypt
            if event.ui_element == buttonDecrypt_decrypt:
                getDecryptionInputs()
                showDecryptionOutputs()
                


        manager.process_events(event)

    manager.update(time_delta)
    
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    
    pygame.display.update()

pygame.quit()
