import player_classV5


class Game:
    def __init__(self):
        self.hand_finger_info = self.get_hands_and_fingers([])
        self.my_players = [player_classV5.Player("player 1", self.hand_finger_info[0], self.hand_finger_info[2], 1, self.hand_finger_info[4]),
                           player_classV5.Player("player 2", self.hand_finger_info[1], self.hand_finger_info[3], 2, self.hand_finger_info[5])]
        global is_player1_a_bot
        is_player1_a_bot = False
        global is_player2_a_bot
        is_player2_a_bot = True

    def get_hands_and_fingers(self, info):
        if len(info) == 0:
            try: # asks the user for input, if it is not an int, it will ask again
                info.append(int(input('How many hands should player 1 have?: ')))
            except:
                self.get_hands_and_fingers(info)
        if len(info) == 1:
            try:
                info.append(int(input('How many hands should player 2 have?: ')))
            except:
                self.get_hands_and_fingers(info)
        if len(info) == 2:
            try:
                info.append(int(input('How many fingers per hand should player 1 have?: ')))
            except:
                self.get_hands_and_fingers(info)
        if len(info) == 3:
            try:
                info.append(int(input('How many fingers per hand should player 2 have?: ')))
            except:
                self.get_hands_and_fingers(info)
        p1_finger_start = [] # sets all of p1's hands to 1
        for i in range(info[0]):
            p1_finger_start.append(1)
        info.append(p1_finger_start)
        p2_finger_start = [] # sets all of p2's hands to 1
        for i in range(info[1]):
            p2_finger_start.append(1)
        info.append(p2_finger_start)
        return info

    def return_pos_info(self):
        return self.hand_finger_info

    def play(self):
        who_player1_plays_on = self.my_players[1]
        who_player2_plays_on = self.my_players[0]
        global turn
        turn = 0

        self.set_all_positions()
        while True:
            # checks if p1 is out
            is_player1_out = self.my_players[0].am_i_out()

            # player 1 gets a turn
            if is_player1_out == False:
                global is_player1_a_bot
                if is_player1_a_bot == False:
                    self.my_players[0].enter_move_by_keyboard(who_player1_plays_on, 1, self)
                elif is_player1_a_bot == True:
                    result = self.one_smart_move(self.tokenize_game_state_p1(), self.tokenize_game_state_p2())
                    if result != []:
                        self.my_players[0].do_smart_move(who_player1_plays_on, result)
                    else:
                        self.my_players[0].do_random_move(who_player1_plays_on)
                turn += 1


            if is_player1_out == True:
                print('Player 2 wins!!! Thanks for playing!')
                print('That game was ' + str(turn) + ' turns long')
                break

            # player 2 gets a turn, but first checks if he is out
            is_player2_out = self.my_players[1].am_i_out()

            if is_player2_out == False:
                global is_player2_a_bot
                if is_player2_a_bot == False:
                    self.my_players[1].enter_move_by_keyboard(who_player2_plays_on, 2, self)
                elif is_player2_a_bot == True:
                    result = self.one_smart_move(self.tokenize_game_state_p1(), self.tokenize_game_state_p2())
                    if result != []:
                        self.my_players[1].do_smart_move(who_player2_plays_on, result)
                    else:
                        self.my_players[1].do_random_move(who_player2_plays_on)
                turn += 1

            if is_player2_out == True:
                print('Player 1 wins!!! Thanks for playing!')
                print('That game was ' + str(turn) + ' turns long')
                break

            # checks if the game is going too long
            if turn == (6*self.my_players[0].my_hands[0].number_of_total_fingers)*len(self.my_players[0].my_hands) or \
                    turn == 12*self.my_players[0].my_hands[0].number_of_total_fingers*len(self.my_players[0].my_hands):
                quit_game = input("It looks like the game is a loop, would you like to quit? (yes/no)")
                if quit_game == "yes":
                    quit_game_confirm = input("Are you sure you would like to stop playing? (yes/no)")
                    if quit_game_confirm == "yes":
                        break
            if turn == 24*self.my_players[0].my_hands[0].number_of_total_fingers*len(self.my_players[0].my_hands):
                print("Your game was to long .______.")
                break

    # puts all of p1's info in a list
    def tokenize_game_state_p1(self):
        current_token_of_game = []
        for i in range(self.my_players[0].num_of_hands):
            current_token_of_game.append(self.my_players[0].my_hands[i].number_of_fingers_showing)
        return current_token_of_game

    # puts all of p2's info in a list
    def tokenize_game_state_p2(self):
        current_token_of_game = []
        for i in range(self.my_players[1].num_of_hands):
            current_token_of_game.append(self.my_players[1].my_hands[i].number_of_fingers_showing)
        return current_token_of_game

    # will check if the bot can take out a hand
    def one_smart_move(self, p1_token, p2_token):
        for p1 in range(len(p1_token)):
            for p2 in range(len(p2_token)):
                if self.my_players[0].my_hands[p1].number_of_fingers_showing + \
                        self.my_players[1].my_hands[p2].number_of_fingers_showing \
                        == self.my_players[0].my_hands[0].number_of_total_fingers:
                    return [p1, p2, turn]  # will return which hand p1 uses and which hand p2 uses
        return []  # default --> returns nothing


    def set_all_positions(self):
        from itertools import combinations_with_replacement
        # from hand_classV5 import Hand
        # hand = Hand('test', self.hand_finger_info[2])
        k = self.hand_finger_info[0]
        l = self.hand_finger_info[1]
        result1 = list(combinations_with_replacement(range(0, self.hand_finger_info[2]), k))
        result2 = list(combinations_with_replacement(range(0, self.hand_finger_info[3]), l))
        hashes1 = []
        hashes2 = []
        for i in range(len(result1)):
            hash = ''
            for j in range(len(result1[i])):
                hash += str(result1[i][j])
            hashes1.append(hash)
        for i in range(len(result2)):
            hash = ''
            for j in range(len(result2[i])):
                hash += str(result2[i][j])
            hashes2.append(hash)
        hashes = []
        for i in hashes1:
            for j in hashes2:
                hashes.append(str(i)+str(j))
        print('-')
        print(hashes)
        print('-')
        self.expand_hash(hashes[58])

    def expand_hash(self, hash):
        print('hash: ' + str(hash))
        p1_hands = hash[0:self.hand_finger_info[0]]
        p2_hands = hash[self.hand_finger_info[0]:]
        print(p1_hands)
        print(p2_hands)
        print('-')


        # from hand_classV5 import Hand # makes everything a Hand
        # complete_array_p1 = []
        # for i in range (len(result)):
        #     temp_arr = []
        #     for j in range(len(result[i])):
        #         temp_arr.append(Hand('', self.return_pos_info()[2], result[i][j]))
        #     complete_array_p1.append(temp_arr)
        # print('-')
        # for i in range (len(complete_array_p1)):
        #     for j in range (len(complete_array_p1[i])):
        #         print(type(complete_array_p1[i][j]))




# actually runs the game
# Game.set_all_positions(Game())
Game.play(Game())
while True:
    print()
    play_again = input('Would you like to play again? (yes/no): ')
    if play_again == 'yes':
        print()
        Game.play(Game())
    else:
        print('Thanks for playing! Have a nice day :)')
        break


# original
        # self.my_hand_bops_opponents_hand(self.my_hands[0], other_player.my_hands[1])
        # lists a number of tokens for possible next game states
        # e.g. [ [2 1 3 3 2] [2 1 1 0 2] [2 1 2 3 2] [2 1 1 4 2] ]
'''
    def sequence_human_vs_human_game(self):
        pass
        # do the game logic so that
        # A vs B, B vs A, ... until someone wins.

    def sequence_human_vs_machine_game(self):
        pass
        # do the game logic so that
        # A vs B, B vs A, ... until someone wins.

    def move_to_given_token_state(self, token):
        pass
        # makes machine move so that the next state is the one represented in the token

    def choose_a_random_token_from_a_list_of_possible_futures(self, token_list):
        pass
        as a staring point, pick randomly from the list given to me
'''