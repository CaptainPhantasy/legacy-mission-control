# RUST Agent Engineering Prompts — IDs 774–873

## Actor Model Agent System (774)
**Contract:** Input: agent capabilities and concurrency requirements. Output: complete actor system design in Rust with message passing, supervision, and lifecycle management.
**Matrix:**
- Define actor message types and protocols
- Implement supervision with restart policies
- Design mailbox and backpressure control
**Content:**
You are a Rust Actor System Architect. Given a set of agent capabilities and concurrency requirements, design a full actor-based agent system using Actix or a custom Tokio runtime.

Agent Capabilities: [CAPABILITIES]
Concurrency: [THREADS]

Produce:
1. ACTOR DEFINITIONS — Per agent: actor struct, message enum, handler implementation, state machine.
2. MESSAGE PASSING — Channel selection (mpsc, broadcast, watch), message serialization, delivery guarantees.
3. SUPERVISION — Parent-child hierarchy, restart strategy (one-for-one, all-for-one), escalation logic.
4. LIFECYCLE — Pre-start checks, graceful stop hooks, mailbox draining, state persistence on shutdown.
5. BACKPRESSURE — Bounded channels, shedding policy, slow consumer mitigation.
6. TESTING — Unit tests with mock actors, integration tests for supervision trees.

Do not ask follow-up questions unless a required input is missing. State assumptions explicitly. Return a completion matrix.

---

## Message Bus Implementation (775)
**Contract:** Input: list of agent services and event types. Output: a high-performance message bus implementation in Rust with publish/subscribe, routing, and delivery tracking.
**Matrix:**
- Design topic-based routing with wildcards
- Implement at-least-once delivery guarantee
- Add dead-letter queue and error reporting
**Content:**
You are a Distributed Messaging Engineer for Rust agent harnesses. Build a message bus that enables asynchronous communication among agent services.

Services: [SERVICES]
Event Types: [EVENTS]

Deliver:
1. TOPOLOGY — Topic namespaces, wildcard patterns, subscription model (push/pull).
2. ROUTING ENGINE — In-memory broker with filtering per agent, support for fan-out and point-to-point.
3. DELIVERY SEMANTICS — At-least-once with idempotent processing keys, acknowledgment protocol, retry with backoff.
4. DEAD-LETTER — Poison message detection, quarantine storage, admin console for reprocessing.
5. OBSERVABILITY — Metrics per channel (throughput, latency, saturation), tracing context injection.
6. CONFIGURATION — TOML/YAML driven setup, runtime hot-reload of subscriptions.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Agent Registry and Discovery (776)
**Contract:** Input: agent metadata schema and discovery scope. Output: a Rust registry module with service registration, health checks, and DNS-like query resolution.
**Matrix:**
- Define agent metadata model and versioning
- Implement heartbeat-based health monitoring
- Build query resolver with load-aware ranking
**Content:**
You are a Rust Service Discovery Specialist. Create an agent registry that enables dynamic discovery for an agent mesh.

Agent Metadata Schema: [SCHEMA]
Scope: [SCOPE]

Design:
1. REGISTRATION — Agent: name, capabilities, endpoint, weight, labels. Register on startup, deregister on shutdown. Lease-based TTL.
2. HEALTH — Periodic heartbeat (gRPC/HTTP), aggressive deadline detection, mark suspect → dead.
3. QUERY API — Filter by capability tags, return ranked list of healthy agents, optional circuit breaker status.
4. REPLICATION — Gossip protocol for multi-node registry, eventually consistent view, anti-entropy.
5. CLIENT SDK — Rust crate with async resolver, connection caching, failover.
6. DASHBOARD — Web UI showing registered agents, health status, version matrix.

Do not ask follow-up questions unless a required input is missing. Return a completion matrix.

---

## State Machine Agent Workflow (777)
**Contract:** Input: workflow steps and transition rules. Output: a Rust state machine implementation that drives agent task execution with error states and timeouts.
**Matrix:**
- Model states, events, and guarded transitions
- Implement persistent state with snapshotting
- Add timeout monitoring and deadline actions
**Content:**
You are a Rust State Machine Designer. Build a finite state machine that governs agent workflow execution.

Workflow Steps: [STEPS]
Transition Rules: [RULES]

Output:
1. STATE DEFINITION — Enum of states, each with on_entry/on_exit hooks. Include error, paused, completed states.
2. EVENT HANDLING — Event enum, dispatch function with pattern matching. Guard closures returning Result.
3. PERSISTENCE — Serde-based snapshot to SQLite/JSON after each transition, restore on restart.
4. TIMEOUTS — Per-state deadline, transition to TimeoutError state, escalation to parent agent.
5. EXECUTION — Async task per step, cancellation token support, parallel sub-state completion.
6. TESTING — Trace generated transitions, assert final state after event injection.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Event Sourcing for Agent Memory (778)
**Contract:** Input: agent domain events and query needs. Output: an event sourcing architecture in Rust with append-only event store and projected read models.
**Matrix:**
- Define domain events and versioning strategy
- Implement append-only store with snapshots
- Build projectors for read-optimized views
**Content:**
You are an Event Sourcing Architect for Rust agent memory systems. Design a durable event store that captures all agent interactions.

Domain Events: [EVENTS]
Queries: [QUERIES]

Design:
1. EVENT STORE — Append-only log with sequence numbers, event envelope (type, timestamp, aggregate ID), storage backend (RocksDB, Sled).
2. SNAPSHOTTING — Aggregate state snapshot every N events, speed up reconstruction.
3. PROJECTIONS — Async materialized views for agent context, latest state, history summaries. Use channels to notify projectors.
4. REPLAY — Function to rebuild agent state from event stream, deterministic state logic.
5. CONCURRENCY — Optimistic concurrency control with expected version, Conflict Resolution strategies.
6. OBSERVABILITY — Event count metrics, lag for projections, snapshot generation time.

Do not ask follow-up questions unless required input missing. Return completion matrix.

---

## Task Supervisor with Retry (779)
**Contract:** Input: task definitions with failure profiles. Output: a Rust supervisor that executes tasks with configurable retry, fallback, and escalation policies.
**Matrix:**
- Define task execution context and hooks
- Implement retry policy with exponential backoff
- Add circuit breaker integration and fallbacks
**Content:**
You are a Resilient Task Supervisor Engineer. Build a robust execution layer for agent tasks.

Task Definitions: [TASKS]
Failure Profiles: [FAILURE_MODES]

Produce:
1. TASK CONTRACT — Input/output types, timeout, priority, idempotency key.
2. RETRY ENGINE — Exponential backoff with jitter, max attempts, retryable vs. non-retryable error classification.
3. CIRCUIT BREAKER — Per downstream service, half-open probing, state transition metrics.
4. FALLBACKS — Degraded response or static cache return, graceful degradation plan.
5. ESCALATION — After retries exhausted: notify parent agent, write dead-letter, trigger incident.
6. METRICS — Task success rate, retry count histogram, circuit state timeline.

Do not ask follow-up questions unless missing required input. State assumptions explicitly.

---

## Agent Lifecycle Manager (780)
**Contract:** Input: agent startup dependencies and shutdown order. Output: a Rust lifecycle manager that orchestrates init, health, and graceful termination across agent services.
**Matrix:**
- Model dependency graph for startup order
- Implement liveness and readiness checks
- Design graceful shutdown with draining
**Content:**
You are a Rust Lifecycle Orchestrator. Create a controller that manages the full lifecycle of agent processes.

Services: [SERVICES]
Dependencies: [DEPENDENCIES]

Design:
1. STARTUP PHASES — Initialize config, connect DB, warm caches, subscribe to channels. Ordered by dependency DAG.
2. HEALTH PROBES — Liveness (simple heartbeat), readiness (all dependencies OK). Expose gRPC/HTTP endpoints.
3. SHUTDOWN SEQUENCE — Stop accepting new work, drain in-flight requests, flush state, close connections, terminate.
4. DEPENDENCY WATCH — Watch for downstream failures, propagate status, abort startup on critical failure.
5. RESTART POLICY — Per-service restart count, cooldown, backoff to avoid crash loops.
6. SIGNAL HANDLING — SIGTERM/SIGINT capture, graceful shutdown timer, force kill after deadline.

No follow-up questions unless input missing. Return a completion matrix.

---

## Plugin System for Agent Skills (781)
**Contract:** Input: skill interface specification and hot-plug requirements. Output: a Rust plugin architecture enabling dynamic loading of agent capabilities via WASM or FFI.
**Matrix:**
- Define stable skill trait and versioning
- Implement WASM host with sandboxing
- Build dynamic loading with dependency injection
**Content:**
You are a Rust Plugin Architect. Design an extensible skill system that allows agents to load new capabilities at runtime without recompilation.

Skill Interface: [TRAIT]
Deployment: WASM or dynamic library

Deliver:
1. SKILL TRAIT — Async function signature, input/output types (serde), metadata (name, version, permissions).
2. WASM HOST — Run skills in Wasmtime/Wasmer sandbox, allocate memory, enforce resource limits (CPU, memory).
3. LOADER — Scan plugin directory, verify signature, hot-reload on change, register in skill registry.
4. DEPENDENCY INJECTION — Provide host functions (logging, HTTP client, KV store) via WIT interface.
5. SECURITY — Capability-based access, no filesystem unless granted, network allowlist.
6. VERSIONING — Semantic version checks, backward compatibility shims, rollback to previous version.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Dependency Injection Container (782)
**Contract:** Input: agent service graph with constructors. Output: a compile-time DI container in Rust that resolves agent components and manages their lifecycles.
**Matrix:**
- Design constructor-based injection with macros
- Implement singleton and scoped lifetimes
- Add lazy initialization and circular check
**Content:**
You are a Rust Dependency Injection Expert. Build a lightweight, type-safe DI container for an agent harness.

Service Graph: [SERVICES]
Lifetimes: [LIFETIME_RULES]

Design:
1. CONTAINER — Thread-safe, holds provider registry, resolves recursively.
2. REGISTRATION — provide<T, Deps> with async factory closure, validated at compile time via traits.
3. LIFETIMES — Singleton (per container), Scoped (per request/task), Transient. Enforce no scope leaks.
4. CIRCULAR DEPENDENCY — Detection algorithm, error with dependency chain print.
5. INJECTION — Constructor injection via derive macro, optional field injection.
6. TESTING — Mock substitution for integration tests, reset container for isolation.

Do not ask follow-up questions unless a required input missing. State assumptions explicitly.

---

## Configuration Driven Agent Assembly (783)
**Contract:** Input: agent spec YAML and environment context. Output: Rust code that assembles agent graph from config, validates, and deploys.
**Matrix:**
- Parse agent spec with schema validation
- Instantiate agents with their dependencies
- Wire channels and start orchestration
**Content:**
You are a Rust Config-Driven Agent Assembler. Create a system that builds the entire agent runtime from a declarative specification.

Agent Spec: [YAML_FILE]
Environment: [ENV]

Steps:
1. PARSE — Read YAML/JSON with serde, validate against JSON schema, fail fast with location.
2. RESOLVE — For each agent: resolve dependencies, create actor/struct instance via DI container, inject config.
3. CHANNELS — Create typed channels per spec, connect input/output ports, set buffer sizes.
4. LIFECYCLE — Start agents in dependency order, trigger readiness, start heartbeats.
5. RELOAD — Watch config file changes, gracefully reload affected agents, drain old instances.
6. VERIFY — Integration check that all agents communicate, return graph visualization.

Do not ask follow-up questions unless required input missing. Return a completion matrix.

---

## Tokio Runtime Configuration (784)
**Contract:** Input: workload profile (I/O vs CPU) and desired parallelism. Output: a tuned Tokio runtime setup with custom scheduler, worker threads, and blocking pool.
**Matrix:**
- Select multi-thread or current-thread runtime
- Configure worker threads and stack size
- Integrate blocking task spawner for CPU work
**Content:**
You are a Tokio Performance Engineer. Configure a Tokio async runtime optimized for LLM agent workloads.

Workload: [WORKLOAD_TYPE]
Cores: [CPU_CORES]

Produce:
1. RUNTIME BUILDER — tokio::runtime::Builder with number of worker threads, thread name prefix, stack size.
2. SCHEDULER — Use work-stealing, tune global queue interval, enable task dumping for debugging.
3. BLOCKING POOL — Spawn CPU-intensive tasks (embedding, tokenization) on spawn_blocking, set max threads.
4. TIMER — Enable time feature, set tick resolution for precise timeouts.
5. TRACING — Integrate tracing subscriber with Tokio-console for task state inspection.
6. METRICS — Expose worker utilization, idle time, task poll counts as prometheus metrics.

