# Abstract {.unnumbered}

Virtual museums have evolved from static digital catalogues into immersive, interactive environments, yet research and practice in this domain remain fragmented across independent trajectories—immersive technology, user experience, accessibility, metadata standards, and community participation—without a unified framework that positions people rather than technology at the centre of design. This paper proposes the Human-Centred Virtual Museum Framework (HCVMF), a conceptual and methodological model for virtual museum design that systematically integrates these dimensions within a layered architecture. The study employs a mixed-methods approach organised in six iterative stages. Three stages have been completed: (1) a needs assessment through semi-structured interviews and surveys with 18 stakeholders across museum professionals, educators, accessibility advocates, and community representatives; (2) a comparative analysis of twelve international virtual museum implementations evaluated against a 28-indicator rubric; and (3) the design of a technical framework integrating WebXR rendering, WCAG 2.1 compliance, Dublin Core and IIIF metadata alignment, and participatory content structures. Preliminary findings reveal a convergent pattern: immersion, accessibility, metadata standards, and community participation function as interdependent rather than competing dimensions when structurally integrated from initial design decisions. The comparative analysis further indicates that higher immersion does not consistently correlate with improved accessibility, confirming the need for integrative approaches. The HCVMF constitutes the principal contribution, offering cultural institutions a transferable, replicable model adaptable to diverse collections and institutional contexts. Ongoing stages—prototype development, user testing, and iterative refinement—will provide empirical validation of the framework's effectiveness.

**Keywords:** Virtual museums, Digital cultural heritage, Human-centred design, Extended reality, Accessibility

# Introduction

Digital cultural heritage has become a central concern for museums seeking to extend their institutional reach beyond physical boundaries (Parry, 2007; Economou & Meintani, 2021). The rapid evolution of virtual museums—from static digital catalogues to immersive, interactive environments—has been accelerated by the global pandemic, which compelled institutions to adopt digital strategies as a structural necessity rather than an optional enhancement (Choi & Kim, 2021; Mason, 2022). Simultaneously, advances in 3D digitisation, extended reality (XR), and participatory design have expanded the possibilities for engaging diverse audiences with cultural collections (Zhang et al., 2024; Bruno et al., 2020; Dolcetti, 2025).

However, current research and practice in this domain have developed along largely independent trajectories. Substantial progress has been achieved in areas such as immersive technology design (Innocente et al., 2023; Carrozzino & Bergamasco, 2021), user experience evaluation (Hazan & Hermon, 2021; Pei et al., 2023), accessibility and inclusive design (Pereira & Cardoso, 2022; Kasemsarn et al., 2024), metadata standards and interoperability (Cornut et al., 2023; López-Menchero & Grande, 2021), and community participation (Arthur et al., 2026; Wang & Meng, 2024). Yet these advances remain fragmented: a comparative analysis of twelve international virtual museum implementations reveals that higher immersion does not consistently correlate with improved accessibility, metadata visibility varies widely across platforms, and community engagement features are peripheral rather than structurally integrated. To date, no widely adopted model systematically combines these dimensions within a unified, human-centred design framework.

This fragmentation constitutes an integrative opportunity. While each domain has matured independently, the absence of a coherent framework that positions people—rather than technology—at the centre of virtual museum design limits the capacity of cultural institutions to create experiences that are simultaneously immersive, accessible, interoperable, and participatory, while also responding to the cultural and gender diversity of contemporary audiences (Figure 1).

The present study addresses this gap through three research questions: (1) What design principles and technical standards are required to integrate user experience, extended reality, accessibility, and metadata interoperability in a virtual museum platform? (2) How do stakeholder needs and comparative analysis of existing models inform the configuration of a human-centred virtual museum framework? (3) To what extent can such a framework serve as a transferable model for cultural institutions with diverse collections and contexts?

The general objective is to develop and evaluate a human-centred conceptual and methodological framework for virtual museum design that integrates UX, XR, digital heritage standards, accessibility, and community engagement. Specific objectives include: (a) assessing stakeholder needs and institutional requirements through structured consultation; (b) identifying design patterns and limitations through comparative analysis of existing virtual museum models; (c) proposing a technical and conceptual architecture that systematically integrates the identified dimensions; and (d) evaluating the framework's applicability through prototype development and user testing.

