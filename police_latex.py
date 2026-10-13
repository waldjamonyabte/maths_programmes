"""
police_latex.py
Exemple de calcul symbolique avec Sympy et rendu mathématique élégant.
Utilise Cambria / Cambria Math si disponible sur Windows.
"""

from sympy import symbols, Eq, solve, diff, integrate, simplify, latex
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def cambria_math_available():
    """Retourne True si une police Cambria est détectée."""
    names = {f.name for f in fm.fontManager.ttflist}
    return any('Cambria' in name for name in names)


def configure_math_font():
    """Configure matplotlib pour utiliser Cambria Math si elle est disponible."""
    if cambria_math_available():
        plt.rcParams['mathtext.fontset'] = 'custom'
        plt.rcParams['mathtext.rm'] = 'Cambria'
        plt.rcParams['mathtext.it'] = 'Cambria:italic'
        plt.rcParams['mathtext.bf'] = 'Cambria:bold'
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Cambria']
        return True
    return False


def build_examples():
    x = symbols('x')
    expr = (x + 1)**5
    equation = Eq(x**2 + 2*x - 3, 0)
    derivative = diff(expr, x)
    integral = integrate(sin(x)/x, x)
    solutions = solve(equation, x)
    simplified = simplify((x**2 - 1)/(x - 1))
    return {
        'expression': expr,
        'equation': equation,
        'derivative': derivative,
        'integral': integral,
        'solutions': solutions,
        'simplified': simplified,
    }


def render_math_text(lines, use_cambria):
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.axis('off')
    y = 0.92
    for text in lines:
        ax.text(
            0.02,
            y,
            text,
            fontsize=26,
            va='top',
            family='Cambria' if use_cambria else 'DejaVu Sans',
        )
        y -= 0.16

    title = 'Affichage symbolique avec Cambria Math' if use_cambria else 'Affichage symbolique avec police par défaut'
    fig.suptitle(title, fontsize=28, fontweight='bold')
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def main():
    use_cambria = configure_math_font()
    examples = build_examples()

    lines = [
        r'Expression : $%s$' % latex(examples['expression']),
        r'Équation : $%s$' % latex(examples['equation']),
        r'Dérivée : $%s$' % latex(examples['derivative']),
        r'Intégrale : $%s$' % latex(examples['integral']),
        r'Solutions : $%s$' % latex(examples['solutions']),
        r'Simplifié : $%s$' % latex(examples['simplified']),
    ]

    print('Cambria disponible :', use_cambria)
    for line in lines:
        print(line)

    render_math_text(lines, use_cambria)


if __name__ == '__main__':
    main()

