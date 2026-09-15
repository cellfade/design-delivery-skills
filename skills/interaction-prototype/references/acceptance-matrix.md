# Risk-based prototype acceptance

Select applicable cases. Do not demand irrelevant states in a simple prototype.

| Case | What to inspect |
|---|---|
| Primary journey | Can the intended user reach the intended outcome from the real entry point? |
| Action first | Can someone begin with the prominent action before visiting prerequisite fields? |
| Missing input | Is the missing item named and reachable without losing completed work? |
| Conflicting input | Does validation identify the conflict and allow correction? |
| Valid input after failure | Does correcting the input remove the blocker and advance the state? |
| Unsaved draft | Do save, submit, cancel and reopen follow the declared draft policy? |
| Different records | Do switching records and roles preserve the right state without leaking another record's edits? |
| No finding or empty state | Is the routine case understandable without implying certainty or permission it cannot provide? |
| False positive / correction | Can a person correct the system and see the downstream result? |
| Additional information | Does new evidence reach the same record and trigger the appropriate reconsideration? |
| Delayed delivery | Are local, sent and received states distinguished if the scenario requires them? |
| Stale action | Can a pending old action still take effect after its evidence or decision is superseded? |
| Repeated action | Do double submit, repeated requests and retries create misleading duplicates? |
| Unavailable evidence | Can the person report failure and see a valid next step? |
| Audit / export | Does the record describe what happened without claiming a downstream process completed? |
| Reset and presets | Does reset clear intended state, and is preset navigation clearly different from workflow progress? |
| Keyboard / constrained viewport | Are primary actions and recovery controls reachable and readable? |

## Evidence record

Case ID; risk; revision/environment; initial record and role; actions; expected result; observed result; screenshot paths; result; untested limits.

When screenshots include generated evidence or synthetic records, preserve that designation. Keep intermediate failing captures distinguishable from final verified captures.

## Readiness wording

Prefer: “The listed release, correction and offline sequences passed on this revision; external delivery is simulated.”
Avoid: “Everything works,” “all possible states are covered,” or “user tested” when only an agent performed the walkthrough.
