from patterns.manipulate import Manipulated

Translated = lambda inner, translation: Manipulated(inner, lambda pos: pos.translate(translation))