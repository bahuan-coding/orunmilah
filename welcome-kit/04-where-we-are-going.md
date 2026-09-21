# 04 · Where We Are Going

Status: In discussion

These are the objectives as discussed so far, September 2026. Numbers follow the original list; 10 was not assigned. Every objective gets an owner and a date before it is called live. What is marked Open is being decided, not hidden.

## Rails

**1. Production volume on DD1 Cielo; DD2 opens in parallel.** We go to production with DD1 Cielo for volumes. That is the rail that carries the book. DD2 is our secondary entity template in Brazil, built on the requirements mapped by Double Diamond. We open it in parallel. It does not gate volume. Double Diamond finishes the template for the checklist: the full document package needed to open acquirer accounts. Validate everything required to open our own accounts with **Cielo, Asaas and EFI**. Cielo is also the live partner Merchant of Record today, and the acquirer on DD1. Production API keys from those acquirers go to the core team; the integration is deployed on PaySecure's white label, where we configure and reconcile. Factoring covers all volumes with 100% anticipation, even where Brazilian credit would take D+30; nothing more; the price must be competitive; nobody sells this to us as a vendor. Re-establish the remittance path with two on-ramp desks, MIPPO/GFS/OrbiFi and Transfero, that turn our reais into USDC in our own wallet for us to send to PaySecure, at a cost no higher than we had before. The three DD2 acquirers run side by side: that is how volume scales horizontally once that template is open. 1 October is day one of October volume, on DD1 Cielo: a partial of the month. 31 October is breakeven. The indicative all-in to stand up one entity and open the three acquirer accounts is about R$ 5,000: lawyer; digitising the company, including 2-step verification on mobile phones for bank and acquirer apps where required; CNPJ; access to the three counterparties. It is a single indicative price. No DD2 entity has been opened and no contract is signed. Open: the day the first DD1 production volume posts; the date DD2 accounts are open.

**5. 3DS and 2D traffic from the US and Europe, with international BIN acceptance.** We focus market enablement on Brazil, Mexico and Colombia. The minimum acceptance criterion for any rail: it processes both 3DS and non-3DS (2D) card traffic originated in Europe and the United States, and it accepts international BINs.

**6. LATAM expansion template. Priority 2.** With legal counsel in each country, establish the minimum we need to operate. Then complete a live registration with each entity, with one 2D supplier in production.

## Money

**2. Breakeven by 31 October 2026.** Do whatever it takes, with a Plan B ready if the primary path fails, to get out of the red. The live book in September is zero until DD1 Cielo carries production volume. From 1 October, volume is on, on DD1 Cielo: that is day one of the month. 31 October is when we cover our costs. Cruise volume is USD 100,000 a day. Hansraj proposes the take rate so we cover the company's costs and hold a reserve. The number is Open. Operational cash reserve is zero. Cielo's MDR at that cruise volume is the 19 September table.

**4. LATAM for European and American cardholders and issuing BINs.** Define the offer that gives those cardholders, identified by those BINs, access to local commercial policy in Latin America, the most cost-efficient market in the world. There is a live opportunity with Finnera of about USD 25 million a month in volume. Renato Paulino will follow up.

## Website Factory (local merchants who want to digitise)

**3. Website Factory.** An orchestration swarm of AI and product managers specialised in each business, producing each digitisation case specifically. In each geography where we have structure, we serve local merchants who want to digitise in that economy: from the CNPJ through operational management with the local entities, until payout. They use our capture channels as a local player. A client's Brazil store uses the same factory. Success of the live site: SimilarWeb and online page validators read it as genuine, high-quality ("top A") — traffic profile, authenticity, organic competitiveness. Commercial owner: Open. Named product managers in the swarm: Open.

## Merchant pipeline

Local merchants through the Website Factory, and merchants who arrive through clients. We do not take our clients' merchants. The checks below apply to both.

**7. Every merchant on the rail in use has its checklist done.** On DD1 Cielo: Cielo's checklist. On DD2: the requirements of all three acquirers connected to the template. Nothing missing before go-live.

**8. Chargeblast: add the CAID.** Configure the pre-dispute alerts solution. No merchant goes live before its CAID is registered with Chargeblast.

## Compliance

**11. Global Pass.** KYB software. Screen every merchant before sending it to any acquirer on the template, so we never breach a PEP or sanctions rule. Diligent from day zero with every new acquirer.

**12. Jumio.** Same purpose: identity verification.

**13. G2.** Same purpose: merchant risk screening.

## Tools

**9. Five Android phones.** Operational phones for hiring. They are also the handsets for 2-step verification on bank and acquirer apps when DD1 Cielo or the DD2 accounts require it.

## Licence

**14. We will be a sub-acquirer, then a payment institution.** We are cross-border players. Sub-acquirer is the status we take next: own merchant IDs at Cielo, Asaas and EFI on DD2, registered with Visa and Mastercard through each acquirer, under the acquirer's licence, not yet a payment institution. Production volume runs on DD1 Cielo while we open DD2 in parallel. The payment-institution path stays the structural moat; filing starts the day sub-acquiring is live. The Central Bank's grant date is not ours to promise. A committee of agents, not people, designs the path. André Silva decides.

## How we get there: process concerns

- Reconciliation is the first job of every day. Hansraj (PaySecure) confirms it. He works the reconciliation SLA together with the Brazilian acquirer processes. The hour is Open.
- Sridhar helps André Silva obtain a Power of Attorney to re-establish the FX contact and contract so settlements can start. Open: Power of Attorney in hand; contract signed. Then we design the reconciliation-to-remittance process.
- On-ramp, from the local bank to PaySecure. Two paths: Cielo's tokenized-PIX rail, or an OTC desk that turns our reais into USDC in our own wallet, which we send on to PaySecure. Objective 1 re-establishes two desks: MIPPO/GFS/OrbiFi and Transfero.
- Operator windows: every operator's cut-off, the daily calculation, and from where and at what time funds are sent onward. Open.
- Factoring: cover all volumes with 100% anticipation, even where Brazilian credit would take D+30; nothing more; the price must be competitive. Nobody sells this to us as a vendor.
- Entity structuring for DD2: options to discuss with Double Diamond, the firm mapping what it takes to open an entity in Brazil. Opened in parallel with DD1 Cielo production. Open: which options, by when.

## How a merchant is created

1 Document validation (KYB screening and the checklist of the rail in use). 2 Website Factory digitisation, from the CNPJ through operational management with the local entities. 3 MID creation (and the CAID). 4 Go live (CAID registered at Chargeblast; the merchant joins the daily reconciliation; payout follows).
