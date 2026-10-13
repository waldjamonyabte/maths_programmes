#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
🧮 CALCULATEUR D'ALGÈBRE COMPLET
Menu avancé pour développement, factorisation et manipulation de variables
"""

from sympy import symbols, expand, factor, simplify, latex, pretty, Symbol, Poly
from sympy import solve, diff, integrate, limit, oo, apart, expand_trig, trigsimp
from sympy import sqrt, sin, cos, tan, log, exp, pi, I, Matrix, gcd, lcm, roots
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import sys

class CalculatriceAlgebre:
    """Calculatrice d'algèbre complète avec menu avancé"""
    
    def __init__(self):
        self.expr_actuelle = None
        self.historique = []
        self.transformations = standard_transformations + (implicit_multiplication_application,)
    
    def afficher_titre(self, texte):
        """Affiche un titre formaté"""
        print("\n" + "█"*80)
        print("█" + texte.center(78) + "█")
        print("█"*80 + "\n")
    
    def afficher_sous_titre(self, texte):
        """Affiche un sous-titre"""
        print("\n" + "─"*80)
        print(f"  {texte}")
        print("─"*80 + "\n")
    
    def afficher_resultat(self, titre, resultat):
        """Affiche un résultat formaté"""
        self.afficher_sous_titre(titre)
        print(f"Forme lisible:\n{pretty(resultat)}\n")
        print(f"LaTeX inline:  ${latex(resultat)}$")
        print(f"LaTeX display: \\[{latex(resultat)}\\]\n")
    
    def menu_principal(self):
        """Affiche le menu principal"""
        self.afficher_titre("🧮 CALCULATEUR D'ALGÈBRE COMPLET")
        print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                         MENU PRINCIPAL                                   ║
