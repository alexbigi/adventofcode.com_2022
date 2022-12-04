from typing import Dict


def main():
    first_total: int = 0
    second_total: int = 0
    knb_dict: Dict[str, int] = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }
    knb_winner: Dict[str, int] = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }

    with open('input.txt') as f:
        while True:
            line: str = f.readline()
            if not line:
                break
            first_total += knb_dict[line.strip()]
            second_total += knb_winner[line.strip()]
    print(first_total)
    print(second_total)


if __name__ == "__main__":
    main()
