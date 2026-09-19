# Latin America market map: scoring detail and counterparty questionnaire

## Scoring dimensions (1 low – 5 high)

1. **Market size for our clients** — volume our target merchants (thin-margin, high-volume, cross-border) could route there.
2. **Share of local methods** — how much of the market runs on PIX-like, boleto-like or local card rails that global brands do not reach.
3. **Regulatory cost and time** — entity, licence or partner needed; months to legal operation. 5 = we already have an entity.
4. **Partner availability** — acquirers, banks and OTC partners willing to onboard us, meeting the acceptance criterion.
5. **Time to first live merchant** — months from decision to first reconciled settlement.
6. **Expected margin at local price** — whether 1% ICC++ holds after local costs.

## Current rows (19 Sep 2026)

- Brazil: entity live (A55 Payments Ltda); partner MoR live; cheapest product; DD2 in progress (secondary entity template from Double Diamond; three acquirers side by side, two OTC partners, by 1 Oct 2026). Scores Open.
- Colombia: A55 de Colombia S.A.S. owned; KYB kit ready; 16 counterparties mapped; Kushki in pipeline. Scores Open.
- Mexico: bank account exists; entity and legal minimums Open. Scores Open.
- Chile: legacy CLP book; decide whether it stays. Scores Open.

## Questionnaire for a prospective acquirer or OTC partner

1. Legal entity, licence, regulator.
2. Methods and card brands; 3DS and 2D support; international BIN acceptance; countries of issuance accepted.
3. Requirements to open our account: document list, KYB on us and on our merchants, PCI evidence expected.
4. Pricing: MDR or fee per method; scheme and interchange pass-through; FX spread; setup and monthly fees; minimums.
5. Settlement: window (D+n), cut-off time, currency, account where funds land, file format and time of the settlement file.
6. Reserve: percentage, basis (gross or net), holding period, release mechanics.
7. Disputes: chargeback process, pre-dispute alert compatibility (Chargeblast, CAID), fraud ratio thresholds applied.
8. Merchant onboarding: per-merchant requirements, MID creation time, prohibited MCCs, high-risk policy.
9. Anticipation: offered or not; cost; who signs assignments.
10. Contacts: operations, compliance, commercial; escalation path; response-time commitment.

Every answer is written into `company-os/product-tech/integrations.md` and `company-os/operations/operator-windows.md` before any contract is signed.
