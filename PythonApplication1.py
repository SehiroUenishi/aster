# 上下左右のみ移動できる迷路でスタートからゴールへの最短経路探索を行うプログラム

# 迷路を定義　1が壁,0が道

maze = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
]

start_position = (0, 0)
end_position = (6, 6)


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0


def aster(maze, start_pos, end_pos):

    # スタートとゴールの初期化
    start_node = Node(None, start_pos)
    end_node = Node(None, end_pos)

    # オープンリストとクローズドリストを作成
    open_list = []
    closed_list = []

    open_list.append(start_node)

    # オープンリストがなくなるまで経路を探索
    while len(open_list) > 0:

        # 現在ノードとインデックスの変数を作成
        current_node = open_list[0]
        current_index = 0

        for index, listed_node in enumerate(open_list):
            # オープンリストの中でF値が一番小さいノードを選ぶ
            if listed_node.f < current_node.f:
                current_node = listed_node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        # 現在ノードがゴール
        if current_node.position == end_node.position:
            # 戻り値用のリスト作成
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # 現在ノードがゴールでない
        child_node = []

        for new_position in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # 迷路外かどうか判定
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # 壁かどうか判定
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # 子ノードを作成
            new_node = Node(current_node, node_position)
            child_node.append(new_node)

        # ノードのF,G,H値を計算
        for calculate_node in child_node:

            # すでに計算済みのノードは除外
            if (
                len(
                    [
                        closed_node
                        for closed_node in closed_list
                        if calculate_node.position == closed_node.position
                    ]
                )
                > 0
            ):
                continue

            if (
                len(
                    [
                        open_node
                        for open_node in open_list
                        if calculate_node.position == open_node.position
                    ]
                )
                > 0
            ):
                continue

            calculate_node.g = current_node.g + 1
            calculate_node.h = (
                (end_node.position[0] - calculate_node.position[0]) ** 2
            ) + ((end_node.position[1] - calculate_node.position[1]) ** 2)
            calculate_node.f = calculate_node.g + calculate_node.h

            open_list.append(calculate_node)


def main():
    maze_path = aster(maze, start_position, end_position)
    print(maze_path)


if __name__ == "__main__":
    main()