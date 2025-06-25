import random
from collections import deque

def init_maze(n):
    return [['V'] * n for _ in range(n)]

def carve_passages_from(x, y, maze, n):
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx < n - 1 and 1 <= ny < n - 1 and maze[nx][ny] == 'V':
            maze[x + dx // 2][y + dy // 2] = ' '
            maze[nx][ny] = ' '
            carve_passages_from(nx, ny, maze, n)

def generate_maze(n):
    if n % 2 == 0:
        n += 1
    maze = init_maze(n)
    maze[1][1] = ' '
    carve_passages_from(1, 1, maze, n)
    maze[n - 2][n - 1] = 'N'  # выход
    return maze, (n - 2, n - 2)

def save_maze_to_file(maze, filename="labirint.txt"):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def read_maze_from_file(filename="labirint.txt"):
    with open(filename, 'r') as f:
        maze = [list(line.strip('\n')) for line in f]
    exit_pos = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'N':
                exit_pos = (i, j)
    return maze, exit_pos

def print_maze(maze):
    GREEN = '\033[92m'
    RESET = '\033[0m'
    for row in maze:
        line = ''
        for ch in row:
            if ch == '+':
                line += GREEN + '+' + RESET
            elif ch == 'N':
                line += GREEN + 'N' + RESET
            elif ch == 'B':
                line += GREEN + 'B' + RESET
            else:
                line += ch
        print(line)

def find_path(maze, start, exit_pos):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]  # Матрица посещённых клеток
    parent = [[None] * n for _ in range(n)]  # Матрица для хранения "откуда пришли"
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x, y = queue.popleft()
        if (x, y) == exit_pos:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maze[nx][ny] in (' ', 'N'):
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    queue.append((nx, ny))
    path = []
    cur = exit_pos
    while cur != start:
        path.append(cur)
        cur = parent[cur[0]][cur[1]]
        if cur is None:
            return []
    path.append(start)
    path.reverse()
    return path

def mark_path(maze, path):
    for x, y in path:
        if maze[x][y] not in ('B', 'N'):
            maze[x][y] = '+'

def input_start_position(maze):
    n = len(maze)
    while True:
        try:
            x = int(input(f"Введите X координату мышки (1..{n-2}): "))
            y = int(input(f"Введите Y координату мышки (1..{n-2}): "))
            if 1 <= x <= n - 2 and 1 <= y <= n - 2:
                if maze[x][y] == ' ':
                    maze[x][y] = 'B'
                    return (x, y)
                else:
                    print("Там стена (V), выберите другую позицию.")
            else:
                print("Координаты вне допустимого диапазона.")
        except ValueError:
            print("Введите целые числа.")

def main():
    while True:
        try:
            N = int(input("Введите размер лабиринта (нечётное число от 5 до 15): "))
            if 5 <= N <= 15:
                if N % 2 == 0:
                    print("Размер должен быть нечётным. Увеличиваем на 1.")
                    N += 1
                break
            else:
                print("Введите число от 5 до 15.")
        except ValueError:
            print("Неверный ввод.")

    maze, _ = generate_maze(N)
    save_maze_to_file(maze)

    maze, exit_pos = read_maze_from_file()

    print("\nСчитанный лабиринт (выход обозначен как N):")
    print_maze(maze)

    start = input_start_position(maze)

    path = find_path(maze, start, exit_pos)
    if not path:
        print("\nПуть до выхода не найден.")
    else:
        mark_path(maze, path)
        print("\nПуть найден:")
        print_maze(maze)
        print(f"\nДлина пути: {len(path)}")

if __name__ == "__main__":
    main()
