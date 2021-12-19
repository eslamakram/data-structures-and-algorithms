from graph import __version__
from graph.graph import *
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_graph_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_graph_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected

def test_graph_size():
    graph = Graph()
    graph.add_node('hello')
    expected = 1
    actual = graph.size()
    assert actual == expected

def test_graph_add_edge_interloper_start():
    graph = Graph()
    start = Vertex('start')
    end = graph.add_node('end')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_graph_add_edge_interloper_end():
    graph = Graph()
    end = Vertex('end')
    start = graph.add_node('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_graph_get_nodes():
    graph = Graph()
    wateen = graph.add_node('wateen')
    tolay = graph.add_node('Tolay')
    khairAllah = Vertex('khairAllah')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected

def test_graph_get_neighbors():
    graph = Graph()
    wateen = graph.add_node('wateen')
    tolay = graph.add_node('Tolay')
    graph.add_edge(wateen, tolay, 44)
    neighbors = graph.get_neighbors(wateen)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[0]
    assert neighbor_edge.vertex.value == 'Tolay'
    assert neighbor_edge.weight == 44

def test_graph_breadth_first():
    # Pandora, Arendelle, Metroville, Monstroplolis, Narnia, Naboo
    graph = Graph()
    # start_vertix = Vertex('Pandora')
    # vertix2 = Vertex('Arendelle')
    # vertix3 = Vertex('Metroville')
    # vertix4 = Vertex('Monstroplolis')
    # vertix5 = Vertex('Narnia')
    # vertix6 = Vertex('Naboo')

    start_vertix = graph.add_node('Pandora')
    vertix2 = graph.add_node('Arendelle')
    vertix3 = graph.add_node('Metroville')
    vertix4 = graph.add_node('Monstroplolis')
    vertix5 = graph.add_node('Narnia')
    vertix6 = graph.add_node('Naboo')

    graph.add_edge(start_vertix, vertix2)
    graph.add_edge(vertix2, vertix3)
    graph.add_edge(vertix2, vertix4)
    graph.add_edge(vertix3, vertix5)
    graph.add_edge(vertix3, vertix6)

    actual = graph.bfs(start_vertix)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstroplolis", "Narnia", "Naboo"]
    assert actual == expected
