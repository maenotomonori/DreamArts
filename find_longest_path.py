def find_longest_path(graph):
    longest_path = []
    max_length = -1.0

    def dfs(current_node, path, length):
        nonlocal longest_path, max_length
            
            # 現在の経路がこれまでの最長経路より長い場合、更新する
        if length > max_length:
            max_length = length
            longest_path = path[:]

            # すべての隣接ノードを探索
        for neighbor, distance in graph.get(current_node, []):
            if neighbor not in path:
                dfs(neighbor, path + [neighbor], length + distance)

    # 各ノードを潜在的な始点として繰り返し処理する
    all_nodes = list(graph.keys())
    for node in all_nodes:
        dfs(node, [node], 0.0)
        
    return longest_path, max_length