Do not ask follow-up questions unless missing required input. State assumptions explicitly.

---

## Channel-Based Agent Communication (785)
**Contract:** Input: communication topology and message sizes. Output: a Rust channel strategy using Tokio mpsc/broadcast/watch for efficient agent-to-agent messaging.
**Matrix:**
- Select channel type per agent edge
- Implement bounded backpressure to avoid OOM
- Add channel metrics: depth, lag, drops
**Content:**
You are a Rust Concurrency Expert. Design the inter-agent communication layer using Tokio channels.

Topology: [TOPOLOGY]
Message Size: [SIZE_EST]

Design:
1. CHANNEL MAP — For each agent pair: choose mpsc (command), broadcast (events), watch (state updates).
2. BOUNDING — Set buffer sizes based on latency budget, overflow policy (drop oldest, block, error).
3. RECEIVER — select! over multiple channels, priority preemption for control messages.
4. BACKPRESSURE — Signal senders when slow, throttle via Semaphore permits.
5. SERIALIZATION — Use bincode/msgpack if cross-process, else pass Arc<Message>.
6. OBSERVABILITY — Channel length gauges, send fail counters, receiver lag histogram.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Work Stealing Task Scheduler (786)
**Contract:** Input: task queue characteristics and priority levels. Output: a custom async task scheduler in Rust that implements work-stealing for agent task execution.
**Matrix:**
- Design priority queues per worker thread
- Implement lock-free steal mechanism
- Add task affinity and fairness starvation prevention
**Content:**
You are a Rust Systems Programmer. Implement a lightweight work-stealing scheduler for agent tasks beyond Tokio defaults.

Queue Characteristics: [CHARACTERISTICS]
Priorities: [LEVELS]

Build:
1. LOCAL QUEUES — Each worker has a bounded lock-free queue (crossbeam or custom) for high priority tasks.
2. GLOBAL QUEUE — For overflow and low-priority tasks, fairness injection.
3. STEALING — Workers steal half of another's queue when idle, using work-stealing with random victim selection.
4. AFFINITY — Allow pinning of tasks to specific workers, e.g., GPU context tasks.
5. PREEMPTION — Cooperative yielding points, budget-based slicing to avoid monopolization.
6. METRICS — Queue depths, steal success rate, task wait times, scheduler overhead.

Do not ask follow-up questions unless required input missing. State assumptions explicitly.

---

## Backpressure and Rate Limiting (787)
**Contract:** Input: service rate limits and agent burst profiles. Output: a Rust middleware that applies backpressure and rate limiting to LLM API calls and downstream services.
**Matrix:**
- Implement token bucket rate limiter
- Design adaptive concurrency limiter
- Add backpressure propagation through channels
**Content:**
You are a Flow Control Engineer. Build a rate limiting and backpressure module for agent harnesses accessing external APIs.

Rate Limits: [LIMITS_TPS]
Burst: [BURST_SIZE]

Implement:
1. TOKEN BUCKET — Per API endpoint, async acquire(n) that awaits tokens, accurate refill with tokio::time.
2. CONCURRENCY LIMITER — Semaphore-based max concurrent requests, with priority queuing for critical calls.
3. BACKPRESSURE — When limit hit, propagate AsyncQueueFull error upstream, agent reduces send rate or sheds load.
4. ADAPTIVE — Monitor latency p95, reduce concurrency limit if latency increases (CoDel algorithm).
5. RETRY INTEROP — Return RateLimitInfo header for retry-after, integrate with retry policy.
6. METRICS — Accepted vs rejected counts, current concurrency, token bucket level.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Mpsc Channel Design for Agent Commands (788)
**Contract:** Input: command types and ordering requirements. Output: a multiple-producer single-consumer channel implementation in Rust for dispatching agent commands with priority lanes.
**Matrix:**
- Define command enum with priority levels
- Implement priority-aware mpsc using queues
- Ensure fairness with starvation prevention
**Content:**
You are a Rust Channel Designer. Create a prioritized MPSC channel for an agent's command queue.

Command Types: [COMMANDS]
Ordering: [PARTIAL_ORDER?]

Produce:
1. CHANNEL STRUCT — Wrapper over multiple tokio::sync::mpsc lanes (high, medium, low).
2. SEND — send(Command, priority), push to appropriate lane, optional timeout.
3. RECEIVE — recv() polls high lane first, then lower, with select!. Optional fairness counter to prevent starvation.
4. CLOSED — On drop of all senders, receiver gets None. Graceful drain before close.
5. BATCH RECV — recv_many(max) to amortize overhead.
6. TEST — Prove ordering under concurrent senders, check no lost commands.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Broadcast Channel for Event Notifications (789)
**Contract:** Input: event schema and fan-out requirements. Output: a Rust broadcast channel with subscriber lag detection and slow consumer eviction for agent events.
**Matrix:**
- Design broadcast channel with ring buffer
- Implement lag monitoring per subscriber
- Add slow consumer eviction and recovery
**Content:**
You are a Publish-Subscribe Specialist. Build a robust broadcast channel for agent system events.

Event Schema: [EVENT_STRUCT]
Subscribers: [MAX_SUBS]

Design:
1. CHANNEL — Use tokio::sync::broadcast, configure capacity, sender must clone for each publisher.
2. SUBSCRIPTION — Each subscriber receives a Receiver, handle resubscribe on lag overflow.
3. LAG MONITORING — Track len() vs capacity, log warning when subscriber lags > 80% capacity.
4. SLOW CONSUMER — Evict subscriber if lag persists, send SlowConsumerError, allow rejoin after recovery.
5. EVENT SERIALIZATION — Wrap Arc<Event> for zero-copy if possible.
6. METRICS — Channel capacity utilization, active subscribers, drop count due to lag.

Do not ask follow-up questions unless input missing. State assumptions explicitly. Return a completion matrix.

---

## Watch Channel for State Updates (790)
**Contract:** Input: state struct and refresh interval. Output: a Rust watch channel pattern for agents to observe state changes and react immediately.
**Matrix:**
- Create watch channel with initial value
- Implement changed() stream with notification
- Guard against stale reads via version check
**Content:**
You are a State Synchronization Engineer. Use Tokio's watch channel to distribute configuration and state to agent components.

State Struct: [STATE]
Refresh Interval: [INTERVAL]

Guide:
1. INITIALIZATION — watch::channel(initial_state), hold Sender in state manager, clone Receiver to all interested agents.
2. UPDATES — Sender::send_if_modified(|state| { ... }) to avoid duplicate notifications.
3. REACTION — Agent tasks loop: receiver.changed().await then read latest, apply delta logic.
4. VERSION CHECK — Embed monotonic version in state to detect missed updates or races.
5. BACKPRESSURE — Ensure sender isn't blocked by slow receivers (watch has no backpressure, latest value overwritten).
6. METRICS — Number of updates per second, receiver count, lag between send and observe.

State assumptions explicitly. No follow-up questions unless missing input.

---

## Async Stream Adapter for LLM Responses (791)
**Contract:** Input: LLM streaming response schema. Output: a Rust adapter that converts SSE/stream into async Stream<Item=Token> with error handling and parsing.
**Matrix:**
- Implement Stream trait for token emission
- Parse SSE format or newline-delimited JSON
- Handle connection drops and reconnect logic
**Content:**
You are a Rust Streaming Integration Engineer. Build an adapter that turns LLM streaming responses into a consumable futures::Stream.

Provider Protocol: [SSE/NDJSON]
Token Type: [TOKEN_STRUCT]

Build:
1. HTTP CLIENT — Reqwest with streaming body, set headers (Authorization, Accept).
2. PARSER — Byte stream → split on double newline → parse each data: line as JSON token.
3. STREAM — Implement Stream<Item = Result<Token, StreamError>> with poll_next. Buffer partial lines.
4. ERROR HANDLING — Transient connection error → retry with backoff; permanent error → terminate stream.
5. CANCEL — Dropping the stream aborts the underlying request, cleanup.
6. TEST — Mock server with controlled token stream and simulated disconnect.

No follow-up questions unless required input missing. State assumptions explicitly.

---

## Concurrent Task Pool with Semaphore (792)
**Contract:** Input: max concurrency and task spawn patterns. Output: a Rust task pool that limits concurrent agent sub-tasks using Tokio semaphore and manages join handles.
**Matrix:**
- Use Arc<Semaphore> for concurrency limit
- Spawn tasks with tokio::spawn and permit
- Track join handles and collect results
**Content:**
You are a Concurrency Control Designer. Build a task pool that runs agent sub-tasks with a cap on parallelism.

Max Concurrent: [LIMIT]
Task Type: [TASK_FN]

Implement:
1. POOL STRUCT — Holds Arc<Semaphore> with max permits, JoinSet for task handles.
2. SPAWN — spawn(async { let _permit = semaphore.acquire().await; /* task */ }), add to JoinSet.
3. AWAIT ALL — join_next loop, collect results, propagate panics, release permits.
4. CANCEL — Drop JoinSet to abort remaining tasks, ensure permits returned.
5. BATCHING — Accept iter of tasks, spawn all with permit wait, return futures.
6. METRICS — Active tasks gauge, queued waiters count, execution duration histogram.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Deadlock Detection for Agent Interactions (793)
**Contract:** Input: agent interaction graph and wait-for rules. Output: a Rust deadlock detector module that monitors locks and channels, alerts, and suggests fixes.
**Matrix:**
- Build wait-for graph from runtime data
- Detect cycles using Tarjan's algorithm
- Integrate with tracing to log deadlock event
**Content:**
You are a Concurrency Safety Expert. Implement a deadlock detection tool for an agent harness.

Interaction Graph: [GRAPH]
Lock Primitives: [Locks/Channels]

Design:
1. INSTRUMENTATION — Wrap Mutex, RwLock, channels with recording of holder and waiter. Use lock tracking with tokio::sync wrappers.
2. GRAPH — Nodes: agents/tasks; edges: holds resource, waits for resource. Update atomically.
3. DETECTOR — Background task runs periodic cycle detection (O(V+E)), reports deadlock with call stacks.
4. RECOVERY — Log error, optionally panic one task to break cycle, send alert.
5. AVOIDANCE — Suggest lock ordering, use try_lock timeouts, prefer message passing.
6. TEST — Inject deliberate deadlock, verify detection within timeout.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Generic Tool Registry with Typed Schema (794)
**Contract:** Input: tool function signatures and JSON schemas. Output: a Rust tool registry that allows agents to register and invoke tools by name with type-safe arguments.
**Matrix:**
- Design Tool trait with call method
- Implement registry with name-based lookup
- Add argument validation using JSON Schema
**Content:**
You are a Tool Integration Architect. Build a type-safe tool registry for an LLM agent harness.

Tool Signatures: [TOOLS]
Schemas: [JSON_SCHEMA]

Build:
1. TOOL TRAIT — async fn invoke(&self, args: Value) -> Result<Value> plus fn schema() -> JSON Schema.
2. REGISTRY — HashMap<String, Box<dyn Tool>>, register at startup, thread-safe with RwLock.
3. INVOCATION — Lookup tool by name, validate arguments against schema (jsonschema crate), call invoke.
4. ERROR HANDLING — Return structured error with code, message, and suggestions.
5. DISCOVERY — Expose list_tools() returning names and schemas for function calling API.
6. TESTING — Mock tool for unit tests, verify registration and validation.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Tool Invocation Pipeline with Retry (795)
**Contract:** Input: tool call sequence and reliability requirements. Output: a Rust pipeline that orchestrates tool execution with retry, timeout, and result aggregation.
**Matrix:**
- Chain tool calls with dependency passing
- Integrate retry policy and circuit breaker
- Collect partial results on failure
**Content:**
You are a Reliable Tool Orchestrator. Build a pipeline executor for sequential tool calls within an agent turn.

Tool Sequence: [SEQUENCE]
Timeouts: [TIMEOUTS]

Design:
1. PIPELINE — Define ordered steps, each step receives previous result as context. Dynamic next tool selection based on result.
2. RETRY — Per step, configurable attempts, backoff. On final failure, mark step as failed.
3. TIMEOUT — Overall pipeline deadline, per-step timeout, cancellation via tokio::time::timeout.
4. PARTIAL RESULTS — Store succeeded steps' outputs, aggregate into final response with status of each.
5. CIRCUIT BREAKER — If a tool consistently fails, open circuit to stop cascading, fallback to static answer.
6. OBSERVABILITY — Trace each step latency, success/failure, tool name, retry count.

