# Routing and runtime boundaries

## Choose useful work before choosing a model

Use a task's context boundary, explicit interface and affordable evaluator to
identify an independent assignment. Prefer substantial bounded work over a swarm
of trivial calls. Use an inexpensive single-agent path when delegation would add
more waiting and interpretation than useful progress. Honor a requested provider
preference when useful work exists; do not translate it into an arbitrary token
percentage or a promise to exhaust a subscription.

Treat model capability and speed as task- and environment-dependent observations.
A main agent may implement, experiment and integrate while workers implement,
investigate or test. Do not bake a permanent GPT-plans/Grok-builds hierarchy into
the package. For example, an explicit Grok preference can assign Grok a CSV writer
and contract tests while GPT builds the export UI against the agreed interface.
A provider-preferred configuration might instead give Grok the feature's main
implementation and GPT an independent compatibility task plus integration.
Resolve exact models and controls at run time; those family names are examples.

For a slower worker, launch early and keep independent work available to the
main agent. Avoid a chain where every small main-agent step waits on another
worker response. Reassess based on accepted patches, repair work and critical-path
waiting. More aggregate compute can accompany a shorter wall time; neither
proves better quality. Do not report invented savings or equal-cost comparisons.

## Pi is a harness, not a subagent API

Plain Pi does not supply a built-in multi-agent scheduler. A skill contributes
instructions and files, not task isolation, a peer message bus or durable state.
Require a host-provided delegation API, an already installed reviewed extension,
or another explicitly selected adapter that can run Pi workers. Inspect its
actual controls before promising concurrency, cancellation or nested teams.

Do not install extensions, start background CLI agents, create services, or build
an A2A server as a fallback during a worksharing run. Report an unavailable Pi
adapter rather than silently switching to a different harness. Installing the
package does not prove provider authentication or authorize API-key billing.

## T3 Code adapter

Follow the host's orchestration rules first. Discover `orchestrator_capabilities`
before the first delegation and retain the catalog for that run; refresh only
as the host permits. Resolve the runnable Pi instance and exact provider-qualified
model ID. A typical launch uses `delegate_task` with explicit
`target.providerInstanceId`, `target.model` and supported `target.options`, such
as `thinking=high` when advertised. Do not invent unsupported option keys, literal
token budgets or service-tier controls.

Use `isolation: "worktree"` for independent code-writing delegates and let T3
prepare the checkout. A prepared child starts from the parent's committed
snapshot, not its uncommitted edits. Pass authorized dirty inputs explicitly as
a bounded snapshot, or make an authorized checkpoint first. Never tell children
to create worktrees themselves. Keep shared-workspace tasks read-only unless the
host can guarantee a sole writer and the task needs that exact workspace.

Use `delegate_task` for other models or requested settings and separate checkouts
as the host requires; native delegation is appropriate only where the host allows
it without defeating Pi/model/isolation choices. Do not make top-level threads
for subagents. Use task completion notifications rather than polling a live task;
read `task_status` only at the completion/handoff point permitted by the host.
Use task cancellation for abandoned/replaced work. A new correction/review is a
new task where required, not a message to a finished child thread.

Keep global launch and concurrency counts across teams, coordinators, worker
replacements and repairs. Do not bypass a host's nesting limit with shell-spawned
agents. If a logical team must run flatly, let the root own dispatch and record
that its team lead did not itself launch workers.

## Other adapters and peer teams

Require documented equivalents for model selection, task lifecycle, isolation,
context handoff, cancellation and any selected permission boundary. Record the
actual adapter, not a T3 tool name it does not expose. Prefer a bounded blocked
result to an improvised unsupervised CLI process.

Use direct peer communication only with an existing supported capability. Label
lead-relayed messages as relayed. Keep one owner for each mutable resource and
version interfaces before sharing updates. Treat a shared workspace and context
exchange as a team pattern, not automatically a leaderless swarm. Reserve a
leaderless swarm for an explicit request and a runtime with enforceable task
claims, permissions, termination and observability; report it unsupported rather
than simulating those guarantees in prose.
