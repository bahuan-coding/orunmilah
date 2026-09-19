# Unit economics: one transaction, step by step

## Structure (variables until real rates are known)

Gross G. Interchange I, scheme fees S, acquirer fee A (together "bank fee" B when the acquirer bundles them), FX F. Our margin M = 1% of G. Reserve R = 10% held.

Net to merchant now = G − B − F − M − R. R is released later, net of refunds and chargebacks. Our revenue = M. Our cost = anything in B or F not recovered from the merchant.

## Real example (CLP book, May file, from the PaySecure response email)

- Gross: 100.00
- Bank fee (flat, pass-through at cost): 3.20
- a55 margin: 1.00
- Reserve held: 10% of (100.00 − 3.20 − 1.00) = 9.58 (net base; BRL used 10% of gross = 10.00)
- Net settled to PaySecure now: 100.00 − 3.20 − 1.00 − 9.58 = 86.22; 9.58 released as it matures.
- Some cards and instalments carried a higher acquirer MDR, up to 4.15%; still pass-through at cost.

## Reserve basis

BRL: 10% of gross. CLP: 10% of net (9.58%). PaySecure point 7: standardise on one basis. Impact on the May book: about USD 1.8K in PaySecure's favour. Decision Open.

## FX

Vector era: FX as a 2% spread, being corrected to 1%. PagSeguro era: explicit 3% FX line. The on-ramp itself (A55 Payments process, 18 Sep 2026 pack): same-day PIX to an OTC desk, USDC into our own wallet, USDC to PaySecure; cost = reais paid − (dollars × that day's PTAX); history about 36.5 bps on the MIPPO book; GFS paper at spot + 0.25%; USD wire about 65 bps as backup. Objective 1: two desks at cost no higher than before. We add no FX markup of our own.

## Factoring

Factoring is our going-forward model: all volumes anticipated, even where Brazilian credit would take D+30, at a competitive price. Nobody sells this to us as a vendor. The historical AmFi pools (A55 junior quota, senior repaid first) are a separate close-out book, not this model. Internal owner of the Factoring process (P29) is still unnamed.
