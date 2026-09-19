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

## Before using any number

Ask four things and write them next to it: source, date, gross or net, currency. A number without all four is Open.

## The model in four lines

- Revenue = volume × margin. Margin is 1% (ICC++). Everything else (interchange, scheme, acquirer fee, FX) passes through at cost. A pass-through we fail to recover is our loss.
- Rolling reserve 15% is held, not earned; it is released as it matures, net of refunds and chargebacks. Legacy books used 10%/9.58%.
- Fixed costs are people and tools. Breakeven volume = fixed cost ÷ margin.
- Cash is what pays the fixed costs while volume is not there; runway = cash ÷ monthly fixed cost.

## Breakeven (objective 2)

Fill `model.md`. Compute breakeven volume. Compare with the volume PaySecure and Finnera can bring by the date. If short, Plan B lines: cost-book actions, legacy releases, Finnera. Write the plan in `finance/README.md`; review in every weekly pulse.

## Explaining to non-finance

Use one transaction of 100 as the story (see `references/unit-economics.md`). Name who receives each piece. End with "our part is 1; the rest passes through". Then the reserve: "10 waits, then comes back".

## Legacy balances with PaySecure

Eight points in `finance/README.md`. Owner is the D1 decision. Status of remittances and releases is Open until confirmed; ask before reporting.

## Depth

Card economics and fraud costs: `~/.cursor/skills/payment-security-specialist/SKILL.md`.
