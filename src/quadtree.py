from __future__ import annotations
import json
from typing import List
import tkinter

"""Module définissant la classe QuadTree."""
class QuadTree:
    """
    Représente un arbre quadtree 
    """
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree,
                       bd: bool | QuadTree, bg: bool | QuadTree):
        """
        Initialise LE noeud QuadTree.
        """
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """
        Profondeur de récursion de l'arbre quadtree.
        """
        depths = [0]
        def calculate_depth(node: bool | QuadTree, current_depth: int) -> None:
            """
            Fonction récursive pour calculer la profondeur de l'arbre quadtree à 4 de profondeurs.
            """
            if isinstance(node, QuadTree):
                depths.append(current_depth)
                calculate_depth(node.hg, current_depth + 1)
                calculate_depth(node.hd, current_depth + 1)
                calculate_depth(node.bd, current_depth + 1)
                calculate_depth(node.bg, current_depth + 1)

        calculate_depth(self, 1)
        return max(depths)

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """
        Charge un fichier texte contenant une représentation
        d'arbre quadtree et renvoie un objet .
        """
        with open(filename, 'r', encoding='utf-8' ) as file:
            data = json.load(file)
        return QuadTree.from_list(data)

    @staticmethod
    def from_list(data: List) -> QuadTree:
        """
        Génère un arbre quadtree à partir d'une représentation de liste
        """
        if isinstance(data, list) and len(data) == QuadTree.NB_NODES:
            return QuadTree(
                QuadTree.from_list(data[0]),
                QuadTree.from_list(data[1]),
                QuadTree.from_list(data[2]),
                QuadTree.from_list(data[3])
            )
        return bool(data)

    def paint(self, level: int = 0) -> str:
        """
        Représentation dans la console de l'arbre QuadTree 
        avec un saut de ligne ajouter à chaque changement de niveau.        
        """
        result = " " * level
        if level > 0:
            result = "\n"  # Ajout d'un saut de ligne à chaque changement de niveau
        if isinstance(self, QuadTree):
            result += self.hg.paint(level + 1) if isinstance(self.hg, QuadTree) else f"{int(self.hg)}"
            result += self.hd.paint(level + 1) if isinstance(self.hd, QuadTree) else f"{int(self.hd)}"
            result += self.bd.paint(level + 1) if isinstance(self.bd, QuadTree) else f"{int(self.bd)}"
            result += self.bg.paint(level + 1) if isinstance(self.bg, QuadTree) else f"{int(self.bg)}"
        else:
            result += f"{int(self)}"
        return result

class tk_quad_tree(QuadTree):
    def __init__(self, root, x, y, size, quadtree_node):
        """
        Initialise un objet TkQuadTree.
        """
        super().__init__(quadtree_node.hg, quadtree_node.hd, quadtree_node.bd, quadtree_node.bg)
        self.root = root
        self.x = x
        self.y = y
        self.size = size

    def paint(self):
        """
        Affiche l'arbre QuadTree dans cette fenêtre Tkinter.
        """
        self.root.title("Résulat de l'arbre quaternaire !")
        canvas = tkinter.Canvas(self.root, width=600, height=600)
        canvas.pack()
        self.draw_square(canvas, self, 300, 300, 200)

    def draw_square(self, canvas, node, x, y, size):
        """
        Dessine l'arbre QuadTree sur la fenetre Tkinter 
        avec des jolies couleurs vertes et rouges.
        """
        if isinstance(node, QuadTree):
            canvas.create_rectangle(x - size, y - size, x + size, y + size, outline="black", width=2, fill="red")
            self.draw_square(canvas, node.hg, x - size//2, y - size//2, size//2)
            self.draw_square(canvas, node.hd, x + size//2, y - size//2, size//2)
            self.draw_square(canvas, node.bd, x + size//2, y + size//2, size//2)
            self.draw_square(canvas, node.bg, x - size//2, y + size//2, size//2)
        else:
            if int(node) == 0:
                canvas.create_rectangle(x - size, y - size, x + size, y + size, outline="black", width=2, fill="green")
            else:
                canvas.create_rectangle(x - size, y - size, x + size, y + size, outline="black", width=2, fill="red")

if __name__ == "__main__":
    root = tkinter.Tk()
    FILE_NAME = "files/quadtree.txt"
    q = QuadTree.from_file(FILE_NAME)
    print(q.paint())
    tk_quadtree = tk_quad_tree(root, 300, 300, 200, q)
    tk_quadtree.paint()
    root.mainloop()
