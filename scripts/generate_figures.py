import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_fig(name):
    path = os.path.join("figures", name)
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"Generated: {path}")
    plt.close()

def generate_graphical_abstract():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Origen
    ax.add_patch(patches.Rectangle((0.5, 1.5), 2, 2, fill=True, color='skyblue', alpha=0.5))
    ax.text(1.5, 2.5, "Origen\n(Comunidad Afectiva)", ha='center', va='center', fontsize=12)

    # Smartphone (Centro)
    ax.add_patch(patches.FancyBboxPatch((4.5, 1), 1, 3, boxstyle="round,pad=0.1", color='gray'))
    ax.text(5, 2.5, "Smartphone\nResignificación", ha='center', va='center', color='white', fontweight='bold')

    # Destino
    ax.add_patch(patches.Rectangle((7.5, 1.5), 2, 2, fill=True, color='lightgreen', alpha=0.5))
    ax.text(8.5, 2.5, "Destino\n(Supervivencia)", ha='center', va='center', fontsize=12)

    # Flechas
    ax.annotate('', xy=(4.4, 2.5), xytext=(2.6, 2.5), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(7.4, 2.5), xytext=(5.6, 2.5), arrowprops=dict(arrowstyle='->', lw=2))

    plt.title("Graphical Abstract: Modelo de Resignificación Migrante", fontsize=16)
    save_fig("graphical_abstract.png")

def generate_prisma():
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    boxes = [
        (1, 8.5, 8, 1, "Identificación: Scopus (n=450), Otros (n=20)"),
        (1, 6.5, 8, 1, "Screening: Títulos y Abstracts (n=380)"),
        (1, 4.5, 8, 1, "Elegibilidad: Texto completo (n=210)"),
        (1, 2.5, 8, 1, "Incluidos: Meta-análisis cualitativo (n=160)")
    ]

    for x, y, w, h, text in boxes:
        ax.add_patch(patches.Rectangle((x, y), w, h, fill=False, lw=2))
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=11)
        if y > 3:
            ax.annotate('', xy=(x+w/2, y-0.1), xytext=(x+w/2, y-0.5), arrowprops=dict(arrowstyle='->'))

    plt.title("Diagrama de Flujo PRISMA 2020", fontsize=14)
    save_fig("prisma_flowchart.png")

def generate_conceptual_framework():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    center = (5, 5)
    circle = patches.Circle(center, 1.5, color='gold', alpha=0.3)
    ax.add_patch(circle)
    ax.text(5, 5, "Resignificación", ha='center', va='center', fontweight='bold')

    nodes = [
        (5, 8, "Conectividad\n(Afectivo)"),
        (2, 3, "Contexto de Uso\n(Funcional)"),
        (8, 3, "Divergencias\n(Riesgo/Apoyo)")
    ]

    for x, y, text in nodes:
        ax.add_patch(patches.Circle((x, y), 1.2, color='skyblue', alpha=0.5))
        ax.text(x, y, text, ha='center', va='center', fontsize=10)
        ax.annotate('', xy=(x, y), xytext=center, arrowprops=dict(arrowstyle='<-', lw=1.5))

    plt.title("Marco Analítico de la Resignificación", fontsize=14)
    save_fig("conceptual_framework.png")

def generate_comparison_matrix():
    fig, ax = plt.subplots(figsize=(8, 6))
    categories = ['Identidad', 'Vínculos', 'Propósito', 'Contenido']
    conventional = [2, 3, 2, 5]
    migrant = [5, 5, 5, 3]

    x = range(len(categories))
    ax.bar(x, conventional, width=0.4, label='Convencional', align='edge', color='lightgray')
    ax.bar(x, migrant, width=-0.4, label='Migrante', align='edge', color='darkblue')

    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel('Intensidad/Centralidad')
    ax.legend()
    plt.title("Comparación de Perfiles de Uso", fontsize=14)
    save_fig("comparison_matrix.png")

def generate_social_capital():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.add_patch(patches.Circle((5, 5), 4, fill=False, ls='--'))
    
    functions = [
        (5, 8.5, "Vínculos Fuertes\n(Familia)"),
        (8.5, 5, "Vínculos Débiles\n(Trabajo)"),
        (5, 1.5, "Vínculos Latentes\n(Comunidad)"),
        (1.5, 5, "Info Interna\n(Rutas/Leyes)")
    ]

    for x, y, text in functions:
        ax.text(x, y, text, ha='center', va='center', bbox=dict(boxstyle="round", facecolor='white'))
        ax.annotate('', xy=(x, y), xytext=(5, 5), arrowprops=dict(arrowstyle='<->'))

    ax.text(5, 5, "Capital Social\nDigital", ha='center', va='center', fontweight='bold')
    plt.title("Funciones del Capital Social Digital", fontsize=14)
    save_fig("social_capital_functions.png")

if __name__ == "__main__":
    create_dir("figures")
    generate_graphical_abstract()
    generate_prisma()
    generate_conceptual_framework()
    generate_comparison_matrix()
    generate_social_capital()