No follow-up questions unless input missing. Return a completion matrix.

---

## Schema Generation from Rust Structs (796)
**Contract:** Input: Rust struct definitions. Output: JSON Schema for each tool input/output derived using schemars, integrated with tool registry.
**Matrix:**
- Add schemars derive to tool structs
- Generate JSON Schema at compile time
- Integrate schema into tool registration
**Content:**
You are a Rust Serialization Specialist. Automate JSON Schema generation for agent tool definitions.

Structs: [STRUCT_NAMES]

Guide:
1. DEPENDENCY — Add schemars crate, enable derive.
2. ANNOTATE — Derive JsonSchema on input/output structs, use #[schemars(title = ...)] for descriptions.
3. SCHEMA GENERATION — At test/build time, generate schema with schema_for!(), embed as static JSON.
4. REGISTRY INTEGRATION — Tool::schema() returns &'static serde_json::Value merged with metadata.
5. VALIDATION — Reuse schema for runtime validation of tool arguments via jsonschema.
6. DOCS — Auto-generate tool documentation from schemas for agent prompt.

Do not ask follow-up questions unless required input missing. State assumptions explicitly.

---

## Function Calling Adapter for OpenAI (797)
**Contract:** Input: tool definitions list. Output: a Rust adapter that formats tools into OpenAI function calling schema and parses responses back into tool calls.
**Matrix:**
- Serialize tools to OpenAI function format
- Parse response delta for tool call chunks
- Handle parallel tool calls in single response
**Content:**
You are an API Integration Engineer. Build a robust adapter for OpenAI's function calling feature.

Tools: [TOOLS]
Streaming: Yes

Implement:
1. SERIALIZE — Convert Tool trait definitions into Vec<ChatCompletionFunctions> with name, description, parameters schema.
2. REQUEST — Include tool_choice (auto or specific), pass to completion API.
3. RESPONSE PARSING — Handle function_call in message, accumulate arguments across streaming chunks, finish_reason tool_calls.
4. PARALLEL — Support multiple tool calls in one response, return Vec<ToolCall>.
5. EXECUTION — Invoke corresponding registered tool, collect results, and send back as tool role message.
6. ERROR — If tool call not found or arguments invalid, return error to model for correction.

No follow-up questions unless missing input. State assumptions explicitly.

---

## Tool Output Validation and Transformation (798)
**Contract:** Input: tool output schema and expected format. Output: a Rust validation module that checks tool results against schema, transforms errors into agent-readable messages.
**Matrix:**
- Validate output JSON against expected schema
- Transform mismatches into descriptive errors
- Support coercion for common type issues
**Content:**
You are a Data Validation Engineer. Build a robust post-processing layer for tool outputs.

Expected Schema: [SCHEMA]
Transformation Rules: [RULES]

Design:
1. VALIDATION — Use jsonschema to validate output against expected schema, return detailed error path.
2. COERCION — Apply implicit conversions (string to number, date parsing) where safe, log warnings.
3. ERROR MESSAGING — Produce user/agent-friendly error like "Field 'count' missing, expected integer".
4. RETRY FEEDBACK — Format error for LLM to suggest correction, e.g., "The tool expects ...".
5. TRANSFORM PIPELINE — Chainable transformers: rename keys, map values, filter nulls.
6. CACHE — Cache validated results to avoid repeated validation.

Do not ask follow-up questions unless missing input. State assumptions explicitly.

---

## Tool Caching Middleware (799)
**Contract:** Input: tool idempotency characteristics and cache TTL. Output: a Rust middleware that caches tool call results with key generation and eviction.
**Matrix:**
- Generate cache key from tool name + args hash
- Store results in LRU cache with TTL
- Support invalidation on mutation events
**Content:**
You are a Caching Strategist. Add a caching layer to the tool invocation pipeline to reduce latency and cost.

Idempotent Tools: [TOOLS]
TTL: [TTL_SECONDS]

Design:
1. CACHE KEY — SHA256 hash of (tool_name, canonical JSON args). Handle non-deterministic fields removal.
2. CACHE STORE — Multi-layer: in-memory LRU (Moka) with TTL, optional Redis backend.
3. MIDDLEWARE — Wrap invoke: check cache, on miss execute tool, store result, return.
4. INVALIDATION — Register invalidation hooks: when state changes, clear related cache keys.
5. MONITORING — Hit/miss ratio, size, eviction rate, per-tool cache statistics.
6. WARNING — For non-idempotent tools, skip cache, emit warning if used.

No follow-up questions unless input missing. Return a completion matrix.

---

## Rate-Aware API Client Builder (800)
**Contract:** Input: API base URL and rate limit headers. Output: a Rust HTTP client wrapper that respects rate limits, retries with backoff, and tracks quota usage.
**Matrix:**
- Parse rate limit headers from response
- Implement token bucket for proactive limiting
- Track remaining quota and emit warnings
**Content:**
You are a Client SDK Engineer. Build a rate-limit-aware HTTP client for external APIs used by agents.

Base URL: [BASE_URL]
Rate Limits: [LIMITS]

Produce:
1. CLIENT WRAPPER — Around reqwest::Client, add middleware via tower layers.
2. RATE LIMIT PARSER — Parse X-RateLimit-Remaining, Retry-After headers, update local token bucket.
3. PROACTIVE WAIT — Before request, acquire permit from rate limiter, await if necessary.
4. RETRY — On 429, use Retry-After duration; on server errors, exponential backoff.
5. QUOTA TRACKING — Expose metrics for remaining calls, reset time, warn at 20% threshold.
6. LOGGING — Log every request with rate limit status for observability.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Tool Error Handling and Fallback (801)
**Contract:** Input: tool error taxonomy and fallback options. Output: a Rust error handling strategy that classifies tool errors and applies graceful fallback responses.
**Matrix:**
- Classify errors into retryable, fatal, partial
- Map each class to a fallback action
- Implement fallback response generation
**Content:**
You are an Error Handling Architect. Design a robust error recovery system for agent tool use.

Error Taxonomy: [TAXONOMY]
Fallback Options: [FALLBACKS]

Implement:
1. ERROR TYPES — Enum: Retryable (network timeout), Fatal (invalid auth), Partial (some sub-results).
2. CLASSIFIER — Match error patterns from tool results, status codes, exception types.
3. FALLBACK CHAIN — For Retryable, retry N times then degrade; for Fatal, skip tool and return static message; for Partial, return subset.
4. DEGRADED RESPONSE — Craft LLM-friendly message: "Tool X unavailable, proceeding with cached data".
5. LOGGING — Structured error log with agent ID, tool, error class.
6. METRICS — Error rates by class, fallback activation count.

No follow-up questions unless missing input. State assumptions explicitly. Return a completion matrix.

---

## Circular Dependency Detector for Tools (802)
**Contract:** Input: tool definitions with dependencies. Output: a Rust algorithm that detects circular dependencies among tools and suggests resolution.
**Matrix:**
- Build dependency graph from tool calls
- Detect cycles using DFS with back edges
- Report cycle with tool names and data flow
**Content:**
You are a Graph Algorithm Specialist. Implement a static analyzer for tool dependency cycles.

Tool Definitions: [TOOLS]

Design:
1. GRAPH CONSTRUCTION — Nodes: tools; directed edge from A to B if A calls B.
2. CYCLE DETECTION — DFS with recursion stack tracking; upon finding a back edge, extract cycle path.
3. REPORTING — List affected tools, print cycle, suggest refactoring (merge tools or break cycle via command pattern).
4. INTEGRATION — Run as part of agent harness startup validation, fail fast with clear error.
5. TEST — Create intentional cycles, ensure detection and accurate path.
6. DOCUMENTATION — Auto-generate dependency diagram (Graphviz) for review.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Tool Documentation Generator (803)
**Contract:** Input: tool implementation code. Output: auto-generated Markdown documentation with signature, description, examples, and error codes.
**Matrix:**
- Extract doc comments and schema metadata
- Generate usage examples from tests
- Produce Markdown with consistent formatting
**Content:**
You are a Rust Documentation Engineer. Create a tool that generates comprehensive documentation for agent tools.

Tool Code: [CODE_PATH]

Build:
1. EXTRACTION — Parse tool trait impl to get function signature, extract doc comments, rustdoc style.
2. SCHEMA — Include JSON Schema from schemars, format as table.
3. EXAMPLES — Locate integration tests, capture request/response, embed as code blocks.
4. ERROR CODES — List possible error variants with descriptions.
5. OUTPUT — Generate single Markdown file per tool, index with tool list.
6. INTEGRATION — CI step validates docs up-to-date, fails if mismatch.

Do not ask follow-up questions unless missing input. State assumptions explicitly.

---

## Type-Safe Prompt Builder with Tera (804)
**Contract:** Input: prompt template and variable types. Output: a Rust system that validates prompt variables at compile time using typed contexts and Tera.
**Matrix:**
- Define typed context struct for template
- Validate all variables present at compile time
- Render template with escaping and error report
**Content:**
You are a Template System Architect. Build a type-safe prompt rendering engine using Tera templates.

Template: [TEMPLATE]
Context Type: [STRUCT]

Steps:
1. STRUCT DEFINITION — Create a Rust struct with all required fields, derive Serialize.
2. TEMPLATE — Tera template with {{ variable }}, loops, conditionals.
3. COMPILE-TIME CHECK — Write build script or proc macro that parses Tera and checks all variables exist in struct, fail build if missing.
4. RENDERING — tera.render("prompt", &context) returns Result, handle missing variable error gracefully.
5. ESCAPING — Auto-escape for text, but allow raw output where safe.
6. TEST — Unit tests for each template with sample context, snapshot testing of output.

No follow-up questions unless input missing. Return a completion matrix.

---

## Variable Injection with Validation (805)
**Contract:** Input: prompt skeleton and insertion points. Output: a Rust module that safely injects user variables into prompts, preventing injection and validating length.
**Matrix:**
- Sanitize inputs to prevent prompt injection
- Validate lengths and allowed characters
- Insert values with proper encoding
**Content:**
You are a Secure Prompt Engineer. Build a safe variable injection system for agent prompts.

Prompt Skeleton: [SKELETON]
Variables: [VAR_LIST]

Design:
1. SANITIZATION — Strip control characters, limit to allowed Unicode categories, neutralize escape sequences.
2. VALIDATION — Max length per variable, regex pattern if specified, reject with error message.
3. INJECTION — Use format! with careful use, or replace {{name}} with sanitized value.
4. GUARDRAILS — Input guard for common injection patterns like "Ignore previous instructions".
5. LOGGING — Log original and sanitized (for audit).
6. TEST — Unit tests for various injection attempts.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Few-Shot Example Compiler (806)
**Contract:** Input: raw examples and output format. Output: a Rust tool that compiles few-shot examples into prompt-optimal format, selecting diverse and representative cases.
**Matrix:**
- Parse examples from JSON/CSV
- Select diverse examples using clustering
- Format examples consistently for the prompt
**Content:**
You are a Data Curation Specialist. Build a few-shot example compiler for agent prompts.

Raw Examples: [EXAMPLES_FILE]
Max Shots: [K]

Implement:
1. LOADING — Read examples, each with input-output pair, optional tags.
2. DIVERSITY SELECTION — Vectorize examples (text embeddings), cluster, pick centroid of each cluster to ensure coverage.
3. FORMATTING — Apply template: "Input: ... Output: ..." with consistent separators.
4. DYNAMIC SELECTION — At runtime, retrieve top-N similar examples based on current query (RAG style).
5. EVALUATION — A/B test few-shot sets for accuracy improvement.
6. EXPORT — Save compiled prompt fragment.

Do not ask follow-up questions unless missing input. Return a completion matrix.

---

## Prompt Optimization Evaluator (807)
**Contract:** Input: candidate prompts and benchmark dataset. Output: a Rust evaluation framework that runs prompts against a vector of test cases and reports accuracy metrics.
**Matrix:**
- Define test case structure with input/expected
- Run each prompt candidate against LLM
- Compute exact match and semantic similarity scores
**Content:**
You are a Prompt Optimization Engineer. Build an automated evaluator for prompt variants.

Benchmark: [TEST_CASES]
Metrics: Exact match, BLEU, cosine similarity

