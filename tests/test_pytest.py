import pytest
from graphs_type import is_full_connected, connection_type, main


@pytest.mark.parametrize("test_input, expected", [((0, 1), False), ((4, 6), True), ((4, 3), False)],
                         ids=["strange_input", "full", "not_full"])
def test_is_full(test_input, expected):
    res = is_full_connected(*test_input)
    assert (res and expected) or (not (res or expected))


types_data = [(3, 2, [(1, 2), (2, 1), (2, 3), (3, 2)], 4), 
    (5, 5, [(1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1), (2, 3), (3, 2)], 4),
    (5, 5, [(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3), (4, 5), (5, 4), (5, 1), (1, 5)], 1), 
    (5, 4,[(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3), (4, 5), (5, 4)], 2), 
    (5, 4, [(1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1)], 3)]

@pytest.fixture(params=types_data)
def types(request):
    return request.param


def test_uncertain(types):
    nodes_num, edges_num, edges, res = types
    assert connection_type(nodes_num, edges_num, edges) == res, f"Should be {res}"


main_data = [(["5", "4"], "неполносвязный, точный тип установить не удалось"),  
    (["5", "4", "1", "2", "2", "1", "1", "3", "3", "1", "1", "4", "4", "1", "1", "5", "5", "1"], "звезда"), 
    (["3", "3", "1", "2", "2", "1", "1", "3", "3", "1", "2", "3", "3", "2"], "полносвязный")]

@pytest.fixture(params=main_data)
def cli(request):
    return request.param


def test_main(capsys, cli):
    test_input, expected = cli
    with pytest.raises(SystemExit) as e:
        main(test_input)
    assert e.type == SystemExit
    assert e.value.code == 0
    captured = capsys.readouterr()
    res = f"Тип вашей сети, исходя из графа: {expected}.\n"
    assert captured.out == res
