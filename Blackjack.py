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
"""Soft_strategy = {'1': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
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
Hard_strategy = {'1': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
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
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0}}"""
                 
Soft_strategy = {'1': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
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
                       '16': 1, '17': 1, '18': 0, '19': 0, '20': 0, '21': 0},
                 '8': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 0, '19': 0, '20': 0, '21': 0},
                 '9': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                       '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                       '16': 1, '17': 1, '18': 0, '19': 0, '20': 0, '21': 0},
                 '10': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
                        '10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
                        '16': 1, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0}}

# Dict of dicts for Player hard total basic strategy
Hard_strategy = {'1': {'4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
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


def stand(p_cards, d_cards):  # player total, dealers hand
    p_tot = sum(p_cards)
    # Is Player bust? Outa here
    if p_tot > 21:
        return

    d_tot = sum(d_cards)
    if len(p_cards) == 2 and p_tot == 21:
        if d_tot == 11 and d_cards[0] == 1:
            d_cards[0] = 11
            return
            # d_cards[1] might be an ace, still blackjack, end hand
        elif d_tot == 11 and d_cards[1] == 1:
            d_cards[1] = 11
            return
        return
        # Handle aces
    if d_tot == 2:
        d_cards[0] = 11
    elif d_cards[0] == 1:
        d_cards[0] = 11
    elif d_cards[1] == 1:
        d_cards[1] = 11

    # Handle Dealer soft totals. Have already hardened d_cards[0] == 11
    # Recalc sum to reflect hard total of ace. Revert to val 1 if bust
    d_tot = sum(d_cards)
    while d_tot < 17:
        d_cards.append(shoe.pop())
        if d_cards[-1] == 1:
            d_cards[-1] = 11
            d_tot = sum(d_cards)
        msg = message('Dealer', d_cards)
        if "Bust" in msg:
            if 11 in d_cards:
                d_cards[d_cards.index(11)] = 1
                msg = message('Dealer', d_cards)
                d_tot = sum(d_cards)
            if d_tot > 17:
                return
        d_tot = sum(d_cards)
    return


def players_strategy(who, hand):
    tot = sum(hand)
    # Handle soft totals. find where the ace resides;
    # check total against Soft_strategy dict;
    # if draw, add new card to hand and revalue ace if necessary;

    if who = 'Player' and 1 in hand:
        # Blackjack?
        if len(hand) == 2 and tot == 11:  # Must be blackjack
            hand[hand.index(1)] = 11      # Total 21
            return(hand)

    while hand[-1] == 1:
        hand[-1] = 11
        tot = sum(hand)
        while tot < 20:
            if Soft_strategy[str(d_cards[0])][str(tot)]:
                hand.append(shoe.pop())
                # Test for ace and make hard total
                if hand[-1] == 1:
                    hand[-1] = 11
                msg = message('Player', hand)
                if "Bust" in msg:
                    if 11 in hand:
                        hand[hand.index(11)] = 1
                        msg = message('Player', hand)
                print(msg)
                tot = sum(hand)
            else:
                break

    while tot < 17:
        if Hard_strategy[str(d_cards[0])][str(tot)]:
            hand.append(shoe.pop())
            tot = sum(hand)
            msg = message('Player', hand)
            print(msg)
        else:
            break
    # Handle aces
    if tot == 2:
        hand[0] = 11
    elif hand[0] == 1:
        hand[0] = 11
    elif hand[1] == 1:
        hand[1] = 11


def dealers_strategy(who, hand):
    # Start checking Dealer's hand. Reveal hidden card. Blackjack?
    tot = sum(hand)
    if tot == 11:
        if hand[0] == 1:
            hand[0] = 11
            print("\nDealers hidden card is 10. Blackjack!")
            return
        # hand[1] might be an ace, still blackjack, end hand
        elif hand[1] == 1:
            hand[1] = 11
            print("\nDealers hidden card is an ace. Blackjack!")
            return

    # Final Player message (needed to confirm Dealer Blackjack or not first)
    p_tot = sum(p_cards)
    # Is Player bust? Outa here
    if p_tot > 21:
        return
    # Is Player Blackjack?
    if len(p_cards) == 2 and p_tot == 21:
        print("Player stands on Blackjack")
        # still need to reveal in case of Dealer Blackjack
        if hand[0] == 10:
            print("\nDealers hidden card is {}".format(hand[1]))
        return
    else:
        print("Player stands on {}".format(p_tot))

    # No blackjacks but still have to reveal and check for aces
    if hand[0] == 1:
        # default to hard total. Can revert if bust.
        hand[0] = 11
        # are there two aces?
        if hand[1] == 1:
            print("\nDealers hidden card is an ace, total {} or {}".
                  format(tot, tot+10))
        # No ace in hand[1] reveal
        else:
            print("\nDealers hidden card is {}, total {} or {}".
                  format(hand[1], tot, tot+10))
    # hand[0] not ace. hand[1]?
    elif hand[1] == 1:
        hand[1] = 11
        print("\nDealers hidden card is an ace, total {} or {}".
              format(tot, tot+10))
    # No aces. Final reveal
    else:
        print("\nDealers hidden card is {}, total {}".
              format(hand[1], tot))

    # Handle Dealer soft totals. Have already hardened hand[0] == 11
    # Recalc sum to reflect hard total of ace. Revert to val 1 if bust
    tot = sum(hand)
    while tot < 17:
        hand.append(shoe.pop())
        if hand[-1] == 1:
            hand[-1] = 11
            tot = sum(hand)
        msg = message('Dealer', hand)
        if "Bust" in msg:
            if 11 in hand:
                hand[hand.index(11)] = 1
                msg = message('Dealer', hand)
            tot = sum(hand)
            if tot > 17:
                print(msg)
                return
        print(msg)
        tot = sum(hand)
    print("Dealer stands on {}".format(tot))

    return


# Stats vars
bank = [100]
bet = [1]
streak = [0]
game_lngth, hnd_win, hnd_lse = [0], [0], [0]  # Number of games, win/lose
cards = []
betting_strategy = [1, 1, 4]
winning_streak, losing_streak, old_ls, old_ws = [0], [0], [0], [0]


def end_hand(p, d):  # Player, Dealer cards
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
    if d_t > 21:
        msg = "Dealer bust. Player wins"
    elif d_t > p_t:
        msg = "Player loses"
    if p_t > 21:
        msg = "Player bust, loses"
    elif p_t > d_t:
        msg = "Player wins"

    if p_t == d_t:
        # Handle effing Blackjacks
        if p_t == 21:
            if len(p) == 2 and len(d) == 2:
                msg = "Push!"
            elif len(p) == 2:
                msg = "Player wins 3:2"
            elif len(d) == 2:
                msg = "Player loses"
            else:
                msg = "Push!"
        else:
            msg = "Push!"

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
    else:
        bank[0] += 2*int(c)*bet[0]
        bet[0] = betting_strategy[strat]
        bank[0] -= bet[0]

    msg = "{:^20}|{:^20}|{:^10}|{:^8}|{:^10}".format(
            "Game: {}, {}/{}".format(game_lngth[0], hnd_win[0], hnd_lse[0]),
            "win/lose {}, {}/{}".format(int(c), old_ws[0], old_ls[0]),
            "avg {}".format(cd_avg),
            "bet {}".format(bet[0]),
            "bank {}".format(bank[0]))
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


def message(who, hand):
    # repeat message routine
    cd = hand[-1]
    tot = sum(hand)
    # Opening hand
    if len(hand) == 2:
        if who == 'Dealer':
            # If Dealer has an ace...
            if hand[0] == 1:
                msg = "\n{} has an ace and one hidden card\n".format(who)
            else:
                msg = "\n{} has {} and one hidden card\n".format(who, hand[0])
            return msg, hand
            # Check for Players Blackjack
        elif BJ(p_cards):
                msg = "Player has an ace and a 10. Blackjack!"
                return msg, hand

            # No Blackjack but need to identify aces for soft total strategy
            elif hand[0] == 1 and hand[1] == 1:
                msg = "Player has two aces, total {}".format(tot+10)
            elif hand[0] == 1:
                hand[0] = 11
                # Need ace to be final card to trigger soft total strategy
                msg = "Player has an ace and {}, total {} or {}".format(
                        hand[1], tot, tot+10)
                hand[0], hand[1] = hand[1], hand[0]
            elif hand[1] == 1:
                hand[1] = 11
                msg = "Player has {} and an ace, total {} or {}".format(
                        hand[0], tot, tot+10)
            else:
                msg = "player has {} and {}, total {}".format(
                        hand[0], hand[1], tot)
            return msg, hand

    # Has ace, Bust? will return with card revalued to 1
    if cd == 11 and tot > 21:
        msg = "Bust"
        return msg, hand
    # Has hard total ace.
    if cd == 11:
        # Not bust, but hard total...
        if tot > 11:
            msg = "{} draws an ace, total {}".format(who, tot)
        # ...otherwise soft total
        else:
            msg = "{} draws an ace, total {} or {}".format(who, tot-10, tot)
    elif cd == 1:
        msg = "{} draws an ace, total {}".format(who, tot)
    else:
        msg = "{} draws {}, total {}".format(who, cd, tot)

    if tot > 21:
        msg = msg + ". Bust!"

    return msg, hand


def BJ(hand):
    if 1 in hand and sum(hand) == 11:
        return True
    else:
        False
        
        
# Main program starts here
while 1:
    ##############################
    # Set up game - Initial deal #
    ##############################

    while len(d_cards) != 2:
        d_cards.append(shoe.pop())
        p_cards.append(shoe.pop())

    # Check for Blackjacks first
    if BJ(p_cards):
        msg = "Player has an ace and a 10. Blackjack!"
        if BJ(d_cards) and d_cards[0] == 1:
            msg = "\nDealers hidden card is 10. Blackjack!"
        else:
            "\nDealers hidden card is an ace. Blackjack!"

    # Dealer total; Player total
    d_tot = sum(d_cards)
    p_tot = sum(p_cards)

    # Reveal opening hands...
    d_msg, d_cards = message('Dealer', d_cards)
    p_msg, p_cards = message('Player', p_cards)
    print(d_msg)
    print(p_msg)

    ###########################################
    #               Start playing             #
    ###########################################

    p_cards = players_strategy('Player', p_cards)







    # Player uses same strategy as Dealer
    p_tot = sum(p_cards)
    while p_tot < 17:
        p_cards.append(shoe.pop())
        if p_cards[-1] == 1:
            p_cards[-1] = 11
            p_tot = sum(p_cards)
        msg = message('Player', p_cards)
        if "Bust" in msg:
            if 11 in p_cards:
                p_cards[p_cards.index(11)] = 1
                msg = message('Player', p_cards)
                p_tot = sum(p_cards)
            if p_tot > 17:
                print(msg)
                break

    stand(p_cards, d_cards)
    p_cards, d_cards = end_hand(p_cards, d_cards)
    # break
    # sleep(1)  # input("press any key")

    if len(shoe) < 52:
        """print("------------------------")
        print(".----------------------.")
        print("|    Shuffling shoe    |")
        print("'----------------------'")
        print("'------------------------------------------------------'")"""
        shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*decks*4
        # shuffle shoe
        random.seed()
        random.shuffle(shoe)