Produce:
1. TEST RUNNER — Iterate over test cases, substitute variables, call LLM API, capture response.
2. SCORING — Implement multiple scorers: exact string match, BLEU score (using rust-bert?), embedding cosine similarity.
3. AGGREGATION — Compute mean, median, confidence intervals across runs.
4. REPORT — Generate markdown report with best prompt, worst, error cases.
5. ITERATIVE — Support genetic algorithm to mutate prompts and re-evaluate.
6. REPRODUCIBILITY — Seed and record all API calls for deterministic replay.

No follow-up questions unless input missing. State assumptions explicitly. Return a completion matrix.

---

## Multi-Modal Prompt Composer (808)
**Contract:** Input: text prompt and image/audio inputs. Output: a Rust module that constructs multi-modal messages for LLMs supporting vision/audio, with proper encoding.
**Matrix:**
- Encode images as base64 data URLs
- Construct message with content parts array
- Validate media formats and size limits
**Content:**
You are a Multi-Modal Integration Engineer. Build a prompt composer for vision/audio-capable LLMs.

Model: [OPENAI_VISION / OTHERS]
Media Inputs: [IMAGES/AUDIO]

Design:
1. MESSAGE STRUCT — Build ChatMessage with role and content list: text parts and image_url parts.
2. IMAGE ENCODING — Read image file, detect MIME type, encode as base64, construct data:image/jpeg;base64,... URL.
3. SIZE CHECK — Validate file size under model limit, resize if necessary.
4. AUDIO — If model supports, encode as base64 with WAV header.
5. MULTIPLE — Support multiple images in one message.
6. VALIDATION — Check total token count from combined parts, warn if exceeds context window.

Do not ask follow-up questions unless input missing. State assumptions explicitly.

---

## Dynamic Prompt Assembly from Context (809)
**Contract:** Input: context documents and system message. Output: a Rust engine that selects and injects relevant context paragraphs into a prompt template based on query similarity.
**Matrix:**
- Embed context chunks and index them
- Retrieve top-k chunks by semantic similarity
- Assemble final prompt with ranked context
**Content:**
You are a Context Assembler Architect. Build a dynamic prompt builder for RAG scenarios.

Context Library: [DOCUMENTS]
Embedding Model: [MODEL]

Steps:
1. CHUNKING — Split documents into paragraphs with overlap, assign IDs.
2. EMBEDDINGS — Compute vector embeddings via onnx/mini-lm, store in usearch index.
3. RETRIEVAL — Given query, compute query embedding, search index for top-K, optional re-rank.
4. ASSEMBLY — Insert retrieved chunks into prompt template using numbered references, truncate to fit token limit.
5. FEEDBACK — Show source citations in agent response.
6. REFRESH — Keep index updated with new documents, background reindexing.

No follow-up questions unless input missing. State assumptions explicitly. Return a completion matrix.

---

## Prompt Versioning and Rollback (810)
**Contract:** Input: prompt registry and change log. Output: a Rust system that versions prompts, allows A/B rollout, and rolls back to previous versions on regressions.
**Matrix:**
- Store prompts in versioned files or database
- Implement canary release with traffic split
- Monitor key metrics and trigger rollback
**Content:**
You are a DevOps for Prompts Engineer. Build a prompt versioning and deployment pipeline.

Prompt Store: [DB/FILES]
Metrics: [ACCURACY/LATENCY]

Design:
1. VERSIONING — Each prompt has schema: id, version, content, metadata, created_at. Store as immutable.
2. REGISTRY — Service to fetch prompt by name and version; agents request via gRPC.
3. CANARY — Traffic router: 10% traffic to new version, compare metrics (success rate, latency).
4. AUTO ROLLBACK — If metric degrades beyond threshold, revert to previous version, alert.
5. TESTING — Shadow mode: send same traffic to old and new, compare results offline.
6. UI — Dashboard for prompt history, diff between versions, approval workflow.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## A/B Testing Framework for Prompts (811)
**Contract:** Input: prompt variants and user segments. Output: a Rust framework that assigns users to variants, logs outcomes, and performs statistical analysis.
**Matrix:**
- Implement hashing-based assignment for stability
- Log prompt variant and outcome atomically
- Compute confidence intervals and significance
**Content:**
You are an Experimentation Platform Engineer. Build an A/B testing module for prompts.

Variants: [PROMPT_IDS]
Traffic Split: [PERCENTAGES]

Implement:
1. ASSIGNMENT — Consistent hash of user/session ID to bucket, map bucket to variant. Reproducible.
2. LOGGING — Structured log per request: variant, task, success, latency, token usage.
3. ANALYSIS — Aggregate logs, compute conversion rate (or other metric) per variant, Z-test for significance.
4. DASHBOARD — Live metrics, lift over control, recommendation when significance reached.
5. FEATURE FLAG — Integration with feature flag system to control rollout.
6. CLEANUP — Archive completed experiments.

Do not ask follow-up questions unless missing input. State assumptions explicitly.

---

## JSON Mode Output Parser (812)
**Contract:** Input: LLM response text. Output: a Rust parser that validates and extracts JSON output from responses, handling common formatting errors and fences.
**Matrix:**
- Extract JSON from markdown fences or raw
- Handle trailing commas and comments gracefully
- Validate parsed JSON against expected schema
**Content:**
You are a Parsing Specialist. Build a resilient JSON extractor for LLM outputs.

Expected Schema: [SCHEMA]

