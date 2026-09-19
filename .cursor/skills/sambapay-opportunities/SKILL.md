---
name: sambapay-opportunities
description: Market and rail opportunities for SambaPay in Latin America: scoring new markets and acquirers, the acceptance criterion (3DS and 2D from the US and Europe, international BINs), the questionnaire for a prospective acquirer or OTC partner, the pipeline register and the Finnera opportunity. Use when André Silva asks whether to open a market, sign an acquirer or OTC, or how to evaluate volume from a prospect.
disable-model-invocation: true
---

# SambaPay opportunities

## Files this skill owns

- `company-os/opportunities/README.md` — focus, scoring, open items.
- `company-os/opportunities/latam-map.md` — one row per market.
- `company-os/commercial/pipeline.md` — one row per prospect or partner.
- `company-os/product-tech/integrations.md` — one row per counterparty.
- `references/latam-market-map.md` — scoring detail and the counterparty questionnaire.

## Acceptance criterion for any rail (objective 5)

Processes 3DS and 2D card traffic originated in Europe and the United States; accepts international BINs; documented settlement window; passes the acquirer's KYB and PCI requirements. A rail that fails one of these is not scored; it is declined.

## Scoring (1–5 each, total of 30; below 15 waits)

Market size for our clients; share of local methods; regulatory cost and time to enter; partner availability; time to first live merchant; expected margin at local price. Write the six numbers and one line of reason in `latam-map.md`.

## Evaluating a prospect's volume (Finnera and others)

Volume is not revenue. Ask: currency, monthly volume, methods, 3DS or 2D share, average ticket, refund and chargeback history, countries of the shoppers, when it can start. Revenue estimate = volume × 1%. Put the row in `pipeline.md` with stage and next step.

## Evaluating an acquirer or OTC partner

Use the questionnaire in `references/latam-market-map.md`. Every answer goes to `integrations.md` and `operations/operator-windows.md`. No contract before the questionnaire is complete. The signup itself, from first contact to first live transaction, is Abner Maioralli's process (P33, Head of Partner Enablement); this skill scores and asks, Abner lands the rail and reports the metrics in `integrations.md`.

## Current focus

Brazil (DD2 by 1 Oct 2026: the secondary entity template built on Double Diamond's requirements, three acquirers side by side plus two OTC partners), then Colombia (entity owned; registrations via the Break Even tool), then Mexico (legal minimums, objective 6).

## The pattern for every market (horizontal scaling)

Entity first, then several rails side by side, then merchants spread across them. One acquirer is a start, never a plan. Score a market only when at least two rails meeting the acceptance criterion are available.
