#
#   Author: Alan Kavanagh
#   Date: 27th July 2016
#   Website: github.com/AlanKavo92
#
###############################

import time
import argparse
import datetime
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def screen(message, tag="KoolFM Voter"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print '{0}: [{1}]: {2}'.format(timestamp, tag, message)


def set_screen_size(driver, width, height):
    screen('Setting screen size to: {0} [w] x {1} [h]'.format(width, height))

    driver.set_window_position(0, 0)
    driver.set_window_size(width, height)


def get_web_page(driver, url):
    screen('Opening webpage {0}'.format(url))

    driver.get(url)


def click_element(element):
    screen('[ ~ Script by github.com/TehJokeR ~ ]')
    screen('https://www.upwork.com/freelancers/~01a543ba2a84adfa3e#/')

    element.click()


def run_clicks(driver, args):
    screen('Script will click vote {0} times'.format(args.count))

    for i in range(1, args.count+1):
        screen('Vote count: {0}'.format(i))

        x = "//*[@id='{0}']".format(args.buttonid)

        undi = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH, x))
        click_element(undi)

        time.sleep(args.interval)


def run_time(driver, args):
    screen('Script will run for {0} minutes'.format(args.timeout))

    timeout_in_seconds = args.timeout * 60
    start = time.time()

    for i in itertools.count():
        screen('Vote count: {0}'.format(i+1))

        if time.time() - start >= timeout_in_seconds:
            break

        x = "//*[@id='{0}']".format(args.buttonid)

        undi = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH, x))
        click_element(undi)

        time.sleep(args.interval)


def create_parser():
    parser = argparse.ArgumentParser(description='Argument parser for Kool FM autoclicker script')
    parser.add_argument('-i', '--interval', type=int, default=3, required=False,
                        help='Time interval between clicks')
    parser.add_argument('-b', '--buttonid', default='fight_6', required=False,
                        help='HTML Button ID to click')
    limits = parser.add_mutually_exclusive_group(required=True)
    limits.add_argument('-c', '--count', type=int,
                        help='Number of times to click the button')
    limits.add_argument('-t', '--timeout', type=int,
                        help='Number of minutes to click the button')
    return parser


screen('[ ~ Script by github.com/AlanKavo92 ~ ]')
screen('https://www.upwork.com/freelancers/~01a543ba2a84adfa3e#/')

screen('Script started')

parser = create_parser()
args = parser.parse_args()

driver = webdriver.Chrome()
set_screen_size(driver, 1280, 800)
get_web_page(driver, 'http://www.koolfm.com.my/super-karoks/#frame-embed')


iframes = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(iframes[1])

if args.count:
    run_clicks(driver, args)
elif args.timeout:
    run_time(driver, args)

screen('Script finished')
screen('[ ~ Script by github.com/AlanKavo92 ~ ]')
screen('https://www.upwork.com/freelancers/~01a543ba2a84adfa3e#/')

driver.close()
