# Operator windows

Every operator's cut-off, settlement window, where funds land and when they move onward. Times in São Paulo time.

| Operator | Type | Currency | Cut-off | Settlement | Funds land in | Sent onward at | Who confirms | Source document |
|---|---|---|---|---|---|---|---|---|
| Partner MoR: Cielo / tokenized-PIX rail | PIX rail | BRL | Open | Open | PaySecure balance | Open | Hansraj | Open |
| Cielo | Acquirer | BRL | Open | Open (D+n) | Local account | Open | Thiago | Open |
| Asaas | Acquirer | BRL | Open | Open (D+n) | Local account | Open | Thiago | Open |
| EFI | Acquirer | BRL | Open | Open (D+n) | Local account | Open | Thiago | Open |
| On-ramp desk 1: MIPPO/GFS/OrbiFi | OTC desk | BRL → USDC | Open (same-day PIX) | Same day | Our attested wallet | Open | Taina | A55_OTC_Action.pdf, 18 Sep 2026 |
| On-ramp desk 2: Transfero | OTC desk | BRL → USDC | Open (same-day PIX) | Same day | Our attested wallet | Open | Taina | A55_OTC_Action.pdf, 18 Sep 2026 |
| Our attested wallet | Custody hop | USDC | — | — | PaySecure wallet, on our instruction | Open | Thiago (custody), Taina (instruction) | Open |
| Local bank (Open) | Bank | BRL | Open | same day | — | Open | Taina | Open |
| PaySecure | Group | USD/EUR | Open | Open | PaySecure balance | — | Hansraj | Open |

Daily calculation (to define with the rows above): for each operator, gross settled − fees − reserve held + reserve released − refunds − chargebacks = net available; sum of net available = amount remitted.
