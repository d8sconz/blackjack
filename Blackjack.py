# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:34:31 2017

@author: Rossz
"""

import random
from time import sleep

# number of decks in the shoe
decks = 6
# cards in the shoe
# shoe = [5, 1, 8, 2, 3, 10, 8]
shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*decks*4
# shuffle shoe
random.seed()
random.shuffle(shoe)
# empty list for dealer and player hand
d_cards = []
p_cards = []


# Dict of dicts for Player soft total basic strategy
Soft_strategy = {'11': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0},
                 '2': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0},
                 '3': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0},
                 '4': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0},
                 '5': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0},
                 '6': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 1, '19': 1, '20': 0, '21': 0},
                 '7': {'4': 1, '5': 1, '6': 1, '7': 1,  '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 0, '19': 0, '20': 0, '21': 0},
                 '8': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 0, '19': 0, '20': 0, '21': 0},
                 '9': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0},
                 '10': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 1, '18': 1, '19': 0, '20': 0, '21': 0}}

# Dict of dicts for Player hard total basic strategy
Hard_strategy = {'11': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '2': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 0, '13': 0, '14': 0, '15': 0,
                       '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '3': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 0, '13': 0, '14': 0, '15': 0,
                       '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '4': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 0, '13': 0, '14': 0, '15': 0,
                       '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '5': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 0, '13': 0, '14': 0, '15': 0,
                       '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '6': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 0, '13': 0, '14': 0, '15': 0,
                       '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '7': {'4': 1, '5': 1, '6': 1, '7': 1,  '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '8': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '9': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '10': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0}}
# Dealers strategy
"""Soft_strategy = {'11': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '2': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '3': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '4': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '5': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '6': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '7': {'4': 1, '5': 1, '6': 1, '7': 1,  '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '8': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '9': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '10': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0}}

# Dict of dicts for Player hard total basic strategy
Hard_strategy = {'11': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '2': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '3': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '4': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '5': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '6': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '7': {'4': 1, '5': 1, '6': 1, '7': 1,  '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '8': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '9': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0},
                 '10': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0}}"""


def players_strategy(hand, d_c):
    tot = sum(hand)
    msg = ""
    # Handle soft totals. find where the ace resides;
    # check total against Soft_strategy dict;
    # if draw, add new card to hand and revalue ace if necessary;
    while 1:
        if 11 in hand:
            if tot > 21:
                hand[hand.index(11)] = 1
                tot = sum(hand)
            elif tot > 19:
                # msg, hand = message('Player', hand)
                break
            elif tot < 20:
                if Soft_strategy[str(d_c[0])][str(tot)]:
                    hand.append(shoe.pop())
                    msg, hand = message("Player", hand)
                    if "Bust" in msg:
                        if 11 in hand:
                            hand[hand.index(11)] = 1
                            msg, hand = message("Player", hand)
                    tot = sum(hand)
                    reveal(msg)
                else:
                    # msg, hand = message('Player', hand)
                    # reveal(msg)
                    break
        if tot < 17:
            if Hard_strategy[str(d_c[0])][str(tot)]:
                hand.append(shoe.pop())
                tot = sum(hand)
                if tot < 11 and hand[-1] == 1:
                    hand[-1] = 11
                msg, hand = message("Player", hand)
                if "Bust" in msg:
                    if 11 in hand:
                        hand[hand.index(11)] = 1
                        msg, hand = message("Player", hand)
                        reveal(msg)
                tot = sum(hand)
                reveal(msg)
            else:
                break
        else:
            break

    if "Bust" in msg:
        return msg
    else:
        msg = "Player stands on {}".format(tot)
        reveal(msg)
        return msg


def dealers_strategy(hand):
    tot = sum(hand)
    msg = "\nDealers hidden card is {}, total {}".format(hand[1], tot)
    reveal(msg)
    # Handle soft totals. find where the ace resides;
    # check total against Soft_strategy dict;
    # if draw, add new card to hand and revalue ace if necessary;
    while 1:
        if 11 in hand:
            if tot > 21:
                hand[hand.index(11)] = 1
                tot = sum(hand)
            elif tot < 17:
                hand.append(shoe.pop())
                msg, hand = message("Dealers", hand)
                if "Bust" in msg:
                    if 11 in hand:
                        hand[hand.index(11)] = 1
                        msg, hand = message("Dealers", hand)
                tot = sum(hand)
                reveal(msg)
        if tot < 17:
            hand.append(shoe.pop())
            tot = sum(hand)
            if tot < 11 and hand[-1] == 1:
                hand[-1] = 11
            msg, hand = message("Dealers", hand)
            if "Bust" in msg:
                if 11 in hand:
                    hand[hand.index(11)] = 1
                    msg, hand = message("Dealers", hand)
                    reveal(msg)
            tot = sum(hand)
            reveal(msg)
        else:
            break

    if "Bust" in msg:
        return msg
    else:
        msg = "Dealer stands on {}".format(tot)
        reveal(msg)
        return msg


# Stats vars
bank = [100]
bet = [1]
streak = [0]
game_lngth, hnd_win, hnd_lse = [0], [0], [0]  # Number of games, win/lose
cards = []
betting_strategy = [1, 2, 2, 4]
winning_streak, losing_streak, old_ls, old_ws = [0], [0], [0], [0]


def message(who, hand):
    # repeat message routine
    cd = hand[-1]
    tot = sum(hand)
    # Opening hand
    if len(hand) == 2:
        if who == 'Dealer':
            # If Dealer has an ace...
            if hand[0] == 1:
                hand[0] = 11
                msg = "{} has an ace and one hidden card\n".format(who)
            elif hand[1] == 1:
                hand[1] = 11
                msg = "{} has {} and one hidden card\n".format(who, hand[0])
            else:
                msg = "{} has {} and one hidden card\n".format(who, hand[0])
            return msg, hand

        # Check for aces for soft total strategy
        if 1 in hand:
            # Two aces?
            if hand[0] == 1 and hand[1] == 1:
                hand[0] = 11
                msg = "Player has two aces, total {}".format(tot+10)
            # Ace is first card?
            elif hand[0] == 1:
                hand[0] = 11
                msg = "Player has an ace and {}, total {} or {}".format(
                        hand[1], tot, tot+10)
            # Ace is second card
            elif hand[1] == 1:
                hand[1] = 11
                msg = "Player has {} and an ace, total {} or {}".format(
                        hand[0], tot, tot+10)
            return msg, hand

        msg = "player has {} and {}, total {}".format(
                hand[0], hand[1], tot)
        return msg, hand

    # Has ace, Bust? will return with card revalued to 1
    if cd == 11 and tot > 21:
        msg = "Bust"
        return msg, hand
    # Has hard total ace.
    if cd == 11:
        msg = "{} draws an ace, total {} or {}".format(who, tot-10, tot)
    elif cd == 1:
        msg = "{} draws an ace, total {}".format(who, tot)
    else:
        msg = "{} draws {}, total {}".format(who, cd, tot)

    if tot > 21:
        msg = msg + ". Bust!"

    return msg, hand


def end_hand(p, d):  # Player, Dealer cards
    msg = ""
    # Keep record of last 10 games for avg value of cards
    game_lngth[0] += 1
    cards.append(p)
    cards.append(d)
    if game_lngth[0] > 10:
        for _ in range(2):
            cards.pop(0)
    cards_ttl = list(sum(cards, []))
    cards_lngth = len(cards_ttl)
    p_t, d_t = sum(p), sum(d)
    cd_avg = round((sum(cards_ttl)/cards_lngth), 2)
    # Who wins?
    # Handle effing Blackjacks
    if BJ(p):
        if BJ(d):
            msg = "Push"
        else:
            msg = "Player wins 3:2"
    # Player bust?
    elif p_t > 21:
        msg = "Player loses"
    # Dealer bust?
    elif d_t > 21:
        msg = "Dealer bust. Player wins"
    # Push?
    elif p_t == d_t:
        msg = "Push!"
    # Who wins?
    elif p_t > d_t:
        msg = "Player wins"
    else:
        msg = "Player loses"

    reveal(msg)

    # Analyse hand
    if "loses" in msg:
        c = -1
        losing_streak[0] += c
        hnd_lse[0] += c
        if streak[0] > 0:
            streak[0] = 0
            losing_streak[0] = -1
        if losing_streak[0] < old_ls[0]:
            old_ls[0] = losing_streak[0]
    elif "3:2" in msg:
        c = 1.5
    elif "wins" in msg:
        c = 1
    else:
        c = '0'

    if int(c) > 0:
        winning_streak[0] += int(c)
        hnd_win[0] += int(c)
        if streak[0] < 0:
            streak[0] = 0
            winning_streak[0] = 1
        if winning_streak[0] > old_ws[0]:
            old_ws[0] = winning_streak[0]

    streak[0] += int(c)  # Shaves off decimal in Blackjack multiplier

    if streak[0] < 0:
        strat = 0
    else:
        strat = streak[0]          # streak can go as high as it likes
    lmt = len(betting_strategy)-1  # but strat will be limited to
    if strat > lmt:                # length of betting_strategy
        strat = lmt

    # Settle account and print result
    if c == -1:
        bet[0] = betting_strategy[0]
        bank[0] -= bet[0]
    elif int(c) == 0:
        bet[0] = betting_strategy[strat]
    else:
        bank[0] += int(2*float(c)*bet[0])
        bet[0] = betting_strategy[strat]
        bank[0] -= bet[0]

    msg = "{:^20}|{:^20}|{:^10}|{:^8}|{:^10}".format(
            "Game: {}, {}/{}".format(game_lngth[0], hnd_win[0], hnd_lse[0]),
            "win/lose {}, {}/{}".format(int(c), old_ws[0], old_ls[0]),
            "avg {}".format(cd_avg),
            "bet {}".format(bet[0]),
            "bank {}".format(bank[0]))
    print("\b"*(len(msg)+1), msg, flush=True)
    if bank[0]+bet[0] <= 0:
        msg = ("You're broke! Resetting - Games: {}, win/loss: {}/{}, "
               "longest {}/{}    ".format(
                       game_lngth[0], hnd_win[0], hnd_lse[0],
                       old_ws[0], old_ls[0]))
        print("\b"*(len(msg)+1), msg, flush=True)

        game_lngth[0], hnd_win[0], hnd_lse[0], old_ws[0] = 0, 0, 0, 0
        old_ls[0], streak[0], winning_streak[0], losing_streak[0] = 0, 0, 0, 0
        bank[0] = 100
        del cards[:]
    if game_lngth[0] == 0:
        print(msg, end="\b"*(len(msg)+1), flush=True)

    """print("\n{}".format(msg))
    print("------------------------")
    print("winning/losing streak is {}".format(streak[0]))
    print("longest win/lose streak is {}/{}".format(old_ws[0], old_ls[0]))
    print("Average card value is {} cards".format(cd_avg))
    print("\nGame has been going for {} hands".format(game_lngth[0]))
    print("------------------------")
    print("current bet is {}".format(bet[0]))
    print(".----------------------.")
    print("|      Bank is {}     |".format(bank[0]))
    print("'----------------------'")
    print("Bank is {}".format(bank[0]))"""

    d = []
    p = []
    return d, p


def BJ(hand):
    if len(hand) == 2:
        if 1 in hand and sum(hand) == 11:
            return True
        else:
            False


def reveal(m):
    print(m)
    return


# Main program starts here
while 1:
    print("\n------------------------")
    ##############################
    # Set up game - Initial deal #
    ##############################

    while len(d_cards) != 2:
        d_cards.append(shoe.pop())
        p_cards.append(shoe.pop())

    # Reveal Dealers card...
    msg, d_cards = message('Dealer', d_cards)
    reveal(msg)

    # Check for Blackjacks first
    if BJ(p_cards):
        p_cards[p_cards.index(1)] = 11
        reveal("Player has an ace and a 10. Blackjack!")
        if d_cards[0] == 10 or d_cards[0] == 1:
            if BJ(d_cards):
                if d_cards[0] == 1:
                    reveal("\nDealers hidden card is 10. Blackjack!")
                else:
                    reveal("\nDealers hidden card is an ace. Blackjack!")
                p_cards, d_cards = end_hand(p_cards, d_cards)
        else:
            reveal("\nDealers hidden card is {}".format(d_cards[1]))
            # Hand over to end_hand function to analyse and reset
            p_cards, d_cards = end_hand(p_cards, d_cards)
    else:
        # Reveal the deal...
        msg, p_cards = message('Player', p_cards)
        reveal(msg)

    ###########################################
    #               Start playing             #
    ###########################################

    while len(d_cards) > 1:
        # while there are cards in the hand, keep playing
        msg = players_strategy(p_cards, d_cards)
        # If player busts just end the game
        if "Bust" in msg:
            p_cards, d_cards = end_hand(p_cards, d_cards)
            break

        # If player doesn't bust continue to check dealers hand
        msg = dealers_strategy(d_cards)
        if "Bust" in msg:
            p_cards, d_cards = end_hand(p_cards, d_cards)
            break

        p_cards, d_cards = end_hand(p_cards, d_cards)

    if len(shoe) < 52:
        """print("------------------------")
        print(".----------------------.")
        print("|    Shuffling shoe    |")
        print("'----------------------'")
        print("------------------------")"""
        shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*decks*4
        # shuffle shoe
        random.seed()
        random.shuffle(shoe)

    sleep(5)
