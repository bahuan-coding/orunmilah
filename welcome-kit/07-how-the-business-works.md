# 07 · How the Business Works

Status: In discussion

Written so engineering understands the money and finance understands the flow. Local merchants through the Website Factory, and merchants who arrive through clients. The flow runs on PaySecure's white label, always-on.

## A payment, in eight steps

1. A shopper pays at the checkout of a store digitised by the Website Factory, or the merchant's own site using our checkout.
2. PaySecure's white label captures the transaction and routes it to the right rail for the method: card (3DS or 2D), PIX, boleto.
3. The acquirer or rail authorises. The approval rate is measured here. Approval times margin is the number we live on.
4. The acquirer settles funds into our local account on its window (D+n). Every operator has a cut-off. Open: those windows are still being written.
5. Reconciliation. The acquirer's file is tied to our ledger line by line. Nothing downstream is trusted until it ties. Hansraj (PaySecure) confirms. He works the reconciliation SLA together with the Brazilian acquirer processes. The hour is Open.
6. Fees, rolling reserve, refunds and chargebacks net out.
7. Remittance: local bank to PaySecure, by one of two paths. The partner's tokenized-PIX rail; or an OTC desk that takes our reais by same-day PIX and sells us USDC into our own wallet, which we then send to PaySecure. The desk's cost is measured against PTAX, the official daily rate. Sridhar helps André Silva obtain a Power of Attorney to re-establish the FX contact and contract so settlements can start. Open: Power of Attorney in hand; contract signed.
8. PaySecure pays the merchant.

## Where the money is made

We price as a margin over cost: ICC++. Acquirer, scheme and FX costs pass through at cost, with no markup. Our fee is the spread above cost. Hansraj proposes the take rate so we cover the company's costs and hold a reserve. Until he proposes the number, the working structure is 1% ICC++.

Operational cash we hold ourselves is zero.

Volume times margin rules everything. Our clients run on thin margins and high volume; a small rate change moves their whole result and ours. Latin America is the most cost-efficient market in the world. That is why the company is here. The priority is to give European and American cardholders, identified by those issuing BINs, access to a local commercial policy.

## Who carries the risk today

**Cielo** acts as Merchant of Record: it carries the merchant risk and the rolling reserve, and is connected to a growing set of local acquirers. We operate as payment facilitator on that rail. We go to production with DD1 Cielo for volumes. We open DD2 in parallel. We take production API keys from the acquirers, deliver them to the core team, and configure and reconcile on PaySecure's white label. We bring the rails and the relationships. PaySecure brings the flow. We will be a sub-acquirer, with own merchant IDs on DD2. The payment-institution licence follows.

## Money in motion, every day

Reconciliation is the first job of every business day. Then money moves: refunds and cancels (Clayton), payouts, reserve and FX (Taina), collections and payables (Rafaela). Factoring: cover all volumes with 100% anticipation, even where Brazilian credit would take D+30; nothing more; the price must be competitive. Nobody sells this to us as a vendor.

## How a merchant is created

1 Document validation: KYB screening (Global Pass, Jumio, G2) and the checklist of the rail in use (Cielo on DD1; all three acquirers when the merchant sits on DD2). 2 Website Factory digitisation, from the CNPJ through operational management with the local entities. 3 MID creation at the acquirers, and the merchant's CAID. 4 Go live, only after the CAID is registered with Chargeblast; the merchant joins the daily reconciliation; payout follows.
