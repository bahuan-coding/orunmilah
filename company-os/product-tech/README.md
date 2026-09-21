# Product and technology

Purpose: the payment engine, the acquirer integrations, the Website Factory.
Owner: Leandro. Operating desk and secrets: Thiago.
Cadence: integrations register updated on every change; incidents reported the hour they appear.
Registers: `integrations.md`.

## What we run

- Payment engine in operation: PaySecure's white label. Always-on culture; processors, authorisation, tokenisation, 3DS, acquirer performance, Chargeback API. We obtain production API keys from acquirers and deliver them to the core team; we configure and reconcile on that instance. The engine is not allowed to go down. Traffic is twenty-four hours, every day, from everywhere. Years of history without unavailability. Same architecture throughout; more than R$ 3 billion already processed on this premise. New technology has been absorbed as it arrived. The live book today is a separate number (the live book in September is zero until DD1 Cielo carries production volume; we go to production with DD1 Cielo; DD2 opens in parallel; 1 October is day one of October volume).
- Merchant portal: onboarding, KYB, proposals (Clayton operates). Local merchants through the Website Factory, and merchants who arrive through clients.
- Operating desk: queues, credit, identity, custody, Key Vault.
- Stack named in internal PCI documentation (verify what is live for SambaPay): Azure Container Apps, PostgreSQL Flexible Server, Redis, Key Vault; Cloudflare WAF; Netlify-hosted checkout page; AWS Cognito SSO; CyberSource tokenisation; Braspag 3DS.

## Website Factory (objective 3)

- An orchestration swarm of AI and product managers specialised in each business. Each digitisation case is produced specifically.
- In each geography where we have structure: local merchants who want to digitise, from the CNPJ through operational management with the local entities, until payout. They use capture channels as a local player. A client's Brazil store uses the same factory.
- Build of the swarm: Leandro (D4). Commercial owner: Open. Named product managers in the swarm: Open.
- Success of the live site: SimilarWeb and online page validators read it as genuine, high-quality ("top A").

## Acceptance criterion for any new rail (objective 5)

Processes 3DS and 2D card traffic originated in Europe and the United States; accepts international BINs; settles on a documented window; passes the KYB and PCI requirements of the acquirer.

## Horizontal scaling (objective 1 and beyond)

Volume grows by integrating several acquirers per market side by side, never by depending on one. Production volume runs on DD1 Cielo. DD2, the secondary entity template in Brazil built on Double Diamond's requirements, opens in parallel with three acquirers and two OTC partners. Every new market repeats the pattern: entity, then several rails, then merchants spread across them. The engine routes each transaction to the rail with the best approval at the best cost.

## Open

Partner MoR is Cielo; Double Diamond fee and date; which stack components are live; Website Factory commercial owner; Factoring process owner (internal, P29). Brazilian / 2D acquirer restart is André Silva (P30).
