# Legacy Mission Control — Prompt Sheet Import Template

This document defines the exact syntax for creating prompt sheets that can be imported into the Legacy Mission Control Prompt Library.

Any file following these rules can be merged in one step.

---

## File Format

Save your prompt sheet as a TypeScript file named `data.ts` with this exact structure:

```typescript
export type Category = 'Agent Engineering' | 'SaaS Ops' | "The Chef's Logic" | 'Growth Marketing' | 'Vibe Coding' | 'YOUR NEW CATEGORY';

export interface Prompt {
  id: number;
  category: Category;
  title: string;
  contract: string;
  matrix: string[];
  content: string;
}

export const prompts: Prompt[] = [
  // Your prompts here
];
```

The importer reads the `prompts` array from this file. The `Category` type and `Prompt` interface are for your IDE's type checking — they help you catch errors before import.

---

## Field Reference

Every prompt object has exactly 6 fields. No extra fields. No missing fields.

```
┌────────────┬───────────┬────────────────────────────────────────────────────┐
│ Field      │ Type      │ Rules                                             │
├────────────┼───────────┼────────────────────────────────────────────────────┤
│ id         │ number    │ Unique integer. Sequential from last ID in library.│
│ category   │ string    │ Exact category name (see Category Rules below).   │
│ title      │ string    │ 3-12 words. Specific. No generic filler.          │
│ contract   │ string    │ 1-2 sentences. Input → Output with constraints.   │
│ matrix     │ string[]  │ Exactly 3 checklist items. Each under 60 chars.   │
│ content    │ string    │ The full prompt text. 100-800 words.              │
└────────────┴───────────┴────────────────────────────────────────────────────┘
```

---

## Category Rules

### Existing Categories (use exact spelling)

These 5 categories already exist in the library. Use these strings exactly:

```
Agent Engineering
SaaS Ops
The Chef's Logic
Growth Marketing
Vibe Coding
```

### Creating a New Category

To create a new category, simply use the new category name in your prompt objects. The importer will:

1. Detect any category not in the existing set
2. Auto-create the category at import time
3. Assign it a color from the reserved palette
4. Add it to the filter bar automatically

**New category names must:**
- Be 2-4 words
- Use Title Case
- Not contain special characters (no hyphens, slashes, pipes)
- Not duplicate an existing category with different casing

**Example — adding a new "Data Engineering" category:**

```typescript
{
  id: 401,
  category: "Data Engineering",
  title: "Pipeline Orchestrator",
  contract: "Input: data sources and transformation requirements. Output: complete pipeline DAG with validation gates.",
  matrix: [
    "Map source-to-target transformations",
    "Define validation checkpoints per stage",
    "Design failure recovery and retry logic"
  ],
  content: "You are a Pipeline Orchestrator..."
}
```

---

## ID Numbering

```
┌─────────────────────────────────────┬────────────────┐
│ Scenario                            │ ID Range       │
├─────────────────────────────────────┼────────────────┤
│ Library already has IDs 1-400       │ Start at 401   │
│ You are the first batch             │ Start at 1     │
│ Adding to a batch you just imported │ Continue count │
└─────────────────────────────────────┴────────────────┘
```

IDs must be:
- Unique integers across the entire library
- Sequential within your batch (no gaps)
- Never reuse a deleted ID

Check the current max ID in the library before assigning IDs.

---

## Field-by-Field Examples

### id

```typescript
// ✅ Correct
id: 401

// ❌ Wrong — string instead of number
id: "401"

// ❌ Wrong — duplicate of existing
id: 1
```

### category

```typescript
// ✅ Correct — existing category, exact spelling
category: "Agent Engineering"

// ✅ Correct — new category (will be auto-created)
category: "Data Engineering"

// ❌ Wrong — wrong casing
category: "agent engineering"

// ❌ Wrong — abbreviated
category: "SaaS"

// ❌ Wrong — has special characters
category: "DevOps / Infra"
```

### title

```typescript
// ✅ Correct — specific, actionable
title: "Circuit Breaker Configurator"

// ✅ Correct — scope + purpose
title: "Agent Memory Eviction Planner"

// ❌ Wrong — too vague
title: "Helper Prompt"

// ❌ Wrong — too long
title: "A Comprehensive Guide to Building Agent Systems"

// ❌ Wrong — placeholder
title: "TBD"
```

### contract

```typescript
// ✅ Correct — Input/Output with constraint
contract: "Input: API schema and auth requirements. Output: Complete endpoint implementation with error handling and rate limiting."

// ✅ Correct — strict summary
contract: "Given a task description and available agent roles, produce a complete swarm configuration with routing rules, parallel execution paths, and a merge strategy."

// ❌ Wrong — too vague
contract: "Build something cool."

// ❌ Wrong — just a description, no contract
contract: "This prompt helps with agents."

// ❌ Wrong — empty
contract: ""
```

