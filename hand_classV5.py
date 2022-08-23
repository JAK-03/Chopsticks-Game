class Hand:
    # initializes properties of a hand
    def __init__(self, name, total_num_of_fingers, num_of_fingers_showing):
        self.number_of_total_fingers = total_num_of_fingers
        self.number_of_fingers_showing = num_of_fingers_showing
        self.hand_out = 0  # 0 is false (the hand is still in) and 1 is true (the hand is out)
        self.name = name

    # prints name and number of fingers showing
    def description_string(self):
        return self.name + "(" + str(self.number_of_fingers_showing) + ")"

    def add_fingers_showing(self, how_many_to_add):
        self.number_of_fingers_showing += how_many_to_add
        self.number_of_fingers_showing = self.number_of_fingers_showing % self.number_of_total_fingers
        # self.number_of_fingers_showing = \
        #     self.number_of_fingers_showing + how_many_to_add
        # if self.number_of_fingers_showing >= self.number_of_total_fingers:
        #     self.number_of_fingers_showing = \
        #         self.number_of_fingers_showing - self.number_of_total_fingers
        if self.number_of_fingers_showing == 0:
            self.hand_out = 1

    def is_hand_out(self):
        if self.hand_out == 0 and self.number_of_fingers_showing == 0:
            self.hand_out = 1

    def bop_another_hand(self, other_hand):
        other_hand.add_fingers_showing(self.number_of_fingers_showing)

    def is_it_okay_to_bop(self, other_hand):
        if self.hand_out == 1:
            print("Oh no, " + self.description_string() + " is out.  Can't play that.")
            return False  # failure!
        if other_hand.hand_out == 1:
            print("Oh no, " + other_hand.description_string() + " is out.  Can't play that.")
            return False  # failure!
        return True

    def __str__(self):
        return str(self.number_of_fingers_showing)