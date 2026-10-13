"""
Module pour afficher des variables mathématiques en police mathématique (LaTeX)
Supporte plusieurs formats : console, fichier, et rendu visuel
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams
import sympy as sp
from sympy import symbols, latex, pretty

# ============================================================================
# APPROCHE 1 : Utiliser SymPy pour l'affichage élégant
# ============================================================================

def afficher_sympy(expression, titre="Expression mathématique"):
    """
    Affiche une expression mathématique avec SymPy (nice print)
    """
    print(f"\n{titre}:")
    print("=" * 50)
    print(pretty(expression))
    print("=" * 50)


# ============================================================================
# APPROCHE 2 : Utiliser LaTeX pour un rendu graphique
# ============================================================================

def afficher_latex(expression, titre="Expression mathématique", fichier_sortie=None):
    """
    Affiche une expression mathématique en LaTeX avec matplotlib
    
    Args:
        expression: Expression SymPy ou chaîne LaTeX
        titre: Titre du graphique
        fichier_sortie: Optionnel, chemin pour sauvegarder l'image
    """
    # Convertir en LaTeX si c'est une expression SymPy
    if not isinstance(expression, str):
        latex_str = latex(expression)
    else:
        latex_str = expression
    
    # Créer la figure
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('off')
    
    # Afficher le texte mathématique
    ax.text(0.5, 0.5, f'${latex_str}$', 
            fontsize=20, 
            ha='center', 
            va='center',
            transform=ax.transAxes)
    
    plt.title(titre, fontsize=14, pad=20)
    
    if fichier_sortie:
        plt.savefig(fichier_sortie, dpi=150, bbox_inches='tight')
        print(f"Image sauvegardée : {fichier_sortie}")
    
    plt.show()


# ============================================================================
# APPROCHE 3 : Classe pour gérer les variables mathématiques
# ============================================================================

class VariableMathematique:
    """
    Classe pour représenter et afficher des variables mathématiques
    """
    
    def __init__(self, nom, symbole_latex=None, valeur=None):
        """
        Initialise une variable mathématique
        
        Args:
            nom: Nom de la variable
            symbole_latex: Symbole LaTeX personnalisé
            valeur: Valeur numérique (optionnel)
        """
        self.nom = nom
        self.symbole_latex = symbole_latex or nom
        self.valeur = valeur
        self.symbole = sp.Symbol(nom)
    
    def __str__(self):
        """Affichage texte simple"""
        if self.valeur is not None:
            return f"{self.nom} = {self.valeur}"
        return self.nom
    
    def afficher_pretty(self):
        """Affichage élégant console"""
        print(f"{self.nom}: {pretty(self.symbole)}")
    
    def latex(self):
        """Retourne la représentation LaTeX"""
        return self.symbole_latex


# ============================================================================
# APPROCHE 4 : Fonction helper pour imprimer dans une police "mathématique"
# ============================================================================

def print_math(expression, format="pretty"):
    """
    Imprime une expression mathématique dans le format spécifié
    
    Args:
        expression: Expression SymPy ou chaîne
        format: "pretty" (console élégante), "latex" (LaTeX), "unicode" (Unicode)
    
    Exemples:
        x = sp.Symbol('x')
        expr = x**2 + 2*x + 1
        print_math(expr, format="pretty")
    """
    if format == "pretty":
        print(pretty(expression))
    elif format == "latex":
        print(latex(expression))
    elif format == "unicode":
        print(pretty(expression, use_unicode=True))


# ============================================================================
# EXEMPLES D'UTILISATION
# ============================================================================

if __name__ == "__main__":
    
    # Créer des symboles
    x, y, z, a, b, c = symbols('x y z a b c')
    
    # EXEMPLE 1 : Affichage simple avec SymPy
    print("\n" + "="*60)
    print("EXEMPLE 1 : Affichage simple avec SymPy")
    print("="*60)
    
    expr1 = x**2 + 2*x + 1
    afficher_sympy(expr1, "Trinôme du second degré")
    
    
    # EXEMPLE 2 : Équation quadratique
    print("\n" + "="*60)
    print("EXEMPLE 2 : Équation quadratique")
    print("="*60)
    
    expr2 = a*x**2 + b*x + c
    afficher_sympy(expr2, "Forme générale")
    
    discriminant = b**2 - 4*a*c
    afficher_sympy(discriminant, "Discriminant")
    
    
    # EXEMPLE 3 : Limite et dérivée
    print("\n" + "="*60)
    print("EXEMPLE 3 : Calculs mathématiques")
    print("="*60)
    
    expr3 = sp.sin(x) / x
    derivee = sp.diff(expr3, x)
    afficher_sympy(derivee, "Dérivée de sin(x)/x")
    
    
    # EXEMPLE 4 : Matrice
    print("\n" + "="*60)
    print("EXEMPLE 4 : Matrice")
    print("="*60)
    
    matrice = sp.Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    afficher_sympy(matrice, "Matrice 3x3")
    
    
    # EXEMPLE 5 : Intégrale
    print("\n" + "="*60)
    print("EXEMPLE 5 : Intégrale")
    print("="*60)
    
    integrale = sp.integrate(x**2, x)
    afficher_sympy(integrale, "Intégrale de x²")
    
    
    # EXEMPLE 6 : Utiliser la classe VariableMathematique
    print("\n" + "="*60)
    print("EXEMPLE 6 : Variables mathématiques personnalisées")
    print("="*60)
    
    var_x = VariableMathematique("x", "\\alpha", 5)
    var_y = VariableMathematique("y", "\\beta", 10)
    
    print(f"Variable 1: {var_x}")
    print(f"Variable 2: {var_y}")
    print(f"LaTeX x: ${var_x.latex()}$")
    print(f"LaTeX y: ${var_y.latex()}$")
    
    
    # EXEMPLE 7 : Différents formats d'affichage
    print("\n" + "="*60)
    print("EXEMPLE 7 : Différents formats")
    print("="*60)
    
    expr_test = (x + y)**2
    
    print("\n[Format PRETTY]")
    print_math(expr_test, format="pretty")
    
    print("\n[Format LATEX]")
    print_math(expr_test, format="latex")
    
    print("\n[Format UNICODE]")
    print_math(expr_test, format="unicode")
    
    
    # EXEMPLE 8 : Affichage graphique avec matplotlib (décommenté pour voir)
    # afficher_latex(x**2 + 2*x + 1, 
    #               "Polynôme du second degré",
    #               fichier_sortie="equation.png")
