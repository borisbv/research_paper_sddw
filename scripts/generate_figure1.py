"""
Genera la Figura 1: Modelo metodológico propuesto.
Diagrama de flujo vertical con retroalimentación cíclica.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(8, 10), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Colors
colors = {
    'ux': '#4A90D9',
    'hallazgos': '#5BA85B',
    'criterios': '#E8943A',
    'implementacion': '#D94A4A',
    'aprendizaje': '#8B5BA8',
    'arrow': '#333333',
    'feedback': '#888888',
    'ux_stages': '#7AB3E8',
}

# Box positions (x_center, y_center)
boxes = [
    (5, 10.5, 'Metodología UX\n(5 etapas cíclicas)', colors['ux']),
    (5, 8.2, 'Hallazgos empíricos', colors['hallazgos']),
    (5, 5.9, 'Criterios de diseño', colors['criterios']),
    (5, 3.6, 'Implementación XR', colors['implementacion']),
    (5, 1.3, 'Aprendizaje de\ncomposición arquitectónica', colors['aprendizaje']),
]

box_width = 4.5
box_height = 1.1

# Draw boxes
for x, y, text, color in boxes:
    bbox = FancyBboxPatch(
        (x - box_width/2, y - box_height/2),
        box_width, box_height,
        boxstyle="round,pad=0.15",
        facecolor=color, edgecolor='white',
        linewidth=2, alpha=0.9
    )
    ax.add_patch(bbox)
    ax.text(x, y, text, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white',
            family='sans-serif')

# Draw downward arrows between boxes
arrow_style = dict(arrowstyle='->', color=colors['arrow'],
                   linewidth=2, mutation_scale=20)
for i in range(len(boxes) - 1):
    x1, y1 = boxes[i][0], boxes[i][1] - box_height/2
    x2, y2 = boxes[i+1][0], boxes[i+1][1] + box_height/2
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=arrow_style)

# UX stages as small labels on the left
ux_stages = ['Empatizar', 'Definir', 'Idear', 'Prototipar', 'Testear']
stage_y_start = 10.9
stage_y_end = 10.1
stage_xs = np.linspace(1.2, 8.8, 5)

for i, (stage, sx) in enumerate(zip(ux_stages, stage_xs)):
    ax.text(sx, 11.5, stage, ha='center', va='center',
            fontsize=7.5, color=colors['ux'], fontweight='bold',
            family='sans-serif',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=colors['ux_stages'],
                      edgecolor=colors['ux'], alpha=0.3, linewidth=0.8))

# Curved feedback arrow on the right side (from bottom back to top)
from matplotlib.patches import FancyArrowPatch
import matplotlib.path as mpath

# Feedback arrow path on the right
feedback_x = 8.2
feedback_points = [
    (boxes[-1][0] + box_width/2 + 0.1, boxes[-1][1]),
    (feedback_x, boxes[-1][1]),
    (feedback_x, boxes[0][1]),
    (boxes[0][0] + box_width/2 + 0.1, boxes[0][1]),
]

# Draw feedback with individual line segments and arrow
ax.annotate('', xy=(feedback_points[3][0], feedback_points[3][1]),
            xytext=(feedback_points[2][0], feedback_points[2][1]),
            arrowprops=dict(arrowstyle='->', color=colors['feedback'],
                          linewidth=1.5, mutation_scale=15,
                          linestyle='--'))

ax.plot([feedback_points[0][0], feedback_points[1][0]],
        [feedback_points[0][1], feedback_points[1][1]],
        color=colors['feedback'], linewidth=1.5, linestyle='--')
ax.plot([feedback_points[1][0], feedback_points[2][0]],
        [feedback_points[1][1], feedback_points[2][1]],
        color=colors['feedback'], linewidth=1.5, linestyle='--')

ax.text(feedback_x + 0.3, 5.9, 'Retroalimentación\niterativa',
        ha='left', va='center', fontsize=8, color=colors['feedback'],
        fontstyle='italic', rotation=90, family='sans-serif')

# Title
ax.text(5, 12.3, 'Figura 1. Modelo metodológico propuesto',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color='#333333', family='sans-serif')

plt.tight_layout()
plt.savefig('C:/Github/research_paper_sddw/paper/figures/figura1-modelo-metodologico.png',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print("Figura 1 generada exitosamente.")
