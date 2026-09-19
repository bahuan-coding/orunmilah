# Operations

Purpose: merchant onboarding, operator windows, reconciliation, remittance.
Owner: Thiago (desk, reconciliation). Merchant creation: Clayton. Money out and remittance: Taina.
Cadence: reconciliation first, every business day; Hansraj (PaySecure) confirms; SLA Open (default: our figure by 11:00 São Paulo).
Registers: `merchant-onboarding.md`, `operator-windows.md`.

## Daily routine (manual until the remittance contract is signed)

1. Pull every operator's settlement file for the previous window.
2. Tie each file to the ledger line by line; record differences with the operator's reference.
3. Post the day's figure to reconciliation@sambapay.tech; Hansraj confirms.
4. Only then: refunds and cancels (Clayton); payouts, reserve, FX (Taina); collections and payables (Rafaela).
5. Remittance to PaySecure per the on-ramp: local PIX → partner tokenized-PIX rail → PaySecure balance. Open: contract; who instructs; time of day.

## Process concerns carried from the objectives

- Reconciliation-to-remittance process is designed after the remittance contract is signed.
- Operator windows: define every cut-off, the daily calculation, from where and at what time funds start being sent onward.
- Factoring: cover all volumes with 100% anticipation, even where Brazilian credit would take D+30; nothing more; the price must be competitive. Nobody sells this to us as a vendor.
- DD2 entity structuring: options to discuss with Double Diamond, the firm mapping the requirements to open an entity in Brazil. Open: options and decision date.

## Open

D5; every row of `operator-windows.md`; Double Diamond fee and date; P29 Factoring process owner (internal).
