# graphs
A simple tool for figuring out the graph connection type/network topology.

## Usage
This module can be run as a separate program via command-line.

For most precise results it requires three carefully crafted arguments: number of nodes graph has, number of edges and a list of paired (connected) nodes. The first node in this list is connected to the second, the third to forth, and so on.

```bash
python -m graphs_type 3 3 1 2 2 1 2 3 3 2 3 1 1 3
Тип вашей сети, исходя из графа: полносвязный.

python -m graphs_type 5 4 1 2 1 3 1 4 1 5 2 1 3 1 4 1 5 1
Тип вашей сети, исходя из графа: звезда.
```

However, the program is fine with not receiving the last argument. Then, it will only check if the graph is full connected.

You also can import the module's functions for your own use.

```python
from graphs import graphs_type

# returns True
graphs_type.is_full_connected(3, 3)

# returns False
graphs_type.is_full_connected(4, 4)

# returns 1
graphs_type.connection_type(5, 5, [(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3), (4, 5), (5, 4), (5, 1), (1, 5)])

# returns 4
graphs_type.connection_type(3, 2, [(1, 2), (2, 1), (2, 3), (3, 2)])
```

## API

The is_full_connected function returns True if the graph is full connected, otherwise False.
The connection_type function output is an integer stored in a dict with full string descriptions of supported types as values. Adjust the function algorithm and extend the dict with your new return value to add your own type. Currently supported types are as follows: full connected, bus (1), ring (2), and star (3). See the picture below.

![Supported types](https://user-images.githubusercontent.com/89975155/147064513-08c33e88-6da7-4e0e-9252-8d4a81ae9cf3.png)


For more details and highlighted source code visit [documentation](https://frootin.github.io/graphs/).

## Background

The module requires Python 3.x and [click](https://click.palletsprojects.com/en/8.0.x/) package installed.

## License

Distributed under [MIT](https://github.com/frootin/graphs-site/blob/main/LICENSE.txt) license.