The principal contribution of this research is the Human-Centred Virtual Museum Framework (HCVMF), a transferable conceptual model that articulates the relationships among immersion, accessibility, metadata standards, narrative design, and community participation. By grounding virtual museum design in people and heritage rather than in technology alone, this framework offers cultural institutions a replicable approach adaptable to diverse collections and institutional contexts.

# State of the Art

## Virtual Museums and Digital Heritage

The concept of the virtual museum has evolved considerably over the past decade, moving from static digital catalogues to immersive, interactive environments that extend institutional reach beyond physical walls (Parry, 2007; Economou & Meintani, 2021). Recent bibliometric analyses reveal a sustained growth in research connecting immersive technologies with museum exhibition design, with particular emphasis on visitor engagement and experiential quality (Li et al., 2023). This evolution has been further accelerated by the COVID-19 pandemic, which compelled museums worldwide to adopt digital strategies as a necessity rather than an option (Choi & Kim, 2021; Mason, 2022). In this post-pandemic context, Song and Evans (2024) propose a phenomenological reconceptualisation of museums through extended reality, arguing that digital objects constitute a new category of museum artefact that challenges traditional curatorial paradigms.

Parallel advances in digitisation technologies have expanded the possibilities for heritage documentation. Systematic reviews confirm that 3D scanning, photogrammetry, and motion capture have become fundamental tools for preserving both tangible and intangible cultural heritage (Skublewska-Paszkowska et al., 2022; Bruno et al., 2020; Guidi & Rodríguez-Gonzálvez, 2022). However, as Storeide et al. (2023) observe in their review of 45 institutional projects, significant limitations persist in the standardisation of 3D workflows, creating barriers to interoperability and long-term preservation. Nikolaou (2024) further identifies organisational and technical challenges that continue to hinder the digital transformation of museum backstage operations, suggesting that institutional capacity remains a critical bottleneck.

## User Experience and Human-Centred Design

User experience evaluation has emerged as a central concern in virtual museum research. Hazan and Hermon (2021) established a methodological framework for assessing meaningful engagement in virtual environments, while Pei et al. (2023) applied these principles empirically to VR interfaces in digital museums. The evidence consistently indicates that visitor satisfaction depends not on technological sophistication alone but on interaction design aligned with user expectations (Li et al., 2023; Hazan & Hermon, 2021; Pei et al., 2023).

Human-centred design (HCD) approaches have gained increasing traction in the cultural heritage sector. Mason and Vavoula (2021) proposed a conceptual framework positioning user needs at the centre of digital heritage design. Co-design methodologies involving heritage professionals and local communities have demonstrated value in creating more meaningful digital experiences (Koutsabasis et al., 2022), and Dolcetti (2025) has argued for embedding participatory design directly into heritage practice. These approaches represent a shift from technology-driven to people-driven development, though their systematic integration into virtual museum design remains limited.

## Extended Reality in Cultural Institutions

Extended reality (XR) technologies—encompassing virtual, augmented, and mixed reality—have been applied with growing frequency in cultural institutions. Zhang et al. (2024) document the rapid expansion of immersive technology applications in cultural heritage, identifying user engagement and preservation as primary research themes. Innocente et al. (2023) distinguish between immersive experiences designed for on-site enrichment and those intended for remote access, while Carrozzino and Bergamasco (2021) demonstrate that immersive VR can complement rather than replace physical museum visits. Nevertheless, a recurring finding is the tension between immersive depth and accessibility: as technological complexity increases, barriers to access for diverse user populations tend to multiply.

## Accessibility, Inclusive Design, and Community Engagement

The intersection of accessibility and digital heritage has received growing scholarly attention. Pereira and Cardoso (2022) identify persistent challenges in making virtual museums accessible to users with diverse abilities, noting that compliance with web accessibility guidelines (World Wide Web Consortium, 2018) remains inconsistent across cultural platforms. Kasemsarn et al. (2024; 2023) advance this discussion by proposing frameworks that integrate inclusive design principles with digital storytelling, demonstrating that accessibility and narrative quality need not be competing priorities. Nappi et al. (2024) contribute models for organising cultural heritage knowledge through accessible and adaptive narratives, emphasising that digital systems should accommodate diverse cognitive and sensory profiles.

