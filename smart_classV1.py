from hand_classV5 import Hand
from game_classV5 import Game
import player_classV5
class Smart:
    def __init__(self, p1, p2, game):
        self.p1 = p1
        self.p2 = p2
        self.game = game
        self.game_info = Game.return_pos_info(self.game)
        self.complete_array_p1 = []
        self.complete_array_p2 = []


    def set_all_positions(self):
        from itertools import combinations_with_replacement
        k = self.game_info[0]
        l = self.game_info[1]
        result1 = list(combinations_with_replacement(range(0, self.game_info[2]), k))
        result2 = list(combinations_with_replacement(range(0, self.game_info[3]), l))
        hashes1 = []
        hashes2 = []
        base = 10
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
        return hashes

    def match_all_positions(self, hashes): # not needed
        big_hashes= []
        for i in hashes:
            for j in hashes:
                big_hashes.append(int(str(i)+str(j)))
        return big_hashes


    # def expand_hash(self, hash):
    #     for i in range(len(hash)):
    #         p1_hands.append()
    #
    # p1_hands = player_classV5.Player("player 1", self.hand_finger_info[0], self.hand_finger_info[2], 1, [])
    #     pass


    # p1_hands and p2_hands are the index that they are in their respective complete_array
    # turn is 1 when player 1 is doing the bopping, and 2 when player 2 is doing the bopping
    # function will return arr with the indexes (in complete_array) of all possible immediate futures
    # [[[p1 hands], [p2 hands], [p1 hand used, p2 hand used], [...]]
    def find_next_move(self, p1_hands, p2_hands, turn):
        if turn % 2 == 1:
            for i in range(len(p1_hands)):
                for i in range(len(p2_hands)):
                    pass

    def sort_least_to_greatest(self, arr): # don't think i need this
        for i in range(len(arr)):
            for j in range(len(arr-1)):
                if arr[i] > arr[j+1]: # might have to switch to arr[i].number_of_fingers...
                    temp = arr[i]
                    arr[i] = arr[j+1]
                    arr[j+1] = temp
        return arr





    '''
    
    int(str(self.my_players[1].my_hands[0])) - turns num of finger showing to int
    
    base_10_num = int('num', base) <-- turns any base into base 10
    
    huge arr
        arr with hand pos, opponent hand pos, #id
    
    functions
        leads to
            will take an arr and return an arr with #ids for what next pos could be
        get all pos
            will populate the huge arr
        best move
            will take an arr and return best move
        sort arr
            will sort current pos into a temp sorted arr
        find spot
            once the best move is found, this will return the hand spot that you use and the oppent uses (unsorting)
            
    '''