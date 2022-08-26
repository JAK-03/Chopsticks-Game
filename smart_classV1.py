from game_classV5 import Game
import player_classV5

class Smart:
    def __init__(self,  game):
        self.game = game
        self.hashes = []
        self.game_info = Game.return_pos_info(self.game)

    def set_all_positions(self):
        from itertools import combinations_with_replacement
        k = self.game_info[0]
        l = self.game_info[1]
        result1 = list(combinations_with_replacement(range(0, self.game_info[2]), k)) # needs to be able to handle more than 10 digits - cannot now
        result2 = list(combinations_with_replacement(range(0, self.game_info[3]), l))
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
        self.hashes = hashes
        return hashes


    def expand_hash(self, hash):
        hands = []
        p1_hands = hash[0:self.game_info[0]]
        p2_hands = hash[self.game_info[0]:]
        hands.append(p1_hands)
        hands.append(p2_hands)
        return hands

    def find_next_moves(self, hash):
        hands = self.expand_hash(hash)
        temp_1 = player_classV5.Player('temp 1', self.game_info[0], self.game_info[2], 1, hands[0])
        temp_2 = player_classV5.Player('temp 2', self.game_info[1], self.game_info[3], 1, hands[1])
        result = temp_1.do_sequential_move(temp_2, [0,0])
        return result #???

    def find_all_next_moves(self, next_move_arr):
        pass

# find next moves
# find best move



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