Design:
1. EXTRACTION — Search for JSON block within triple backticks (```json ... ```), else take whole response.
2. CLEANING — Remove trailing commas, fix unescaped quotes, strip comments (//) using heuristics.
3. PARSING — Deserialize with serde_json, catch errors, apply common fixes iteratively (up to 3 attempts).
4. VALIDATION — Check against JSON Schema if provided, return detailed mismatch.
5. FALLBACK — If still invalid, return structured error with raw response for agent to request correction.
6. CONFIG — Toggle strict mode.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Prompt Cost Estimator by Token (813)
**Contract:** Input: prompt text and model pricing. Output: a Rust utility that counts tokens using tiktoken-rs and calculates cost before making API call.
**Matrix:**
- Integrate tiktoken-rs for token counting
- Load model pricing from configuration
- Estimate cost and emit budget warning
**Content:**
You are a Cost Optimization Engineer. Build a prompt cost estimator module.

Model: [MODEL_PRICE_PER_1K]
Prompt: [PROMPT_TEXT]

Implement:
1. TOKEN COUNT — Use tiktoken-rs with model-specific encoding, count prompt + expected max output.
2. PRICING — Config file with model name and cost per 1K input/output tokens.
3. ESTIMATE — Compute: (input_tokens * price_input + output_tokens * price_output) / 1000.
4. GUARD — If estimated cost exceeds budget, warn or block call.
5. METRICS — Accumulate daily spend, top agent spenders.
6. LOGGING — Record actual cost after response for reconciliation.

Do not ask follow-up questions unless missing input. State assumptions explicitly.

---

## Conversation History Manager with Summarization (814)
**Contract:** Input: chat messages and token limit. Output: a Rust module that maintains conversation history, summarizes older messages, and injects into context intelligently.
**Matrix:**
- Implement sliding window with truncation
- Summarize truncated messages with LLM call
- Merge summary and recent history for prompt
**Content:**
You are a Context Window Manager. Design a memory manager for long conversations.

Token Limit: [MAX_TOKENS]
Summarization Model: [MODEL]

Steps:
1. HISTORY STORE — Append-only list of messages with timestamps, stored in memory.
2. WINDOW — Keep last N messages that fit within 80% token budget; older messages become candidates for summarization.
3. SUMMARIZE — Periodically (or on threshold) call LLM to produce concise summary of truncated messages, store with metadata.
4. INJECTION — Build prompt: [System] + [Summary] + [Recent Messages].
5. REFRESH — Incremental summary update to avoid redundant LLM calls.
6. USER CONTROL — Allow user to clear history or mark parts as important.

No follow-up questions unless input missing. Return a completion matrix.

---

## Sliding Window Context Builder (815)
**Contract:** Input: token limit and message stream. Output: a Rust algorithm that maintains a sliding window of the most recent messages that fit within a token budget.
**Matrix:**
- Count tokens efficiently with cache
- Implement window sliding with message eviction
- Optionally preserve system message always
**Content:**
You are an Efficient Context Engineer. Build a sliding window context manager for streaming agent conversations.

Token Budget: [BUDGET]
Preserve System: Yes

Design:
1. STRUCT — VecDeque of messages, token count cache per message.
2. ADD — On new message, tokenize, push back, adjust total tokens. While total > budget, pop front (except system).
3. REBUILD — Provide as_messages() to return current window slice for LLM request.
4. PERSISTENCE — Optionally persist overflow messages to disk for later retrieval.
5. METRICS — Window size in messages and tokens, eviction count.
6. TEST — Boundary cases: large single message exceeding budget.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Vector Store Integration for RAG (816)
**Contract:** Input: document collection and embedding model. Output: a Rust module that indexes documents into a vector database (Qdrant/Pinecone) and retrieves nearest neighbors.
**Matrix:**
- Embed documents using ONNX or API
- Store vectors with metadata in vector DB
- Implement retrieval with filtering and scoring
**Content:**
You are a Vector Database Integrator. Build a RAG backend for agent knowledge retrieval.

Vector DB: [QDRANT_URL]
Embedding: [MODEL]

Implement:
1. CLIENT — Use qdrant-client or reqwest for REST, async operations.
2. INDEXING — Read documents, chunk, generate embeddings (batch), upsert into collection with payload (title, date, chunk).
3. RETRIEVAL — On query, embed, search with top-k, apply filters, return payload + score.
4. REFRESH — Detect new/edited documents, update vectors.
5. PERFORMANCE — Use bulk API, limit concurrent embedding calls.
6. MONITORING — Index size, query latency, embedding latency.

Do not ask follow-up questions unless missing input. State assumptions explicitly. Return a completion matrix.

---

## Hybrid Semantic and Keyword Search (817)
**Contract:** Input: query string and document corpus. Output: a Rust search module that combines BM25 keyword search with vector similarity for improved retrieval accuracy.
**Matrix:**
- Implement BM25 indexing with Tantivy
- Fuse BM25 and vector scores via RRF
- Return merged result set with ranks
**Content:**
You are a Search Engineer. Build a hybrid search engine for agent knowledge bases.

Corpus: [DOCUMENTS]

Design:
1. KEYWORD INDEX — Use tantivy to build index with BM25 similarity, async writer.
2. VECTOR INDEX — Use usearch or external vector DB for dense retrieval.
3. QUERY — Accept query string, search both, get two result sets.
4. FUSION — Reciprocal Rank Fusion: score = 1/(k + rank) from each list, sum, re-rank.
5. FILTERS — Apply metadata filters on both sides.
6. BENCHMARK — Evaluate recall improvement over single method.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Memory Pruning using Relevance Scores (818)
**Contract:** Input: conversation history and importance model. Output: a Rust module that prunes low-relevance messages to conserve token budget while preserving critical information.
**Matrix:**
- Score each message by relevance to task
- Implement pruning algorithm with importance threshold
- Preserve last N messages unconditionally
**Content:**
You are a Memory Efficiency Expert. Build an intelligent memory pruner for agent conversations.

Task Importance: [CURRENT_TASK]

Implement:
1. SCORING — Use a small classifier or heuristic (recency, keyword match, user flag) to assign relevance score 0-1 to each message.
2. PRUNING — When total tokens exceed budget, sort by score ascending, remove lowest until budget met, keeping last K irrespective.
3. PROTECTION — Mark system message and critical user info as protected.
4. RECALC — After pruning, inform agent of removed context via metadata.
5. FEEDBACK — Allow agent to request full history on demand.
6. METRICS — Messages pruned, tokens saved.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Episodic Memory for Agent Sessions (819)
**Contract:** Input: agent session logs and retrieval query. Output: a Rust system that stores episodic memories and retrieves similar past experiences to guide agent decisions.
**Matrix:**
- Structure memory as event-time-context triples
- Index memories by embedding or keywords
- Retrieve top similar episodes for prompt
**Content:**
You are a Cognitive Architect. Build an episodic memory system for agents.

Session Logs: [LOGS]

Design:
1. MEMORY SCHEMA — Struct: timestamp, agent_id, task, decision, outcome, embedding.
2. STORAGE — Append to SQLite with vector extension or external DB.
3. EMBEDDING — Compute embedding of decision+context, store.
4. RETRIEVAL — At decision time, embed current context, query for similar episodes, return top-K.
5. FEEDBACK — Update memory with actual outcome to improve future retrieval.
6. PRIVACY — Allow scrubbing PII from stored memories.

No follow-up questions unless missing input. Return a completion matrix.

---

## Knowledge Graph Builder from Conversations (820)
**Contract:** Input: conversation text. Output: a Rust module that extracts entities and relations, builds an RDF/Property graph, and updates incrementally.
**Matrix:**
- Extract entities and relations using NLP
- Store graph in Neo4j or in-memory
- Query graph for relevant context
**Content:**
You are a Knowledge Graph Engineer. Build a dynamic knowledge graph that evolves with agent conversations.

Conversation Stream: [STREAM]

Implement:
1. EXTRACTION — Simple regex NER or calls to LLM for triple extraction.
2. GRAPH — Use petgraph or Neo4j driver; nodes: entities, edges: relations with confidence.
3. INCREMENTAL — Upon new information, merge into graph, deduplicate, update confidence.
4. QUERY — Provide API to traverse graph for answering questions, return subgraph as context.
5. VISUALIZATION — Generate Graphviz dot output for debugging.
6. PERSISTENCE — Serialize graph to JSON or database.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Contextual Cache with TTL (821)
**Contract:** Input: prompt and response pairs, TTL policy. Output: a Rust cache that stores LLM responses keyed by prompt hash, serving repeated queries instantly within TTL.
**Matrix:**
- Generate cache key from normalized prompt
- Implement LRU eviction and TTL expiration
- Support invalidation on upstream change
**Content:**
You are a Caching Specialist. Build a semantic cache for LLM responses to reduce latency and cost.

TTL: [SECONDS]

Design:
1. KEY GEN — Normalize prompt (lowercase, trim, remove extra spaces), hash with SHA256.
2. STORE — Moka cache with time-to-live and max capacity. Async-friendly.
3. READ — Before LLM call, check cache; if hit, return cached response.
4. WRITE — After successful LLM call, store response in cache with TTL.
5. INVALIDATION — On data source update, clear relevant cache entries by tag.
6. METRICS — Hit rate, miss rate, latency saved.

Do not ask follow-up questions unless input missing. State assumptions explicitly.

---

## Persistent Memory Backend Adapter (822)
**Contract:** Input: agent state structure and storage requirements. Output: a Rust adapter that persists agent memory to SQLite/Redis with async read/write and schema migration.
**Matrix:**
- Define trait for memory store
- Implement SQLite backend with migrations
- Add Redis backend for low-latency access
**Content:**
You are a Storage Abstraction Engineer. Build a pluggable persistent memory layer for agents.

Memory Struct: [STRUCT]
Backends: [SQLITE, REDIS]

Design:
1. TRAIT — AsyncMemoryStore with get(key) -> Option<Value>, set(key, value), delete, list_prefix.
2. SQLITE IMPL — Create table, use rusqlite with r2d2 pool, JSON column for flexible schema.
3. REDIS IMPL — Use redis-rs async, store as JSON string, set TTL.
4. MIGRATION — Simple version table, run SQL migrations on startup.
5. CACHING — In-memory read-through cache to reduce DB load.
6. TEST — Integration tests with real SQLite/Redis instances.

No follow-up questions unless input missing. Return a completion matrix.

---

## Context Compression for Long Documents (823)
**Contract:** Input: long document and max token length. Output: a Rust module that compresses text via extractive summarization while preserving key entities and instructions.
**Matrix:**
- Segment document into semantically coherent chunks
- Score sentences by importance using heuristics
- Select top sentences to fit token budget
**Content:**
You are a Text Compression Engineer. Build a lossy but intelligent compressor for agent context.

Max Tokens: [MAX_TOKENS]

Implement:
1. SEGMENT — Split into sentences, group by topic similarity.
2. SCORING — TF-IDF, position, named entity presence, ask LLM for key points (optional).
3. SELECTION — Greedy or ILP to pick highest scoring sentences up to token limit.
4. PRESERVATION — Always include last paragraph (often instructions) and any explicit "IMPORTANT" markers.
5. OUTPUT — Return compressed text.
6. EVAL — Measure information retention on QA tasks.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Sequential Agent Pipeline Executor (824)
**Contract:** Input: ordered agent steps. Output: a Rust executor that runs agents sequentially, passing output of one as input to next, with error propagation.
**Matrix:**
- Define pipeline as vector of agent tasks
- Implement step-by-step execution with context
- Support conditional early termination at step
**Content:**
You are a Workflow Orchestrator. Build a simple sequential pipeline for agent tasks.

Pipeline Steps: [STEPS]

Design:
1. PIPELINE CONFIG — List of step descriptors: agent_id, input mapping from previous output, output key.
2. EXECUTOR — Loop through steps, await each, pass result as context to next. On error, abort pipeline with error.
3. CONTEXT — Shared HashMap<String, Value> that accumulates outputs, accessible to each step.
4. EARLY EXIT — Each step can return a decision to stop pipeline.
5. TRACING — Log step start, duration, result.
6. TEST — Mock agents, verify correct data flow.

No follow-up questions unless input missing. Return a completion matrix.

---

## Parallel Fan-Out/Merge Orchestrator (825)
**Contract:** Input: task list and merge strategy. Output: a Rust orchestrator that fans out tasks to multiple agents concurrently and merges results as per strategy.
**Matrix:**
- Spawn concurrent tasks with tokio::spawn
- Collect results with JoinSet or FuturesUnordered
- Apply merge strategy: vote, concat, or select
**Content:**
You are a Concurrency Orchestrator. Build a fan-out/fan-in executor for agent swarms.

Tasks: [TASK_LIST]
Merge: [STRATEGY]

Implement:
1. FAN-OUT — For each task, spawn async task that invokes agent, push join handle.
2. AWAIT — Use futures::future::join_all or JoinSet to wait for all, with timeout per task.
3. ERROR — If any task fails, collect errors but continue others (unless fail-fast).
4. MERGE — If vote, majority; if concat, combine texts; if best, select highest confidence.
5. CANCEL — On overall timeout, abort pending tasks.
6. METRICS — Number of tasks, latencies, merge time.

Do not ask follow-up questions unless missing input. Return a completion matrix.

---

## Conditional Router with Decision Trees (826)
**Contract:** Input: routing rules and agent graph. Output: a Rust router that evaluates conditions on message content and sends to appropriate agent.
**Matrix:**
- Define conditions using JSON logic or DSL
- Implement decision tree traversal
- Support default fallback route
**Content:**
You are a Message Router Architect. Build a content-based router for an agent mesh.

Routing Rules: [RULES]

Design:
1. RULE ENGINE — Accept condition trees (e.g., if intent="booking" AND confidence>0.8 route to BookingAgent).
2. PARSER — Evaluate condition using jsonlogic crate or custom DSL.
3. TRAVERSAL — Ordered list of rules, first match wins.
4. DEFAULT — Fallback to general agent if no rule matches.
5. DYNAMIC — Support runtime rule updates via gRPC.
6. LOGGING — Record which rule fired and values.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Human-in-the-Loop Approval Workflow (827)
**Contract:** Input: agent decision and approval threshold. Output: a Rust workflow that suspends agent execution, sends approval request to a human, and resumes upon response.
**Matrix:**
- Define approval request with decision payload
- Implement pause mechanism and callback channel
- Timeout and default action if no response
**Content:**
You are a Workflow Engineer. Build a human-in-the-loop gate for sensitive agent actions.

Approval Request: [REQUEST]
Timeout: [SECONDS]

Implement:
1. TRIGGER — Agent yields control with a PendingApproval state.
2. CHANNEL — Use oneshot channel: agent sends request to approval service, awaits response on receiver.
3. APPROVAL SERVICE — Expose REST/gRPC endpoint for human to approve/reject with comments.
4. TIMEOUT — If no response by deadline, execute default policy (reject or auto-approve based on risk).
5. RESUME — On response, agent resumes with decision and comment.
6. AUDIT — Log all approval events for compliance.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Multi-Agent Debate Coordinator (828)
**Contract:** Input: debate topic and participant agent list. Output: a Rust coordinator that facilitates rounds of arguments, summarizes positions, and reaches consensus.
**Matrix:**
- Manage conversation rounds with turn order
- Collect arguments and distribute summaries
- Implement consensus scoring with voting
**Content:**
You are a Debate Moderator Engineer. Build a multi-agent debate protocol.

Participants: [AGENTS]
Rounds: [NUMBER]

Design:
1. ROUND STRUCTURE — Each agent gets turn to present argument or rebuttal. Coordinator manages turn queue.
2. MESSAGE DISTRIBUTION — After each round, compile summary and send to all agents.
3. CONSENSUS — After final round, each agent votes for best solution; weighted or majority.
4. CHAIR — Coordinator ensures time limits, cuts off rambling.
5. OUTPUT — Final consensus statement with dissenting opinions.
6. LOGGING — Full debate transcript for analysis.

No follow-up questions unless input missing. State assumptions explicitly. Return a completion matrix.

---

## Swarm Intelligence Task Allocator (829)
**Contract:** Input: task queue and agent capabilities. Output: a Rust scheduler that assigns tasks to agents using swarm algorithms like ant colony or market-based bidding.
**Matrix:**
- Model agents with capability scores and load
- Implement bidding protocol for task allocation
- Optimize for global throughput and fairness
**Content:**
You are a Swarm Engine Engineer. Build a decentralized task allocation system for agent swarms.

Agent Capabilities: [CAPABILITIES]
Tasks: [TASK_STREAM]

Implement:
1. AGENT PROFILE — Skills vector, current load, location.
2. BIDDING — Announce task, agents compute bid (cost estimate + capability), submit.
3. WINNER SELECTION — Choose lowest cost that meets requirements; notify.
4. FAIRNESS — Prevent starvation with reserve slots for low-util agents.
5. MONITORING — Task queue depths, agent utilization, allocation latency.
6. DYNAMIC — Re-allocate if agent fails.

State assumptions explicitly. No follow-up questions unless input missing.

---

## DAG Orchestrator with Dependencies (830)
**Contract:** Input: task DAG (nodes and dependencies). Output: a Rust executor that runs tasks respecting dependencies, maximizing parallelism, detects cycles.
**Matrix:**
- Represent DAG and detect cycles on build
- Schedule tasks using topological order
- Execute with max parallelism via semaphore
**Content:**
You are a DAG Execution Engine Architect. Build an orchestrator for agent task DAGs.

Task DAG: [DAG_JSON]

Design:
1. GRAPH — Use petgraph to store tasks as nodes, dependencies as edges. Validate acyclic.
2. SCHEDULE — Topological sort, identify tasks with no pending dependencies, launch them.
3. EXECUTION — Worker pool: each completed task signals dependent tasks to decrement counter, when counter 0 launch.
4. PARALLELISM — Cap with semaphore to avoid resource exhaustion.
5. ERROR — On task failure, optionally cancel downstream.
6. VISUALIZATION — Export to Graphviz for debugging.

No follow-up questions unless input missing. Return a completion matrix.

---

## Timeout and Deadline Propagation (831)
**Contract:** Input: task deadline and subtask graph. Output: a Rust middleware that propagates deadlines to subtasks, ensuring overall timeout is respected.
**Matrix:**
- Split deadline among subtasks proportionally
- Implement context deadline that cascades
- Cancel subtasks on overall deadline exceed
**Content:**
You are a Deadline Management Engineer. Implement deadline propagation for agent task trees.

Overall Deadline: [DEADLINE_MS]

Design:
1. DEADLINE CONTEXT — Attach deadline to root task.
2. PROPAGATION — When spawning subtask, compute remaining time, subtract overhead, pass as own deadline.
3. TIMEOUT — Each subtask wraps with tokio::time::timeout, on expiry sends cancellation.
4. CASCADE — If subtask cancelled, parent can decide to fail or use partial result.
5. MONITORING — Log timeline, detect tight deadlines.
6. TEST — Simulate varying subtask durations.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Checkpoint and Resume for Long Tasks (832)
**Contract:** Input: long-running task state and checkpoint interval. Output: a Rust mechanism to periodically save task state and resume from last checkpoint after restart.
**Matrix:**
- Serialize task state with serde
- Save checkpoint to durable storage
- Implement resume procedure on startup
**Content:**
You are a Fault-Tolerance Engineer. Build a checkpoint system for agent tasks.

Task State: [STATE_STRUCT]
Checkpoint Interval: [SECS]

Implement:
1. STATE — Serde Serialize + Deserialize struct capturing all needed progress.
2. CHECKPOINT — Periodically clone state and write to file or DB atomically.
3. RESUME — On task start, check for existing checkpoint, load, continue from there.
4. DUPLICATE PREVENTION — Use idempotency key to avoid re-execution of completed steps.
5. GARBAGE — Delete checkpoints after successful completion.
6. TEST — Simulate crash and verify seamless resume.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Sub-Process Fork and Join (833)
**Contract:** Input: main workflow with fork points. Output: a Rust pattern that forks execution into parallel sub-workflows, joining results with a barrier.
**Matrix:**
- Fork point spawns concurrent async tasks
- Join point collects all results with timeout
- Support dynamic number of forks
**Content:**
You are a Parallel Workflow Designer. Implement a fork/join construct for agent orchestrations.

Workflow: [WORKFLOW_DEF]

Design:
1. FORK — At fork step, for each branch, spawn tokio::task and pass a clone of context.
2. CONTEXT — Branches get read-only snapshot of context, produce their own sub-context.
3. JOIN — Use JoinSet or FuturesUnordered to await all branches. Merge sub-contexts using strategy.
4. TIMEOUT — Overall fork timeout; if any branch times out, cancel others.
5. ERROR — Partial results propagation.
6. TRACING — Create span per branch.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Tracing Span Configuration for Agent Calls (834)
**Contract:** Input: agent interaction model. Output: a Rust tracing setup that instruments agent calls with spans, events, and correlation IDs for debugging.
**Matrix:**
- Create spans per agent invocation with attributes
- Propagate trace context across async tasks
- Export spans to Jaeger or OTLP collector
**Content:**
You are an Observability Engineer. Configure tracing for an agent harness.

Exporter: [JAEGER_OTLP]

Steps:
1. INIT — Set up tracing_subscriber with fmt layer and opentelemetry_jaeger / otlp layer.
2. INSTRUMENT — Add #[instrument] macro to agent handler functions, include fields: agent_name, session_id.
3. PROPAGATION — Extract/inject trace context from gRPC headers or message envelopes.
4. SPANS — Create child spans for tool calls, LLM requests, cache lookups.
5. EVENTS — Log key events (request start, error, rate limit).
6. SAMPLING — Configure sampling rate to control volume.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Structured Logger with Key-Value Context (835)
**Contract:** Input: log structure schema. Output: a Rust logging setup using tracing that outputs structured JSON logs with agent identity and request ID.
**Matrix:**
- Define JSON format for log lines
- Inject agent_id and trace_id into every log
- Support dynamic log levels per agent
**Content:**
You are a Logging Specialist. Build a structured logging layer for the agent harness.

Schema: [FIELDS]

Implement:
1. SUBSCRIBER — tracing_subscriber::fmt().json() with custom event format.
2. CONTEXT — Use tracing::Span to store agent_id, request_id; propagate automatically.
3. FIELDS — Enforce presence of required fields via compile-time checks or runtime panic.
4. LEVEL CONTROL — Per agent log level from config, change at runtime via reload.
5. FILTERING — Ability to filter logs by agent_id for debugging.
6. DESTINATION — Output to stdout, with optional file sink.

No follow-up questions unless input missing. Return a completion matrix.

---

## Metrics Recorder for Agent Performance (836)
**Contract:** Input: key performance indicators. Output: a Rust metrics module using metrics crate that records counters, histograms, and gauges for agent operations.
**Matrix:**
- Define metrics: request count, latency, error
- Record metrics with labels (agent, tool)
- Expose via Prometheus endpoint
**Content:**
You are a Metrics Engineer. Set up a metrics pipeline for the agent harness.

KPIs: [LIST]

Design:
1. LIBRARY — Use metrics and metrics-exporter-prometheus.
2. INSTRUMENTS — counter!("agent.requests.total", "agent" => agent_id), histogram!("agent.duration").
3. RECORDING — Wrap agent calls with timer, increment counters on completion/error.
4. EXPOSER — Spawn HTTP server on /metrics, serve Prometheus text format.
5. DASHBOARD — Provide Grafana dashboard JSON.
6. ALERTING — Config rules for alerts on error rate spike.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Alert Manager for Anomaly Thresholds (837)
**Contract:** Input: metric thresholds and alert channels. Output: a Rust system that evaluates metrics against thresholds and sends alerts via Slack/email.
**Matrix:**
- Define rules in config: metric > threshold
- Evaluate periodically with hysteresis
- Send alert with context and dashboard link
**Content:**
You are a Monitoring Engineer. Build an internal alerting system for agent operations.

Rules: [RULES_YAML]
Channels: [SLACK_WEBHOOK, EMAIL]

Implement:
1. RULE ENGINE — Load from YAML, each rule: metric name, condition, severity, cooldown.
2. EVALUATION — Background task polls metrics (from Prometheus or in-memory), checks thresholds.
3. HYSTERESIS — Alert only after condition persists for N checks, clear after M checks below.
4. DISPATCH — Format alert message with metric value, agent, link to dashboard, send via reqwest to Slack.
5. ACK — Track alert state, avoid duplicates.
6. TEST — Simulate metric spikes.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Agent Activity Replay for Debugging (838)
**Contract:** Input: event log from agent run. Output: a Rust tool that replays agent actions deterministically for debugging and regression testing.
**Matrix:**
- Capture all non-deterministic inputs
- Implement replay engine using recorded inputs
- Allow step-by-step execution and inspection
**Content:**
You are a Debugging Toolsmith. Build an activity replayer for agent sessions.

Event Log: [LOG_FILE]

Design:
1. RECORDING — During agent execution, record all external inputs (LLM responses, tool results) with sequence numbers and timestamps.
2. REPLAY ENGINE — Reads log, feeds recorded responses instead of real API calls, runs agent logic deterministically.
3. STEP MODE — Support pause after each step, inspect state.
4. DIVERGENCE CHECK — Compare states with original run, flag differences.
5. SERIALIZATION — Save agent state at each step for inspection.
6. INTEGRATION — Use in CI to verify agent behavior after code changes.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Distributed Trace Context Propagator (839)
**Contract:** Input: inter-service message protocol. Output: a Rust middleware that injects and extracts W3C Trace Context into agent messages for distributed tracing.
**Matrix:**
- Implement W3C traceparent header injection
- Extract context from incoming messages
- Continue span across service boundaries
**Content:**
You are a Distributed Tracing Specialist. Enable end-to-end traceability across agent services.

Protocol: [GRPC/HTTP]

Implement:
1. PROPAGATOR — Use opentelemetry::global::get_text_map_propagator().
2. INJECT — Before sending a message, inject trace context into headers/metadata.
3. EXTRACT — On receiving, extract and set as current span's parent.
4. LINKING — Ensure spans from different services connect under a single trace.
5. MIDDLEWARE — Create Tower layer for HTTP, interceptor for gRPC.
6. TEST — Verify trace continuity in Jaeger.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Latency Heatmap Generator (840)
**Contract:** Input: latency data stream. Output: a Rust processor that aggregates percentiles and generates a latency heatmap for agent operations.
**Matrix:**
- Compute p50, p95, p99 over time windows
- Store aggregates in time-series DB
- Render heatmap via ASCII or image
**Content:**
You are a Performance Analyst. Build a latency visualization tool.

Data Stream: [METRICS]

Implement:
1. AGGREGATOR — Use t-digest or HDR histogram to compute percentiles over sliding windows.
2. STORAGE — Write aggregates to InfluxDB or Prometheus.
3. HEATMAP — Generate SVG/PNG heatmap using plotters crate: X=time, Y=latency bucket, color=density.
4. ALERT — If p99 exceeds SLO, trigger alert.
5. EXPORT — Serve via HTTP endpoint.
6. CONFIG — Window size, number of buckets.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Log Aggregation and Filtering (841)
**Contract:** Input: log streams from multiple agents. Output: a Rust log aggregator that collects, filters, and routes logs to a central store.
**Matrix:**
- Collect logs via TCP/UDP or shared queue
- Filter by agent, level, or regex
- Forward to Loki or Elasticsearch
**Content:**
You are a Logging Infrastructure Engineer. Build a lightweight log aggregator for the agent harness.

Transport: [UDP/TCP]

Design:
1. COLLECTOR — Listen on port, parse JSON lines, buffer in channel.
2. FILTER — Apply rules to drop or redact sensitive fields.
3. BATCH — Accumulate logs, batch send to Loki's push API.
4. IN-MEMORY — For development, store recent logs in ring buffer and serve via /logs endpoint.
5. RESILIENCE — Retry on remote failures, buffer to disk if needed.
6. MONITORING — Throughput, buffer depth.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Health Check Dashboard Builder (842)
**Contract:** Input: service health endpoints. Output: a Rust mini-dashboard that aggregates health statuses and presents a simple HTML page.
**Matrix:**
- Probe health endpoints periodically
- Aggregate status to overall health
- Serve status page with auto-refresh
**Content:**
You are a DevOps Tooling Engineer. Build a lightweight health dashboard for the agent system.

Health Endpoints: [URLS]

Implement:
1. PROBER — Async HTTP client, GET /health, check for 200 and optional JSON status.
2. AGGREGATOR — Collect results, if any critical service down, overall status red.
3. HTML — Use maud or askama to render status page with icons.
4. HISTORY — Keep last N probe results, show timeline.
5. ENDPOINT — Serve at /dashboard.
6. ALERT — Optional callback on status change.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Incident Response Playbook Generator (843)
**Contract:** Input: incident type and runbook template. Output: a Rust tool that fills a runbook with agent-specific details and suggests corrective actions.
**Matrix:**
- Map incident types to response procedures
- Populate template with live agent data
- Suggest remediation based on similar past incidents
**Content:**
You are an Incident Management Engineer. Build an automated runbook generator.

Incident: [TYPE]

Design:
1. PLAYBOOK REPO — Store Markdown templates per incident class.
2. CONTEXT — Fetch current agent state, recent errors, resource usage.
3. FILL — Replace placeholders with live data, highlight anomalies.
4. SUGGESTIONS — Query past incident resolutions from log, rank by success.
5. PRESENTATION — Render as formatted message for incident channel.
6. LOG — Record generated playbook and outcome for learning.

No follow-up questions unless input missing. Return a completion matrix.

---

## Circuit Breaker for External Services (844)
**Contract:** Input: service endpoint and failure threshold. Output: a Rust circuit breaker implementation that opens on repeated failures and half-opens after timeout.
**Matrix:**
- Track consecutive failures with atomic counters
- Implement open/half-open/closed state machine
- Use failsafe or custom state with config
**Content:**
You are a Resilience Pattern Engineer. Implement a circuit breaker for LLM API calls.

Endpoint: [URL]
Threshold: [FAILURES]

Design:
1. STATE — Enum: Closed(consecutive_fails), Open(until time), HalfOpen.
2. CLOSED — Count failures. On threshold exceeded, transition to Open, set reset deadline.
3. OPEN — Reject calls immediately with error. After timeout, transition to HalfOpen.
4. HALF-OPEN — Allow one probe call; if succeeds, go Closed; if fails, back to Open.
5. METRICS — Circuit state, transitions count.
6. INTEGRATION — Wrap async function with circuit breaker.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Exponential Backoff Retry Policy (845)
**Contract:** Input: max retries and base delay. Output: a Rust module that calculates exponential backoff with jitter for retrying failed agent calls.
**Matrix:**
- Define retry config: attempts, base delay, max delay
- Implement delay calculation with full jitter
- Integrate with async task using loop+timer
**Content:**
You are a Retry Specialist. Build a configurable retry policy module.

Config: max_retries=5, base=100ms, max_delay=30s

Implement:
1. POLICY STRUCT — Holds settings.
2. DELAY FN — delay = min(base * 2^attempt, max_delay); jitter = rand::random(0..delay);
3. EXECUTOR — Async function retry(|| async { ... }) that loops, catches errors, sleeps backoff, re-raises after max.
4. CLASSIFICATION — Only retry on transient errors (status 429, 5xx, timeout).
5. LOGGING — Log each attempt with delay.
6. TEST — Verify backoff timing via simulated clock.

No follow-up questions unless input missing. Return a completion matrix.

---

## Fallback Strategy Designer (846)
**Contract:** Input: primary and fallback service endpoints. Output: a Rust strategy that automatically switches to fallback on failure and returns to primary when healthy.
**Matrix:**
- Define primary and fallback resources
- Implement health checker for primary
- Seamlessly route requests to fallback
**Content:**
You are a High Availability Engineer. Build a fallback routing layer.

Primary: [PRIMARY_URL]
Fallback: [FALLBACK_URL]

Design:
1. ROUTER — Wrap client, maintain primary active flag.
2. HEALTH — Periodic ping to primary; if fails N times, set inactive, route to fallback.
3. REVIVE — Continue probing primary; if healthy for M cycles, restore.
4. REQUEST — On each request, if primary active use it, else fallback. Include retry logic within each.
5. CONSISTENCY — Ensure fallback can serve without data loss (cached data).
6. METRICS — Active backend metric, failover events count.

Do not ask follow-up questions unless input missing. State assumptions explicitly.

---

## Graceful Degradation Planner (847)
**Contract:** Input: service dependencies and criticality. Output: a Rust engine that disables non-critical features when dependencies fail to maintain core agent functions.
**Matrix:**
- Classify dependencies as critical or soft
- Implement feature flags for each capability
- Automatically disable features on dependency failure
**Content:**
You are a Degradation Architect. Build a system that gracefully degrades agent capabilities under stress.

Dependencies: [DEPENDENCY_MAP]

Design:
1. CLASSIFY — Each agent capability tied to required dependencies; mark as critical/optional.
2. MONITOR — Track health of each dependency.
3. FLAGS — Use AtomicBool per feature; on dependency failure, flip flag to false.
4. ADAPT — Agent logic checks flag before proceeding; if disabled, provide generic fallback message.
5. RECOVER — When dependency recovers, re-enable feature.
6. COMMUNICATE — Inform user that some features are temporarily unavailable.

No follow-up questions unless input missing. Return a completion matrix.

---

## Idempotency Key Middleware (848)
**Contract:** Input: request type and storage backend. Output: a Rust middleware that ensures idempotent processing of agent requests using idempotency keys and response caching.
**Matrix:**
- Generate or extract idempotency key from request
- Check storage for existing response
- Store response after first processing completion
**Content:**
You are a Transactional Safety Engineer. Build an idempotency layer for agent API calls.

Storage: [REDIS/SQL]

Implement:
1. KEY — Client provides Idempotency-Key header; if missing, generate for internal calls.
2. CHECK — Before processing, try to retrieve stored response by key. If found and not expired, return immediately.
3. LOCK — Set a pending state with TTL to avoid concurrent processing.
4. PROCESS — Execute request, store result with final status (success/error).
5. CLEANUP — Expire old entries.
6. METRICS — Idempotency hit ratio.

Do not ask follow-up questions unless input missing. State assumptions explicitly.

---

## Error Classification and Routing (849)
**Contract:** Input: raw error and context. Output: a Rust classifier that assigns error codes and routes to appropriate handler (retry, fallback, alert).
**Matrix:**
- Parse error into structured code and message
- Map error code to action (retry, skip, abort)
- Log and metric the classified error
**Content:**
You are an Error Taxonomy Specialist. Build an error classifier for agent operations.

Error Types: [ENUM]

Design:
1. CLASSIFY — Function that takes anyhow::Error or similar, matches known patterns (HTTP status, JSON error code), produces enum variant.
2. ACTIONS — Config-driven mapping: Retryable -> retry policy, Fatal -> abort task, Degraded -> use fallback.
3. CONTEXT — Enrich error with agent_id, step, timestamp.
4. ROUTER — Central error handler that invokes appropriate action.
5. FEEDBACK — When user-visible, format error message clearly.
6. DATABASE — Record error for analysis.

No follow-up questions unless input missing. Return a completion matrix.

---

## Self-Healing Agent with Recovery (850)
**Contract:** Input: agent failure modes and recovery procedures. Output: a Rust pattern that detects agent failure, attempts auto-recovery steps, and reports if unable.
**Matrix:**
- Detect failure via health checks or panics
- Attempt predefined recovery steps in order
- Escalate to human if auto-recovery fails
**Content:**
You are a Resilience Architect. Design a self-healing mechanism for agents.

Failure Modes: [MODES]

Implement:
1. WATCHDOG — Separate task monitors agent heartbeats; on missed beats, trigger recovery.
2. RECOVERY STEPS — Step list: restart agent process, clear cache, reconnect to services, reload config.
3. ATTEMPT LOOP — Try each step, verify health after, limit total attempts.
4. ESCALATION — If all steps fail, log incident, notify operator, enter safe mode.
5. SAFE MODE — Agent responds with "temporarily unavailable, please try later".
6. METRICS — Recovery attempts, success rate.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Chaos Engineering Test Generator (851)
**Contract:** Input: system topology and failure scenarios. Output: a Rust tool that injects faults (latency/drop) into agent communications to validate resilience.
**Matrix:**
- Define failure scenarios: delay, error, kill
- Inject faults via middleware or proxy
- Measure system behavior under chaos
**Content:**
You are a Chaos Engineer. Build a fault injection framework for agent harness testing.

Topology: [GRAPH]

Design:
1. FAULT MODELS — Delay (add latency), Exception (return error), Partition (block messages).
2. INJECTOR — Proxy between agents that can be toggled per edge.
3. SCENARIOS — Script chaos experiments: "kill agent A for 10s", "increase latency 500ms on tool calls".
4. ORCHESTRATOR — Run experiment, collect metrics during steady-state vs chaos.
5. VALIDATION — Assert that system remains within SLAs or degrades gracefully.
6. REPORT — Generate experiment report.

No follow-up questions unless input missing. Return a completion matrix.

---

## Timeout Escalation Protocol (852)
**Contract:** Input: task hierarchy and timeout values. Output: a Rust protocol that escalates timeouts up the call chain, eventually alerting a supervisor agent.
**Matrix:**
- Detect timeout at leaf task
- Propagate timeout to parent with context
- Trigger escalation to supervisor or fallback
**Content:**
You are a Timeout Management Engineer. Implement an escalation protocol for agent timeouts.

Hierarchy: [AGENT_TREE]

Design:
1. TIMEOUT DETECTION — Wrap tasks with tokio::time::timeout. On elapse, return TimeoutError with detail.
2. PARENT HANDLING — Parent catches timeout, may retry or escalate. Includes timeout chain info.
3. ESCALATION — If parent cannot resolve, escalate further, eventually to a supervisor agent that decides on fallback or abort.
4. LOGGING — Chain of timeouts with timestamps.
5. CONFIG — Per-agent timeout values from config.
6. METRICS — Timeout rates per level.

Do not ask follow-up questions unless input missing. State assumptions explicitly.

---

## Bulkhead Pattern for Isolation (853)
**Contract:** Input: agent thread pools and resource quotas. Output: a Rust implementation that isolates agent groups in separate thread pools to contain cascading failures.
**Matrix:**
- Partition agents into isolated execution groups
- Allocate separate Tokio runtime or semaphore
- Monitor and enforce resource limits per group
**Content:**
You are a Resiliency Architect. Apply the bulkhead pattern to agent execution.

Groups: [AGENT_GROUPS]
Resources: [CPU/LIMITS]

Implement:
1. ISOLATION — Create separate Tokio runtimes per group, or use per-group semaphore with max concurrency.
2. RESOURCE LIMITS — Cap number of concurrent tasks per group.
3. FAILURE CONTAINMENT — If one group exhausts its capacity, others unaffected.
4. QUEUING — Reject or queue requests when group at capacity, with timeout.
5. MONITORING — Utilization per group, rejected count.
6. CONFIG — Dynamic adjustment of limits.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Streaming Token Processor with Backpressure (854)
**Contract:** Input: async stream of tokens. Output: a Rust pipeline that processes tokens on-the-fly (e.g., display, parse) with backpressure to prevent memory overload.
**Matrix:**
- Consume token stream with async for_each
- Apply transformation and buffering
- Implement backpressure via bounded channel
**Content:**
You are a Stream Processing Engineer. Build a token stream processing pipeline.

Token Stream: [STREAM]

Design:
1. SOURCE — Accept impl Stream<Item = Token> from LLM.
2. TRANSFORM — Apply mapping, e.g., decode, filter stop tokens.
3. BUFFER — Use tokio::sync::mpsc bounded channel to decouple processing stages, applying backpressure.
4. SINK — Downstream consumer (WebSocket, stdout) reads from channel.
5. CANCELLATION — If consumer stops, upstream stream is dropped and cancelled.
6. METRICS — Token throughput, buffer utilization.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Batch Call Optimizer for Multiple Prompts (855)
**Contract:** Input: list of prompts and concurrency limit. Output: a Rust optimizer that groups prompts into batch calls where API supports it, reducing round trips.
**Matrix:**
- Detect batch API support and max batch size
- Group prompts by model and priority
- Execute batches with concurrent limit
**Content:**
You are a Throughput Optimizer. Implement a batching layer for LLM API calls.

Prompts: [PROMPTS]
Max Batch: [SIZE]

Design:
1. BATCH API — Check if provider supports batching (e.g., OpenAI batch endpoint).
2. GROUPING — Accumulate prompts over a time window or by count, group by model.
3. EXECUTION — Submit batch as single HTTP request, await completion, map results back to individual callers.
4. FALLBACK — If batch fails, fall back to individual calls.
5. RETRY — Retry failed items within batch individually.
6. COST — Report savings from batch.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Connection Pool for LLM Providers (856)
**Contract:** Input: provider endpoints and max connections. Output: a Rust connection pool manager using reqwest's pool that reuses HTTP connections and limits concurrency.
**Matrix:**
- Configure reqwest Client with pool settings
- Limit max idle connections per host
- Implement keep-alive and timeout tuning
**Content:**
You are a Network Performance Engineer. Optimize HTTP connection pooling for LLM APIs.

Endpoints: [URLS]
Max Connections: [N]

Produce:
1. CLIENT BUILDER — reqwest::Client::builder().pool_max_idle_per_host(20).pool_idle_timeout(Duration::from_secs(90)).
2. CONCURRENCY — Use Arc<Client> shared across tasks.
3. DNS — Set tcp_keepalive, tcp_nodelay.
4. MONITORING — Expose connection pool metrics (idle, total).
5. ADAPTIVE — Adjust pool size based on latency.
6. TEST — Benchmark throughput with and without pooling.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Caching Strategy for Repeated Queries (857)
**Contract:** Input: query distribution and cache budget. Output: a Rust multi-level caching solution (in-memory + Redis) for agent tool calls and LLM responses.
**Matrix:**
- Implement L1 in-memory cache with Moka
- Add L2 Redis cache with async client
- Design cache population and invalidation
**Content:**
You are a Cache Architect. Design a two-level caching strategy.

Cache Budget: [MEMORY_SIZE]

Implement:
1. L1 — High-speed moka cache with TTL and max capacity.
2. L2 — Redis as shared cache for distributed agents, with longer TTL.
3. READ — Check L1, miss -> check L2, miss -> compute and populate both.
4. WRITE — Write-through to L2 and L1.
5. INVALIDATION — Pub/sub channel for cache eviction across instances.
6. MONITORING — Hit rates per level.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Request Deduplication Middleware (858)
**Contract:** Input: request stream with potential duplicates. Output: a Rust middleware that detects duplicate requests within a time window and returns cached response.
**Matrix:**
- Compute request fingerprint from content
- Store ongoing request futures in map
- Collapse duplicates to single execution
**Content:**
You are a Deduplication Engineer. Build a request deduplicator to prevent redundant LLM calls.

Window: [SECONDS]

Design:
1. FINGERPRINT — Hash canonical JSON of request (model, messages, tools).
2. REGISTRY — DashMap mapping fingerprint to SharedFuture.
3. HANDLER — On new request, check map; if future exists, await it; otherwise insert new future and execute.
4. EVICTION — Remove entry after future completes or times out.
5. CONCURRENCY — Use Arc<tokio::sync::Mutex<Option<Result>>> for shared future.
6. METRICS — Dedup hit count.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Lazy Initialization of Agent Resources (859)
**Contract:** Input: resource list with heavy initialization. Output: a Rust pattern that defers resource creation until first use, with thread-safe lazy static or OnceCell.
**Matrix:**
- Use OnceCell or LazyLock for singletons
- Ensure async initialization with tokio::sync
- Handle initialization errors gracefully
**Content:**
You are a Resource Efficiency Engineer. Implement lazy initialization for agent components (e.g., embedding models, DB pools).

Resources: [LIST]

Implement:
1. STATIC — Use std::sync::LazyLock or once_cell::sync::OnceCell for global resources.
2. ASYNC — For async init, use tokio::sync::OnceCell or async_oncecell.
3. INIT FUNC — Define async fn get_resource() -> Arc<Resource> that calls cell.get_or_init(|| async {...}).
4. ERROR — Propagate initialization error; cache error state to avoid repeated failures.
5. TEARDOWN — Provide shutdown to release resources.
6. TEST — Verify lazy behavior.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Async Request Coalescing (860)
**Contract:** Input: high-frequency identical requests. Output: a Rust module that merges simultaneous identical requests into a single backend call and fans out results.
**Matrix:**
- Batch arrivals within a micro-window
- Execute single request on behalf of group
- Distribute result to all waiters
**Content:**
You are a Coalescing Engineer. Build a request coalescer for LLM queries.

Max Batch Window: [MS]

Design:
1. GATHER — When request arrives, create a oneshot channel for response, push into a queue keyed by request hash.
2. TIMER — After a short delay, drain queue for that key, send single request.
3. FANOUT — On response, send clone to all waiters via their oneshot channels.
4. TIMEOUT — If timer expires waiting, send error to waiters.
5. THROTTLE — Cap number of waiters per key.
6. METRICS — Coalescing ratio.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Memory Profiling for Agent State (861)
**Contract:** Input: agent runtime snapshot. Output: a Rust profiling tool that tracks memory usage of agent state, identifies leaks, and suggests optimizations.
**Matrix:**
- Integrate dhat or bytehound for profiling
- Track allocations per agent component
- Generate report with top allocation sites
**Content:**
You are a Performance Profiling Engineer. Build a memory profiler for the agent harness.

Profiling Target: [BINARY]

Steps:
1. INSTRUMENT — Use #[global_allocator] with dhat or link with bytehound.
2. COLLECT — Run workload, capture heap profile.
3. ANALYSIS — Parse output to find total memory, leaked blocks, high-alloc paths.
4. REPORT — Generate HTML/JSON report with agent-specific tags.
5. CI — Integrate profiling into test suite with memory budget.
6. GUARD — Fail test if memory exceeds threshold.

Do not ask follow-up questions unless input missing. State assumptions explicitly.

---

## Load Shedding Orchestrator (862)
**Contract:** Input: overload signal and shedding policy. Output: a Rust module that gracefully sheds low-priority agent tasks when system approaches overload.
**Matrix:**
- Define congestion signal (CPU, queue depth)
- Implement task prioritization schema
- Shed tasks above threshold with back-pressure
**Content:**
You are a Overload Protection Engineer. Implement load shedding for an agent task queue.

Overload Signal: [QUEUE_DEPTH>90%]

Design:
1. DETECTION — Monitor system metrics (CPU, memory, task queue length).
2. CLASSIFICATION — Tasks tagged with priority (critical, normal, best-effort).
3. SHEDDER — When overload signal active, reject best-effort tasks, queue normal tasks, only process critical.
4. FEEDBACK — Return 503 or throttle signal to senders.
5. RECOVERY — When conditions clear, resume normal.
6. METRICS — Shed count, overload duration.

No follow-up questions unless input missing. Return a completion matrix.

---

## Throughput Benchmark Suite (863)
**Contract:** Input: agent endpoint and load profile. Output: a Rust benchmarking tool that measures throughput and latency under various load levels, producing a report.
**Matrix:**
- Generate synthetic requests respecting profile
- Ramp up concurrency and measure metrics
- Report p50, p99, max throughput
**Content:**
You are a Performance Benchmark Engineer. Build a load generator for agent services.

Profile: [REQUESTS_PER_SECOND]

Implement:
1. GENERATOR — Tokio tasks that send requests at controlled rate using tokio::time::interval.
2. METRICS — Record latency histogram per request, success/error count.
3. RAMP — Gradually increase concurrency to find saturation point.
4. ANALYSIS — Compute throughput, latency percentiles.
5. REPORT — Output CSV and summary to stdout.
6. INTEGRATION — Can be used in CI for performance regression.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Mock LLM Server for Integration Tests (864)
**Contract:** Input: expected requests and canned responses. Output: a Rust mock HTTP server (wiremock or custom) that simulates LLM API for testing agent logic.
**Matrix:**
- Define expected request patterns
- Return predefined JSON responses
- Support latency and error simulation
**Content:**
You are a Testing Tooling Engineer. Build a mock LLM server for deterministic tests.

Behavior: [CONFIG]

Design:
1. SERVER — Use wiremock or axum to listen on localhost.
2. MATCHING — Match requests by path, body JSON includes certain strings.
3. RESPONSES — Return specified JSON with tokens, delay, error.
4. STATE — Support sequence of responses per conversation.
5. LOGGING — Record all requests for assertion.
6. RESET — Clear state between tests.

No follow-up questions unless input missing. State assumptions explicitly. Return a completion matrix.

---

## Regression Test Generator for Agent Behavior (865)
**Contract:** Input: agent specification and golden files. Output: a Rust test harness that replays conversations and asserts responses match golden expectations.
**Matrix:**
- Load test case: input messages, expected output
- Execute agent logic with recorded LLM responses
- Assert output matches golden with tolerance
**Content:**
You are a Test Automation Engineer. Build a regression suite for agent behavior.

Test Cases: [DIR]

Implement:
1. TEST CASE — JSON file with conversation, expected final message or tool calls.
2. MOCK LAYER — Intercept LLM calls, return recorded responses from test case.
3. EXECUTOR — Run agent logic, capture final output.
4. ASSERTION — Compare output with golden, allow minor variations (e.g., whitespace).
5. ORGANIZE — Group by agent/scenario.
6. CI — Run on every PR.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Fuzzing Input Generator for Prompts (866)
**Contract:** Input: prompt template and valid input schema. Output: a Rust fuzzer that generates malformed or edge-case variable values to test prompt robustness.
**Matrix:**
- Generate inputs using arbitrary crate
- Mutate valid inputs to produce edge cases
- Monitor response for crashes or infinite loops
**Content:**
You are a Security Testing Engineer. Build a fuzzer for agent prompt inputs.

Template: [TEMPLATE]
Schema: [SCHEMA]

Design:
1. GENERATOR — Use arbitrary to create varied inputs: empty strings, very long, unicode, special chars.
2. MUTATOR — Take valid input, flip bits, add injection strings.
3. RUNNER — Feed generated inputs to agent, capture response and errors.
4. DETECTOR — Flag panics, timeouts, or suspicious outputs.
5. CORPUS — Save interesting inputs for regression.
6. REPORT — Summarize findings.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Golden File Assertion for Agent Outputs (867)
**Contract:** Input: agent response and golden file path. Output: a Rust test utility that compares structured output with a stored golden file, updating with explicit flag.
**Matrix:**
- Serialize agent output to canonical JSON
- Compare with existing golden file
- Support update mode to accept new baseline
**Content:**
You are a Testing Tooling Engineer. Implement golden file testing for agent outputs.

Golden File: [FILE]

Build:
1. WRITE — In test, produce output, serialize with serde_json with sorted keys.
2. COMPARE — Read golden file, assert_eq; if different, fail with diff.
3. UPDATE — Environment variable UPDATE_GOLDEN=1 overwrites file with new output.
4. INTEGRATION — Add to standard test, fail CI if differences without update flag.
5. FORMAT — Ensure consistent formatting.
6. DOCS — Explain how to update goldens.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Continuous Integration Pipeline for Agent Harness (868)
**Contract:** Input: source code and test suite. Output: a CI configuration (GitHub Actions) that builds the Rust agent harness, runs tests, lints, and benchmarks.
**Matrix:**
- Cache Cargo dependencies for speed
- Run clippy and fmt checks
- Execute unit, integration, and benchmark tests
**Content:**
You are a DevOps Engineer. Generate a CI pipeline for a Rust agent harness repository.

CI System: GitHub Actions

Steps:
1. CHECKOUT — actions/checkout.
2. TOOLCHAIN — Install Rust stable, components (clippy, rustfmt).
3. CACHE — Cache ~/.cargo and target/.
4. LINT — cargo clippy -- -D warnings and cargo fmt --check.
5. TEST — cargo test --all-features.
6. BENCH — cargo bench (optional).
7. COVERAGE — cargo tarpaulin and upload.
8. BUILD — cargo build --release for artifact.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Docker Compose for Agent Service (869)
**Contract:** Input: service definitions and dependencies. Output: a docker-compose.yml that boots the agent harness with all required services (DB, cache, mock LLM).
**Matrix:**
- Define services with healthchecks
- Configure networks and volumes
- Use environment files for configuration
**Content:**
You are a Containerization Specialist. Write a Docker Compose setup for the agent system.

Services: [AGENT_SERVICE, DB, REDIS]

Produce:
1. SERVICE — Build from Dockerfile, publish ports, environment from .env.
2. DEPENDENCIES — Postgres, Redis with health checks.
3. MOCK — Optionally include mock-llm service for testing.
4. VOLUMES — Persist data.
5. NETWORK — Internal bridge.
6. COMMANDS — Provide Makefile targets: up, down, logs.

State assumptions explicitly. No follow-up questions unless input missing. Return a completion matrix.

---

## Kubernetes Manifest Generator (870)
**Contract:** Input: agent deployment scale and resource requests. Output: Kubernetes YAML manifests (Deployment, Service, HPA) for the agent harness.
**Matrix:**
- Define Deployment with resource limits
- Add liveness/readiness probes
- Configure HorizontalPodAutoscaler
**Content:**
You are a K8s Application Engineer. Generate production manifests for the agent harness.

Namespace: [NAMESPACE]
Replicas: [MIN/MAX]

Design:
1. DEPLOYMENT — Container image, env vars, resource requests/limits, security context.
2. PROBES — HTTP GET /health, /ready, with initial delay.
3. SERVICE — ClusterIP exposing agent API.
4. HPA — Scale on CPU/memory, min/max replicas.
5. CONFIGMAP — Non-sensitive config.
6. SECRETS — API keys, passwords.

No follow-up questions unless input missing. State assumptions explicitly.

---

## Canary Deployment for Agent Updates (871)
**Contract:** Input: new agent version and rollout percentage. Output: a Rust traffic splitter that gradually shifts traffic to new agent version and auto-rolls back on errors.
**Matrix:**
- Split traffic based on percentage config
- Monitor error rate on canary
- Automate rollback if error threshold breached
**Content:**
You are a Release Engineer. Implement a canary deployment mechanism for agent services.

Old version: [v1]
New version: [v2]

Design:
1. SPLITTER — Service mesh or custom proxy that routes X% of requests to new version.
2. CONFIG — Dynamically adjustable percentage via admin API.
3. MONITOR — Compare error rates and latencies between versions.
4. ROLLBACK — If canary error rate > 2x baseline, set percentage to 0, alert.
5. PROMOTE — If stable, increase to 100%, remove old version.
6. LOGGING — Tag requests with version header.

Do not ask follow-up questions unless input missing. Return a completion matrix.

---

## Health and Readiness Probe Design (872)
**Contract:** Input: service dependencies and critical checks. Output: a Rust health check module that exposes liveness and readiness endpoints for orchestration.
**Matrix:**
- Implement /healthz with simple OK
- Implement /readyz with dependency checks
- Return 503 if not ready, include details
**Content:**
You are a Reliability Engineer. Design health check endpoints for the agent harness.

Dependencies: [DB, REDIS]

Implement:
1. LIVENESS — Simple ping, always returns 200 if process alive.
2. READINESS — Check all critical dependencies: DB connection, Redis ping, model loaded. Return 200 if all ok, else 503 with JSON body describing failing checks.
3. ENDPOINTS — Using actix-web or axum, mount at /healthz and /readyz.
4. CACHING — Cache readiness result for a few seconds to avoid overloading checks.
5. TIMEOUT — Each check has timeout.
6. CONFIG — List of critical deps from config.

State assumptions explicitly. No follow-up questions unless input missing.

---

## Crash Loop Recovery and Autoheal (873)
**Contract:** Input: agent process crash frequency. Output: a Rust watchdog that detects crash loops, applies exponential backoff restarts, and eventually triggers alert.
**Matrix:**
- Track restart count and timestamps
- Implement exponential backoff on restart
- Alert and pause after max crash loop duration
**Content:**
You are a Site Reliability Engineer. Build a crash loop recovery controller for agent processes.

Max Restarts: [N]

Design:
1. SUPERVISOR — Monitor child process, on exit, check recent exit history.
2. BACKOFF — Delay restart by min(2^restart_count, max_delay) seconds.
3. CRASH LOOP DETECT — If restarts > N within time window, stop restarting, alert operator.
4. ALERT — Send incident notification with logs.
5. MANUAL — Provide API to reset crash counter and restart.
6. LOGGING — Record every restart with reason.

No follow-up questions unless input missing. Return a completion matrix.
