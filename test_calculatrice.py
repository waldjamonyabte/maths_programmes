#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test rapide de la calculatrice"""

from calculatrice_algebre_menu import CalculatriceAlgebre
from sympy import symbols, expand, factor

x = symbols('x')

print("\n✅ TEST: Calculatrice d'Algèbre chargée avec succès!\n")

calc = CalculatriceAlgebre()

# Test 1: Développement
print("\n" + "="*80)
print("TEST 1: DÉVELOPPEMENT")
print("="*80)
calc.expr_actuelle = (x + 2)*(x - 3)
calc.developper()

# Test 2: Factorisation
print("\n" + "="*80)
print("TEST 2: FACTORISATION")
print("="*80)
calc.expr_actuelle = x**2 + 5*x + 6
calc.factoriser()

# Test 3: Affichage LaTeX pur
print("\n" + "="*80)
print("TEST 3: AFFICHAGE LaTeX")
print("="*80)
calc.expr_actuelle = (x**2 + 1)/(x - 1)
calc.afficher_latex_pur()

print("\n✨ Les tests sont terminés! Lance le programme avec:")
print("   python calculatrice_algebre_menu.py")
print("\n")
