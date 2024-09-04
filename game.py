import random
import time

class Player:
    def __init__(self, name, speed, accuracy, stamina):
        self.name = name
        self.speed = speed
        self.accuracy = accuracy
        self.stamina = stamina
        self.special_ability = random.choice(["Super Dribble", "Power Shot"])

    def use_special_ability(self):
        return self.special_ability

class MyGame:
    def __init__(self):
        self.players = {}
        self.oppositions = {}
        self.pos = [0, 1]
        self.goal1 = 0
        self.goal2 = 0

    def add_player(self, name, speed, accuracy, stamina):
        self.players[name] = Player(name, speed, accuracy, stamina)

    def add_opposition(self, name, speed, accuracy, stamina):
        self.oppositions[name] = Player(name, speed, accuracy, stamina)

    def play(self, keeps, shoots, dribbles, defences, player_stats, shoot_stats, dribble_stats, defence_stats, keep_stats, player_names, opposition_names, goal_or_not, defence_text, goal_text, dribble_text, pass_text, teamname, oppname):
        self.keeps = keeps
        self.shoots = shoots
        self.dribbles = dribbles
        self.defences = defences
        self.player_stats = player_stats
        self.shoot_stats = shoot_stats
        self.dribble_stats = dribble_stats
        self.defence_stats = defence_stats
        self.keep_stats = keep_stats
        self.player_names = player_names
        self.opposition_names = opposition_names
        self.goal_or_not = goal_or_not
        self.defence_text = defence_text
        self.goal_text = goal_text
        self.dribble_text = dribble_text
        self.pass_text = pass_text
        self.teamname = teamname
        self.oppname = oppname

        self.start_time = time.time()
        self.play_match()

    def play_match(self):
        while (time.time() - self.start_time) <= 180:
            if self.possession() == 0:
                self.player_turn()
            else:
                self.opposition_turn()

        self.end_match()

    def possession(self):
        return random.choice(self.pos)

    def player_turn(self):
        player = random.choice(list(self.players.values()))
        print(f"{player.name} [s]hoot, [d]ribble, [p]ass, [a]bility")
        action = input()
        time.sleep(2)
        if action.lower() == 's':
            self.handle_shoot(player)
        elif action.lower() == 'd':
            self.handle_dribble(player)
        elif action.lower() == 'p':
            self.handle_pass(player)
        elif action.lower() == 'a':
            self.use_special_ability(player)

    def handle_shoot(self, player):
        print(f"{player.name} takes a shot!")
        shot_type = input(f"Choose a shot type {list(self.shoots.keys())}: ").lower()
        time.sleep(2)
        if shot_type not in self.shoots:
            print('Invalid shot type')
            return

        shoot_value = self.shoot_stats[shot_type]
        defence = random.choice(self.defences)
        defence_value = self.defence_stats[defence]

        if shoot_value < defence_value:
            print(f"But {random.choice(self.opposition_names)} defends it")
            time.sleep(2)
            self.pos = [1]
        else:
            keep_type = random.choice(self.keeps)
            keep_value = self.keep_stats[keep_type]

            if shoot_value < keep_value:
                print(f"But {random.choice(self.opposition_names)} saves it")
                self.pos = [1]
            else:
                if random.choice(self.goal_or_not) == 0:
                    print(f"But {random.choice(self.opposition_names)} saves it")
                    self.pos = [1]
                else:
                    print(f"Nice Shot! {random.choice(self.goal_text)}")
                    self.goal1 += 1
                    self.pos = [1]

        print(f"Score: {self.teamname} {self.goal1} - {self.oppname} {self.goal2}")
        time.sleep(2)

    def handle_dribble(self, player):
        print(f"{player.name} attempts to dribble!")
        dribble_type = input(f"Choose a dribble type {list(self.dribbles.keys())}: ").lower()
        time.sleep(2)
        if dribble_type not in self.dribbles:
            print('Invalid dribble type')
            return

        dribble_value = self.dribble_stats[dribble_type]
        opposition = random.choice(self.oppositions.values())
        opposition_value = opposition.speed

        if dribble_value > opposition_value:
            print(f"{random.choice(self.dribble_text)}")
            self.pos = [0]
        else:
            print("But he lost the ball")
            self.pos = [1]

        time.sleep(2)

    def handle_pass(self, player):
        print(f"{player.name} makes a pass!")

        pass_value = self.player_stats[player.name]
        opposition = random.choice(self.oppositions.values())
        opposition_value = opposition.speed

        if pass_value > opposition_value:
            print(f"{random.choice(self.pass_text)}")
            self.pos = [0]
        else:
            print("But he missed the pass")
            self.pos = [1]

        time.sleep(2)

    def use_special_ability(self, player):
        ability = player.use_special_ability()
        print(f"{player.name} uses special ability: {ability}!")
        if ability == "Power Shot":
            self.handle_shoot(player)
        elif ability == "Super Dribble":
            self.handle_dribble(player)

    def opposition_turn(self):
        opposition = random.choice(list(self.oppositions.values()))
        print(f"{opposition.name} is with the ball")
        action = random.choice(['s', 'd', 'p'])
        time.sleep(2)

        if action == 's':
            self.opposition_shoot(opposition)
        elif action == 'd':
            self.opposition_dribble(opposition)
        elif action == 'p':
            self.opposition_pass(opposition)

    def opposition_shoot(self, opposition):
        print(f"{opposition.name} takes a shot!")
        shot_type = random.choice(list(self.shoots.keys()))
        print(f"Shot type: {shot_type}")
        shoot_value = self.shoot_stats[shot_type]
        defence_type = random.choice(self.defences)
        defence_value = self.defence_stats[defence_type]

        if shoot_value < defence_value:
            print(f"{random.choice(self.defence_text)}")
            self.pos = [0]
        else:
            keep_type = random.choice(self.keeps)
            keep_value = self.keep_stats[keep_type]

            if shoot_value < keep_value:
                print(f"But {random.choice(self.player_names)} saves it")
                self.pos = [0]
            else:
                if random.choice(self.goal_or_not) == 0:
                    print(f"But {random.choice(self.player_names)} saves it")
                    self.pos = [0]
                else:
                    print(f"{random.choice(self.goal_text)}")
                    self.goal2 += 1
                    self.pos = [0]

        print(f"Score: {self.teamname} {self.goal1} - {self.oppname} {self.goal2}")
        time.sleep(2)

    def opposition_dribble(self, opposition):
        print(f"{opposition.name} attempts to dribble!")
        dribble_type = random.choice(list(self.dribbles.keys()))
        print(f"Dribble type: {dribble_type}")
        dribble_value = self.dribble_stats[dribble_type]
        player = random.choice(list(self.players.values()))
        player_value = player.speed

        if dribble_value > player_value:
            print(f"{random.choice(self.dribble_text)}")
            self.pos = [1]
        else:
            print("But he lost the ball")
            self.pos = [0]

        time.sleep(2)

    def opposition_pass(self, opposition):
        print(f"{opposition.name} makes a pass!")
        pass_type = random.choice(list(self.shoots.keys()))
        print(f"Pass type: {pass_type}")
        pass_value = opposition.speed
        player = random.choice(list(self.players.values()))
        player_value = player.speed

        if pass_value > player_value:
            print(f"{random.choice(self.pass_text)}")
            self.pos = [1]
        else:
            print("But he missed the pass")
            self.pos = [0]

        time.sleep(2)

    def end_match(self):
        print(f"And that's the end of the match!\nBeautiful match if I say so myself\nAll players played their parts perfectly well\nAnd it was worth the effort")
        print(f"Final Score: {self.teamname} {self.goal1} - {self.oppname} {self.goal2}")
        player_pos = round((self.player_possesion / (self.player_possesion + self.opposition_possesion)) * 100)
        opposition_pos = round((self.opposition_possesion / (self.player_possesion + self.opposition_possesion)) * 100, 2)
        print(f"{self.team
