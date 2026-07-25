/*
ULOS Genesis Identity Schema

Illustrative schema demonstrating the relationship between
identity, memory, and knowledge representation.

This file is intended for architectural discussion and
does not represent the complete production implementation.
*/

CREATE (architect:Entity {
    uuid: "genesis-001",
    type: "Architect",
    name: "Obinna",
    created_at: datetime()
})

CREATE (memory:Memory {
    uuid: "memory-001",
    tier: "HOT",
    decay_rate: 0.05,
    created_at: datetime(),
    last_accessed: datetime()
})

CREATE (topic:Concept {
    name: "Identity Persistence"
})

CREATE (architect)-[:EXPERIENCED]->(memory)

CREATE (memory)-[:RELATES_TO]->(topic)