### matrix

```typescript
// ✅ Correct — exactly 3 actionable checklist items
matrix: [
  "Define each agent's role and output schema",
  "Map dependency graph between agents",
  "Specify merge logic for final output"
]

// ❌ Wrong — not 3 items
matrix: [
  "Do the thing"
]

// ❌ Wrong — too long
matrix: [
  "First you need to understand the entire system architecture and then map all the components to their respective agent roles before proceeding"
]

// ❌ Wrong — vague
matrix: [
  "Think about it",
  "Do it",
  "Check it"
]
```

### content

```typescript
// ✅ Correct — clear role, inputs, steps, output format
content: "You are a Deployment Pipeline Builder. Given a service and deployment target, produce a complete CI/CD pipeline.\n\nService: [SERVICE]\nTarget: [ENVIRONMENT]\n\nProduce:\n1. BUILD STAGE — Compile, lint, unit test.\n2. SECURITY SCAN — Dependency audit, SAST.\n3. DEPLOY — Staging first, then production with canary.\n4. VERIFICATION — Smoke tests, health checks.\n5. ROLLBACK — Trigger conditions and procedure.\n\nDo not ask follow-up questions unless a required input is missing. State assumptions explicitly."

// ❌ Wrong — too short, no structure
content: "Build a pipeline."

// ❌ Wrong — placeholder
content: "[INSERT PROMPT HERE]"
```

---

## Complete Example — 3 Prompts with 1 New Category

```typescript
export type Category = 'Agent Engineering' | 'SaaS Ops' | "The Chef's Logic" | 'Growth Marketing' | 'Vibe Coding' | 'Data Engineering';

export interface Prompt {
  id: number;
  category: Category;
  title: string;
  contract: string;
  matrix: string[];
  content: string;
}

export const prompts: Prompt[] = [
  {
    "id": 401,
    "category": "Data Engineering",
    "title": "ETL Pipeline Designer",
    "contract": "Input: source systems and target schema. Output: complete ETL pipeline with transformation steps, validation gates, and error handling.",
    "matrix": [
      "Map source fields to target schema",
      "Define transformation logic per field",
      "Design validation and rejection handling"
    ],
    "content": "You are an ETL Pipeline Designer. Given source systems and a target data schema, design a complete extract-transform-load pipeline.\n\nSource Systems: [SOURCES]\nTarget Schema: [SCHEMA]\n\nDesign:\n1. EXTRACTION — For each source: connection method, query frequency, incremental vs. full load, error handling.\n2. TRANSFORMATION — Field mapping table. Type conversions. Business logic rules. Derived fields.\n3. LOADING — Target write strategy (upsert, append, overwrite). Batch size. Transaction boundaries.\n4. VALIDATION — Row count checks. Null percentage thresholds. Referential integrity.\n5. MONITORING — Success/failure alerts. Data freshness SLA. Pipeline runtime tracking.\n6. RECOVERY — Idempotent re-run design. Point-in-time restart capability.\n\nDo not ask follow-up questions unless a required input is missing. Return a completion matrix."
  },
  {
    "id": 402,
    "category": "Data Engineering",
    "title": "Data Quality Gate Builder",
    "contract": "Input: dataset and quality rules. Output: automated quality gate with pass/fail criteria, quarantine logic, and alerting.",
    "matrix": [
      "Define quality rules per field",
      "Implement pass/fail threshold logic",
      "Design quarantine and alert routing"
    ],
    "content": "You are a Data Quality Gate Builder. Create an automated quality gate for a data pipeline.\n\nDataset: [DATASET]\nQuality Rules: [RULES]\n\nBuild:\n1. RULE ENGINE — For each quality rule: check type (range, format, uniqueness, referential), severity (block, warn), remediation.\n2. EXECUTION — When to run: pre-load, post-load, scheduled. Batch vs. streaming.\n3. THRESHOLDS — Pass/fail criteria per rule. Aggregated quality score calculation.\n4. QUARANTINE — Where failed records go. Schema. Retention. Review workflow.\n5. ALERTING — Who gets notified when. Severity escalation rules.\n6. DASHBOARD — Quality score trends. Top failing rules. Volume metrics.\n\nDo not ask follow-up questions unless a required input is missing. Return a completion matrix."
  },
  {
    "id": 403,
    "category": "SaaS Ops",
    "title": "Database Index Optimizer",
    "contract": "Input: slow query log and table schemas. Output: index recommendations with estimated impact, creation SQL, and rollback plan.",
    "matrix": [
      "Analyze slow queries for index opportunities",
      "Estimate impact and rank by priority",
      "Generate safe creation and rollback SQL"
    ],
    "content": "You are a Database Index Optimizer. Analyze slow queries and produce actionable index recommendations.\n\nSlow Queries: [QUERIES]\nTable Schemas: [SCHEMAS]\nDatabase: PostgreSQL\n\nAnalyze:\n1. QUERY ANALYSIS — For each slow query: current execution plan, bottleneck (seq scan, nested loop, sort), estimated rows vs. actual.\n2. INDEX CANDIDATES — Proposed indexes with: columns, type (btree, hash, gin, gist), supporting queries, estimated cost improvement.\n3. PRIORITY RANKING — By impact (estimated speedup) divided by cost (write overhead, disk space).\n4. CREATION SQL — CREATE INDEX CONCURRENTLY statements. Safe for production. No table locks.\n5. ROLLBACK — DROP INDEX statements for each recommendation.\n6. VERIFICATION — Queries to run before and after to measure actual improvement.\n\nDo not ask follow-up questions unless a required input is missing. Return a completion matrix."
  }
];
```

