#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interface interactive pour le calculateur d'algèbre LaTeX
Menu intuitif pour manipuler des expressions algébriques
"""

from algebre_latex import AlgebreTerm
import sys

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "█"*70)
    print("█" + " CALCULATEUR D'ALGÈBRE AVEC AFFICHAGE LaTeX ".center(68) + "█")
    print("█"*70)
    print("""
    📝 OPÉRATIONS DISPONIBLES:
    
    1️⃣  Développer une expression
    2️⃣  Factoriser une expression
    3️⃣  Simplifier une expression
    4️⃣  Dériver une expression
    5️⃣  Intégrer une expression
    6️⃣  Résoudre une équation (f(x) = 0)
    7️⃣  Substituer une variable
    8️⃣  Afficher en LaTeX pur (copier-coller)
    0️⃣  Quitter
    
""")
    print("█"*70 + "\n")

def input_expression():
    """Demande une expression à l'utilisateur"""
    print("\n📌 Exemples d'expressions valides:")
    print("   • x**2 + 3*x + 2")
    print("   • (a + b)*(a - b)")
    print("   • x**3 - 2*x**2 + 5*x - 1")
    print("   • sin(x) + cos(x)")
    
    expr_str = input("\n✏️  Saisissez votre expression: ").strip()
    
    if not expr_str:
        print("❌ Expression vide!")
        return None
    
    try:
        return AlgebreTerm(expr_str)
    except Exception as e:
        print(f"❌ Erreur d'analyse: {e}")
        return None

def operation_developper():
    """Développe une expression"""
    expr = input_expression()
    if expr:
        expr.developper()

def operation_factoriser():
    """Factorise une expression"""
    expr = input_expression()
    if expr:
        expr.factoriser()

def operation_simplifier():
    """Simplifie une expression"""
    expr = input_expression()
    if expr:
        expr.simplifier()

def operation_deriver():
    """Dérive une expression"""
    expr = input_expression()
    if expr:
        variable = input("\n📌 Variable de dérivation (ex: x): ").strip()
        if variable:
            try:
                expr.deriver(variable)
            except Exception as e:
                print(f"❌ Erreur: {e}")

def operation_integrer():
    """Intègre une expression"""
    expr = input_expression()
    if expr:
        variable = input("\n📌 Variable d'intégration (ex: x): ").strip()
        if variable:
            try:
                expr.integrer(variable)
            except Exception as e:
                print(f"❌ Erreur: {e}")

def operation_resoudre():
    """Résout une équation"""
    expr = input_expression()
    if expr:
        variable = input("\n📌 Variable à résoudre (ex: x): ").strip()
        if variable:
            try:
                expr.resoudre(variable)
            except Exception as e:
                print(f"❌ Erreur: {e}")

def operation_substituer():
    """Substitue une variable"""
    expr = input_expression()
    if expr:
        variable = input("\n📌 Variable à substituer (ex: x): ").strip()
        if variable:
            valeur = input(f"📌 Valeur de {variable}: ").strip()
            if valeur:
                try:
                    expr.substituer(variable, valeur)
                except Exception as e:
                    print(f"❌ Erreur: {e}")

def operation_latex_pur():
    """Affiche le code LaTeX brut"""
    expr = input_expression()
    if expr:
        latex_code = expr.afficher_latex_pur()
        print("\n" + "─"*70)
        print("📋 CODE LaTeX (copier-coller):")
        print("─"*70)
        print(f"\nInline:  ${latex_code}$")
        print(f"Display: \\[{latex_code}\\]")
        print(f"\nCode brut:\n{latex_code}\n")

def main():
    """Boucle principale du programme"""
    operations = {
        '1': ("Développer", operation_developper),
        '2': ("Factoriser", operation_factoriser),
        '3': ("Simplifier", operation_simplifier),
        '4': ("Dériver", operation_deriver),
        '5': ("Intégrer", operation_integrer),
        '6': ("Résoudre", operation_resoudre),
        '7': ("Substituer", operation_substituer),
        '8': ("LaTeX pur", operation_latex_pur),
    }
    
    while True:
        afficher_menu()
        choix = input("👉 Choisissez une opération (0-8): ").strip()
        
        if choix == '0':
            print("\n👋 Au revoir!\n")
            break
        
        if choix in operations:
            nom_operation, fonction = operations[choix]
            print(f"\n{'='*70}")
            print(f"   {nom_operation.upper()}")
            print(f"{'='*70}")
            fonction()
        else:
            print("❌ Choix invalide! Veuillez entrer 0-8.")
        
        input("\n\n⏎ Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programme interrompu par l'utilisateur.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erreur fatale: {e}\n")
        sys.exit(1)