╚══════════════════════════════════════════════════════════════════════════╝

   ┌─────────────────────────────────────────────────────────────────────┐
   │ 1️⃣  SAISIR UNE NOUVELLE EXPRESSION                                  │
   └─────────────────────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 📊 OPÉRATIONS BASIQUES                                               │
   ├─────────────────────────────────────────────────────────────────────┤
   │  2️⃣  Développer (expand)         │ 3️⃣  Factoriser (factor)         │
   │  4️⃣  Simplifier                  │ 5️⃣  Réduire aux même dénominateur│
   └─────────────────────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 🔍 CALCUL ET ANALYSE                                                │
   ├─────────────────────────────────────────────────────────────────────┤
   │  6️⃣  Dériver (f'(x))             │ 7️⃣  Intégrer ∫f(x)dx            │
   │  8️⃣  Résoudre équation          │ 9️⃣  Calculer limite             │
   └─────────────────────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 🔧 MANIPULATIONS AVANCÉES                                            │
   ├─────────────────────────────────────────────────────────────────────┤
   │ 🔟 Substituer variable           │ 1️⃣1️⃣ Décomposer en éléments simples│
   │ 1️⃣2️⃣ Racines et zéros           │ 1️⃣3️⃣ PGCD/PPCM                   │
   │ 1️⃣4️⃣ Trigonométrie              │ 1️⃣5️⃣ Matrice/déterminant        │
   └─────────────────────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────────────────────┐
   │ 📋 AFFICHAGE ET HISTORIQUE                                           │
   ├─────────────────────────────────────────────────────────────────────┤
   │ 1️⃣6️⃣ Afficher l'expression actuelle  │ 1️⃣7️⃣ Afficher en LaTeX pur    │
   │ 1️⃣8️⃣ Historique des opérations      │ 0️⃣  QUITTER                  │
   └─────────────────────────────────────────────────────────────────────┘

""")
    
    def saisir_expression(self):
        """Saisit une nouvelle expression"""
        self.afficher_sous_titre("📝 SAISIR UNE NOUVELLE EXPRESSION")
        print("💡 Exemples valides:")
        print("   • x**2 + 3*x + 2")
        print("   • (a + b)*(a - b)")
        print("   • sin(x)**2 + cos(x)**2")
        print("   • x**3 - 2*x**2 + 5*x - 1")
        print("   • (x**2 - 1)/(x - 1)")
        
        expr_str = input("\n✏️  Saisissez l'expression: ").strip()
        
        if not expr_str:
            print("❌ Expression vide!")
            return False
        
        try:
            self.expr_actuelle = parse_expr(expr_str, transformations=self.transformations)
            self.historique.append(("Nouvelle", self.expr_actuelle))
            self.afficher_resultat("✅ Expression acceptée", self.expr_actuelle)
            return True
        except Exception as e:
            print(f"❌ Erreur d'analyse: {e}")
            return False
    
    def verifier_expression(self):
        """Vérifie qu'une expression est définie"""
        if self.expr_actuelle is None:
            print("⚠️  Aucune expression définie! Saisissez d'abord une expression.")
            return False
        return True
    
    def developper(self):
        """Développe l'expression"""
        if not self.verifier_expression():
            return
        
        resultat = expand(self.expr_actuelle)
        self.historique.append(("Développement", resultat))
        self.afficher_resultat("✨ DÉVELOPPEMENT", resultat)
        self.expr_actuelle = resultat
    
    def factoriser(self):
        """Factorise l'expression"""
        if not self.verifier_expression():
            return
        
        resultat = factor(self.expr_actuelle)
        self.historique.append(("Factorisation", resultat))
        self.afficher_resultat("🎯 FACTORISATION", resultat)
        self.expr_actuelle = resultat
    
    def simplifier(self):
        """Simplifie l'expression"""
        if not self.verifier_expression():
            return
        
        resultat = simplify(self.expr_actuelle)
        self.historique.append(("Simplification", resultat))
        self.afficher_resultat("🧹 SIMPLIFICATION", resultat)
        self.expr_actuelle = resultat
    
    def reduire_denominateur(self):
        """Réduit aux même dénominateur"""
        if not self.verifier_expression():
            return
        
        resultat = apart(self.expr_actuelle)
        self.historique.append(("Réduction dénominateur", resultat))
        self.afficher_resultat("🔄 RÉDUCTION AUX MÊME DÉNOMINATEUR", resultat)
        self.expr_actuelle = resultat
    
    def deriver(self):
        """Dérive l'expression"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable de dérivation (ex: x): ").strip()
        if not variable:
            return
        
        try:
            var = Symbol(variable)
            resultat = diff(self.expr_actuelle, var)
            self.historique.append((f"Dérivée ({variable})", resultat))
            self.afficher_resultat(f"📈 DÉRIVÉE par rapport à {variable}", resultat)
            self.expr_actuelle = resultat
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def integrer(self):
        """Intègre l'expression"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable d'intégration (ex: x): ").strip()
        if not variable:
            return
        
        try:
            var = Symbol(variable)
            resultat = integrate(self.expr_actuelle, var)
            self.historique.append((f"Intégrale ({variable})", resultat))
            
            self.afficher_sous_titre(f"∫ INTÉGRALE par rapport à {variable}")
            print(f"Intégrande:\n{pretty(self.expr_actuelle)}\n")
            print(f"Résultat:\n{pretty(resultat)}\n")
            print(f"LaTeX: $\\int ({latex(self.expr_actuelle)}) d{variable} = {latex(resultat)} + C$\n")
            
            self.expr_actuelle = resultat
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def resoudre(self):
        """Résout l'équation"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable à résoudre (ex: x): ").strip()
        if not variable:
            return
        
        try:
            var = Symbol(variable)
            solutions = solve(self.expr_actuelle, var)
            
            self.afficher_sous_titre(f"🔍 RÉSOLUTION DE: {pretty(self.expr_actuelle)} = 0")
            
            if not solutions:
                print("❌ Aucune solution trouvée")
            else:
                print(f"✅ {len(solutions)} solution(s) trouvée(s):\n")
                for i, sol in enumerate(solutions, 1):
                    print(f"   {variable}_{i} = {pretty(sol)}")
                    print(f"           LaTeX: ${latex(sol)}$\n")
            
            if solutions:
                self.historique.append((f"Résolution ({variable})", solutions))
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def calculer_limite(self):
        """Calcule une limite"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable (ex: x): ").strip()
        point = input("📌 Point vers lequel tendre (ex: 0, oo, -oo): ").strip()
        
        if not variable or not point:
            return
        
        try:
            var = Symbol(variable)
            # Convertir "oo" en symbole d'infini
            if point.lower() in ['oo', '+oo', 'infinity']:
                pt = oo
            elif point.lower() in ['-oo', '-infinity']:
                pt = -oo
            else:
                pt = parse_expr(point, transformations=self.transformations)
            
            resultat = limit(self.expr_actuelle, var, pt)
            self.historique.append((f"Limite ({variable}→{point})", resultat))
            
            self.afficher_sous_titre(f"📊 LIMITE quand {variable} → {point}")
            print(f"Expression: {pretty(self.expr_actuelle)}\n")
            print(f"Limite: {pretty(resultat)}")
            print(f"LaTeX: $\\lim_{{{variable} \\to {point}}} ({latex(self.expr_actuelle)}) = {latex(resultat)}$\n")
            
            self.expr_actuelle = resultat
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def substituer(self):
        """Substitue une variable"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable à substituer (ex: x): ").strip()
        valeur = input(f"📌 Valeur de {variable} (ex: 2, pi, i): ").strip()
        
        if not variable or not valeur:
            return
        
        try:
            var = Symbol(variable)
            val = parse_expr(valeur, transformations=self.transformations)
            resultat = self.expr_actuelle.subs(var, val)
            self.historique.append((f"Substitution ({variable}={valeur})", resultat))
            
            self.afficher_resultat(f"🔄 SUBSTITUTION ({variable} = {valeur})", resultat)
            self.expr_actuelle = resultat
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def decomposer_elements_simples(self):
        """Décompose en éléments simples"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable (ex: x): ").strip()
        if not variable:
            return
        
        try:
            var = Symbol(variable)
            resultat = apart(self.expr_actuelle, var)
            self.historique.append(("Décomposition éléments simples", resultat))
            self.afficher_resultat("🔀 DÉCOMPOSITION EN ÉLÉMENTS SIMPLES", resultat)
            self.expr_actuelle = resultat
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def calculer_racines(self):
        """Calcule les racines/zéros"""
        if not self.verifier_expression():
            return
        
        variable = input("\n📌 Variable (ex: x): ").strip()
        if not variable:
            return
        
        try:
            var = Symbol(variable)
            racines = roots(self.expr_actuelle, var)
            
            self.afficher_sous_titre(f"🌳 RACINES/ZÉROS de {pretty(self.expr_actuelle)}")
            
            if not racines:
                print("❌ Aucune racine trouvée")
            else:
                print(f"✅ Racines avec multiplicités:\n")
                for racine, multiplicite in racines.items():
                    print(f"   {variable} = {pretty(racine)} (multiplicité: {multiplicite})")
                    print(f"           LaTeX: ${latex(racine)}$\n")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def calculer_pgcd_ppcm(self):
        """Calcule le PGCD/PPCM"""
        print("\n📌 Entrez deux expressions (ou polynômes)\n")
        
        expr1_str = input("1ère expression: ").strip()
        expr2_str = input("2ème expression: ").strip()
        
        if not expr1_str or not expr2_str:
            return
        
        try:
            expr1 = parse_expr(expr1_str, transformations=self.transformations)
            expr2 = parse_expr(expr2_str, transformations=self.transformations)
            
            pgcd_result = gcd(expr1, expr2)
            ppcm_result = lcm(expr1, expr2)
            
            self.afficher_sous_titre("🔢 PGCD / PPCM")
            print(f"Expression 1: {pretty(expr1)}")
            print(f"Expression 2: {pretty(expr2)}\n")
            
            print(f"PGCD: {pretty(pgcd_result)}")
            print(f"      LaTeX: ${latex(pgcd_result)}$\n")
            
            print(f"PPCM: {pretty(ppcm_result)}")
            print(f"      LaTeX: ${latex(ppcm_result)}$\n")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def operations_trigonometriques(self):
        """Opérations trigonométriques"""
        if not self.verifier_expression():
            return
        
        print("\n📌 Opérations trigonométriques:")
        print("1. Développer trigonométrique (expand_trig)")
        print("2. Simplifier trigonométrique (trigsimp)")
        
        choix = input("\nChoisissez: ").strip()
        
        try:
            if choix == '1':
                resultat = expand_trig(self.expr_actuelle)
                titre = "🔄 DÉVELOPPEMENT TRIGONOMÉTRIQUE"
                self.historique.append(("Trig expand", resultat))
            elif choix == '2':
                resultat = trigsimp(self.expr_actuelle)
                titre = "🧹 SIMPLIFICATION TRIGONOMÉTRIQUE"
                self.historique.append(("Trig simp", resultat))
            else:
                print("❌ Choix invalide")
                return
            
            self.afficher_resultat(titre, resultat)
            self.expr_actuelle = resultat
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def operations_matrice(self):
        """Opérations sur matrices"""
        print("\n⚠️  Fonctionnalité en développement pour les matrices")
        print("Exemple: Matrix([[1, 2], [3, 4]])")
    
    def afficher_expression_actuelle(self):
        """Affiche l'expression actuelle"""
        if self.expr_actuelle is None:
            print("⚠️  Aucune expression définie")
            return
        
        self.afficher_resultat("📊 EXPRESSION ACTUELLE", self.expr_actuelle)
    
    def afficher_latex_pur(self):
        """Affiche le code LaTeX pur"""
        if self.expr_actuelle is None:
            print("⚠️  Aucune expression définie")
            return
        
        self.afficher_sous_titre("📋 CODE LaTeX PUR (COPIER-COLLER)")
        code_latex = latex(self.expr_actuelle)
        print(f"Inline:   ${code_latex}$")
        print(f"Display:  \\[{code_latex}\\]")
        print(f"\nCode brut:\n{code_latex}\n")
    
    def afficher_historique(self):
        """Affiche l'historique des opérations"""
        if not self.historique:
            print("⚠️  Aucune opération dans l'historique")
            return
        
        self.afficher_sous_titre("📜 HISTORIQUE DES OPÉRATIONS")
        
        for i, (operation, resultat) in enumerate(self.historique, 1):
            print(f"{i}. {operation}")
            if isinstance(resultat, list):
                for sol in resultat:
                    print(f"   → {pretty(sol)}")
            else:
                print(f"   → {pretty(resultat)}")
            print()
    
    def demarrer(self):
        """Démarre la calculatrice interactive"""
        while True:
            self.menu_principal()
            choix = input("👉 Entrez votre choix (0-18): ").strip()
            
            operations = {
                '1': self.saisir_expression,
                '2': self.developper,
                '3': self.factoriser,
                '4': self.simplifier,
                '5': self.reduire_denominateur,
                '6': self.deriver,
                '7': self.integrer,
                '8': self.resoudre,
                '9': self.calculer_limite,
                '10': self.substituer,
                '11': self.decomposer_elements_simples,
                '12': self.calculer_racines,
                '13': self.calculer_pgcd_ppcm,
                '14': self.operations_trigonometriques,
                '15': self.operations_matrice,
                '16': self.afficher_expression_actuelle,
                '17': self.afficher_latex_pur,
                '18': self.afficher_historique,
                '0': None,
            }
            
            if choix in operations:
                if choix == '0':
                    print("\n👋 Merci d'avoir utilisé la Calculatrice d'Algèbre!")
                    print("🧮 À bientôt!\n")
                    break
                else:
                    try:
                        operations[choix]()
                    except Exception as e:
                        print(f"\n❌ Erreur: {e}")
            else:
                print("❌ Choix invalide! Veuillez entrer un numéro entre 0 et 18.")
            
            input("\n\n⏎ Appuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    try:
        calc = CalculatriceAlgebre()
        calc.demarrer()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programme interrompu.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erreur fatale: {e}\n")
        sys.exit(1)
