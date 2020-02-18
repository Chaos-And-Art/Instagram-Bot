from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import random

from Modes.not_following import NotFollow
from Modes.like_random import LikeRandom
from Modes.like_following import LikeFollowing


class InstagramBot(NotFollow, LikeRandom, LikeFollowing):

    def __init__(self, username=None, password=None):

        self.username = username
        self.password = password

    def login(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        initUser = self.driver.find_element_by_name("username")
        initUser.send_keys(self.username)
        initPass = self.driver.find_element_by_name("password")
        initPass.send_keys(self.password)
        initPass.send_keys(Keys.RETURN)
        time.sleep(4)

        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()


def menu_command_list():
    print("\nChoose from the command list the action you would like performed.")
    print("\n" + "~"*85)
    print("COMMANDS:")
    print("Like Following = Liking the pictures of the people that you follow")
    print("Like Random = Liking the pictures of random photos based on hash list")
    print("Get Not Following = Finds all the people that you follow but don't follow you back")
    print("Exit = Exit Program")
    print("~"*85)
    time.sleep(2)
    print("\nNOTICE: You will have to close the browser, or kill the terminal")
    print("in order for the program to stop.")


def random_hashtag():
    print("\nWould you like to pick your own hashtag, or random hashtag?")
    print("\n" + "~"*85)
    print("COMMANDS:")
    print("Choose = Like photos based on the hashtag you enter.")
    print("Random = Like photos from a random hashtag chosen.")
    print("~"*85)


def photo_amount():
    print("~"*85)
    print("Enter a number to determine roughly how many photos you want to like.")
    print(
        "Every number after '1' increments by 12. [1 = 45 Photos], [2 = 57], [3 = 69]...")
    print("~"*85)


def check_int():
    while True:
        photo_amount()
        _input = input("-> ")
        try:
            amount = int(_input)
            bot.login()
            time.sleep(1)
            bot.like_hash_photo(tag, amount)
        except ValueError:
            print("Input is not a valid number. Try again using an integer value.")


if __name__ == "__main__":

    username = "USERNAME"
    password = "PASSWORD"

    bot = InstagramBot(username, password)

    hashtags = ['amazing', 'beautiful', 'adventure', 'photography',
                'artsy', 'best', 'fun', 'happy', 'funny', 'love',
                'instagood', 'instagood', 'fashion', 'beauty', 'city',
                'pretty', 'vintage']

    while True:
        menu_command_list()
        _input = input("-> ")

        if _input == "Exit" or _input == "exit":
            break
        if _input == "Like Following" or _input == "like following":
            bot.login()
            time.sleep(1)
            bot.like_follow_photo()
        if _input == "Like Random" or _input == "like random":
            random_hashtag()
            _input = input("-> ")
            if _input == "Choose" or _input == "choose":
                print("Enter the hashtag you would like to use")
                _input = input("-> ")
                tag = _input
                check_int()
            elif _input == "Random" or _input == "random":
               check_int()
        if _input == "Get Not Following" or _input == "get not following":
            bot.login()
            time.sleep(1)
            bot.get_notFollowing()
