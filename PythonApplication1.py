# �㉺���E�݈̂ړ��ł�����H�ŃX�^�[�g����S�[���ւ̍ŒZ�o�H�T�����s���v���O����

# ���H���`�@1����,0����

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

    # �X�^�[�g�ƃS�[���̏�����
    start_node = Node(None, start_pos)
    end_node = Node(None, end_pos)

    # �I�[�v�����X�g�ƃN���[�Y�h���X�g���쐬
    open_list = []
    closed_list = []

    open_list.append(start_node)

    # �I�[�v�����X�g���Ȃ��Ȃ�܂Ōo�H��T��
    while len(open_list) > 0:

        # ���݃m�[�h�ƃC���f�b�N�X�̕ϐ����쐬
        current_node = open_list[0]
        current_index = 0

        for index, listed_node in enumerate(open_list):
            # �I�[�v�����X�g�̒���F�l����ԏ������m�[�h��I��
            if listed_node.f < current_node.f:
                current_node = listed_node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        # ���݃m�[�h���S�[��
        if current_node.position == end_node.position:
            # �߂�l�p�̃��X�g�쐬
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # ���݃m�[�h���S�[���łȂ�
        child_node = []

        for new_position in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # ���H�O���ǂ�������
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # �ǂ��ǂ�������
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # �q�m�[�h���쐬
            new_node = Node(current_node, node_position)
            child_node.append(new_node)

        # �m�[�h��F,G,H�l���v�Z
        for calculate_node in child_node:

            # ���łɌv�Z�ς݂̃m�[�h�͏��O
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