# Feasibility and roadmap

## Available resources

The team has four M4 MacBook Air machines. A Pi 4-class node and a controlled CAN bench are planned. Fleet clients and V2X traffic will initially be simulated. The dashboard and AI orchestration can run on a Mac separately from the Pi.

## Team budget ceiling

These are planning allocations from the proposal, not current vendor quotations.

| Allocation | INR |
|---|---:|
| Pi and essentials | 9,000 |
| CAN interface and bench | 4,000 |
| Storage and cables | 2,000 |
| API and testing | 2,000 |
| Contingency | 3,000 |
| **Total** | **20,000** |

NVIDIA API access is a candidate, subject to available models, access terms and quotas. Free API availability is not assumed. AI outages must not stop deterministic detection or evidence logging.

## Staged milestones

| Stage | Planned work | Exit evidence |
|---|---|---|
| 1. Review and specification | Literature comparison, scope, threat assumptions, event schema and label taxonomy | Reviewable design and agreed experiment protocol |
| 2. Data and baselines | CAN ingestion, V2X simulation, synchronized scenarios, independent detectors | Reproducible baseline runs and checked labels |
| 3. Attribution and fleet | Timing policy, DYNOTEARS comparison, signed votes and fallback | Ablations and documented fault behaviour |
| 4. GhostTrace | Hash chains, receipts, retained evidence and reconciliation | Tampering/outage test results |
| 5. Investigation and SOC | Read-only agent, cited hypotheses, dashboard and human review | Report-quality and permission-enforcement evaluation |
| 6. Research package | Repeated experiments, edge measurements, dataset documentation and manuscript | Reproducible artifacts and supported contribution claims |

Dates and individual assignments remain to be agreed by the team. At repository creation, only the proposal, presentation, literature guide and planning documents are complete.
