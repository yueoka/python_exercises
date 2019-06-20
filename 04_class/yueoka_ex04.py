# -*- coding: utf-8 -*-
import unittest


class Bot():
    def __init__(self, owner_name):
        self.owner_name=name
        """
        WRITE YOUR CODE HERE
        """

    def reply(self, call):
        if call=="Hello":
            print("Hi, I'm Bill.aaa")
        elif call=="Hello my Boss!":
            print("Hi, I'm Angy.")
        """
        WRITE YOUR CODE HERE
        """


class TestBot(unittest.TestCase):
    def test_bot_reply(self):
        bot = Bot("Angy")
        self.assertEqual("Hello", bot.reply("Hi, I'm Bill."))
        self.assertEqual("Hello my Boss!", bot.reply("Hi, I'm Angy."))

if __name__=='--main--':
    unittest.main()

aaa=Bot('Hello')
aaa.reply()
