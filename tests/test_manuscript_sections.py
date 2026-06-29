"""Tests de validación para las secciones del manuscrito (TDD para tareas 4.1 y 4.2)."""

import os
import re
import pytest

# --- Utilidades de validación ---

def count_words(text: str) -> int:
    """Cuenta palabras en texto plano, excluyendo YAML frontmatter y comentarios HTML."""
    # Remover frontmatter YAML
    text = re.sub(r'^---.*?---', '', text, flags=re.DOTALL)
    # Remover comentarios HTML
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Remover encabezados Markdown puros (solo #)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # Remover etiquetas Quarto como {.unnumbered}
    text = re.sub(r'\{[^}]*\}', '', text)
    # Remover marcadores de formato Markdown
    text = re.sub(r'\*\*|__|\*|_', '', text)
    return len(text.split())


def extract_section(text: str, heading: str) -> str:
    """Extrae contenido bajo un heading específico hasta el siguiente heading del mismo nivel."""
    pattern = rf'^(#+)\s*{re.escape(heading)}.*?\n(.*?)(?=^\1\s|\Z)'
    match = re.search(pattern, text, flags=re.DOTALL | re.MULTILINE)
    return match.group(2).strip() if match else ''


def extract_citations(text: str) -> list[str]:
    """Extrae citekeys de referencias Quarto [@citekey] o [@key1; @key2].
    Excluye referencias cruzadas de Quarto (@fig-, @tbl-, @sec-, @eq-, @lst-)
    y falsos positivos como direcciones de correo electrónico."""
    # Remover emails para evitar falsos positivos (e.g., user@domain)
    cleaned = re.sub(r'[\w.+-]+@[\w-]+\.[\w.-]+', '', text)
    matches = re.findall(r'@([\w-]+)', cleaned)
    cross_ref_prefixes = ('fig-', 'tbl-', 'sec-', 'eq-', 'lst-', 'thm-', 'lem-', 'cor-', 'def-')
    return list(set(m for m in matches if not m.startswith(cross_ref_prefixes)))


# --- Tests para 4.1: Portada y Abstract ---

class TestTitlePage:
    """Validaciones para la portada (index.qmd)."""

    @pytest.fixture
    def title_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'index.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_title_exists_and_not_placeholder(self, title_content):
        """El título no debe ser un placeholder."""
        assert '[Pendiente' not in title_content
        assert '[Nombre del autor]' not in title_content

    def test_has_author_and_affiliation(self, title_content):
        """Debe incluir autor y afiliación real."""
        content_lower = title_content.lower()
        assert 'boris' in content_lower or 'autor' in content_lower

    def test_has_keywords_spanish(self, title_content):
        """Debe incluir palabras clave en español."""
        assert 'palabras clave' in title_content.lower() or 'keywords' in title_content.lower()

    def test_keywords_count(self, title_content):
        """Debe tener entre 4 y 6 palabras clave."""
        # Buscar línea de keywords en español
        match = re.search(r'[Pp]alabras\s+clave.*?:\s*(.*?)$', title_content, re.MULTILINE)
        if match:
            keywords = [k.strip() for k in match.group(1).split(',') if k.strip()]
            assert 4 <= len(keywords) <= 6, f"Se encontraron {len(keywords)} keywords, se esperan 4-6"


class TestAbstract:
    """Validaciones para el abstract (paper/01-abstract.qmd)."""

    @pytest.fixture
    def abstract_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'paper', '01-abstract.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_abstract_not_placeholder(self, abstract_content):
        """El abstract no debe ser un placeholder."""
        assert '[Pendiente de redacción]' not in abstract_content
        assert '[Pending]' not in abstract_content

    def test_abstract_max_250_words(self, abstract_content):
        """El abstract en español no debe exceder 250 palabras."""
        # Extraer solo la sección en español (entre "Resumen" y "Abstract")
        parts = re.split(r'^#+\s*Abstract', abstract_content, flags=re.MULTILINE)
        resumen = parts[0] if parts else abstract_content
        word_count = count_words(resumen)
        assert word_count <= 250, f"Abstract (ES) tiene {word_count} palabras, máximo 250"

    def test_abstract_min_words(self, abstract_content):
        """El abstract debe tener contenido sustancial (mínimo 100 palabras)."""
        word_count = count_words(abstract_content)
        assert word_count >= 100, f"Abstract tiene solo {word_count} palabras, mínimo 100"

    def test_abstract_has_objective(self, abstract_content):
        """El abstract debe mencionar el objetivo del estudio."""
        content_lower = abstract_content.lower()
        objective_terms = ['objetivo', 'propósito', 'finalidad', 'busca', 'analiza', 'examina', 'evalúa', 'categoriza']
        assert any(term in content_lower for term in objective_terms), \
            "El abstract debe mencionar el objetivo del estudio"

    def test_abstract_has_methodology(self, abstract_content):
        """El abstract debe mencionar la metodología."""
        content_lower = abstract_content.lower()
        method_terms = ['metodolog', 'método', 'enfoque', 'estudio documental', 'descriptivo', 'evaluación', 'análisis']
        assert any(term in content_lower for term in method_terms), \
            "El abstract debe mencionar la metodología"

    def test_abstract_has_results(self, abstract_content):
        """El abstract debe mencionar resultados principales."""
        content_lower = abstract_content.lower()
        result_terms = ['resultado', 'hallazgo', 'encontr', 'revel', 'muestra', 'identific', 'top 5', 'cinco']
        assert any(term in content_lower for term in result_terms), \
            "El abstract debe mencionar resultados"

    def test_abstract_has_english_version(self, abstract_content):
        """Debe incluir versión en inglés del abstract."""
        assert 'abstract' in abstract_content.lower()


# --- Tests para 4.2: Introducción y Marco Teórico ---

class TestIntroduction:
    """Validaciones para la introducción (paper/02-introduction.qmd)."""

    @pytest.fixture
    def intro_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'paper', '02-introduction.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @pytest.fixture
    def bib_keys(self):
        """Extrae todas las citekeys del archivo .bib."""
        path = os.path.join(os.path.dirname(__file__), '..', 'references', 'references.bib')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return set(re.findall(r'@\w+\{([\w-]+),', content))

    def test_intro_not_placeholder(self, intro_content):
        """La introducción no debe ser un placeholder."""
        assert '[Pendiente de redacción]' not in intro_content

    def test_intro_min_words(self, intro_content):
        """La introducción debe tener contenido sustancial (mínimo 800 palabras)."""
        word_count = count_words(intro_content)
        assert word_count >= 800, f"Introducción tiene {word_count} palabras, mínimo 800"

    def test_intro_has_citations(self, intro_content):
        """La introducción debe contener citas bibliográficas."""
        citations = extract_citations(intro_content)
        assert len(citations) >= 10, f"Introducción tiene {len(citations)} citas, mínimo 10"

    def test_intro_citations_exist_in_bib(self, intro_content, bib_keys):
        """Todas las citas de la introducción deben existir en references.bib."""
        citations = extract_citations(intro_content)
        missing = [c for c in citations if c not in bib_keys]
        assert not missing, f"Citas no encontradas en .bib: {missing}"

    def test_intro_mentions_wcag_evolution(self, intro_content):
        """La introducción debe mencionar la evolución de WCAG."""
        content_lower = intro_content.lower()
        assert 'wcag' in content_lower, "Debe mencionar WCAG"
        # Debe mencionar al menos WCAG 2.1 y 2.2
        assert 'wcag 2.1' in content_lower or '2.1' in content_lower
        assert 'wcag 2.2' in content_lower or '2.2' in content_lower

    def test_intro_mentions_four_principles(self, intro_content):
        """La introducción debe mencionar los 4 principios WCAG."""
        content_lower = intro_content.lower()
        principles = ['perceptible', 'operable', 'comprensible', 'robusto']
        found = [p for p in principles if p in content_lower]
        assert len(found) >= 4, f"Solo se mencionan {len(found)}/4 principios WCAG: {found}"

    def test_intro_mentions_ai(self, intro_content):
        """La introducción debe vincular IA con accesibilidad."""
        content_lower = intro_content.lower()
        ai_terms = ['inteligencia artificial', 'ia', 'machine learning', 'aprendizaje automático',
                     'procesamiento de lenguaje natural', 'visión por computadora']
        assert any(term in content_lower for term in ai_terms), \
            "La introducción debe mencionar tecnologías de IA"

    def test_intro_has_research_question(self, intro_content):
        """La introducción debe formular pregunta de investigación o hipótesis."""
        content_lower = intro_content.lower()
        rq_terms = ['pregunta de investigación', 'hipótesis', 'objetivo general',
                     'se propone', 'este estudio busca', 'el presente estudio',
                     'objetivo de este', 'objetivo del presente']
        assert any(term in content_lower for term in rq_terms), \
            "Debe formular pregunta de investigación u objetivo"

    def test_intro_mentions_disability_types(self, intro_content):
        """La introducción debe mencionar los tipos de discapacidad evaluados."""
        content_lower = intro_content.lower()
        disabilities = ['visual', 'motora', 'cognitiva', 'auditiva']
        found = [d for d in disabilities if d in content_lower]
        assert len(found) >= 3, f"Solo se mencionan {len(found)}/4 tipos de discapacidad"

    def test_intro_defines_scope(self, intro_content):
        """La introducción debe definir el alcance del estudio."""
        content_lower = intro_content.lower()
        scope_terms = ['alcance', '41 tecnología', 'cuarenta y una', 'dataset',
                       'conjunto de datos', 'muestra']
        assert any(term in content_lower for term in scope_terms), \
            "Debe definir el alcance del estudio"


# --- Tests para 5.1: Metodología ---

class TestMethodology:
    """Validaciones para la sección de metodología (paper/03-methodology.qmd)."""

    @pytest.fixture
    def method_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'paper', '03-methodology.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @pytest.fixture
    def bib_keys(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'references', 'references.bib')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return set(re.findall(r'@\w+\{([\w-]+),', content))

    def test_methodology_not_placeholder(self, method_content):
        """La metodología no debe ser un placeholder."""
        assert '[Pendiente de redacción]' not in method_content

    def test_methodology_min_words(self, method_content):
        """La metodología debe tener contenido sustancial (mínimo 600 palabras)."""
        word_count = count_words(method_content)
        assert word_count >= 600, f"Metodología tiene {word_count} palabras, mínimo 600"

    def test_describes_study_design(self, method_content):
        """Req 2.1: Debe describir el diseño como estudio documental-descriptivo con enfoque mixto."""
        content_lower = method_content.lower()
        assert 'documental' in content_lower or 'descriptivo' in content_lower, \
            "Debe describir el diseño como estudio documental-descriptivo"
        assert 'mixto' in content_lower or 'cualitativo' in content_lower or 'cuantitativo' in content_lower, \
            "Debe mencionar el enfoque mixto (cualitativo-cuantitativo)"

    def test_describes_sample_selection(self, method_content):
        """Req 2.2: Debe detallar criterios de selección de las 41 tecnologías."""
        content_lower = method_content.lower()
        assert '41' in method_content or 'cuarenta y una' in content_lower, \
            "Debe mencionar las 41 tecnologías"
        selection_terms = ['criterio', 'selección', 'inclusión', 'exclusión', 'muestra']
        assert any(term in content_lower for term in selection_terms), \
            "Debe detallar criterios de selección"

    def test_defines_three_dimensions(self, method_content):
        """Req 2.3: Debe definir las 3 dimensiones: usabilidad, robustez y operabilidad."""
        content_lower = method_content.lower()
        dimensions = ['usabilidad', 'robustez', 'operabilidad']
        found = [d for d in dimensions if d in content_lower]
        assert len(found) == 3, f"Solo se mencionan {len(found)}/3 dimensiones: {found}"

    def test_defines_dimension_indicators(self, method_content):
        """Req 2.3: Debe definir indicadores por dimensión."""
        content_lower = method_content.lower()
        usability_indicators = ['precisión', 'sensibilidad', 'tiempo de respuesta']
        robustness_indicators = ['multidispositivo', 'multi-navegador', 'multi-os',
                                  'multiplataforma', 'navegador', 'sistema operativo']
        operability_indicators = ['navegación por teclado', 'comandos de voz',
                                   'teclado', 'voz']
        assert any(i in content_lower for i in usability_indicators), \
            "Debe definir indicadores de usabilidad"
        assert any(i in content_lower for i in robustness_indicators), \
            "Debe definir indicadores de robustez"
        assert any(i in content_lower for i in operability_indicators), \
            "Debe definir indicadores de operabilidad"

    def test_explains_evaluation_scale(self, method_content):
        """Req 2.4: Debe explicar la escala de evaluación (1-5)."""
        content_lower = method_content.lower()
        scale_terms = ['escala', 'mapeo', 'categórico', 'numérico', 'conversión',
                       'likert', 'puntuación', 'baja', 'media', 'alta']
        assert any(term in content_lower for term in scale_terms), \
            "Debe explicar la escala de evaluación"

    def test_describes_disability_categorization(self, method_content):
        """Req 2.5: Debe describir la categorización por tipo de discapacidad."""
        content_lower = method_content.lower()
        disabilities = ['visual', 'motora', 'cognitiva', 'auditiva']
        found = [d for d in disabilities if d in content_lower]
        assert len(found) >= 4, f"Solo se mencionan {len(found)}/4 tipos de discapacidad"

    def test_describes_data_source(self, method_content):
        """Req 2.6: Debe describir la fuente de datos y su estructura."""
        content_lower = method_content.lower()
        data_terms = ['dataset', 'conjunto de datos', 'base de datos', 'fuente de datos',
                      'datos', 'variables', 'registro']
        assert any(term in content_lower for term in data_terms), \
            "Debe describir la fuente de datos"

    def test_describes_weighting_method(self, method_content):
        """Debe describir el método de ponderación para el ranking."""
        content_lower = method_content.lower()
        weight_terms = ['ponder', 'peso', '0.40', '0.30', '40%', '30%', 'pesos']
        assert any(term in content_lower for term in weight_terms), \
            "Debe describir el método de ponderación"

    def test_methodology_has_citations(self, method_content):
        """La metodología debe contener citas bibliográficas."""
        citations = extract_citations(method_content)
        assert len(citations) >= 3, f"Metodología tiene {len(citations)} citas, mínimo 3"

    def test_methodology_citations_exist_in_bib(self, method_content, bib_keys):
        """Todas las citas de la metodología deben existir en references.bib."""
        citations = extract_citations(method_content)
        missing = [c for c in citations if c not in bib_keys]
        assert not missing, f"Citas no encontradas en .bib: {missing}"


# --- Tests para 5.2: Resultados ---

class TestResults:
    """Validaciones para la sección de resultados (paper/04-results.qmd)."""

    @pytest.fixture
    def results_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'paper', '04-results.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @pytest.fixture
    def bib_keys(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'references', 'references.bib')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return set(re.findall(r'@\w+\{([\w-]+),', content))

    def test_results_not_placeholder(self, results_content):
        """Los resultados no deben ser un placeholder."""
        assert '[Pendiente de redacción]' not in results_content

    def test_results_min_words(self, results_content):
        """Los resultados deben tener contenido sustancial (mínimo 800 palabras)."""
        word_count = count_words(results_content)
        assert word_count >= 800, f"Resultados tiene {word_count} palabras, mínimo 800"

    def test_presents_disability_categorization(self, results_content):
        """Req 3.1-3.2: Debe presentar la categorización por tipo de discapacidad."""
        content_lower = results_content.lower()
        disabilities = ['visual', 'motora', 'cognitiva', 'auditiva']
        found = [d for d in disabilities if d in content_lower]
        assert len(found) >= 4, f"Solo se mencionan {len(found)}/4 tipos de discapacidad"

    def test_analyzes_coverage(self, results_content):
        """Req 3.3: Debe analizar cobertura, identificando sobre y subrepresentación."""
        content_lower = results_content.lower()
        coverage_terms = ['cobertura', 'sobrerrepresent', 'subrepresent', 'brecha',
                          'mayor concentración', 'menor representación', 'predomin']
        assert any(term in content_lower for term in coverage_terms), \
            "Debe analizar la cobertura por categoría"

    def test_groups_by_product_type(self, results_content):
        """Req 3.4: Debe agrupar tecnologías por tipo de producto."""
        content_lower = results_content.lower()
        product_types = ['asistente', 'lector de pantalla', 'interfaz cerebro',
                         'seguimiento ocular', 'control de cursor', 'navegación por voz',
                         'subtitulado', 'herramienta']
        found = [p for p in product_types if p in content_lower]
        assert len(found) >= 4, f"Solo se mencionan {len(found)} tipos de producto"

    def test_presents_top5_ranking(self, results_content):
        """Req 4.2: Debe presentar las 5 mejores tecnologías con sus puntuaciones."""
        content_lower = results_content.lower()
        top5_names = ['deepseek', 'grid', 'chatgpt', 'gemini', 'google assistant']
        found = [t for t in top5_names if t in content_lower]
        assert len(found) >= 5, f"Solo se mencionan {len(found)}/5 tecnologías del top 5"

    def test_includes_top5_justification(self, results_content):
        """Req 4.3: Debe analizar por qué las top 5 sobresalen."""
        content_lower = results_content.lower()
        justification_terms = ['sobresale', 'destaca', 'puntuación', 'ventaja',
                                'superior', 'primera posición', 'lidera', 'mejor']
        assert any(term in content_lower for term in justification_terms), \
            "Debe justificar por qué las top 5 sobresalen"

    def test_references_figures(self, results_content):
        """Req 5.4: Debe referenciar figuras en el texto."""
        figure_refs = re.findall(r'@fig-', results_content)
        assert len(figure_refs) >= 3, \
            f"Debe referenciar al menos 3 figuras, encontradas {len(figure_refs)}"

    def test_references_tables(self, results_content):
        """Req 5.4: Debe referenciar tablas en el texto."""
        # Buscar referencias a tablas (Tabla N, @tbl-, Cuadro N)
        table_refs = re.findall(r'@tbl-|[Tt]abla\s+\d', results_content)
        assert len(table_refs) >= 2, \
            f"Debe referenciar al menos 2 tablas, encontradas {len(table_refs)}"

    def test_includes_descriptive_statistics(self, results_content):
        """Req 5.3: Debe presentar estadísticas descriptivas."""
        content_lower = results_content.lower()
        stat_terms = ['media', 'mediana', 'desviación estándar', 'promedio', 'sd', 'σ']
        assert any(term in content_lower for term in stat_terms), \
            "Debe presentar estadísticas descriptivas"

    def test_includes_figures_markup(self, results_content):
        """Req 5.1: Debe incluir las 3 figuras generadas."""
        figure_includes = re.findall(r'!\[.*?\]\(.*?fig-.*?\.png\)', results_content)
        assert len(figure_includes) >= 3, \
            f"Debe incluir al menos 3 figuras, encontradas {len(figure_includes)}"

    def test_includes_comparative_table(self, results_content):
        """Req 4.4/5.2: Debe incluir tabla comparativa top 5 vs promedios."""
        content_lower = results_content.lower()
        assert 'promedio' in content_lower or 'media general' in content_lower, \
            "Debe incluir comparación con promedios generales"


# --- Tests para 6.1: Discusión ---

class TestDiscussion:
    """Validaciones para la sección de discusión (paper/05-discussion.qmd)."""

    @pytest.fixture
    def discussion_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'paper', '05-discussion.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @pytest.fixture
    def bib_keys(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'references', 'references.bib')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return set(re.findall(r'@\w+\{([\w-]+),', content))

    def test_discussion_not_placeholder(self, discussion_content):
        """La discusión no debe ser un placeholder."""
        assert '[Pendiente de redacción]' not in discussion_content

    def test_discussion_min_words(self, discussion_content):
        """La discusión debe tener contenido sustancial (mínimo 800 palabras)."""
        word_count = count_words(discussion_content)
        assert word_count >= 800, f"Discusión tiene {word_count} palabras, mínimo 800"

    def test_contrasts_with_literature(self, discussion_content):
        """Req 6.1: Debe contrastar hallazgos con la literatura existente."""
        content_lower = discussion_content.lower()
        contrast_terms = ['convergencia', 'divergencia', 'coincide', 'contrasta',
                          'concuerda', 'difiere', 'confirma', 'contradice',
                          'en línea con', 'a diferencia de', 'consistente con']
        assert any(term in content_lower for term in contrast_terms), \
            "Debe contrastar hallazgos con la literatura existente"

    def test_argues_theoretical_gap(self, discussion_content):
        """Req 6.2: Debe argumentar vacío de conocimiento teórico."""
        content_lower = discussion_content.lower()
        gap_terms = ['vacío', 'brecha', 'ausencia', 'carencia', 'falta',
                     'marco conceptual', 'marco teórico', 'integración teórica',
                     'conocimiento teórico']
        assert any(term in content_lower for term in gap_terms), \
            "Debe argumentar la existencia de un vacío de conocimiento teórico"

    def test_argues_practical_gap(self, discussion_content):
        """Req 6.3: Debe argumentar vacío práctico en implementación."""
        content_lower = discussion_content.lower()
        practical_terms = ['implementación', 'práctic', 'brecha práctica',
                           'adopción', 'despliegue', 'operabilidad',
                           'vacío práctico', 'barrera']
        assert any(term in content_lower for term in practical_terms), \
            "Debe argumentar la existencia de un vacío práctico"

    def test_discusses_limitations(self, discussion_content):
        """Req 6.4: Debe discutir limitaciones del estudio."""
        content_lower = discussion_content.lower()
        limitation_terms = ['limitación', 'limitaciones', 'restricción',
                            'tamaño de muestra', 'sesgo', 'alcance limitado']
        assert any(term in content_lower for term in limitation_terms), \
            "Debe discutir las limitaciones del estudio"

    def test_proposes_future_research(self, discussion_content):
        """Req 6.5: Debe proponer líneas futuras de investigación."""
        content_lower = discussion_content.lower()
        future_terms = ['línea futura', 'investigación futura', 'futuros estudios',
                        'futuras investigaciones', 'se recomienda', 'sería deseable',
                        'queda pendiente', 'líneas de investigación']
        assert any(term in content_lower for term in future_terms), \
            "Debe proponer líneas futuras de investigación"

    def test_links_to_sdg(self, discussion_content):
        """Req 6.6: Debe vincular con ODS 10 y ODS 4."""
        content_lower = discussion_content.lower()
        assert 'ods' in content_lower or 'objetivo' in content_lower and 'desarrollo sostenible' in content_lower, \
            "Debe mencionar los Objetivos de Desarrollo Sostenible"
        sdg_terms = ['ods 10', 'ods 4', 'reducción de desigualdades',
                     'educación de calidad', 'desarrollo sostenible']
        assert any(term in content_lower for term in sdg_terms), \
            "Debe vincular con ODS 10 y/o ODS 4"

    def test_discussion_has_citations(self, discussion_content):
        """La discusión debe contener citas bibliográficas sustanciales."""
        citations = extract_citations(discussion_content)
        assert len(citations) >= 8, f"Discusión tiene {len(citations)} citas, mínimo 8"

    def test_discussion_citations_exist_in_bib(self, discussion_content, bib_keys):
        """Todas las citas de la discusión deben existir en references.bib."""
        citations = extract_citations(discussion_content)
        missing = [c for c in citations if c not in bib_keys]
        assert not missing, f"Citas no encontradas en .bib: {missing}"


# --- Tests para 6.2: Conclusiones ---

class TestConclusions:
    """Validaciones para la sección de conclusiones (paper/06-conclusion.qmd)."""

    @pytest.fixture
    def conclusion_content(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'paper', '06-conclusion.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_conclusion_not_placeholder(self, conclusion_content):
        """Las conclusiones no deben ser un placeholder."""
        assert '[Pendiente de redacción]' not in conclusion_content

    def test_conclusion_min_words(self, conclusion_content):
        """Las conclusiones deben tener contenido sustancial (mínimo 300 palabras)."""
        word_count = count_words(conclusion_content)
        assert word_count >= 300, f"Conclusiones tiene {word_count} palabras, mínimo 300"

    def test_synthesizes_main_findings(self, conclusion_content):
        """Req 6.5: Debe sintetizar los hallazgos principales."""
        content_lower = conclusion_content.lower()
        synthesis_terms = ['hallazgo', 'resultado', 'evidencia', 'muestra',
                           'revela', 'demuestra', 'confirma', 'identifica']
        assert any(term in content_lower for term in synthesis_terms), \
            "Debe sintetizar los hallazgos principales"

    def test_reaffirms_contribution(self, conclusion_content):
        """Debe reafirmar la contribución original del paper."""
        content_lower = conclusion_content.lower()
        contribution_terms = ['contribución', 'aporta', 'aporte', 'contribuye',
                              'original', 'novedoso', 'innovador', 'propuesto']
        assert any(term in content_lower for term in contribution_terms), \
            "Debe reafirmar la contribución original"

    def test_summarizes_future_research(self, conclusion_content):
        """Debe resumir líneas futuras de investigación."""
        content_lower = conclusion_content.lower()
        future_terms = ['futura', 'futuro', 'línea', 'recomendación',
                        'pendiente', 'próximo', 'investigación']
        assert any(term in content_lower for term in future_terms), \
            "Debe resumir líneas futuras de investigación"

    def test_mentions_key_technologies(self, conclusion_content):
        """Debe hacer referencia a las tecnologías clave del estudio."""
        content_lower = conclusion_content.lower()
        tech_terms = ['tecnología', 'ia', 'inteligencia artificial', 'wcag',
                      'accesibilidad']
        found = [t for t in tech_terms if t in content_lower]
        assert len(found) >= 3, \
            f"Solo se mencionan {len(found)} términos clave del estudio"


# --- Tests para 7.1: Consistencia terminológica y validación final ---

class TestTerminologicalConsistency:
    """Validaciones de consistencia terminológica del manuscrito completo (Tarea 7.1)."""

    PAPER_DIR = os.path.join(os.path.dirname(__file__), '..', 'paper')
    QMD_FILES = [
        '01-abstract.qmd', '02-introduction.qmd', '03-methodology.qmd',
        '04-results.qmd', '05-discussion.qmd', '06-conclusion.qmd',
    ]

    @pytest.fixture
    def all_content(self):
        """Lee todo el contenido del manuscrito como un solo string."""
        parts = []
        for fname in self.QMD_FILES:
            path = os.path.join(self.PAPER_DIR, fname)
            with open(path, 'r', encoding='utf-8') as f:
                parts.append(f.read())
        index_path = os.path.join(self.PAPER_DIR, '..', 'index.qmd')
        with open(index_path, 'r', encoding='utf-8') as f:
            parts.append(f.read())
        return '\n'.join(parts)

    @pytest.fixture
    def bib_keys(self):
        path = os.path.join(self.PAPER_DIR, '..', 'references', 'references.bib')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return set(re.findall(r'@\w+\{([\w-]+),', content))

    @pytest.fixture
    def included_tables(self):
        """Lee las tablas Markdown incluidas en el paper."""
        parts = []
        data_dir = os.path.join(self.PAPER_DIR, 'data')
        for fname in ['tabla-matriz-discapacidad.md', 'tabla-comparativa-top5.md']:
            path = os.path.join(data_dir, fname)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    parts.append(f.read())
        return '\n'.join(parts)

    # --- Consistencia de nombres de tecnologías ---

    def test_chatgpt_consistent_spelling(self, all_content, included_tables):
        """ChatGPT debe escribirse sin espacio en todo el manuscrito y tablas."""
        combined = all_content + '\n' + included_tables
        occurrences = re.findall(r'Chat\s+GPT', combined)
        assert len(occurrences) == 0, \
            f"'Chat GPT' (con espacio) aparece {len(occurrences)} veces. Usar 'ChatGPT'"

    def test_deepseek_consistent_spelling(self, all_content, included_tables):
        """DeepSeek debe escribirse con S mayúscula en todo el manuscrito y tablas."""
        combined = all_content + '\n' + included_tables
        wrong = re.findall(r'\bDeepseek\b', combined)
        assert len(wrong) == 0, \
            f"'Deepseek' (s minúscula) aparece {len(wrong)} veces. Usar 'DeepSeek'"

    # --- Citas vs referencias ---

    def test_all_citations_exist_in_bib(self, all_content, bib_keys):
        """Todas las citas del manuscrito deben tener entrada en references.bib."""
        citations = extract_citations(all_content)
        missing = [c for c in citations if c not in bib_keys]
        assert not missing, f"Citas sin entrada en .bib: {missing}"

    def test_no_orphan_bib_entries(self, all_content, bib_keys):
        """Advertencia: detecta entradas en .bib no citadas en el manuscrito."""
        citations = set(extract_citations(all_content))
        unused = bib_keys - citations
        # Solo advertencia, no falla (puede haber refs pendientes)
        assert len(unused) <= 5, \
            f"Hay {len(unused)} entradas en .bib no citadas: {unused}"

    # --- Figuras y tablas ---

    def test_all_figure_labels_referenced(self, all_content):
        """Todas las figuras definidas deben ser referenciadas en el texto."""
        defined = set(re.findall(r'\{#(fig-[\w-]+)\}', all_content))
        referenced = set(re.findall(r'@(fig-[\w-]+)', all_content))
        unreferenced = defined - referenced
        assert not unreferenced, \
            f"Figuras definidas pero no referenciadas: {unreferenced}"

    def test_all_table_labels_referenced(self, all_content):
        """Todas las tablas definidas deben ser referenciadas en el texto."""
        defined = set(re.findall(r'\{#(tbl-[\w-]+)\}', all_content))
        referenced = set(re.findall(r'@(tbl-[\w-]+)', all_content))
        unreferenced = defined - referenced
        assert not unreferenced, \
            f"Tablas definidas pero no referenciadas: {unreferenced}"

    def test_all_figure_refs_have_definitions(self, all_content):
        """Todas las referencias @fig- deben tener definición correspondiente."""
        defined = set(re.findall(r'\{#(fig-[\w-]+)\}', all_content))
        referenced = set(re.findall(r'@(fig-[\w-]+)', all_content))
        undefined = referenced - defined
        assert not undefined, \
            f"Referencias a figuras sin definición: {undefined}"

    def test_all_table_refs_have_definitions(self, all_content):
        """Todas las referencias @tbl- deben tener definición correspondiente."""
        defined = set(re.findall(r'\{#(tbl-[\w-]+)\}', all_content))
        referenced = set(re.findall(r'@(tbl-[\w-]+)', all_content))
        undefined = referenced - defined
        assert not undefined, \
            f"Referencias a tablas sin definición: {undefined}"

    # --- Abstract ---

    def test_spanish_abstract_max_250_words(self):
        """El abstract en español no debe exceder 250 palabras."""
        path = os.path.join(self.PAPER_DIR, '01-abstract.qmd')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        parts = re.split(r'^#+\s*Abstract', content, flags=re.MULTILINE)
        resumen = parts[0] if parts else content
        word_count = count_words(resumen)
        assert word_count <= 250, \
            f"Abstract (ES) tiene {word_count} palabras, máximo 250"

    # --- Glosario terminológico ---

    def test_wcag_version_consistent(self, all_content):
        """WCAG 2.2 debe mencionarse sin espacio pegado (no WCAG2.2)."""
        wrong_patterns = re.findall(r'WCAG2\.2', all_content)
        assert len(wrong_patterns) == 0, \
            f"Formato inconsistente de WCAG 2.2 (falta espacio): {wrong_patterns}"

    def test_dimensions_consistent_naming(self, all_content):
        """Las tres dimensiones deben nombrarse consistentemente."""
        content_lower = all_content.lower()
        assert 'usabilidad' in content_lower
        assert 'robustez' in content_lower
        assert 'operabilidad' in content_lower

    def test_disability_types_consistent(self, all_content):
        """Los tipos de discapacidad deben nombrarse consistentemente."""
        content_lower = all_content.lower()
        assert 'discapacidad visual' in content_lower or 'visual' in content_lower
        assert 'discapacidad motora' in content_lower or 'motora' in content_lower
        assert 'discapacidad cognitiva' in content_lower or 'cognitiva' in content_lower
        assert 'discapacidad auditiva' in content_lower or 'auditiva' in content_lower
