import random
import time
from hand_classV5 import Hand


class Player:
    def __init__(self, name, num_of_hands, total_num_of_fingers, player_num, fingers):
        self.name = name
        self.num_of_hands = num_of_hands
        self.my_hands = []
        for i in range(num_of_hands):
            if i + 1 == 1:
                self.my_hands.append(Hand(name + "'s " + str(i+1) + "st hand", total_num_of_fingers, int(fingers[i])))
            elif i + 1 == 2:
                self.my_hands.append(Hand(name + "'s " + str(i+1) + "nd hand", total_num_of_fingers, int(fingers[i])))
            elif i + 1 == 3:
                self.my_hands.append(Hand(name + "'s " + str(i+1) + "rd hand", total_num_of_fingers, int(fingers[i])))
            else:
                self.my_hands.append(Hand(name + "'s " + str(i+1) + "th hand", total_num_of_fingers, int(fingers[i])))
        self.player_num = player_num

    # def __init__(self, name):
    #     self.name = name
    #     self.my_hands[0] = Hand(name + "'s Left")
    #     self.my_hands[1] = Hand(name + "'s Right")

    def print_my_hand(self):
        all_my_hands = ''
        for i in range(self.num_of_hands):
            all_my_hands += str(self.my_hands[i].number_of_fingers_showing)
            all_my_hands += ' '
        if self.num_of_hands == 1:
            print("I am " + self.name + " my hand is " + all_my_hands)
        else:
            print("I am " + self.name + " my hands are " + all_my_hands)

    def print_my_hand_and_my_opponents_hand(self, opponent):
        # print('|' + str(self.player_num) + '|')
        if self.player_num == 1:
            opponent.print_my_hand()
            self.print_my_hand()
        elif self.player_num == 2:
            self.print_my_hand()
            opponent.print_my_hand()


    def my_hand_bops_opponents_hand(self, my_hand, opponents_hand, show):
        if not my_hand.is_it_okay_to_bop(opponents_hand):
            return False
        if show:
            print(my_hand.description_string() + " bops " + opponents_hand.description_string())  # prints who played what
        my_hand.bop_another_hand(opponents_hand)  # adds the two hands together
        return True

    def enter_move_by_keyboard(self, other_player, player_number, game):
        move = input("Player " + str(player_number) + " enter move: ")
        success = False
        where_to_split = move.find('to')
        if where_to_split != -1:
            try:
                hand_i_use = int(move[0:where_to_split-1]) - 1
                hand_they_use = int(move[where_to_split + 3:]) - 1
                # print('|' + str(hand_i_use) + '| |' + str(hand_they_use) +'|')
                success = self.my_hand_bops_opponents_hand(self.my_hands[hand_i_use], other_player.my_hands[hand_they_use], True)
            except:
                print('', end='')
        if not success:
            self.enter_move_by_keyboard(other_player, player_number, game)
            return
        self.print_my_hand_and_my_opponents_hand(other_player)

    def do_random_move(self, other_player):
        hands_i_have_left = []
        hands_they_have_left = []
        for i in range(self.num_of_hands):
            self.my_hands[i].is_hand_out()
            if self.my_hands[i].hand_out == 0:
                hands_i_have_left.append(i)
        for i in range(other_player.num_of_hands):
            other_player.my_hands[i].is_hand_out()
            if other_player.my_hands[i].hand_out == 0:
                hands_they_have_left.append(i)
        # play the move
        self.my_hand_bops_opponents_hand(self.my_hands[random.choice(hands_i_have_left)],
                other_player.my_hands[random.choice(hands_they_have_left)], True)
        time.sleep(.5)
        self.print_my_hand_and_my_opponents_hand(other_player)

    def do_smart_move(self, other_player, smarty_move):
        success = False
        # first checks if there is a smart choice
        if smarty_move[2] % 2 == 0:
            success = self.my_hand_bops_opponents_hand(self.my_hands[smarty_move[0]], other_player.my_hands[smarty_move[1]], True)
        if smarty_move[2] % 2 == 1:
            success = self.my_hand_bops_opponents_hand(self.my_hands[smarty_move[1]], other_player.my_hands[smarty_move[0]], True)
        if not success:
            self.do_random_move(other_player)
            return
        time.sleep(.5)
        self.print_my_hand_and_my_opponents_hand(other_player)

    def do_sequential_move(self, other_player, arr):
        # (hopefully) returns an array of hashes that the inputed hash
        # arr = [0, 0, hashes I lead to] --> arr[0] is which hand i use and arr[1] is hand they use
        temp_hands = []
        for i in other_player.my_hands:
            temp_hands.append(i.number_of_fingers_showing)
        temp_player = Player('temp', other_player.num_of_hands, other_player.my_hands[0].number_of_total_fingers, 2, temp_hands)
        if self.my_hands[arr[0]] != 0:
             if other_player.my_hands[arr[1]] != 0:
                self.my_hand_bops_opponents_hand(self.my_hands[arr[0]], other_player.my_hands[arr[1]], False)
                hash = ''
                # sorts hands into least to greatest
                # sorting my hands
                temp_hash = []
                for i in self.my_hands:
                    temp_hash.append(str(i))
                for i in range(len(temp_hash)):
                    for j in range(len(temp_hash)):
                        if temp_hash[i] < temp_hash[j]:
                            temp = temp_hash[i]
                            temp_hash[i] = temp_hash[j]
                            temp_hash[j] = temp
                for i in temp_hash:
                    hash += i
                temp_hash = []
                # sorting other player's hands
                for i in other_player.my_hands:
                    temp_hash.append(str(i))
                for i in range(len(temp_hash)):
                    for j in range(len(temp_hash)):
                        if temp_hash[i] < temp_hash[j]:
                            temp = temp_hash[i]
                            temp_hash[i] = temp_hash[j]
                            temp_hash[j] = temp
                for i in temp_hash:
                    hash += i
                append = True
                for i in arr:
                    if hash == i:
                        append = False
                if append:
                    arr.append(hash)
        if arr[0] == len(self.my_hands)-1:
            if arr[1] == len(other_player.my_hands)-1:
                # removes the counters
                arr.pop(0)
                arr.pop(0)
                # sorts the original hash
                hash = ''
                temp_hash = []
                for i in self.my_hands:
                    temp_hash.append(str(i))
                for i in range(len(temp_hash)):
                    for j in range(len(temp_hash)):
                        if temp_hash[i] < temp_hash[j]:
                            temp = temp_hash[i]
                            temp_hash[i] = temp_hash[j]
                            temp_hash[j] = temp
                for i in temp_hash:
                    hash += i
                temp_hash = []
                for i in temp_player.my_hands:
                    temp_hash.append(str(i))
                for i in range(len(temp_hash)):
                    for j in range(len(temp_hash)):
                        if temp_hash[i] < temp_hash[j]:
                            temp = temp_hash[i]
                            temp_hash[i] = temp_hash[j]
                            temp_hash[j] = temp
                for i in temp_hash:
                    hash += i
                arr.insert(0, hash)
                return arr
            else:
                arr[0] = 0
                arr[1] += 1
        else:
            arr[0] += 1
        return self.do_sequential_move(temp_player, arr)

    def am_i_out(self):
        out = True
        for i in range(len(self.my_hands)):
            if self.my_hands[i].hand_out == 0:
                out = False
        return out