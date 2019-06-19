#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
import time
from matplotlib import pyplot as plt


class SlotMachine:

    def __init__(self):
        self.description = """\tWelcome!\n
        This is a simple naive slot machine you can find in most casinos\n
        \n
        You can refer to the manual below for possible options..."""

        self.cash = 498
        self.bet = 10
        self.multiplier = 1
        self._winning_multiplier = 3
        self._jackpot_multiplier = 7
        # self.history = [self.cash]

    def __repr__(self):
        print(self.description)
        print("""\n====================================\n
        Now you have {} dollars!\n
        You are playing with multiplier {} (All bet and winning are multiplied by {})
        GOOD LUCK\n
        ====================================\n""".format(self.cash, self.multiplier, self.multiplier))

    def manual(self):
        print("""
        Play:\t Positive integer (indicating how many games you want to play or None for just one game\n
        Set multiplier:\t "m=5"\n
        Add money:\t "add=500" \t and then send money to Lingxiao via Wechat :)\n

        """)

    # 绘图
    def plot(self, xlable, ylable):
        x = [x for x in range(xlable)]
        plt.title("Game")
        plt.plot(x, ylable)

        plt.show()

    def print_draw(self):
        """
        The actual draw function and it prints out the number
        Here is the rule:
        Draw 3 integers ranging from 1 to 9 exclusively
        :return: number draw as a tuple, i.e. (7, 7, 7)
        """
        # 稳赚算法
        a = [x for x in range(1, 10)]
        b = [x for x in range(1, 10)]
        c = [x for x in range(1, 10)]

        win_codes = list(zip(a, b, c))
        random.shuffle(a)
        win_code = a[1] - 1
        print(win_codes[win_code])
        return win_codes[win_code]

        # 随机中奖算法
        # random_list = []
        # for index in range(3):
        #     a = random.randint(1, 9)
        #     random_list.append(a)
        #
        # random_tup = tuple(random_list)
        #
        # return random_tup

    def draw(self, n=1):
        """
        The draw function that draws a number and determines whether you got a winning number.
        It also updates your cash
        :param n: number of draws
        :return: None
        """
        random_draw = self.print_draw()

        if random_draw[0] == random_draw[1] == random_draw[2] != 7:
            self.history = self.cash + self.bet * self._winning_multiplier
            print(" 中奖了 哈哈！")
            time.sleep(1)
            print(" 中奖了 哈哈哈！！")
            time.sleep(1)
            print(" 中奖了 哈哈哈哈哈哈！！！")
            time.sleep(1)
        elif random_draw[0] == random_draw[1] == random_draw[2] == 7:
            self.history = self.cash + self.bet * self._jackpot_multiplier
            print("王炸 哈哈！")
            time.sleep(1)
            print("王炸 哈哈哈！！")
            time.sleep(1)
            print("王炸 哈哈哈哈哈哈！！！")
            time.sleep(1)
        else:
            print("————没中奖——————")
            self.history = self.cash - self.bet
        print('中奖号：', random_draw)
        print('赌资金额：%s 块'% self.history)
        self.cash = self.history
        return self.history, self.bet

    def play(self):
        """
        Write an infinite loop asking for user prompt after each draw
        The user should input an positive integer indicating how many draws he want
        Note that the game should break when user's cash value drops below the bet of a single game: bet* multiplier
        You should ask if the player wants to adds more money and continue to play
        :return:
        """
        b = int(input("玩几把："))
        flag = 0
        money = []
        while True:
            flag += 1
            histroy_, bet = self.draw()
            money.append(histroy_)
            if histroy_ < self.bet:
                print('您只能玩个 %s 把...' % flag)
                break

            if flag == b:
                print('次数已用完！！！')
                break

        self.plot(flag, money)

    def restart_game(self):100
        """
        Restart the game and reset everything back to its initial state
        :return:
        """


if __name__ == "__main__":
    slot = SlotMachine()
    slot.play()
