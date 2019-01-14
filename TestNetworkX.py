# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx

if (__name__ == "__main__"):
    node1 = "test1@example.com"
    node2 = "test2@gmail.com"
    node3 = "test3@yahoo.co.jp"
    node4 = "test4@hotmail.co.jp"
    node5 = "test5@outlook.com"
    node6 = "test6@yahoo.com"
    node7 = "test7@outlook.com"
    node8 = "test8@icloud.com"
    node9 = "test9@hotmail.com"
    node10 = "test10@outlook.co.jp"
    G = nx.DiGraph()
    # ノードの追加
    G.add_node(node1, count=2)
    G.add_node(node2, count=1)
    G.add_node(node3, count=1)
    G.add_node(node4, count=1)
    G.add_node(node5, count=1)
    G.add_node(node6, count=1)
    G.add_node(node7, count=1)
    G.add_node(node8, count=1)
    G.add_node(node9, count=1)
    G.add_node(node10, count=1)

    #　エッジの追加
    G.add_edge(node1, node2, weight=15)
    G.add_edge(node1, node3, weight=33)
    G.add_edge(node1, node4, weight=17)
    G.add_edge(node1, node5, weight=7)
    G.add_edge(node1, node6, weight=21)
    G.add_edge(node1, node7, weight=9)
    G.add_edge(node1, node8, weight=13)
    G.add_edge(node1, node9, weight=3)
    G.add_edge(node1, node10, weight=10)
    # G.add_edge(node2, node4, weight=6)
    # G.add_edge(node8, node7, weight=2)
    # G.add_edge(node4, node5, weight=20)

    # 図の大きさ: (横幅*100px, 高さ*100px)
    plt.figure(figsize=(12, 6))

    # ノード間の調整
    pos = nx.spring_layout(G, k=0.5)

    # ラベルの設定
    nx.draw_networkx_labels(G, pos, fontsize=12,
                            font_family="Yu Gothic", font_weight="bold")

    # ノードサイズの設定
    node_size = []
    for name, count in G.nodes(data=True):
        node_size.append(count["count"] * 50)

    nx.draw_networkx_nodes(G, pos, node_color="b", node_shape="o",
                           alpha=1.0, node_size=node_size)

    # エッジの太さの設定
    edge_width = []
    for node1, node2, weight in G.edges(data=True):
        edge_width.append(weight["weight"] * 1)
    # width: エッジの太さ
    # edge_color: エッジの色
    # style: エッジのスタイル、点線等
    # alpha: 透明度
    # arrow:
    # arrowstyle: 矢印のスタイル
    nx.draw_networkx_edges(G, pos, width=edge_width,
                           edge_color="c", style="solid",
                           allows=False, arrowstyle="-|>", arrowsize=1,
                           alpha=0.5)

    # グラフの描画
    plt.axis("off")
    plt.show()
    pass