---

## Validation Checklist

Before submitting your prompt sheet, verify every item:

```
┌─────┬───────────────────────────────────────────────────────┐
│  #  │ Check                                                 │
├─────┼───────────────────────────────────────────────────────┤
│  1  │ File is named data.ts                                 │
│  2  │ File exports prompts as a typed array                  │
│  3  │ Every prompt has all 6 fields                          │
│  4  │ Every id is a unique integer                           │
│  5  │ IDs start after the current library max                │
│  6  │ Categories match existing names exactly OR are new     │
│  7  │ New category names are 2-4 words, Title Case           │
│  8  │ Every title is 3-12 words, specific, not generic       │
│  9  │ Every contract describes Input → Output                │
│ 10  │ Every matrix has exactly 3 items                       │
│ 11  │ Every matrix item is under 60 characters               │
│ 12  │ Every content field is 100-800 words                   │
│ 13  │ No placeholder text remains (TBD, TODO, INSERT)        │
│ 14  │ No duplicate titles                                    │
│ 15  │ No duplicate content                                   │
│ 16  │ Strings are properly escaped (quotes, backslashes)     │
│ 17  │ TypeScript compiles without errors                     │
└─────┴───────────────────────────────────────────────────────┘
```

---

## Content Writing Guidelines

### Strong Prompt Content Follows This Pattern:

1. **Role declaration** — "You are a [Specific Role]."
2. **Task statement** — "Given [inputs], produce [output]."
3. **Input placeholders** — Use `[BRACKETS]` for variables the user fills in.
4. **Numbered steps** — Each step has a clear action and expected result.
5. **Output format** — Specify what the final artifact looks like.
6. **Deterministic guardrails** — At least one of:
   - "Do not ask follow-up questions unless a required input is missing."
   - "State assumptions explicitly."
   - "Return a completion matrix."
   - "Prefer a practical working artifact over theoretical perfection."

### Anti-Patterns to Avoid:

```
┌──────────────────────────────────────┬──────────────────────────────────────┐
│ Do Not                               │ Do Instead                           │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ "Help me with..."                    │ "Given X, produce Y."               │
│ "Think about..."                     │ "Analyze X and output Y."           │
│ Content under 50 words               │ Content between 100-800 words       │
│ "Do whatever you think is best"      │ "Produce [specific artifact]."      │
│ No structure, wall of text           │ Numbered steps with clear sections  │
│ Generic titles ("Helper Tool")       │ Specific ("Circuit Breaker Builder")│
│ Matrix items over 60 chars           │ Concise checklist items             │
│ Reusing content from other prompts   │ Unique content for each prompt      │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## How Import Works

When you provide a `data.ts` file:

1. The importer reads the `prompts` array
2. It validates every object against the 6-field schema
3. It checks for ID conflicts against the existing library
4. It detects new categories and adds them with auto-assigned colors
5. It merges the new prompts into the library's PROMPTS constant
6. The filter bar, search, and metrics update automatically

If any prompt fails validation, the entire import is rejected with a specific error message telling you which field in which prompt is wrong.

---

## Quick-Start Template (Copy This)

```typescript
export type Category = 'Agent Engineering' | 'SaaS Ops' | "The Chef's Logic" | 'Growth Marketing' | 'Vibe Coding';

export interface Prompt {
  id: number;
  category: Category;
  title: string;
  contract: string;
  matrix: string[];
  content: string;
}

export const prompts: Prompt[] = [
  {
    "id": 401,
    "category": "Agent Engineering",
    "title": "",
    "contract": "Input: . Output: .",
    "matrix": [
      "",
      "",
      ""
    ],
    "content": ""
  }
];
```

Copy the quick-start template, fill in the fields, duplicate the object for each prompt, and you're ready to import.
