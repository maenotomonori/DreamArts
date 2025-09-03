import sys

def find_longest_path(graph):
    longest_path = []
    max_length = -1.0

    def dfs(current_node, path, length):
        nonlocal longest_path, max_length
        
        # 現在の経路がこれまでの最長経路より長い場合、更新する
        if length > max_length:
            max_length = length
            longest_path = path[:]

        # すべての隣接ノードを探索する
        for neighbor, distance in graph.get(current_node, []):
            if neighbor not in path:
                # 隣接ノードに対して再帰的にdfsを呼び出す
                dfs(neighbor, path + [neighbor], length + distance)

    # 各ノードを潜在的な始点として繰り返し処理する
    all_nodes = list(graph.keys())
    for node in all_nodes:
        dfs(node, [node], 0.0)
        
    return longest_path, max_length

def main():
    graph = {}
    
    # 標準入力からデータを読み込む
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            start_node, end_node, distance = line.split()
            start_node = int(start_node)
            end_node = int(end_node)
            distance = float(distance)
        except ValueError:
            # 期待される形式に一致しない行はスキップする
            continue

        # グラフにエッジを追加する。グラフは無向である。
        if start_node not in graph:
            graph[start_node] = []
        if end_node not in graph:
            graph[end_node] = []

        graph[start_node].append((end_node, distance))
        graph[end_node].append((start_node, distance))
        
    # グラフが空の場合を処理する
    if not graph:
        print()
        return

    # 最長経路を見つける
    longest_path, max_length = find_longest_path(graph)

    # 結果を出力する
    for node in longest_path:
        print(node)

if __name__ == "__main__":
    main()
