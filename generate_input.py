import networkx as nx
import argparse
import random

args = argparse.ArgumentParser()

args.add_argument('-n', help='Number of nodes in the graph', type=int, default=1000)
args.add_argument('--no-output', '-o', help='Wheter it bothers to generate the correct output too', type=bool, default=False)
# args.add_argument('-b', help='Average branching factor', type=float, default=5)
args.add_argument('--output', help='output file names', default='graph')


def step_path(graph, node):
    number = 1
    queue = set()
    graph.node[node]['age'] = random.randrange(1,35)
    for neighbor in graph.neighbors(node):
        queue.add(neighbor)
    while len(queue) > 0:
        node = queue.pop()
        age = random.randrange(1,100)
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
    p = 0.5
    graph = nx.erdos_renyi_graph(v, p)
    start_node = random.randrange(v)
    number = set_ages_path(graph, start_node)
    set_ages_non_path(graph)
    return graph, start_node, number

def write_to_file(graph, start, number, filename):
    # for i in graph.nodes():
    #     print(i, graph.node[i]['age'])
    # for i in graph.edges():
    #     print(i)
    with open(filename + '.in', "w+") as f:
        f.write("{}\n".format(len(graph.nodes())))
        f.write("{}\n".format(len(graph.edges())))
        for node in graph.nodes():
            f.write("{} {}\n".format(node+1, graph.node[node]['age']))
        for i, j in graph.edges:
            f.write("{} {}\n".format(i+1, j+1))
        f.write("{}\n".format(start+1))
    with open(filename + '.out', "w+") as f:
        f.write("{}\n".format(number))


def write_to_file_no_output(n, filename):
    print('writeing to file')
    # for i in graph.nodes():
    #     print(i, graph.node[i]['age'])
    # for i in graph.edges():
    #     print(i)
    # f.write("{}\n".format(len(graph.nodes())))
    # f.write("{}\n".format(len(graph.edges())))
    edge_count = 0
    print('first write')
    with open(filename + '.in', "w+") as f:
        for node in range(1, n+1):
            f.write("{} {}\n".format(node, str(random.randrange(1,100))))
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if random.random() < 1/2:
                    edge_count += 1
                    f.write("{} {}\n".format(i, j))

        f.write("{}\n".format(random.randrange(1,n+1)))
    print('rewrite')
    with open(filename + '.in', "r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write("{}\n{}\n".format(n,edge_count) + content)


if __name__=='__main__':
    args = args.parse_args()
    if not args.no_output:
        graph, start, number = gen_graph(args.n)
        write_to_file(graph, start, number, args.output)
    else:
        print('generating graph')
        # graph = nx.erdos_renyi_graph(args.n, 0.5)
        write_to_file_no_output(args.n,args.output)