Metadata standards and interoperability constitute another area where independent progress has been substantial yet fragmented. López-Menchero and Grande (2021) reviewed interoperability frameworks for digital heritage, while Cornut et al. (2023) demonstrated the application of Linked Open Usable Data and IIIF standards to image archives, revealing both the potential and the complexity of semantic interoperability in cultural collections. These developments remain largely disconnected from the user experience and accessibility considerations discussed above.

Community participation in digital heritage has similarly evolved from passive consumption toward active engagement. Simon's (2010) foundational work on the participatory museum has been extended by recent research examining crowdsourcing and community co-creation in digital contexts (Arthur et al., 2026). Wang and Meng (2024) propose a model connecting museum digitalisation with visitors' cognitive identity and public engagement, suggesting that meaningful participation requires addressing not only technological interfaces but also cultural symbolism and identity formation. Lombardo and Damiano (2020) further argue that narrative-based approaches can bridge the gap between curatorial intent and visitor agency, though integrated frameworks remain rare.

## Comparative Analysis of Existing Models

A comparative analysis of twelve virtual museum implementations—including exhibitions by the Smithsonian Institution, the British Museum, the Van Gogh Museum, the National Gallery, the Art Institute of Chicago, the Hermitage Museum, and the Dalí Museum—reveals patterns that underscore the current fragmentation. Navigation approaches range from linear slideshows to free-exploration 360° environments, reflecting an unresolved tension between curatorial guidance and visitor autonomy. Higher immersion does not consistently correlate with improved accessibility; none of the twelve cases offers comprehensive embedded accessibility features. Multimedia integration enhances engagement but demands significant production resources, metadata visibility varies widely, and community participation features remain peripheral rather than structurally integrated.

These findings reveal that while significant advances have been made independently in immersion, digitisation, narrative design, accessibility, metadata standards, and community engagement, no widely adopted model systematically integrates these dimensions within a unified, human-centred framework that also accounts for the cultural and gender diversity of contemporary museum audiences. This integrative opportunity—rather than a deficit in any single domain—defines the research gap that the present study addresses.

# Methodology

This study adopts a mixed-methods research design combining qualitative and quantitative approaches to address the multidimensional nature of virtual museum development (Creswell & Creswell, 2018; Mason & Vavoula, 2021). The integration of methods is justified by the need to capture both subjective stakeholder experiences and measurable usability outcomes within a single coherent framework. The research follows a sequential exploratory strategy in which qualitative findings from early stages inform the design parameters of subsequent stages (Dolcetti, 2025).

## Research Design

The methodology comprises six iterative stages organised within a human-centred design cycle (Figure 2):

**Stage 1 — Needs Assessment (completed).** Semi-structured interviews and surveys were conducted with museum professionals (curators, archivists, educators, IT staff) and community stakeholders (educators, visitors, accessibility advocates) to identify institutional priorities, technical constraints, and desired user experiences. Purposive sampling ensured representation of diverse functional roles, cultural backgrounds, and gender perspectives (n=18 participants across four stakeholder categories, achieving thematic saturation as confirmed by redundancy in final interviews). Interview protocols addressed preservation priorities, audience expectations, accessibility requirements, and resource constraints.

**Stage 2 — Comparative Analysis (completed).** A structured evaluation of twelve international virtual museum implementations was conducted, including the Smithsonian Institution, British Museum, Van Gogh Museum, Google Arts & Culture, and eight additional platforms. Analysis criteria encompassed navigation design, immersion levels, accessibility compliance, metadata visibility, community engagement features, and educational integration (Hazan & Hermon, 2021; Economou & Meintani, 2021). Each platform was assessed against a 28-indicator rubric derived from WCAG 2.1 guidelines, IIIF standards, and UX heuristics.

**Stage 3 — Technical Framework Design (completed).** Based on findings from Stages 1 and 2, a conceptual and technical architecture was proposed integrating: 3D gallery environments (WebXR/Unity WebGL), high-resolution imaging pipelines, metadata management aligned with Dublin Core and IIIF specifications, and accessibility features compliant with WCAG 2.1 AA standards (Cornut et al., 2023; López-Menchero & Grande, 2021; World Wide Web Consortium, 2018).

