class Player(object):
    """Az osztaly leirasa."""
    # class Player:

    GENDER = ('male', 'female', 'other')

    def __init__(self, first_name: str, last_name: str, height_cm: int, weight_kg: int = None):
        """Init metodus.

        Ez a medodus hivodik meg a peldanyositas soram.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.height_cm: int = height_cm
        self.weight_kg: int = weight_kg
        self.personal_data: dict = {}

    @staticmethod
    def static_weight_to_lbs(weight_kg: int) -> float:
        pounds = weight_kg * 2.20462262
        return pounds

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    """Kosarlabda jatekost reprezentalo osztaly."""

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Object: {self.string}'

    def __init__(
        self, first_name, last_name, height_cm,
            points, rebounds, assists, weight_kg=None,):
        super().__init__(
            first_name=first_name, last_name=last_name,
            height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def weight_to_lbs(self):
        # Feluldefinialjuk a Player metodusat.
        return 'Ez fog lefutni a BasketballPlayeren'

    def weight_lbs(self):
        return super().weight_to_lbs()


class FootballPlayer(Player):

    def __init__(self, first_name, last_name, height_cm, weight_kg,
                 goals, yellow_cards, red_cards):
        super().__init__(
            first_name=first_name, last_name=last_name,
            height_cm=height_cm, weight_kg=weight_kg,
        )
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(
    first_name="Lebron", last_name="James",
    height_cm=203, weight_kg=113,
    points=27.2, rebounds=7.4, assists=7.2,
)
kev_dur = BasketballPlayer(
    first_name="Kevin", last_name="Durant",
    height_cm=210, weight_kg=108,
    points=27.2, rebounds=7.1, assists=4,
)

print(lebron.__doc__)
print(lebron.first_name)
print(lebron.height_cm)

print(kev_dur.last_name)
print(kev_dur.rebounds)

print(lebron.weight_lbs())
print(Player.static_weight_to_lbs(80))

# list of players
# bball_players = [lebron, kev_dur]

# for player in bball_players:
#     print(player.last_name + ", " + player.first_name)
