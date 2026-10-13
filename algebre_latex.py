"""
Module d'algèbre avec affichage LaTeX dans le terminal
Automatise développement, factorisation et manipulations algébriques
"""

from sympy import symbols, expand, factor, simplify, latex, pretty, Symbol, Poly
from sympy import solve, diff, integrate, limit, oo
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import re

class AlgebreTerm:
    """Classe pour manipuler et afficher des expressions algébriques"""
    
    def __init__(self, expr_str=None, expr_sympy=None):
        """
        Initialise une expression algébrique
        expr_str : chaîne de caractères (ex: "x**2 + 2*x + 1")
        expr_sympy : expression SymPy directe
        """
        if expr_sympy is not None:
            self.expr = expr_sympy
        elif expr_str is not None:
            # Parse avec support de multiplication implicite
            transformations = standard_transformations + (implicit_multiplication_application,)
            self.expr = parse_expr(expr_str, transformations=transformations)
        else:
            self.expr = None
    
    def afficher(self, titre="Expression"):
        """Affiche l'expression avec formatage LaTeX"""
        if self.expr is None:
            print("❌ Aucune expression définie")
            return
        
        print("\n" + "="*60)
        print(f"📐 {titre}")
        print("="*60)
        print(f"\nForme lisible:\n{pretty(self.expr)}\n")
        print(f"LaTeX:\n${latex(self.expr)}$\n")
    
    def developper(self, afficher=True):
        """Développe l'expression et retourne un nouvel AlgebreTerm"""
        resultat = expand(self.expr)
        if afficher:
            print("\n" + "─"*60)
            print("✨ DÉVELOPPEMENT")
            print("─"*60)
            print(f"\nExpression initiale:\n{pretty(self.expr)}\n")
            print(f"Expression développée:\n{pretty(resultat)}\n")
            print(f"LaTeX:\n${latex(resultat)}$\n")
        return AlgebreTerm(expr_sympy=resultat)
    
    def factoriser(self, afficher=True):
        """Factorise l'expression et retourne un nouvel AlgebreTerm"""
        resultat = factor(self.expr)
        if afficher:
            print("\n" + "─"*60)
            print("🎯 FACTORISATION")
            print("─"*60)
            print(f"\nExpression initiale:\n{pretty(self.expr)}\n")
            print(f"Expression factorisée:\n{pretty(resultat)}\n")
            print(f"LaTeX:\n${latex(resultat)}$\n")
        return AlgebreTerm(expr_sympy=resultat)
    
    def simplifier(self, afficher=True):
        """Simplifie l'expression"""
        resultat = simplify(self.expr)
        if afficher:
            print("\n" + "─"*60)
            print("🧹 SIMPLIFICATION")
            print("─"*60)
            print(f"\nExpression initiale:\n{pretty(self.expr)}\n")
            print(f"Expression simplifiée:\n{pretty(resultat)}\n")
            print(f"LaTeX:\n${latex(resultat)}$\n")
        return AlgebreTerm(expr_sympy=resultat)
    
    def deriver(self, variable, afficher=True):
        """Dérive par rapport à une variable"""
        var = Symbol(variable)
        resultat = diff(self.expr, var)
        if afficher:
            print("\n" + "─"*60)
            print(f"📈 DÉRIVÉE par rapport à {variable}")
            print("─"*60)
            print(f"\nExpression initiale:\n{pretty(self.expr)}\n")
            print(f"Dérivée:\n{pretty(resultat)}\n")
            print(f"LaTeX:\n$\\frac{{d}}{{d{variable}}} = {latex(resultat)}$\n")
        return AlgebreTerm(expr_sympy=resultat)
    
    def integrer(self, variable, afficher=True):
        """Intègre par rapport à une variable"""
        var = Symbol(variable)
        resultat = integrate(self.expr, var)
        if afficher:
            print("\n" + "─"*60)
            print(f"∫ INTÉGRALE par rapport à {variable}")
            print("─"*60)
            print(f"\nExpression initiale:\n{pretty(self.expr)}\n")
            print(f"Intégrale:\n{pretty(resultat)}\n")
            print(f"LaTeX:\n$\\int {latex(self.expr)} d{variable} = {latex(resultat)} + C$\n")
        return AlgebreTerm(expr_sympy=resultat)
    
    def resoudre(self, variable, afficher=True):
        """Résout l'équation (expr = 0)"""
        var = Symbol(variable)
        solutions = solve(self.expr, var)
        if afficher:
            print("\n" + "─"*60)
            print(f"🔍 RÉSOLUTION ({variable})")
            print("─"*60)
            print(f"\nÉquation: {pretty(self.expr)} = 0\n")
            print(f"Solutions:\n")
            for i, sol in enumerate(solutions, 1):
                print(f"  {variable}_{i} = {pretty(sol)}")
                print(f"       LaTeX: ${latex(sol)}$\n")
        return solutions
    
    def substituer(self, variable, valeur, afficher=True):
        """Substitue une variable par une valeur"""
        var = Symbol(variable)
        resultat = self.expr.subs(var, valeur)
        if afficher:
            print("\n" + "─"*60)
            print(f"🔄 SUBSTITUTION ({variable} = {valeur})")
            print("─"*60)
            print(f"\nExpression initiale:\n{pretty(self.expr)}\n")
            print(f"Après substitution:\n{pretty(resultat)}\n")
            print(f"LaTeX:\n${latex(resultat)}$\n")
        return AlgebreTerm(expr_sympy=resultat)
    
    def afficher_latex_pur(self):
        """Affiche uniquement le code LaTeX"""
        return latex(self.expr)
    
    def copier_latex(self):
        """Retourne le code LaTeX pour copier-coller"""
        return f"${latex(self.expr)}$"