**Stage 4 — Prototype Development (in progress).** A functional prototype featuring a curated selection from an archival collection is under development, incorporating interactive elements (zoomable imagery, audio narration, thematic navigation pathways) within an accessible 3D environment.

**Stage 5 — User Testing (planned).** Usability testing will recruit participants from educational institutions, community organisations, and general audiences (target n=45) to evaluate engagement, navigation efficiency, accessibility, and learning outcomes through mixed instruments (task completion metrics, System Usability Scale, semi-structured debriefing).

**Stage 6 — Evaluation and Refinement (planned).** Qualitative feedback and quantitative analytics will be triangulated to refine the implementation strategy and validate the proposed framework's transferability.

## Data Analysis

Qualitative data from interviews and open-ended responses are analysed through thematic analysis following Braun and Clarke's six-phase protocol (Braun & Clarke, 2006). Quantitative data from surveys, usability metrics, and comparative indicators are processed through descriptive statistics and cross-case pattern analysis. Triangulation across data sources ensures analytical rigour.

## Research Team

The project is developed through an interdisciplinary collaboration involving researchers in architecture and digital design, user experience specialists, heritage professionals, and educational technology experts (Figure 3). This composition ensures that technical, curatorial, pedagogical, and accessibility perspectives are structurally integrated into the research process rather than addressed as secondary considerations (Koutsabasis et al., 2022).

## Ethical Considerations

The study protocol addresses informed consent for all participants, data anonymisation procedures, and institutional review compliance. Accessibility, inclusive representation, and sensitivity to cultural and gender diversity are embedded as design principles throughout the research cycle, ensuring that the methodology itself models the human-centred values it seeks to evaluate (Kasemsarn et al., 2024; Pereira & Cardoso, 2022).

# Results

This section presents preliminary findings from the three completed research stages. As Stages 4–6 remain in progress, the results reported here represent an empirical foundation upon which the proposed framework is being iteratively developed and refined.

## Findings from Needs Assessment (Stage 1)

Semi-structured interviews and surveys with 18 stakeholders across four categories (museum professionals, educators, accessibility advocates, and community representatives) revealed three priority clusters relevant to Research Question 1. First, participants consistently identified the need for scalable digital infrastructure capable of accommodating diverse collection types—from two-dimensional archival documents to three-dimensional sculptural objects—without requiring separate platforms for each format. Second, accessibility emerged not as a peripheral concern but as a foundational design requirement: stakeholders emphasised that inclusive access should be embedded from initial architecture decisions rather than retrofitted after development (Pereira & Cardoso, 2022; Kasemsarn et al., 2024). Third, participants expressed a strong preference for narrative-driven experiences that contextualise objects within thematic and historical frameworks, rather than isolated catalogue entries (Lombardo & Damiano, 2020; Hazan & Hermon, 2021).

## Findings from Comparative Analysis (Stage 2)

The structured evaluation of twelve international virtual museum implementations against a 28-indicator rubric yielded findings directly addressing Research Question 2. Navigation approaches varied substantially: four platforms employed linear guided tours, five offered free-exploration 360° environments, and three combined both modes. Higher immersion levels (measured through XR integration complexity) did not consistently correlate with improved accessibility compliance; in fact, the three most technically immersive platforms scored lowest on WCAG 2.1 adherence. Metadata visibility presented significant variation: only four of twelve platforms exposed structured metadata to users beyond basic object labels. Community engagement features, when present, remained peripheral—limited to comment sections or social media sharing—rather than structurally integrated into the curatorial or navigational architecture (Economou & Meintani, 2021; Arthur et al., 2026). These patterns confirm the fragmentation identified in the literature and indicate that existing models do not systematically integrate immersion, accessibility, interoperability, and participation within a unified framework.

## Technical Framework Design Outcomes (Stage 3)

Building on Stages 1 and 2, the proposed technical architecture addresses Research Question 1 by integrating four structural layers: (a) a 3D environment layer supporting WebXR and Unity WebGL rendering for scalable immersive experiences; (b) a metadata management layer aligned with Dublin Core and IIIF specifications to ensure interoperability (Cornut et al., 2023; López-Menchero & Grande, 2021); (c) an accessibility layer implementing WCAG 2.1 AA compliance across all interaction modes, including alternative navigation pathways, screen reader compatibility, and adjustable visual parameters (World Wide Web Consortium, 2018); and (d) a participation layer enabling community-contributed narratives and co-curated thematic pathways. This layered architecture ensures that each dimension functions independently while maintaining structural integration through shared metadata and user interaction protocols.

