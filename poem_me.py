from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
import pickle
import os

def driver_init():
    fop = Options()
    fop.add_argument('--headless')
    fop.add_argument('--window_size1920x1080')
    return webdriver.Firefox(options = fop)


def poem_of_the_day(driver):
    os.system('clear')
    os.system('clear')
    remove_html = re.compile('<.*?>')
    driver.get('https://www.poetryfoundation.org/poems')
    boxes = driver.find_elements_by_class_name('o-card-bd')
    boxes[0].find_element_by_tag_name('a').click()
    poem_tag = driver.find_elements_by_tag_name('div')[0]
    poem = poem_tag.text.split('\n')
    poem = poem[17::]
    for p in poem:
        if 'Copyright ©' in p:
            break
        print(p)
    return {poem[0] : poem}


def poem_archive(poem = '!NO_POEM', return_archive = False):
    try:
        archive = pickle.load(open('poem_archive.p', 'rb'))
    except:
        archive = {}
    if return_archive:
        return pd.DataFrame(archive)
    if poem != '!NO_POEM':
        archive.update(poem)
        pickle.dump(archive, open('poem_archive.p', 'wb'))

def poem_ui(driver):
    print('<><><><><><>')
    print('------------POEM_OF_THE_DAY------------')
    poem = poem_of_the_day(driver)
    print('---------------------------------------')
    while True:
        command = input('>>WOULD_YOU_LIKE_TO_ARCHIVE_THIS_POEM?(Y/N)>> ')
        if command == 'Y':
            poem_archive(poem)
            break
        if command == 'N':
            break
    return
    
    
