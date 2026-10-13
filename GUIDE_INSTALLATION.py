#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Guide d'installation des bibliothèques mathématiques
"""

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   📚 BIBLIOTHÈQUES MATHÉMATIQUES PYTHON - GUIDE D'INSTALLATION              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝


📝 POUR MES SCRIPTS DE CALCULATRICE D'ALGÈBRE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ESSENTIEL (obligatoire):
────────────────────────
1️⃣  SymPy
   └─ Calcul symbolique (développement, factorisation, dérivée, intégrale)
   └─ Affichage LaTeX
   └─ Résolution d'équations
   
   Installation:
   $ pip install sympy


╔══════════════════════════════════════════════════════════════════════════════╗
║  RECOMMANDÉ (pour des fonctionnalités avancées)                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

2️⃣  NumPy
   └─ Mathématiques numériques rapides
   └─ Matrices et tableaux multidimensionnels
   └─ Calculs vectorisés
   
   Installation:
   $ pip install numpy

3️⃣  SciPy
   └─ Algorithmes scientifiques avancés
   └─ Optimisation, intégration numérique
   └─ Statistiques, traitement du signal
   
   Installation:
   $ pip install scipy

4️⃣  Matplotlib
   └─ Tracer des courbes et graphiques
   └─ Visualisation de fonctions mathématiques
   └─ Génération de graphes
   
   Installation:
   $ pip install matplotlib

5️⃣  MPMath
   └─ Arithmétique à précision arbitraire
   └─ Fonctions spéciales mathématiques
   
   Installation:
   $ pip install mpmath


╔══════════════════════════════════════════════════════════════════════════════╗
║  INSTALLATION RAPIDE (tous à la fois)                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

Ouvrez un terminal (CMD, PowerShell, ou Bash) et tapez:

$ pip install sympy numpy scipy matplotlib mpmath


Ou depuis le répertoire du projet:

$ pip install -r requirements.txt


╔══════════════════════════════════════════════════════════════════════════════╗
║  VÉRIFIER L'INSTALLATION                                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

Testez que tout fonctionne:

$ python -c "import sympy; print('✅ SymPy OK')"
$ python -c "import numpy; print('✅ NumPy OK')"
$ python -c "import scipy; print('✅ SciPy OK')"
$ python -c "import matplotlib; print('✅ Matplotlib OK')"


╔══════════════════════════════════════════════════════════════════════════════╗
║  DESCRIPTION DÉTAILLÉE DE CHAQUE BIBLIOTHÈQUE                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

🔷 SymPy - Calcul symbolique
   ├─ Développement d'expressions: (x+1)² → x² + 2x + 1
   ├─ Factorisation: x² + 5x + 6 → (x+2)(x+3)
   ├─ Dérivation: d/dx(x³) = 3x²
   ├─ Intégration: ∫x² dx = x³/3
   ├─ Résolution: x² - 5x + 6 = 0 → x = 2, 3
   ├─ Simplification automatique
   └─ Affichage LaTeX pour math beautifully formatted
   
   Utilisation:
   >>> from sympy import symbols, expand, factor, latex
   >>> x = symbols('x')
   >>> expr = (x + 1)**2
   >>> print(expand(expr))
   x**2 + 2*x + 1
   >>> print(latex(expand(expr)))
   x^{2} + 2 x + 1


🔷 NumPy - Tableaux et matrices
   ├─ Création de matrices
   ├─ Opérations matricielles rapides
   ├─ Algèbre linéaire
   └─ Calculs vectorisés (plus rapide que les boucles Python)
   
   Utilisation:
   >>> import numpy as np
   >>> A = np.array([[1, 2], [3, 4]])
   >>> B = np.array([[5, 6], [7, 8]])
   >>> print(np.dot(A, B))  # Multiplication matricielle


🔷 SciPy - Algorithmes scientifiques
   ├─ Intégration numérique: ∫f(x)dx
   ├─ Optimisation: Trouver min/max
   ├─ Résolution d'équations différentielles
   ├─ Transformée de Fourier
   └─ Statistiques avancées
   
   Utilisation:
   >>> from scipy import integrate
   >>> def f(x): return x**2
   >>> result, error = integrate.quad(f, 0, 1)
   >>> print(result)  # 0.333...


🔷 Matplotlib - Tracer des courbes
   ├─ Graphiques 2D et 3D
   ├─ Courbes paramétrées
   ├─ Histogrammes, boîtes à moustaches
   └─ Enregistrement en PNG, PDF, SVG
   
   Utilisation:
   >>> import matplotlib.pyplot as plt
   >>> import numpy as np
   >>> x = np.linspace(-10, 10, 100)
   >>> y = x**2
   >>> plt.plot(x, y)
   >>> plt.show()


🔷 MPMath - Précision arbitraire
   ├─ Calculs avec 100 décimales ou plus
   ├─ Fonctions spéciales (Bessel, Hermite, etc.)
   ├─ Nombres complexes haute précision
   └─ Séries infinies
   
   Utilisation:
   >>> from mpmath import mp, pi, sqrt
   >>> mp.dps = 50  # 50 décimales
   >>> print(mp.pi)


╔══════════════════════════════════════════════════════════════════════════════╗
║  MINIMAL POUR MES SCRIPTS                                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

Pour faire fonctionner calculatrice_algebre_menu.py, vous avez besoin de:

   ✅ ESSENTIEL:
      $ pip install sympy

   🎯 OPTIONNEL (pour plus de fonctionnalités):
      $ pip install numpy scipy matplotlib


╔══════════════════════════════════════════════════════════════════════════════╗
║  PROBLÈMES COURANTS                                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

❌ "pip: command not found"
   → Utilisez: python -m pip install sympy

❌ "Permission denied"
   → Utilisez: pip install --user sympy
   
❌ Module not found après installation
   → Vérifiez que vous utilisez le bon Python:
     python --version
     pip --version

❌ SymPy est lent au démarrage
   → C'est normal, il compile certains modules
   → La 2ème exécution est plus rapide


╔══════════════════════════════════════════════════════════════════════════════╗
║  PRÊT À DÉMARRER!                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

Une fois sympy installé, lancez:

   $ python calculatrice_algebre_menu.py


Bon calcul ! 🧮✨

""")
