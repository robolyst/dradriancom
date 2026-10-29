# DrAdrian redesign

## Audit

Audited the live HTML at https://dradrian.com on 29 October 2026 and the master branch of robolyst/dradriancom. The live page matched the repository homepage.

- The near-full-screen opening carried a name, a broad developer/data-engineer title and social icons, with no specific proposition or contact action.
- The biography presented breadth before explaining its relevance to a trading team.
- Employer logos provided little role context; BlueCrest was absent.
- Recent quantitative publications were not individually surfaced. The long mixed works list diluted the hiring narrative.
- Custom elements replaced semantic headings; social images lacked accessible names; the footer had a malformed anchor. External font loading was unnecessary.

## Design proposal and page structure

An understated editorial page using warm white (#faf9f6), navy (#142838), copper (#936345), serif display type and system sans-serif body text. No external font dependency or animation.

1. Hero: “I turn quantitative research into production trading systems.” Role, London location, contact action and employer context.
2. Approach: quantitative research, production engineering, technical ownership.
3. Experience: BlueCrest, Millennium, Akuna, Lick, Airtasker, with concise responsibility descriptions.
4. Writing: selected OSQuant articles on factor models, CVaR, covariance and monitoring.
5. Open source: recx and streetview, explaining purpose and engineering relevance.
6. Research background: native expandable list of selected peer-reviewed work.
7. Contact: invitation for relevant London roles; verified existing email and LinkedIn destinations.

## Factual basis

Employer responsibilities draw on the user's supplied career context and redesign brief. Dates and current-employment status are deliberately omitted because a complete current CV was not supplied. “Senior Quantitative Developer” is professional positioning, not a claim about an employer's contractual job title. No performance, P&L, latency, strategy parameters, dataset names or proprietary implementation details are included.

Existing homepage: https://dradrian.com/
Public writing, titles, authorship and article metadata checked against https://osquant.com/ and the linked article pages. The featured matrix is decorative, not measured market data. Project descriptions and contact destinations are retained from the original homepage; no adoption or audience statistics are asserted. Academic links retained from original source, excluding entries with apparent metadata inconsistencies.

## Implementation

Dependency-free HTML/CSS. Root index.html remains the entry point for existing static hosting. Run `python scripts/build.py` to generate a dist directory for preview/static export. The preview hosting manifest serves only dist, keeping repository documents out of the published export.

Keyboard focus, skip navigation, labelled landmarks, semantic headings and native details disclosure. Responsive layouts at 700px and 1000px. All substantive content and navigation work without JavaScript.

## Revision following visual feedback

The first direction leaned too heavily on a generic portfolio vocabulary: numbered sections, three matching capability columns, repeated promotional headlines and a decorative factor-model graphic. Following feedback, these were removed. The final direction uses an asymmetric personal introduction, employer responsibilities, a dated reading list and compact project descriptions. Copper is limited to small details and links; there are no coloured section bands or promotional closing slogans.
