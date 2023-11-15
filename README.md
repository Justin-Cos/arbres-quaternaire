# Exercices ludiques en python

Vous trouverez ici un ensemble d'exercices permettant de pratiquer python mais également découvrir quelques pans annexes de l'informatique en général.
Ces exercices sont issus d'un livre réalisé par Pascal Lafourcade et Malika More.

## Exercice : Arbre quaternaire
Un quadtree ou arbre quaternaire (arbre Q) est une structure de données de type arbre dans laquelle chaque nœud a quatre fils. Les quadtrees sont le plus souvent utilisés pour partitionner un espace bidimensionnel en le subdivisant récursivement en quatre nœuds. 
![img.png](files/quadtree.png)

Il existe plusieurs types de quadtree. Dans notre cas il s'agit d'un quadtree "region".
Le quadtree «région» représente une partition de l'espace en deux dimensions en décomposant la région en quatre quadrants égaux, puis chaque quadrant en quatre sous-quadrants, et ainsi de suite, avec chaque «nœud terminal» comprenant des données correspondant à une sous-région spécifique. Chaque nœud de l'arbre a exactement : soit quatre enfants, soit aucun (cas d'un nœud terminal).
Chaque `Noeud` comportant quatre éléments. Il s'agit d'une technique connue pour l'encodage d'images.  Pour simplifier, les images sont carrées, de couleur noir et blanc 
et de côté 2^n.

Un noeud à quatre fils est représenté : 
```python
from __future__ import annotations

class QuadTree:
    def __init(hg: bool|QuadTree, hd: bool|QuadTree, bg: bool|QuadTree, bd: bool|QuadTree):
        pass
    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1
    @staticmethod
    def fromFile(filename):
        # Your code here
        pass
    @staticmethod
    def fromList(data):
        pass 
    
    def paint(self):
        """ Textual representation of the QuadTree"""

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
```

Assurez-vous que la lecture du fichier se passe sans encombre, en lançant les tests unitaires :
```shell
python -m pytest tests/test_quadtree.py -x
```

A partir du fichier `files/quadtree.txt`, générez le QuadTree associé. 
Puis, réalisez une interface graphique en utilisant la classe `TkQuadTree`, permettant de la représenter. 

Bonus : 
Remplacez les valeurs binaires des feuilles par des valeurs numériques, combinez celà à un [tileset](https://docs.godotengine.org/en/stable/_images/using_tilesets_kenney_abstract_platformer_tile_sheet.webp). 
Et voilà, vous avez généré votre tilemap par le biais d'un quadtree.