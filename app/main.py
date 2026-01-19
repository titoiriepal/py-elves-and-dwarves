from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player):

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        text = f"{self.nickname} is playing"
        text += f" a song on the {self._musical_instrument}"
        print(text)


class Dwarf(Player):

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):

    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        bow_level: int,
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> None:
        return self._bow_level * 3

    def player_info(self) -> str:
        text = f"Elf Ranger {self.nickname}. "
        text += f"{self.nickname} has bow of the {self._bow_level} level."
        return text


class Druid(Elf):

    def __init__(
        self, nickname: str, musical_instrument: str, favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        text = f"Druid {self.nickname}. "
        text += f"{self.nickname} has a "
        text += f"favourite_spell: {self._favourite_spell}"
        return text


class DwarfWarrior(Dwarf):

    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int,
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        text = f"Dwarf warrior {self.nickname}. "
        text += f"{self.nickname} has a hummer "
        text += f"of the {self._hummer_level} level."
        return text


class DwarfBlacksmith(Dwarf):

    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        skill_level: int,
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self) -> None:
        return self._skill_level

    def player_info(self) -> str:
        text = f"Dwarf blacksmith {self.nickname} "
        text += f"with the skill of the {self._skill_level} level."
        return text


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        print(elf.play_elf_song())
