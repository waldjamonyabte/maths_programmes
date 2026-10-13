import string

# Système de chiffres étendu : '0' suivi des caractères ASCII imprimables (sauf '0')
DIGITS = '0' + ''.join(chr(i) for i in range(32, 127) if chr(i) != '0')

def to_decimal(num_str, base):
    """
    Convertit une chaîne représentant un nombre en base donnée vers la base décimale.
    Supporte les bases jusqu'à 95 (caractères ASCII imprimables).
    """
    if base > len(DIGITS):
        raise ValueError(f"Base {base} trop élevée, maximum {len(DIGITS)}")
    decimal = 0
    for char in num_str:
        try:
            digit = DIGITS.index(char)
        except ValueError:
            raise ValueError(f"Caractère invalide: {char}")
        if digit >= base:
            raise ValueError(f"Chiffre {digit} hors de portée pour la base {base}")
        decimal = decimal * base + digit
    return decimal

def from_decimal(decimal, base):
    """
    Convertit un nombre décimal vers une chaîne en base donnée.
    Supporte les bases jusqu'à 95.
    """
    if base > len(DIGITS):
        raise ValueError(f"Base {base} trop élevée, maximum {len(DIGITS)}")
    if decimal == 0:
        return DIGITS[0]  # '0'
    digits_list = []
    while decimal > 0:
        remainder = decimal % base
        digits_list.append(DIGITS[remainder])
        decimal //= base
    return ''.join(reversed(digits_list))

def convert_base(num_str, from_base, to_base):
    """
    Convertit un nombre d'une base à une autre.
    """
    decimal = to_decimal(num_str, from_base)
    return from_decimal(decimal, to_base)

def generate_html_result(num_str, from_base, to_base, result):
    """
    Génère un fichier HTML avec le résultat formaté en LaTeX avec MathJax.
    """
    # Calcul détaillé : conversion en décimal
    decimal_value = to_decimal(num_str, from_base)
    decimal_terms = []
    for i, char in enumerate(num_str):
        digit = DIGITS.index(char)
        exponent = len(num_str) - i - 1
        decimal_terms.append(f"({digit}) \\times {from_base}^{{{exponent}}}")
    decimal_expression = " + ".join(decimal_terms)

    html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversion de Base Avancée - MathJax</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }}
        .container {{
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        h1 {{
            color: #667eea;
            text-align: center;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #764ba2;
            margin-top: 30px;
        }}
        .result-box {{
            background: #f0f4ff;
            border-left: 5px solid #667eea;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        .step {{
            background: #fafafa;
            border-left: 5px solid #764ba2;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
        }}
        .math-formula {{
            font-size: 1.1em;
            line-height: 1.8;
            margin: 10px 0;
        }}
        .explanation {{
            color: #555;
            font-size: 0.95em;
            margin: 5px 0;
        }}
        footer {{
            text-align: center;
            margin-top: 30px;
            color: #999;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔢 Convertisseur de Base Avancée</h1>
        
        <div class="result-box">
            <h2>Résultat Principal</h2>
            <div class="math-formula">
                $${num_str}_{{{from_base}}} = {result}_{{{to_base}}}$$
            </div>
        </div>

        <div class="step">
            <h2>Étape 1 : Conversion en Base Décimale</h2>
            <div class="explanation">
                Chaque chiffre est multiplié par la base élevée à sa position.
            </div>
            <div class="math-formula">
                $${num_str}_{{{from_base}}} = {decimal_expression} = {decimal_value}_{{10}}$$
            </div>
        </div>

        <div class="step">
            <h2>Étape 2 : Conversion vers la Base Cible</h2>
            <div class="explanation">
                Division successive par la base cible, en gardant les restes.
            </div>
            <div class="math-formula">
                $${decimal_value}_{{{10}}} \\rightarrow {result}_{{{to_base}}}$$
            </div>
        </div>

        <div class="step">
            <h2>Algorithme Détaillé</h2>
            <div class="math-formula">
                \\begin{{align}}
                \\text{{Conversion en décimal:}} & \\quad N_{{b}} = \\sum_{{i=0}}^{{n-1}} d_i \\times b^{{i}} \\\\
                \\text{{Conversion vers base}} & \\quad r_i = N \\mod b, \\; N \\leftarrow \\lfloor N/b \\rfloor
                \\end{{align}}
            </div>
        </div>

        <div class="result-box">
            <h2>Informations de Conversion</h2>
            <div class="explanation">
                <strong>Nombre source :</strong> {num_str}<br>
                <strong>Base source :</strong> {from_base}<br>
                <strong>Valeur décimale :</strong> {decimal_value}<br>
                <strong>Base cible :</strong> {to_base}<br>
                <strong>Nombre cible :</strong> {result}
            </div>
        </div>

        <footer>
            <p>Générée avec Python et MathJax</p>
        </footer>
    </div>
</body>
</html>
"""
    with open("resultat_conversion.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✓ Fichier HTML généré : resultat_conversion.html")
    print("  Ouvrez le fichier dans un navigateur pour voir le rendu LaTeX avec MathJax.")

if __name__ == "__main__":
    print("=== Convertisseur de Base Avancée ===")
    print("Résultats affichés avec rendu MathJax dans un fichier HTML.")
    print()

    # Demander les entrées
    num_str = input("Entrez le nombre à convertir (en tant que chaîne) : ")
    from_base = int(input("Entrez la base source (entier > 1) : "))
    to_base = int(input("Entrez la base cible (entier > 1) : "))

    try:
        result = convert_base(num_str, from_base, to_base)
        print(f"Le nombre {num_str} en base {from_base} correspond à {result} en base {to_base}.")
        generate_html_result(num_str, from_base, to_base, result)
    except ValueError as e:
        print(f"Erreur : {e}")