# Exemples d'utilisation
if __name__ == "__main__":
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  CALCULATEUR D'ALGÈBRE AVEC LATEX".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60 + "\n")
    
    # Exemple 1: Développement
    print("\n🔷 EXEMPLE 1: DÉVELOPPEMENT")
    print("─"*60)
    expr1 = AlgebreTerm("(x + 2)*(x - 3)")
    expr1.afficher("Expression initiale")
    resultat1 = expr1.developper()
    
    # Exemple 2: Factorisation
    print("\n\n🔷 EXEMPLE 2: FACTORISATION")
    print("─"*60)
    expr2 = AlgebreTerm("x**2 + 5*x + 6")
    expr2.afficher("Expression initiale")
    resultat2 = expr2.factoriser()
    
    # Exemple 3: Développement d'un trinôme
    print("\n\n🔷 EXEMPLE 3: TRINÔME")
    print("─"*60)
    expr3 = AlgebreTerm("(a + b + c)**2")
    expr3.afficher("Expression initiale")
    resultat3 = expr3.developper()
    
    # Exemple 4: Dérivée
    print("\n\n🔷 EXEMPLE 4: DÉRIVÉE")
    print("─"*60)
    expr4 = AlgebreTerm("x**3 + 2*x**2 - 5*x + 3")
    expr4.afficher("Expression initiale")
    expr4.deriver("x")
    
    # Exemple 5: Résolution d'équation
    print("\n\n🔷 EXEMPLE 5: RÉSOLUTION D'ÉQUATION")
    print("─"*60)
    expr5 = AlgebreTerm("x**2 - 5*x + 6")
    expr5.afficher("Équation: f(x) = 0")
    expr5.resoudre("x")
    
    # Exemple 6: Substitution
    print("\n\n🔷 EXEMPLE 6: SUBSTITUTION")
    print("─"*60)
    expr6 = AlgebreTerm("2*x**2 + 3*x - 5")
    expr6.afficher("Expression initiale")
    expr6.substituer("x", 2)
    
    print("\n" + "█"*60)
    print("█" + " Fin des exemples ".center(58) + "█")
    print("█"*60 + "\n")
