# Token usage without savings promises

[Português](tokens.md) · [Back](../README.en.md)

There is no reliable usage percentage for this selection without measuring real tasks. A shorter profile contains less text, but that does not determine total execution usage.

| Situation | What happens |
| --- | --- |
| Downloading or copying profiles with the local installer | No model calls. |
| Making profiles available in Codex | May add metadata to context, depending on the client. It does not start six tasks by itself. |
| Assigning a task to an agent | Instructions, context and responses contribute to usage. |
| Running several agents | Adds individual processing and coordination. |
| Watching local Habblaud animations | Visualization does not require a new model response. |
| Sending work or messages through Habblaud | The agent may consume additional tokens. |

## Arithmetic examples, not forecasts

These numbers are invented solely to explain the comparison. They are not measurements of this package, industry averages or an expected range.

| Hypothetical scenario | Without selection | With selection | Change |
| --- | ---: | ---: | ---: |
| An extra review adds work | 10,000 tokens | 13,000 tokens | +30% |
| A review prevents repeated attempts | 10,000 tokens | 8,000 tokens | −20% |

Formula: `(total with profiles − total without profiles) ÷ total without profiles × 100`.

The 13,000 example could include 8,000 for the main agent, 3,000 for a reviewer and 2,000 for coordination. That breakdown is also fictional. In real measurements, check whether a parent's counter already includes children to avoid double-counting.

There is no single conversion rate from tokens to money: model, input, cached input, output, reasoning and billing method may differ. Do not add reasoning again if the provider already includes it in output totals. With subscriptions, also track the product's displayed usage and limits.

## Measure actual results

1. Pick a small task with objective success criteria.
2. Keep the project revision, model, reasoning effort and tools consistent.
3. Run once without these profiles and once with the selected profile, starting from equivalent states.
4. Record all involved sessions' usage, time, confirmed findings and tests. Note cache and context differences.
5. Repeat across more tasks. Compare quality alongside cost; one trial does not establish a general advantage.

To limit wasted work, narrow each assignment, avoid duplicate full-project reads and request short conclusions with references. Add agents when there is distinct work for them. These are guidelines, not a savings guarantee.

## Sources

- [OpenAI: subagents, usage and configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents).
- [Habblaud: local sources, integration and messages](https://github.com/marmottajr/habblaud).
- [Agency Agents: comparative evaluation discussion](https://github.com/msitarzewski/agency-agents/discussions/434).
