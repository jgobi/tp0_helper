import networkx as nx
import argparse
import random

args = argparse.ArgumentParser()

args.add_argument('-n', help='Number of nodes in the graph', type=int, default=1000)
# args.add_argument('-b', help='Average branching factor', type=float, default=5)
args.add_argument('--output', '-o', help='output file names', default='graph')


def step_path(graph, node):
    number = 1
    queue = set()
    graph.node[node]['age'] = random.randrange(0, 35)
    for neighbor in graph.neighbors(node):
        queue.add(neighbor)
    while len(queue) > 0:
        node = queue.pop()
        age = random.randrange(0,100)
        graph.node[node]['age'] = age
        if age >= 35:
            continue
        number += 1
        for neighbor in graph.neighbors(node):
            if 'age' in graph.node[neighbor]:
                continue
            queue.add(neighbor)

    return number

def set_ages_path(graph, start_node):
    return step_path(graph, start_node)

def set_ages_non_path(graph):
    for node in graph.nodes():
        if 'age' not in graph.node[node].keys():
            graph.node[node]['age'] = random.randrange(0, 100)


def gen_graph(v):
    p = random.random()
    graph = nx.erdos_renyi_graph(v, p)
    start_node = random.choice(graph.nodes())
    number = set_ages_path(graph, start_node)
    set_ages_non_path(graph)
    return graph, start_node, number

def write_to_file(graph, start, number, filename):
    # for i in graph.nodes():
    #     print(i, graph.node[i]['age'])
    # for i in graph.edges():
    #     print(i)
    print(start)
    print(number)

if __name__=='__main__':
    args = args.parse_args()
    graph, start, number = gen_graph(args.n)
    write_to_file(graph, start, number, args.output)
