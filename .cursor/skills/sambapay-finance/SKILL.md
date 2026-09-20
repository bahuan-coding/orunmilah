---
name: sambapay-finance
description: Finance for SambaPay: the paytech business model (1% ICC++ pass-through pricing), unit economics per transaction, rolling reserve mechanics, breakeven arithmetic, cash, FX corridors, PaySecure legacy balances, and the finance sections of the London pack. Use when André Silva asks about money, pricing, margin, breakeven, cash, reserve, or how to explain any of these to someone who is not in finance.
disable-model-invocation: true
---

# SambaPay finance

## Files this skill owns

- `company-os/finance/README.md` — model, objective 2 plan, cost book (board view), legacy balances with PaySecure.
- `company-os/finance/model.md` — the five numbers, breakeven arithmetic, per-transaction template.
- `references/unit-economics.md` — the waterfall with the real CLP example.
- `references/business-committee.md` — thesis (cheap-market presence) and October arithmetic. The eight cannot be told that 1 October has no volume and that 31 October is breakeven.

## Before using any number

Ask four things and write them next to it: source, date, gross or net, currency. A number without all four is Open.

## The model in four lines

- Revenue = volume × take rate. Hansraj proposes the take rate so we cover the company's costs and hold a reserve. Until he proposes the number, working structure is 1% ICC++. Everything else (interchange, scheme, acquirer fee, FX) passes through at cost. A pass-through we fail to recover is our loss.
- Rolling reserve: omit a going-forward percentage from the Welcome Kit until named. Do not write 15% as the rule. Legacy books used 10%/9.58%; that is history, not the going-forward rule.
- Fixed costs are people and tools. Breakeven volume = fixed cost ÷ margin.
- Cash is what pays the fixed costs while volume is not there; runway = cash ÷ monthly fixed cost.

## Breakeven (objective 2)

1 October: DD2 accounts open, volume starts, day one of the month. 31 October: breakeven. The live book in September is zero. Do not write those as if 1 October were a day without volume. Fill `model.md`. Compute breakeven volume. Compare with the volume PaySecure and Finnera can bring by the date. If short, Plan B lines: cost-book actions, legacy releases, Finnera. Write the plan in `finance/README.md`; review in every weekly pulse. Thesis and October words: `references/business-committee.md`.

## Explaining to non-finance

Use one transaction of 100 as the story (see `references/unit-economics.md`). Name who receives each piece. End with "our part is the take rate Hansraj proposes; until then the working structure is 1; the rest passes through". Do not teach a going-forward rolling reserve percentage.

## Legacy balances with PaySecure

Eight points in `finance/README.md`. Owner is the D1 decision. Status of remittances and releases is Open until confirmed; ask before reporting.

## Depth

Card economics and fraud costs: `~/.cursor/skills/payment-security-specialist/SKILL.md`.
