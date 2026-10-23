# nexus-moderator-ai
Sovereign local-first AI moderation engine. While Meta pays billions to Google for Gemini to moderate its ecosystem, Nexus offers a hybrid NLP + rule-based alternative. Zero cloud, zero telemetry, fully auditable. Real-time filtering for ads, spam, and scams. Own your data.
graph LR
    A[Input Message] --> B{Length Check}
    B -->|Short| C[Quick Scan]
    B -->|Long| D[Deep NLP Analysis]
    C --> E[Rule-Based Filters]
    D --> F[ML Model]
    E --> G[Score Aggregation]
    F --> G
    G -->|Score > 0.8| H[BLOCK]
    G -->|Score > 0.5| I[REVIEW]
    G -->|Score <= 0.5| J[ALLOW]
