import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src import QuadTree, TkQuadTree

def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.from_file(filename)
    assert q.depth == 4

def test_single():
    filename = "files/quadtree_easy.txt"
    q = QuadTree.from_file(filename)
    assert q.depth == 1

#TODO : ajouter d'autres tests
