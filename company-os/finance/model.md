# Finance model

Fill the blanks; each number needs a source and a date. Board view.

| Number | Value | As of | Source | Owner |
|---|---|---|---|---|
| Monthly processed volume (BRL) | Premises: today zero until DD1 Cielo carries production volume; cruise USD 100,000/day (confirmed) | 21 Sep 2026 | André Silva | André Silva |
| Realised take rate (%) | Open (Hansraj proposes so we cover costs and hold a reserve; working structure 1% ICC++) | 19 Sep 2026 | André Silva | Hansraj / André Silva |
| Fixed cost base per month (BRL) | Open. September salary book R$ 175,279.99 for seven people (ledger 22 Sep 2026). Providers are not in this figure. | 22 Sep 2026 | company-os/finance/history/2026-09/ledger.json | André Silva |
| Cash position (BRL, USD) | Operational cash reserve: zero (premise) | 19 Sep 2026 | André Silva | Taina |
| Reserve held by the partner MoR (BRL) | Open (legacy). Going-forward rolling reserve omitted from the kit until named | 19 Sep 2026 | André Silva | Taina |
| Receivable from PaySecure legacy items (USD) | about 680–710K actionable | email undated | Eight-point response | D1 owner |
| DD2 entity stand-up, one-off (BRL) | about 5,000, indicative all-in (lawyer; digitising including 2-step on mobile for bank/acquirer apps; CNPJ; three acquirer accounts). No contract | 19 Sep 2026 | André Silva | André Silva |
| Finnera volume if won (USD per month) | about 25,000,000 | 19 Sep 2026 | André Silva's note | André Silva |
| Capital for the licence path | Premise: the minimum funds for the elected modality (D22) | 19 Sep 2026 | André Silva | André Silva |

## Breakeven arithmetic

Breakeven volume per month = fixed cost base ÷ realised take rate.
Example with placeholders: R$ 180,680 ÷ 1% = R$ 18,068,000 of monthly volume, before CLT payroll and before any pass-through mismatch. Replace with real numbers.

## Unit economics per transaction (template)

| Line | Who receives | Basis |
|---|---|---|
| Interchange | Issuing bank | pass-through at cost |
| Scheme fees | Visa / Mastercard | pass-through at cost |
| Acquirer fee (bank fee) | Acquirer | pass-through at cost (example 3.20%) |
| FX / on-ramp | OTC desk (BRL → USDC into our wallet) | pass-through at cost; history about 36.5 bps against PTAX; target ≤ previous |
| SambaPay margin | SambaPay | take rate (Hansraj proposes; working 1%) |
| Rolling reserve | Held, then released | Open (omitted from the kit until named) |
