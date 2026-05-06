#!/bin/bash
# Compile manuscript to DOCX for RES submission
# Format: Times New Roman 12pt, line spacing 1.5, margins 2.5cm

set -e

OUTPUT_DIR="_book"
OUTPUT_FILE="$OUTPUT_DIR/memorias-casas-piernas-manuscrito.docx"

echo "=== Compilando manuscrito para RES ==="

# Concatenate all sections in order
cat \
  paper/00-frontmatter.md \
  paper/01-introduccion.md \
  paper/02-marco-teorico.md \
  paper/03-metodologia.md \
  paper/04-resultados.md \
  paper/05-discusion.md \
  paper/06-conclusion.md \
  > "$OUTPUT_DIR/manuscrito-completo.md"

echo "✅ Manuscrito ensamblado: $(wc -w < "$OUTPUT_DIR/manuscrito-completo.md") palabras"

# Convert to DOCX with Pandoc
pandoc "$OUTPUT_DIR/manuscrito-completo.md" \
  --from markdown \
  --to docx \
  --reference-doc="$OUTPUT_DIR/reference.docx" \
  --lua-filter="_book/res-format.lua" \
  --bibliography=references/references.bib \
  --citeproc \
  --csl=https://raw.githubusercontent.com/citation-style-language/styles/master/chicago-author-date.csl \
  --metadata title="Memorias de casas con piernas: voces de los que se fueron, voces de los que llegaron" \
  --variable mainfont="Times New Roman" \
  --variable fontsize=12pt \
  --variable geometry:margin=2.5cm \
  --variable linestretch=1.5 \
  -o "$OUTPUT_FILE"

echo "✅ DOCX generado: $OUTPUT_FILE"
echo "=== Compilación completa ==="
