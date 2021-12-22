"""
Python3 program for figuring out network topology
by Nathalia Bogdanova, KI21-17/1b.
"""


import click


def is_full_connected (v: int, r: int) -> bool:
    """
    This function checks if graph is full connected.

    :param v: number of nodes graph has
    :param r: number of edges graph has
    :return: True if all nodes are connected, otherwise False

    :example:

    >>> is_full_connected(0, 1)
    False
    >>> is_full_connected(4, 6)
    True
    >>> is_full_connected(4, 3)
    False
    """
    full = v*(v - 1) // 2
    if r == full:
        return True
    return False


def connection_type (v: int, r: int, links: list[tuple[int, int]]) -> int:
    """
    Function figures out the type of not full connected graphs (networks).

    :param v: number of nodes graph has
    :param r: number of edges graph has
    :param links: tuples containing two connected nodes each
    :return: number used as a key in the outer dict with connection types as values

    :example:

    >>> connection_type(3, 2, [(1, 2), (2, 1), (2, 3), (3, 2)])
    4
    >>> connection_type(5, 5, [(1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1), (2, 3),(3, 2)])
    4
    >>> connection_type(5, 5, [(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3), (4, 5), (5, 4), (5, 1), (1, 5)])
    1
    >>> connection_type(5, 4, [(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3), (4, 5), (5, 4)])
    2
    >>> connection_type(5, 4, [(1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1)])
    3
    """
    if v == 3:
        return 4

    connections = {}
    for link in links:
        if link[0] in connections:
            connections[link[0]] += 1
        else:
            connections[link[0]] = 1
    
    uni = set(connections.values())

    if len(uni) == 1 and v == r:
        return 1
    if uni == {1, 2} and v - r == 1:
        return 2
    if uni == {1, r}:
        return 3

    return 4


connection_types = {1: "кольцо",
                    2: "шина",
                    3: "звезда",
                    4: "неполносвязный, точный тип установить не удалось"}


@click.command()
@click.argument("v", type=int)
@click.argument("r", type=int)
@click.argument("nodes", nargs=-1)
def main(v: int, r: int, nodes: list[str]) -> None:
    """Function to provide command-line interface.
    
    :param v: number of nodes graph has
    :param r: number of edges graph has
    :param nodes: list of paired nodes (every two nodes are a pair)
    :return: None

    :example:

    >>> main(["5", "4", "1", "2", "2", "1", "1", "3", "3", "1", "1", "4", "4", "1", "1", "5", "5", "1"])
    Тип вашей сети, исходя из графа: звезда.
    >>> main(["5"])                                                                                     
    Usage:  [OPTIONS] V R [NODES]...
    Try ' --help' for help.
    ...
    Error: Missing argument 'R'.
    >>> main(["5", "4"])
    Тип вашей сети, исходя из графа: неполносвязный, точный тип установить не удалось.
    """
    if is_full_connected(v, r):
        res = "полносвязный"
    else:
        links = []
        for i in range(0, len(nodes) - 1, 2):
            link = (nodes[i], nodes[i + 1])
            links.append(link)
        t = connection_type(v, r, links)
        res = connection_types[t]
    click.echo(f"Тип вашей сети, исходя из графа: {res}.")


if __name__ == "__main__":    #pragma: no cover
    main()
