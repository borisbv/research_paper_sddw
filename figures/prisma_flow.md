# Figura 1. Diagrama de flujo PRISMA 2020

```mermaid
flowchart TD
    %% Fase de Identificación
    subgraph Identificacion [Identificación]
        A[Registros identificados en bases de datos:\nScopus (n = 412)\nWoS (n = 285)\nGoogle Scholar (n = 150)\nTotal: 847]
    end

    %% Fase de Cribado
    subgraph Cribado [Cribado]
        B[Registros tras eliminar duplicados\n(n = 644)]
        C[Registros cribados por título y resumen\n(n = 644)]
        D[Registros excluidos\n(n = 332)]
    end

    %% Fase de Elegibilidad
    subgraph Elegibilidad [Elegibilidad]
        E[Artículos a texto completo evaluados para elegibilidad\n(n = 312)]
        F[Artículos a texto completo excluidos con razones:\n- Migración tangencial (n = 84)\n- Sin perspectiva comunicativa (n = 52)\n- No peer-reviewed (n = 18)\nTotal: 154]
    end

    %% Fase de Inclusión
    subgraph Inclusion [Inclusión]
        G[Estudios incluidos en la síntesis cualitativa\n(n = 158)]
        H[Estudios adicionales identificados vía bola de nieve\n(n = 5)]
        I[Estudios totales incluidos en la revisión\n(n = 163)]
    end

    %% Conexiones
    A --> B
    B --> C
    C --> E
    C --> D
    E --> G
    E --> F
    G --> I
    H --> I
```

**Nota:** Adaptado de Page et al. (2021). El corpus final de 163 artículos constituye la base para la tipología de resignificación propuesta.