## Preliminary Patterns

Across the three stages, a convergent pattern emerges: effective virtual museum design requires treating immersion, accessibility, metadata standards, and community participation not as competing priorities to be balanced but as interdependent dimensions that reinforce one another when structurally integrated. This preliminary finding informs the Human-Centred Virtual Museum Framework presented in the Discussion.

# Discussion

## Interpretation of Preliminary Findings

The convergent pattern identified across the three completed stages—that immersion, accessibility, metadata standards, and community participation function as interdependent rather than competing dimensions—challenges the implicit assumption underlying much current practice. The comparative analysis revealed that platforms prioritising technological sophistication tend to score lower on accessibility compliance, a finding consistent with the tension between immersive depth and inclusive access documented by Innocente et al. (2023) and Pereira and Cardoso (2022). However, the needs assessment suggests this tension is not inherent but rather a consequence of design approaches that treat these dimensions sequentially rather than integratively. Stakeholders consistently articulated accessibility as a foundational requirement rather than a supplementary feature, aligning with the inclusive design frameworks proposed by Kasemsarn et al. (2024; 2023).

The finding that narrative-driven experiences were preferred over catalogue-based navigation extends the work of Lombardo and Damiano (2020) and Hazan and Hermon (2021) by situating narrative design within a broader architectural framework. While previous research has demonstrated the value of storytelling in cultural heritage contexts, the present study indicates that narrative structures can serve as an integrative mechanism connecting curatorial intent, visitor agency, and community participation within a single interaction model.

## The Human-Centred Virtual Museum Framework

These findings inform the proposed Human-Centred Virtual Museum Framework (HCVMF), which constitutes the principal contribution of this research (Figure 4). The HCVMF articulates virtual museum design as the structured integration of four interdependent layers: (a) an immersive environment layer providing scalable XR experiences adaptable to diverse technological capacities (Zhang et al., 2024; Carrozzino & Bergamasco, 2021); (b) an accessibility and inclusive design layer embedding WCAG 2.1 compliance and Universal Design principles from initial architecture decisions (World Wide Web Consortium, 2018; Pereira & Cardoso, 2022); (c) a metadata and interoperability layer ensuring semantic coherence through Dublin Core and IIIF alignment (Cornut et al., 2023; López-Menchero & Grande, 2021); and (d) a participation and narrative layer enabling community-contributed content and co-curated thematic pathways (Arthur et al., 2026; Wang & Meng, 2024).

The framework's distinguishing characteristic is that it positions people and heritage—rather than technology—at its structural centre, drawing on human-centred design principles (Mason & Vavoula, 2021; Dolcetti, 2025). Each layer operates independently yet maintains structural integration through shared metadata protocols and user interaction pathways, ensuring that enhancements in one dimension do not compromise performance in others.

## Limitations

Several limitations should be acknowledged. First, the framework is grounded in preliminary findings from three of six planned stages; validation through prototype testing and user evaluation (Stages 4–6) remains necessary. Second, the comparative analysis, while encompassing twelve international platforms, does not claim exhaustive coverage of the field. Third, the transferability of the HCVMF to institutions with substantially different resource capacities and collection types requires empirical verification beyond the current case study.

## Implications

Despite these limitations, the HCVMF offers a replicable conceptual architecture for cultural institutions seeking to develop virtual museums that are simultaneously immersive, accessible, interoperable, and participatory. Future research should prioritise empirical validation through user testing across diverse populations—attending to gender, age, ability, and cultural background—longitudinal assessment of community engagement outcomes, and exploration of the framework's adaptability to institutions operating in varied cultural, technological, and socioeconomic contexts (Koutsabasis et al., 2022; Economou & Meintani, 2021).

# Conclusions

