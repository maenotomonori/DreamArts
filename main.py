import sys
from find_longest_path import find_longest_path

def main():
    graph = {}
    
    # 標準入力からデータを読み込む
    for line in sys.stdin:
        line = line.strip()

        if line == "find":
            break
        
        if not line:
            continue
        
        try:
            start_node, end_node, distance = line.split()
            start_node = int(start_node)
            end_node = int(end_node)
            distance = float(distance)

            if start_node <= 0 or end_node <= 0:
                print("ノードIDは正の値で入力してください。")
                continue

            if distance <= 0:
                print("距離は正の値で入力してください。")
                continue

            if start_node == end_node:
                print("警告: 自己ループが検出されました。この辺は無視されます。")
                continue

        except ValueError:
            print("入力形式が正しくありません")
            continue

        # グラフにエッジを追加する。グラフは無向である。
        if start_node not in graph:
            graph[start_node] = []
        if end_node not in graph:
            graph[end_node] = []

        graph[start_node].append((end_node, distance))
        graph[end_node].append((start_node, distance))
        
    if not graph:
        print("グラフが空です。")
        return

    # 最長経路を見つける
    longest_path, max_length = find_longest_path(graph)

    # 結果を出力する
    for node in longest_path:
        print(node)

if __name__ == "__main__":
    main()