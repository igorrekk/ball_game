import random


class Ball:
    def __init__(self, balls):
        self.balls = balls

    def play(self):
        destroyed = 0
        destroyed_spisok = []

        while True:
            chains = self.find_ball()
            if not chains:
                break

            # Удаляем цепочки и считаем уничтоженные шарики
            destroyed_count = 0
            for start, end in reversed(chains):
                destroyed_count += end - start + 1
                destroyed_spisok.append(self.balls[start:end + 1])
                del self.balls[start:end + 1]

            destroyed += destroyed_count

        return destroyed, destroyed_spisok

    def find_ball(self):
        chains = []
        start = 0
        n = len(self.balls)
        for i in range(1, n + 1):
            if i == n or self.balls[i] != self.balls[start]:
                if i - start >= 3:
                    chains.append((start, i - 1))
                start = i
        return chains

    def get_balls(self):
        return self.balls


def main():
    while True:
        try:
            n = int(input("Введите количество шариков: "))
            if not (3 <= n <= 100000):
                print("Ошибка: Количество должно быть от 3 до 100000.")
                continue

            choice = input("Выбрать цвета рандомно? (y/любое другое): ").strip().lower()
            if choice == 'y':
                values = [random.randint(0, 9) for _ in range(n)]
            else:
                user_input = input(f"Введите {n} цветов через пробел (от 0 до 9): ")
                values = list(map(int, user_input.strip().split()))
                if len(values) != n:
                    print("Ошибка: Количество введённых значений не совпадает с заявленным.")
                    continue

            break

        except ValueError:
            print("Ошибка: Введите корректное число.")

    print("\nИсходный список шариков:")
    print(values)

    game = Ball(values)
    destroyed_count, destroyed_spisok = game.play()

    print("\nСписок шариков после удаления цепочек из 3 и более одинаковых:")
    print(game.get_balls())

    if destroyed_spisok:
        print("\nУдалённые цепочки:")
        for chain in destroyed_spisok:
            print(chain)
    else:
        print("\nЦепочек из 3 и более одинаковых шаров для удаления не найдено.")

    print(f"\nОбщее количество уничтоженных шариков: {destroyed_count}")


if __name__ == "__main__":
    main()