This research addressed the integrative challenge of virtual museum design through three interrelated questions. Regarding the first—what design principles and technical standards are required to integrate UX, XR, accessibility, and metadata interoperability—the study indicates that a layered architecture combining WebXR rendering, WCAG 2.1 compliance, Dublin Core and IIIF alignment, and participatory content structures can function as interdependent rather than competing dimensions when embedded from initial design decisions. The second question—how stakeholder needs and comparative analysis inform a human-centred framework—is answered through the convergent findings from needs assessment and the twelve-platform evaluation: accessibility must be foundational rather than supplementary, narrative-driven interaction models serve as integrative mechanisms, and community engagement requires structural rather than peripheral implementation. The third question—regarding transferability—remains partially addressed; preliminary architectural decisions support adaptability to diverse institutional contexts, though empirical validation through Stages 4–6 is necessary.

The principal contribution is the Human-Centred Virtual Museum Framework (HCVMF), a conceptual model that positions people and heritage at the structural centre of virtual museum design. By articulating the relationships among immersion, accessibility, metadata standards, narrative design, and community participation as structurally integrated layers, the HCVMF offers cultural institutions a replicable approach adaptable to collections of varying scale and nature (Figure 5).

Future applications of this framework extend beyond the current case study. The layered architecture and human-centred principles are designed to be transferable to institutions operating in diverse cultural, technological, and resource contexts. Ongoing work in Stages 4–6—prototype development, user testing, and iterative refinement—will provide empirical evidence regarding the framework's effectiveness and adaptability across different institutional environments.

# References

Arthur, P. L., Hearn, L., & Smith, I. (2026). Reviewing crowdsourcing and community engagement in museums. *Publications*, *14*(1), 6. https://doi.org/10.3390/publications14010006

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, *3*(2), 77–101. https://doi.org/10.1191/1478088706qp063oa

Bruno, F., Lagudi, A., Barbieri, L., & Cozza, M. (2020). 3D digitization and visualization in cultural heritage: A review. *Digital Applications in Archaeology and Cultural Heritage*, *18*, e00162. https://doi.org/10.1016/j.daach.2020.e00162

Carrozzino, M., & Bergamasco, M. (2021). Beyond virtual museums: Experiencing immersive virtual reality in real museums. *Journal of Cultural Heritage*, *49*, 1–12. https://doi.org/10.1016/j.culher.2021.03.004

Choi, B., & Kim, J. (2021). Changes and challenges in museum management after the COVID-19 pandemic. *Journal of Open Innovation: Technology, Market, and Complexity*, *7*(2), 148. https://doi.org/10.3390/joitmc7020148

Cornut, M., Raemy, J. A., & Spiess, F. (2023). Annotations as knowledge practices in image archives: Application of Linked Open Usable Data and machine learning. *Journal on Computing and Cultural Heritage*, *16*(4), 1–19. https://doi.org/10.1145/3625301

Creswell, J. W., & Creswell, J. D. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE Publications.

Dolcetti, F. (2025). Crafting digital experiences: Embedding human-centred and participatory design into archaeological practice. *Journal on Computing and Cultural Heritage*, *18*(1). https://doi.org/10.1145/3700880

Economou, M., & Meintani, E. (2021). Promoting heritage through virtual museums: A systematic review. *Curator: The Museum Journal*, *64*(3), 471–490. https://doi.org/10.1111/cura.12421

Guidi, G., & Rodríguez-Gonzálvez, P. (2022). 3D scanning and photogrammetry for cultural heritage documentation: A review of recent applications. *Remote Sensing*, *14*(3), 715. https://doi.org/10.3390/rs14030715

Hazan, S., & Hermon, S. (2021). Evaluating user experience in virtual museums: A methodological framework. *Digital Scholarship in the Humanities*, *36*(4), 1002–1018. https://doi.org/10.1093/llc/fqab020

Innocente, C., Ulrich, L., Moos, S., & Vezzetti, E. (2023). A framework study on the use of immersive XR technologies in the cultural heritage domain. *Journal of Cultural Heritage*, *62*, 268–283. https://doi.org/10.1016/j.culher.2023.06.001

Kasemsarn, K., Harrison, D., & Nickpour, F. (2023). Applying inclusive design and digital storytelling to facilitate cultural tourism: A review and initial framework. *Heritage*, *6*(2), 1411–1428. https://doi.org/10.3390/heritage6020077

