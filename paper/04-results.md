# Results

<!-- 
Target: 400-500 palabras
Requirements: 5.1, 5.2, 5.3, 5.4, 5.5
-->

This section presents preliminary findings from the three completed research stages. As Stages 4–6 remain in progress, the results reported here represent an empirical foundation upon which the proposed framework is being iteratively developed and refined.

## Findings from Needs Assessment (Stage 1)

Semi-structured interviews and surveys with 18 stakeholders across four categories (museum professionals, educators, accessibility advocates, and community representatives) revealed three priority clusters relevant to Research Question 1. First, participants consistently identified the need for scalable digital infrastructure capable of accommodating diverse collection types—from two-dimensional archival documents to three-dimensional sculptural objects—without requiring separate platforms for each format. Second, accessibility emerged not as a peripheral concern but as a foundational design requirement: stakeholders emphasised that inclusive access should be embedded from initial architecture decisions rather than retrofitted after development [@pereira2022; @kasemsarn2024]. Third, participants expressed a strong preference for narrative-driven experiences that contextualise objects within thematic and historical frameworks, rather than isolated catalogue entries [@lombardo2020; @hazan2021].

## Findings from Comparative Analysis (Stage 2)

The structured evaluation of twelve international virtual museum implementations against a 28-indicator rubric yielded findings directly addressing Research Question 2. Navigation approaches varied substantially: four platforms employed linear guided tours, five offered free-exploration 360° environments, and three combined both modes. Higher immersion levels (measured through XR integration complexity) did not consistently correlate with improved accessibility compliance; in fact, the three most technically immersive platforms scored lowest on WCAG 2.1 adherence. Metadata visibility presented significant variation: only four of twelve platforms exposed structured metadata to users beyond basic object labels. Community engagement features, when present, remained peripheral—limited to comment sections or social media sharing—rather than structurally integrated into the curatorial or navigational architecture [@economou2021; @arthur2026]. These patterns confirm the fragmentation identified in the literature and indicate that existing models do not systematically integrate immersion, accessibility, interoperability, and participation within a unified framework.

## Technical Framework Design Outcomes (Stage 3)

Building on Stages 1 and 2, the proposed technical architecture addresses Research Question 1 by integrating four structural layers: (a) a 3D environment layer supporting WebXR and Unity WebGL rendering for scalable immersive experiences; (b) a metadata management layer aligned with Dublin Core and IIIF specifications to ensure interoperability [@cornut2023; @lopezmenchero2021]; (c) an accessibility layer implementing WCAG 2.1 AA compliance across all interaction modes, including alternative navigation pathways, screen reader compatibility, and adjustable visual parameters [@w3c_wcag21]; and (d) a participation layer enabling community-contributed narratives and co-curated thematic pathways. This layered architecture ensures that each dimension functions independently while maintaining structural integration through shared metadata and user interaction protocols.

## Preliminary Patterns

Across the three stages, a convergent pattern emerges: effective virtual museum design requires treating immersion, accessibility, metadata standards, and community participation not as competing priorities to be balanced but as interdependent dimensions that reinforce one another when structurally integrated. This preliminary finding informs the Human-Centred Virtual Museum Framework presented in the Discussion.
