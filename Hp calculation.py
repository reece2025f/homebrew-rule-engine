class CharacterClass:
    HIT_DIE_DATA = {
        6: {"max": 6, "full_avg": 4, "half_avg": 2},
        8: {"max": 8, "full_avg": 5, "half_avg": 3},
        10: {"max": 10, "full_avg": 6, "half_avg": 3},
        12: {"max": 12, "full_avg": 7, "half_avg": 4},
    }

    def __init__(self, hit_die, level):
        self.hit_die = hit_die
        self.level = level

    @classmethod
    def is_valid_hit_die(cls, hit_die):
        return hit_die in cls.HIT_DIE_DATA

    def calculate_primary_health(self, con):
        health = self.HIT_DIE_DATA[self.hit_die]["max"] + con
        if self.level > 1:
            health += (self.HIT_DIE_DATA[self.hit_die]["full_avg"] + con) * (self.level - 1)
        return health

    def calculate_multiclass_health(self, primary_class_level):
        capped_level = min(self.level, primary_class_level)
        return self.HIT_DIE_DATA[self.hit_die]["half_avg"] * capped_level


class HealthCalculator:
    def __init__(self):
        self.con = 0
        self.primary_class = None
        self.multiclasses = []

    def get_int_input(self, prompt, error_message="Enter a valid int"):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print(error_message)

    def prompt_con(self):
        self.con = self.get_int_input("Enter your con bonus: ")

    def prompt_primary_class(self):
        while True:
            hit_die = self.get_int_input("Enter your current class hit die (6, 8, 10, or 12): ", "Enter a valid hit die")
            if not CharacterClass.is_valid_hit_die(hit_die):
                print("Hit die must be 6, 8, 10, or 12")
                continue
            break

        while True:
            level = self.get_int_input("Enter your current class level: ")
            if level <= 0:
                print("Enter a class level of at least 1")
                continue
            break

        self.primary_class = CharacterClass(hit_die, level)

    def prompt_multiclasses(self):
        while True:
            response = input("Add a multiclass? (y/n): ").strip().lower()
            if response != "y":
                break
            while True:
                hit_die_input = input("Enter multiclass hit die (6, 8, 10, 12, or back): ").strip().lower()
                if hit_die_input == "back":
                    break
                try:
                    hit_die = int(hit_die_input)
                    if not CharacterClass.is_valid_hit_die(hit_die):
                        print("Hit die must be 6, 8, 10, or 12")
                        continue
                except ValueError:
                    print("Enter a valid int or back")
                    continue

                level_input = input("Enter level in that class or back: ").strip().lower()
                if level_input == "back":
                    continue
                try:
                    level = int(level_input)
                    if level <= 0:
                        print("Enter a multiclass level of at least 1")
                        continue
                    self.multiclasses.append(CharacterClass(hit_die, level))
                    break
                except ValueError:
                    print("Enter a valid int or back")

    def calculate_total_health(self):
        total_health = self.primary_class.calculate_primary_health(self.con)
        for mc in self.multiclasses:
            total_health += mc.calculate_multiclass_health(self.primary_class.level)
        return max(1, total_health)

    def run(self):
        self.prompt_con()
        self.prompt_primary_class()
        self.prompt_multiclasses()
        total_health = self.calculate_total_health()
        print(f"Total health: {total_health}")


class Application:
    def run(self):
        while True:
            calculator = HealthCalculator()
            calculator.run()
            while True:
                choice = input("Enter exit to quit or redo to restart: ").strip().lower()
                if choice == 'exit':
                    return
                elif choice == 'redo':
                    break
                else:
                    print("Please type exit or redo.")


if __name__ == "__main__":
    app = Application()
    app.run()