Kasemsarn, K., Sawadsri, A., Harrison, D., & Nickpour, F. (2024). Museums for older adults and mobility-impaired people: Applying inclusive design principles and digital storytelling guidelines—A review. *Heritage*, *7*(4), 1893–1916. https://doi.org/10.3390/heritage7040090

Koutsabasis, P., Partheniadis, K., Gardeli, A., & Vogiatzidakis, P. (2022). Co-designing the user experience of location-based games for a network of museums: Involving cultural heritage professionals and local communities. *Multimodal Technologies and Interaction*, *6*(5), 36. https://doi.org/10.3390/mti6050036

Li, J., Wider, W., Ochiai, Y., & Fauzi, M. A. (2023). A bibliometric analysis of immersive technology in museum exhibitions: Exploring user experience. *Frontiers in Virtual Reality*, *4*, 1240562. https://doi.org/10.3389/frvir.2023.1240562

Lombardo, V., & Damiano, R. (2020). Storytelling for cultural heritage: Toward a model for narrative-based virtual museum experiences. *Information*, *11*(3), 154. https://doi.org/10.3390/info11030154

López-Menchero Bendicho, V. M., & Grande, A. (2021). Digital heritage and metadata standards: A review of interoperability frameworks. *Heritage*, *4*(3), 2143–2160. https://doi.org/10.3390/heritage4030120

Mason, M. (2022). The contribution of design thinking to museum digital transformation in post-pandemic times. *Multimodal Technologies and Interaction*, *6*(9), 79. https://doi.org/10.3390/mti6090079

Mason, M., & Vavoula, G. (2021). Digital cultural heritage design practice: A conceptual framework. *The Design Journal*, *24*(3), 405–424. https://doi.org/10.1080/14606925.2021.1889738

Nappi, M. L., Buono, M., & Chivarán, C. (2024). Models and tools for the digital organisation of knowledge: Accessible and adaptive narratives for cultural heritage. *Heritage Science*, *12*, 112. https://doi.org/10.1186/s40494-024-01219-z

Nikolaou, P. (2024). Museums and the post-digital: Revisiting challenges in the digital transformation of museums. *Heritage*, *7*(3), 1784–1800. https://doi.org/10.3390/heritage7030084

Parry, R. (2007). *Recoding the museum: Digital heritage and the technologies of change*. Routledge.

Pei, X., Fu, S., & Jiang, T. (2023). An empirical study on user experience evaluation of VR interface in digital museums. *Data and Information Management*, *7*(4), 100057. https://doi.org/10.1016/j.dim.2023.100057

Pereira, A. M., & Cardoso, J. C. S. (2022). Inclusive virtual museums: Accessibility challenges and opportunities. *Universal Access in the Information Society*, *21*(4), 1023–1037. https://doi.org/10.1007/s10209-021-00830-4

Simon, N. (2010). *The participatory museum*. Museum 2.0.

Skublewska-Paszkowska, M., Milosz, M., Powroznik, P., & Lukasik, E. (2022). 3D technologies for intangible cultural heritage preservation—literature review for selected databases. *Heritage Science*, *10*, 3. https://doi.org/10.1186/s40494-021-00633-x

Song, Z., & Evans, L. (2024). The museum of digital things: Extended reality and museum practices. *Frontiers in Virtual Reality*, *5*, 1396280. https://doi.org/10.3389/frvir.2024.1396280

Storeide, M. S. B., George, S., Sole, A., & Hardeberg, J. Y. (2023). Standardization of digitized heritage: A review of implementations of 3D in cultural heritage. *Heritage Science*, *11*, 249. https://doi.org/10.1186/s40494-023-01079-z

Wang, Z., & Meng, J. (2024). Dialogues with cultural heritage via museum digitalisation: Developing a model of visitors' cognitive identity, technological agent, cultural symbolism, and public engagement. *Museum Management and Curatorship*, *39*(6), 810–833. https://doi.org/10.1080/09647775.2023.2269164

World Wide Web Consortium. (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*. https://www.w3.org/TR/WCAG21/

Zhang, J., Ahmad, W., & Sanmugam, M. (2024). The impact of immersive technologies on cultural heritage: A bibliometric study of VR, AR, and MR applications. *Sustainability*, *16*(15), 6446. https://doi.org/10.3390/su16156446
