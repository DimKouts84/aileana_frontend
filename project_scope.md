# Project Scope


# Front End



## Neo4J Database Schema

### Nodes

``` CYPHER
[(:BENEFIT {name: "BENEFIT", indexes: [], constraints: []}), (:INDUSTRY {name: "INDUSTRY", indexes: [], constraints: []}), (:SKILL {name: "SKILL", indexes: [], constraints: []}), (:EXPERIENCE {name: "EXPERIENCE", indexes: [], constraints: []}), (:JOB {name: "JOB", indexes: ["embedding"], constraints: []}), (:RESPONSIBILITY {name: "RESPONSIBILITY", indexes: [], constraints: []})]
```

### Relationships

``` CYPHER
[[:NEEDS {name: "NEEDS"}], [:REQUIRES {name: "REQUIRES"}], [:HAS {name: "HAS"}], [:OFFERS {name: "OFFERS"}], [:POSTS {name: "POSTS"}]]
```

