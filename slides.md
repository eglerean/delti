---
theme: ./slidev-theme-aalto-scicomp
themeConfig:
  palette: aalto-classic
  titles: aalto
  credit:
    text: Enrico Glerean · CC BY 4.0
    url: https://eglerean.github.io/
  download:
    url: /Glerean_2026_DataEthicsLawTechnology.pdf
    text: Download PDF
favicon: https://eglerean.github.io/favicon.svg
title: Data, ethics, law, technologies, individuals
author: Enrico Glerean
info: |
  Slides by Enrico Glerean (https://eglerean.github.io/), CC BY 4.0.
  Course: Digital Health and Human Behaviour
  Source: https://github.com/eglerean/delti
keywords: data ethics, GDPR, AI Act, MDR, EHDS, anonymisation, personal data, privacy, research ethics, Enrico Glerean, https://eglerean.github.io/
layout: cover
class: no-footer
hexText: "DATA\nETHICS\nLAW\nTECH"
hexSeed: 7
---
###### CS-E4150 - Digital Health and Human Behavior

# Data, Ethics, Law, Technologies, Individuals
Applied data ethics for digital health

::presenter::
**Dr. Enrico Glerean**, Staff Scientist, Aalto University, November 2026

<div class="license-line"><CcBy /> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a> · <a href="https://github.com/eglerean/delti" target="_blank" rel="noopener" class="gh-link" title="Slides on GitHub" aria-label="Slides on GitHub"><carbon-logo-github class="gh-icon" /></a></div>

<style>
h1 { font-size: 2.5rem !important; line-height: 1.1 !important; }
p { font-size: 0.95rem; }
.cover-presenter p { font-size: 0.85rem; }
.license-line { margin-top: 0.45rem; font-size: 0.75rem; white-space: nowrap; }
.gh-icon { vertical-align: -0.2em; width: 1.15em; height: 1.15em; }
.license-line a.gh-link { border-bottom: none; text-decoration: none; color: inherit; }
</style>

<!--
Lecture 6 of CS-E4150 Digital Health and Human Behaviour. Three hours with a 10-minute break.
The title is also the map: Data, Ethics, Law, Technology, Individuals. Every section divider shows where we are.
-->

---
layout: two-cols
---

::header::
# Outline: D·E·L·T·I

::left::

### Outline
1. Intro: Ethics is not Law
2. <b>D</b>ata about individuals
3. <b>E</b>thics
4. <b>L</b>aw
5. <b>T</b>echnology
6. <b>I</b>ndividuals
::right::

### Learning outcomes

After this lecture you can:

1. Understand the fundamental principles of ethics and law in research and innovation with data from individuals
2. Evaluate where ethics and law might diverge
3. Apply appropriate technological solutions for dealing with sensitive data


---
layout: default
---

# Briefly about the speaker

**Enrico Glerean, DSc.**

- **Staff scientist and data agent** (background in neuroimaging), helping and training researchers with handling personal data (anonymisation, secure computing), medical images, clinical trials/Findata, research ethics and research integrity (AI and new technologies), statistics
- Other affiliations/COI: **CodeRefinery** (Nordic network to teach computational reproducibility), **Finnish Reproducibility Network** (national network to raise awareness in reproducibility), Support Pool of Experts at the **European Data Protection Board** (open training materials on personal data, AI and cybersecurity), Aalto University's representative at the **EU AI Act Advisory Forum**

<!--
Several slides in the T block draw on the EDPB book "Fundamentals of Secure AI Systems with Personal Data".
-->

---
layout: default
---

# You will make design choices that no DPO can undo later

- As a **researcher**, you design the processing: what to collect, from whom, where to compute, what to publish. The university is the controller, but your plan decides what it controls.
- As a **data scientist** in a company, the data protection officer advises and the product team decides. Accountability (GDPR Art 5(2), 24) sits with the organisation, and your design is what it is accountable for.
- In this course your data are mostly **health data**: they need a legal basis *and* an Article 9 condition, and often a DPIA.
- The law sets a **floor**. Ethics asks whether you should do it at all, and how well.

<div class="card yellow">

**Thesis of today:** ethics is not law. When they diverge, you have to resolve the gap, and document how you did it.

</div>

<!--
A DPO advises and checks. The design decisions are yours, and they are hard to change once data are collected.
-->

---
layout: section
color: dark
hexText: "D"
class: title-middle
---

# D. Data about individuals

<span class="delti-on">D</span> · E · L · T · I — what makes data personal, and when it becomes health data

---
layout: default
title: "Personal data is any information relating to an identifiable person"
---

###### D · Data about individuals

# Personal data is any information relating to an identifiable person

- **GDPR Art 4(1):** "any information relating to an identified or identifiable natural person"
- **Relating to:** by its content, its purpose or its effect on the person
- **Identifiable:** by any means *reasonably likely* to be used, by the controller or by anyone else (Recital 26)
- **Per entity:** the same dataset can be personal data for one holder and not for another (CJEU C-413/23 P, *EDPS v SRB*, 2025)
- **Out of scope:** truly anonymous data, and data of deceased persons (Recital 27), although national law may still protect them, e.g. patient records
- **Practical rule:** if you collect information **from** or **about** people, treat it as personal data

<!--
Students often think "personal data" means names. The definition is about identifiability and relation, not labels.
The SRB judgment matters for data sharing: what is anonymous for a recipient may still be personal for the sender who holds the key.
-->

---
layout: default
title: "Identifiers come in degrees, and sensor data are among them"
---

###### D · Data about individuals

# Identifiers come in degrees, and sensor data are among them

1. **Direct identifiers:** enough on their own to identify a person<br>- e.g. name, personal identity code, face image, voice, fingerprints, brain scan images, DNA
2. **Strong indirect identifiers:** identify a person fairly easily<br>- e.g. postal address, phone number, email address, a rare disease, a unique job title, student ID, IP address, cookie identifier, location data
3. **Indirect identifiers:** identify a person when combined with other information<br>- e.g. age, sex, education, occupation, income, marital status, mother tongue, place of work or study, postal code, municipality
4. **Sensor and behavioural data:** patterns that are unique to a person<br>- e.g. location traces, gait from accelerometers, ECG and heart-rate patterns, typing rhythm, sleep timing

<!--
Items 1 to 3 follow the three-tier scheme used by social science data archives.
Item 4 is the one that matters most in this course: none of these signals carry a name, and all of them can single people out.
-->

---
layout: default
title: "Sensor data identify people even without names"
---

###### D · Data about individuals

# Sensor data identify people even without names

- **Four points are enough:** four location–time points uniquely identified 95% of 1.5 million people in mobile phone data (de Montjoye et al., 2013)
- **Demographics are enough:** 15 demographic attributes would correctly re-identify 99.98% of Americans in any dataset (Rocher et al., 2019)
- **A few ratings are enough:** movie ratings with dates re-identified Netflix Prize users (Narayanan & Shmatikov, 2008)
- **Aggregates can reveal too:** Strava's heat map of shared activities exposed military bases (2018)

<div class="ref-bottom">Jarmul, K. (2023). Practical Data Privacy, ch. 4. O'Reilly. · Glerean, E. (2025). Fundamentals of Secure AI Systems with Personal Data, ch. 4. EDPB Support Pool of Experts.</div>

<!--
The lesson: removing names does not anonymise. Uniqueness grows with every extra column and every extra day of sensor data.
Smartwatch data are high-dimensional and longitudinal, which is exactly the setting in which these attacks work.
-->

---
layout: default
title: "Health data include what you infer, not only what you measure"
---

###### D · Data about individuals

# Health data include what you infer, not only what you measure

<div class="grid-2">
<div>

**Special categories (GDPR Art 9(1))**

- Racial or ethnic origin
- Political opinions; religious or philosophical beliefs
- Trade union membership
- Genetic data; biometric data used to identify a person
- **Data concerning health**
- Sex life or sexual orientation

Processing them is **prohibited unless** an Art 9(2) condition applies (L block).

</div>
<div class="card yellow">

**Inference counts**

- Data that **indirectly reveal** a special category are covered (CJEU C-184/20, *OT*, 2022)
- Online orders of pharmacy-only medicines are health data (CJEU C-21/23, *Lindenapotheke*, 2024)
- A model that predicts low mood or insomnia from sleep and activity **creates** health data
- Repeated GPS visits to a place of worship or a clinic can reveal religion or health

</div>
</div>

<!--
Digital phenotyping is inference by design, so its outputs are special-category data even when the inputs looked harmless.
Art 9 is a prohibition with exceptions, not a permission with extra requirements.
-->

---
layout: section
color: dark
hexText: "E"
class: title-middle
---

# E. Ethics

D · <span class="delti-on">E</span> · L · T · I — principles, their conflicts, and when review is mandatory

---
layout: default
title: "Ethics, law and research integrity answer different questions"
---

###### E · Ethics

# Ethics, law and research integrity answer different questions

<div class="compact">

| | Question | Sources | Who enforces |
| --- | --- | --- | --- |
| **Ethics** | Should we do this, and how? | Principles, professional codes, ethics committees | Peers, committees, the public |
| **Law** | May we, and what must we do? | GDPR, AI Act, MDR, national law | Authorities and courts |
| **Research integrity** | Are we doing research honestly and verifiably? | ALLEA code (2023), TENK RCR guidelines (2023) | Universities, TENK |

</div>

- They overlap but do not coincide: a study can be lawful and unethical, or ethical and unlawful
- Things can be **ethical but illegal** (giving humanitarian help without permission), or **legal but unethical** (exploiting loopholes to avoid paying taxes)

<!--
Integrity is the third leg students often forget: openness and reproducibility pull against privacy, which is one of today's main tensions.
-->

---
layout: default
title: "Ethics feeds law, and what people accept feeds ethics"
---

###### E · Ethics

# Ethics feeds law, and what people accept feeds ethics

<div class="cascade">
<svg viewBox="0 -6 665 282" role="img" aria-label="Normative cascade: Ethics leads to Law, Law to Business, Business to Customers, and Customers loop back to Ethics">
  <defs>
    <marker id="nc-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" class="nc-head" />
    </marker>
  </defs>
  <path d="M 606 207 A 294 119 0 0 1 54 146" class="nc-line nc-dash" marker-end="url(#nc-arrow)" />
  <path d="M 135 23.5 A 45.7 45.7 0 0 1 210.7 58" class="nc-line" marker-end="url(#nc-arrow)" />
  <path d="M 300 70.5 A 45.7 45.7 0 0 1 375.7 105" class="nc-line" marker-end="url(#nc-arrow)" />
  <path d="M 467.5 116 A 45.7 45.7 0 0 1 543 150.5" class="nc-line" marker-end="url(#nc-arrow)" />
  <ellipse cx="75" cy="71" rx="75" ry="71" class="nc-oval" /><text x="75" y="71" class="nc-label">Ethics</text>
  <ellipse cx="244" cy="121" rx="75" ry="71" class="nc-oval" /><text x="244" y="121" class="nc-label">Law</text>
  <ellipse cx="414" cy="165" rx="75" ry="71" class="nc-oval" /><text x="414" y="165" class="nc-label">Business</text>
  <ellipse cx="585" cy="206" rx="75" ry="71" class="nc-oval" /><text x="585" y="206" class="nc-label">Customers</text>
</svg>
</div>

- **People** decide in what kind of society they want to live; their values become the ethical principles that law builds on
- You can replace "business" with "government" or "research", and "customers" with "citizens" or "participants"
- Example ahead: the GDPR's research rules apply only to research that follows ethical standards (L block)

<div class="ref-bottom">Floridi, L. (2023). The Ethics of Artificial Intelligence: Principles, Challenges, and Opportunities. Oxford University Press.</div>

<style>
.cascade { margin: 0 0 0.75rem; }
.cascade svg { width: 420px; height: auto; display: block; }
.nc-oval { fill: #fff; stroke: #000; stroke-width: 1.5; }
.nc-label { font-size: 20px; text-anchor: middle; dominant-baseline: middle; fill: #000; }
.nc-line { fill: none; stroke: #000; stroke-width: 2; }
.nc-dash { stroke-dasharray: 7 5; }
.nc-head { fill: #000; }
</style>

<!--
The dashed arrow is the feedback loop: what customers or participants tolerate shifts what society considers ethical.
-->

---
layout: default
title: "Five principles: four from bioethics, one added for AI"
---

###### E · Ethics

# Five principles: four from bioethics, one added for AI

<div class="compact">

| **Principle** | **Meaning** | **In digital health** |
| --- | --- | --- |
| **Beneficence** | Promote well-being and dignity | Sensor-based early warning of a depressive relapse |
| **Nonmaleficence** | Avoid harm, incl. to privacy and security | Store daily distance instead of raw GPS traces |
| **Autonomy** | Respect people's informed choices; keep humans in control | Participants can stop sharing watch data at any time, without penalty |
| **Justice** | Share benefits and burdens fairly; avoid discrimination | Check that the model works as well for groups under-represented in training |
| **Explicability** | Make AI understandable and accountable | Users and clinicians can see why a "low-mood day" was flagged, and contest it |

</div>

<div class="ref-bottom">Beauchamp, T. & Childress, J. (2019). Principles of Biomedical Ethics, 8th ed. · Floridi, L. (2023). The Ethics of Artificial Intelligence.</div>

<!--
Floridi's unified framework keeps the four bioethics principles and adds explicability as the enabling principle for AI.
-->

---
layout: default
title: "The hard cases are conflicts between principles"
---

###### E · Ethics

# The hard cases are conflicts between principles

<div class="grid-2-3">
<div class="card">

**Example: should we open the study data?**

- **For:** beneficence (others build on it), justice and integrity (results can be checked)
- **Against:** nonmaleficence (re-identification), autonomy (participants agreed to *this* study)

</div>
<div>

**A method you can document**

1. Name the conflict, and who carries each risk
2. List options: aggregate release, controlled access, tested synthetic data, data-use agreements
3. Choose the least intrusive option that still serves the purpose
4. Write down the decision and when you will revisit it

</div>
</div>

- Principles alone cannot guarantee ethical AI: they need methods and accountability (Mittelstadt, 2019)
- The law balances in the same way: freedom of research (Charter Art 13) against data protection (Art 8), through proportionality (Art 52(1))

<!--
This is the method students will reuse in the pair task. The answer is rarely "open" or "closed"; it is usually "as open as possible, as closed as necessary".
-->

---
layout: default
title: "Ethics review starts with listing the issues"
---

###### E · Ethics

# Ethics review starts with listing the issues

**Horizon Europe ethics issues table** ([guidance](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/how-to-complete-your-ethics-self-assessment_en.pdf))

<div class="grid-2">
<div>

1. Human embryonic stem cells and human embryos
2. **Humans**
3. Human cells and tissues
4. **Personal data**
5. Animals

</div>
<div>

6. Non-EU countries
7. Environment, health and safety
8. **Artificial intelligence**
9. Other ethics issues

Cross-cutting: potential **misuse** of results. Dual use is handled in the separate security self-assessment.

</div>
</div>

A typical data science project ticks 2, 4 and 8, and sometimes 6.

<div class="ref-bottom">More: <a href="https://www.aalto.fi/en/for-personnel-highlights-and-support-for-your-work/different-perspectives-to-research-ethics-how-to-make-an-ethics-self-assessment-in-research-projects" target="_blank" rel="noopener">Aalto: how to make an ethics self-assessment</a></div>

<!--
This is the official list from "How to complete your ethics self-assessment" (v2.0, 2021).
-->

---
layout: default
title: "Ethical pre-review in Finland depends on the type of study"
---

###### E · Ethics

# Ethical pre-review in Finland depends on the type of study

<div class="prereview">
<div>

1. **Medical research** (Medical Research Act 488/1999): opinion from a regional medical research ethics committee, e.g. [HUS](https://www.hus.fi/tutkimus-ja-opetus/tutkijan-palvelut/sahkoiset-palvelut-tutkijalle), before starting
    - **Clinical drug trials:** [Tukija](https://tukija.fi/en/frontpage) gives the ethics opinion for every trial, academic or commercial; Fimea authorises
    - **Clinical investigations of medical devices:** Fimea (MDR) plus an ethics committee opinion
2. **Non-medical research:** review by a university ethics committee ([e.g. at Aalto](https://www.aalto.fi/en/services/research-ethics-review-research-ethics-committee)) only if one of these applies ([TENK 2019](https://www.tenk.fi/sites/tenk.fi/files/Ihmistieteiden_eettisen_ennakkoarvioinnin_ohje_2019.pdf)):
    1. deviates from **informed consent**
    2. intervenes in **physical integrity**
    3. involves **minors under 15** without parental consent
    4. uses exceptionally **strong stimuli**
    5. may cause **mental harm** beyond daily life
    6. may **threaten the safety** of participants or researchers

</div>
<div class="card yellow warning-card">
  <img src="/images/warning.svg" alt="Warning icon">
  <p><strong>Most studies on existing data, and most industry research, need no ethics review. The ethical judgement then stays with you.</strong></p>
</div>
</div>

<style>
.prereview { display: grid; grid-template-columns: minmax(0, 3fr) minmax(0, 1fr); gap: 1.5rem; align-items: end; }
.warning-card img { width: 64px; height: 64px; border-radius: 0; margin-bottom: 0.5rem; }
</style>

<!--
Tukija reviews all clinical drug trials, not only industry ones. Clinical investigations of medical devices go through Fimea.
-->

---
layout: default
title: "Industry research has no mandatory ethics review"
---

###### E · Ethics

# Industry research has no mandatory ethics review

- Companies experiment on users every day (A/B tests); most are product decisions, not research
- **Facebook, 2014:** news feeds of 689,003 users were altered for one week to test emotional contagion. Consent relied on the data use policy; the journal later added an editorial expression of concern
- What fills the gap in the EU today:
    - data protection impact assessment (GDPR Art 35)
    - fundamental rights impact assessment for some deployers of high-risk AI (AI Act Art 27)
    - conformity assessment for regulated products
    - internal review boards, staff, reputation
- A company that claims "scientific research" to use the GDPR's research rules must meet the research criteria, including ethical standards (EDPB Guidelines 1/2026)

<div class="ref-bottom">Kramer, A., Guillory, J. & Hancock, J. (2014). Experimental evidence of massive-scale emotional contagion through social networks. PNAS 111(24).</div>

<!--
The question is not whether companies care about ethics, but which mechanisms push ethics into them.
-->

---
layout: section
color: dark
hexText: "L"
class: title-middle
---

# L. Law

D · E · <span class="delti-on">L</span> · T · I — from fundamental rights to the GDPR, the AI Act and device rules

---
layout: two-cols
title: "Human rights become binding EU law through the Charter"
---

::header::
###### L · Law

# Human rights become binding EU law through the Charter

::left::

### Universal Declaration of Human Rights (1948)

- Adopted by the United Nations; not binding law
- 30 articles; "all human beings are born free and equal in dignity and rights"
- **Art 12:** privacy
- **Art 27:** the right to share in scientific advancement and its benefits
- [Read all 30 at least once](https://www.un.org/en/about-us/universal-declaration-of-human-rights); data risks per article are in the appendix

::right::

### EU Charter of Fundamental Rights (binding since 2009)

- **Art 7:** respect for private and family life
- **Art 8:** protection of personal data, the basis of the GDPR
- **Art 13:** freedom of the arts and sciences
- **Art 52(1):** limits on rights must be provided by law, necessary and proportionate

Data protection law is the balance between Art 8 and Art 13, written down.

<!--
Art 8 makes data protection a right separate from privacy; that is why the EU regulates personal data even when nothing "private" is involved.
-->

---
layout: default
title: "The GDPR in one slide"
---

###### L · Law

# The GDPR in one slide

- **Regulation (EU) 2016/679:** adopted in 2016, applies since 25 May 2018, with national specifications (Finland: Data Protection Act 1050/2018)
- **Scope:** organisations in the EU, and organisations elsewhere that offer services to people in the EU or monitor them (Art 3)
- **Roles follow decisions:** the controller decides why and how; a processor acts on its documented instructions (Art 28); joint controllers decide together (Art 26)
- **Running case:** the university is the controller of the study; the watch vendor is a processor if it only syncs data for you, and a controller for anything it uses for its own purposes; the spin-out is a new controller
- **Authority in Finland:** Office of the Data Protection Ombudsman ([tietosuoja.fi](https://tietosuoja.fi/en/home))
- **Fines:** up to €20 million or 4% of worldwide annual turnover (Art 83(5))

<!--
Roles must be documented, especially in public–private partnerships (EDPB Guidelines 1/2026). The spin-out cannot simply inherit the study data: it needs its own legal basis and an agreement with the university.
-->

---
layout: default
title: "The principles of the GDPR, applied to research"
---

###### L · Law

# The principles of the GDPR, applied to research

<div class="small compact">

| **GDPR principle (Art 5)** | **Practical actions in research projects** |
| --- | --- |
| **1. Lawfulness, fairness, transparency** | Identify the legal basis and, for health data, the Art 9 condition<br>Tell participants what you do in a privacy notice; no hidden purposes |
| **2. Purpose limitation** | Define purposes before collecting<br>Further use for research is presumed compatible (Art 5(1)(b)), but still needs a lawful basis |
| **3. Data minimisation** | Collect only what the question needs<br>Pseudonymise early; aggregate when you can |
| **4. Accuracy** | Record data correctly and document errors<br>A research dataset is a snapshot: correct mistakes, do not "refresh" it |
| **5. Storage limitation** | Set retention periods<br>Longer storage for research is allowed with safeguards (Art 5(1)(e)) |
| **6. Integrity and confidentiality** | Access control, encryption, approved storage and compute, training for the team |
| **7. Accountability** | Record of processing, DPIA when required, documented decisions, the DPO consulted |

</div>

<!--
Informed consent belongs to research ethics, not to lawfulness (next slide), and a change of purpose for research does not automatically require new consent.
-->

---
layout: default
title: "Consent to take part is not the same as the GDPR legal basis"
---

###### L · Law

# Consent to take part is not the same as the GDPR legal basis

<div class="grid-2">
<div class="card">

### Research ethics consent

- Required by research ethics (TENK, Declaration of Helsinki) and by law for medical research
- Informs and protects participants
- Withdrawing means leaving the study

</div>
<div class="card">

### GDPR legal basis (Art 6)

- Finnish universities usually rely on **public interest**: Art 6(1)(e) with Data Protection Act s. 4(3)
- Consent (Art 6(1)(a)) only if freely given, specific, informed, unambiguous and withdrawable: hard with power imbalances
- Withdrawing GDPR consent stops processing based on it

</div>
</div>

Ask for both when needed, but keep the two requests **clearly distinguishable** (EDPB Guidelines 1/2026, paras 53–55).

<!--
The most common researcher misconception. With a public-interest basis, data already collected may be kept after someone leaves the study if erasure would seriously impair the research (Art 17(3)(d)); say so in the privacy notice.
-->

---
layout: default
title: "Six legal bases, used differently in academia and industry"
---

###### L · Law

# Six legal bases, used differently in academia and industry

<div class="small compact">

| **Legal basis (Art 6(1))** | **Typical in academia** | **Typical in industry** |
| --- | --- | --- |
| **(a) Consent** | Possible, but fragile with power imbalances and withdrawal | Common for apps; must be freely given and granular |
| **(b) Contract** | Rarely | Providing the service the user signed up for; not for research |
| **(c&#8203;) Legal obligation** | Statutory reporting | Tax, product vigilance |
| **(d) Vital interests** | Emergencies only | Emergencies only |
| **(e) Public interest** | Main basis for Finnish universities (Data Protection Act s. 4(3)) | Only if a law gives the company that task |
| **(f) Legitimate interests** | Limited for public bodies performing their tasks (Art 6(1), last subparagraph) | Common for commercial research, with a documented balancing test (EDPB Guidelines 1/2024; 1/2026 para 61) |

</div>

<!--
Legitimate interest is the usual basis for research in companies.
"Explicit" consent is the stricter Art 9(2)(a) standard, not the Art 6 standard.
-->

---
layout: default
title: "Health data need two locks: a legal basis and an Article 9 condition"
---

###### L · Law

# Health data need two locks: a legal basis and an Article 9 condition

- **Lock 1:** a legal basis under Art 6 (previous slide)
- **Lock 2:** an exception to the Art 9(1) prohibition. Common ones in research:
    - **(a)** explicit consent
    - **(j)** scientific research based on EU or national law, with Art 89(1) safeguards
    - **(h), (i)** health care and public health
- **Finland:** Data Protection Act s. 6(1)(7) allows research processing, with suitable and specific safeguards (s. 6(2))
- **Registry data:** secondary use of Finnish health and social data goes through the Secondary Use Act (552/2019) and Findata
- **From 2029:** the EHDS adds an EU-wide route for secondary use (later in this block)

<div class="ref-bottom">EDPB Guidelines 1/2026 on processing of personal data for scientific research purposes (version for consultation, April 2026).</div>

<!--
Member States may add conditions for genetic, biometric or health data (Art 9(4)).
-->

---
layout: default
title: "The GDPR's research rules apply only to genuine research"
---

###### L · Law

# The GDPR's research rules apply only to genuine research

<div class="grid-2">
<div>

**Six indicative factors** (EDPB Guidelines 1/2026, para 11)

1. Methodical and systematic approach
2. **Adherence to ethical standards**
3. Verifiability and transparency
4. Autonomy and independence
5. Research objectives
6. Potential to contribute to existing knowledge

</div>
<div class="card yellow">

**Where ethics becomes law**

Following ethical standards is a condition for the legal privileges of research.

</div>
</div>

- Commercial research can qualify; a retailer analysing its own sales does not (Example 3)
- The Council's Digital Omnibus mandate (21 Oct 2026) proposes a GDPR definition of scientific research that requires ethical standards. Not law yet.

<!--
This is the cleanest illustration of the normative cascade from the E block.
-->

---
layout: two-cols
title: "Research gets flexibility, and participants keep rights"
---

::header::
###### L · Law

# Research gets flexibility, and participants keep rights

::left::

### Flexibility for research

- Further use presumed compatible (Art 5(1)(b))
- Longer storage with safeguards (Art 5(1)(e))
- Broad consent for a defined research area, with extra safeguards (Recital 33; EDPB 1/2026 paras 40–49)
- Information exemption for disproportionate effort (Art 14(5)(b))
- Derogations from rights by law (Art 89(2); Finnish Data Protection Act s. 31)
- Erasure exception (Art 17(3)(d)); objection limited for public-interest research (Art 21(6))

::right::

### Rights of the data subject

- Information (Art 13, 14) and access (15)
- Rectification (16) and erasure (17)
- Restriction (18) and portability (20)
- Objection (21)
- No decisions based solely on automated processing with legal or similarly significant effects (22; CJEU C-634/21, *SCHUFA*)
- Complaint to the Data Protection Ombudsman (77)

<!--
The flexibility comes with a condition: pseudonymise or anonymise where the purpose allows; identify people directly only where strictly necessary (EDPB 1/2026).
-->

---
layout: default
title: "The data protection impact assessment"
---

###### L · Law

# The data protection impact assessment

<div class="dpia">
<div>

A tool for evaluating the risks of processing personal data.

Aalto guidelines as an example:<br>**DPIA if 2 or more are true**

<div class="small">

1. processing of personal data for evaluation or **scoring** purposes
2. processing of personal data for **automated decision-making** with legal or similar significant effect
3. processing of personal data for **systematic monitoring**
4. processing of **special categories of personal data** or personal data that is confidential by law (sensitive data)
5. personal data is processed on a **large scale** at the regional, national or international level
6. personal data is **combined from different sources**
7. processing of personal data concerning **vulnerable data subjects, children in particular**
8. in light of the achieved state of technological knowledge, **a new technology is used on a large scale to process personal data**
9. personal data is transferred **outside the European Union**
10. the processing makes it difficult for data subjects to **exercise a right** or use a service

</div>
</div>
<div class="dpia-fig">
  <img src="/images/dpia-process.png" alt="Flowchart of the DPIA process steps">
  <p class="small"><a href="https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/data-protection-impact-assessments-dpias/how-do-we-do-a-dpia/" target="_blank" rel="noopener">Figure source</a></p>
</div>
</div>

<style>
.dpia { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 0.8fr); gap: 1.5rem; align-items: start; }
.dpia-fig img { width: 100%; height: auto; }
.dpia-fig p { text-align: right; margin-top: 0.3rem; }
</style>

<!--
The running case ticks 3, 4, 6 and 7 (students can be vulnerable when the researchers are their teachers): a DPIA is clearly needed.
-->

---
layout: default
title: "Three assessments ask three different questions"
---

###### L · Law

# Three assessments ask three different questions

<div class="small compact">

| **Assessment** | **Question** | **Required when** | **Who** |
| --- | --- | --- | --- |
| **Ethics review** | Should we do this study, and is it fair to participants? | Medical research; TENK conditions; funder rules | Ethics committee |
| **DPIA** (GDPR Art 35) | What are the risks to people's rights, and how do we reduce them? | Likely high risk, e.g. health data with systematic monitoring | Controller, advised by the DPO |
| **Conformity assessment** (MDR, AI Act) | Is the product safe, and does it meet its requirements? | Medical devices; high-risk AI systems | Manufacturer or provider, often a notified body |
| **FRIA** (AI Act Art 27) | What does deploying this high-risk AI do to fundamental rights? | Public bodies and some private deployers of high-risk AI | Deployer |

</div>

Passing one does not pass the others.

<!--
Students often assume an ethics approval covers data protection, or the reverse. Different questions, different owners, different documents.
-->

---
layout: two-cols
title: "The AI Act regulates AI by risk, and its dates have moved"
---

::header::
###### L · Law

# The AI Act regulates AI by risk, and its dates have moved

::left::

### What it regulates

- **AI system** (Art 3(1)): a machine-based system that infers from its inputs how to generate outputs such as predictions, content, recommendations or decisions
- **Prohibited practices** (Art 5)
- **High-risk systems** (Art 6; Annexes I and III)
- **Transparency duties** (Art 50): chatbots, deepfakes, emotion recognition
- **Minimal risk:** no new duties
- **General-purpose AI models** (Art 51–55)

::right::

### When it applies

- **1 Aug 2024:** entry into force
- **2 Feb 2025:** prohibitions; AI literacy (Art 4)
- **2 Aug 2025:** general-purpose AI models
- **2 Aug 2026:** transparency duties (Art 50)
- **2 Dec 2027:** high-risk, Annex III
- **2 Aug 2028:** high-risk in products (Annex I), incl. medical devices

<p class="small">Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI)</p>

<!--
There is no "medium risk" tier. The high-risk dates were postponed by the Digital Omnibus on AI, in force since 27 July 2026.
The Commission's guidelines on the AI system definition (Feb 2025) explain each element of the definition.
-->

---
layout: default
title: "The research exemption ends where the product begins"
---

###### L · Law

# The research exemption ends where the product begins

- **Art 2(6):** AI systems or models developed and put into service **for the sole purpose** of scientific research and development are out of scope
- **Art 2(8):** research, testing and development **before** placing on the market or putting into service are out of scope; **testing in real-world conditions is not**
- It covers applied research and company R&D, not only basic research
- It exempts from the AI Act only: the GDPR, ethics review and the MDR still apply
- **AI literacy (Art 4)** applies to providers and deployers, e.g. a university that deploys AI tools for its staff

<div class="card blue">

**Running case:** the study's model is out of scope; the spin-out's app is in scope.

</div>

<!--
The exemption is not limited to basic research, and it ends when the system is placed on the market or put into service.
-->

---
layout: default
title: "Some AI practices have been banned since February 2025"
---

###### L · Law

# Some AI practices have been banned since February 2025

<div class="ban">
<div>

**Prohibited practices (Art 5)**

- Harmful manipulation or deception
- Exploiting vulnerabilities (age, disability, social or economic situation)
- Social scoring
- Predicting crime from profiling alone
- Untargeted scraping of facial images
- **Emotion inference at work and in education, except for medical or safety reasons**
- Biometric categorisation inferring sensitive traits
- Real-time remote biometric identification for law enforcement in public spaces (narrow exceptions)

</div>
<div class="card yellow">

**Running case**

A university uses the app to monitor students' stress from heart-rate data: emotion inference in education, from biometric data.

Prohibited, unless the purpose is medical or safety. Self-reported mood alone is not biometric data.

</div>
</div>

<style>
.ban { display: grid; grid-template-columns: minmax(0, 3fr) minmax(0, 2fr); gap: 1rem; align-items: start; }
</style>

<div class="ref-bottom">European Commission (2025). Guidelines on prohibited artificial intelligence practices under the AI Act.</div>

<!--
The ban concerns emotion recognition systems, which infer emotions from biometric data (Art 3(39)). Physiological signals such as heart rate can be biometric data under the AI Act.
Critics argue the exceptions (e.g. for law enforcement) weaken the protection; others argue the Act is too burdensome.
-->

---
layout: three-cols
title: "High-risk AI in health comes through two routes"
---

::header::
###### L · Law

# High-risk AI in health comes through two routes

::left::

### Product route (Art 6(1), Annex I)

AI that is, or is a safety component of, a product needing third-party conformity assessment:

- **Medical devices** (MDR) and IVDs (IVDR)
- Machinery, toys, radio equipment, lifts
- Vehicles, aviation, marine equipment

::center::

### Use-case route (Art 6(2), Annex III)

- Biometrics
- Critical infrastructure
- Education and vocational training
- Employment
- Essential services and benefits
- Law enforcement
- Migration, asylum, border control
- Justice and democracy

::right::

### Health examples

- Diagnostic or triage software that needs a notified body (MDR class IIa and above)
- Eligibility for public healthcare services (Annex III, 5(a))
- Pricing of life and health insurance (5(c&#8203;))
- Emergency call triage (5(d))
- Admission or assessment in education (3)

<!--
High-risk under the AI Act does not change the MDR class; it adds requirements (MDCG 2025-6 / AIB 2025-1).
Draft Commission guidelines on high-risk classification were published on 19 May 2026.
-->

---
layout: default
title: "Intended purpose decides whether your app is a medical device"
---

###### L · Law

# Intended purpose decides whether your app is a medical device

- A **medical device** has a medical purpose: diagnosis, prevention, monitoring, prediction, prognosis, treatment or alleviation of disease (MDR Art 2(1))
- The manufacturer's **claims** decide: "track your sleep" is wellness; "detect insomnia" or "predict depressive episodes" is medical
- **MDR Rule 11** for software:
    - information for diagnostic or therapeutic decisions: class IIa, or IIb/III if the decisions can cause serious harm
    - monitoring physiological processes: class IIa (IIb for vital parameters with immediate danger)
    - all other software: class I
- Class IIa and above need a **notified body**; with AI inside, the system is also high-risk under the AI Act
- Clinical investigations need Fimea's authorisation or notification, and an ethics opinion

<div class="ref-bottom">MDCG 2019-11 (qualification and classification of software). MDCG 2025-6 / AIB 2025-1 (interplay between MDR, IVDR and the AI Act).</div>

<!--
The wellness/medical line is where many digital-health start-ups live, and where marketing claims create legal obligations.
Ask the room: before anyone deploys this, how would you show it works? A medical claim needs clinical evidence (MDR Art 61, clinical evaluation). For software, MDCG 2020-1 asks for three things: a valid clinical association, technical performance and clinical performance.
The same logic applies to wearable measures without a medical claim. The V3 framework (Goldsack et al., 2020, npj Digital Medicine) separates verification (does the sensor record correctly?), analytical validation (does the algorithm measure what it claims, e.g. sleep stages against polysomnography?) and clinical validation (does the measure track the health state in the target population?).
-->

---
layout: two-cols
title: "Device data come with user rights, and health data with a reuse framework"
---

::header::
###### L · Law

# Device data come with user rights, and health data with a reuse framework

::left::

### Data Act (Regulation (EU) 2023/2854)

- Applies since 12 Sep 2025
- Users of connected products, e.g. wearables, can access the data they generate and have it shared with third parties
- Products placed on the market after 12 Sep 2026 must offer access by design
- Personal data in it remain under the GDPR

::right::

### EHDS (Regulation (EU) 2025/327)

- In force since 26 Mar 2025
- Primary use: people's access to their electronic health data
- Secondary use through health data access bodies, in secure processing environments
- Includes data from wellness apps and medical devices (Art 51)
- Most secondary-use rules apply from March 2029
- Finland today: Secondary Use Act 552/2019 and Findata

<!--
For research: the Data Act lets participants ask the vendor to share their own watch data with you, instead of relying on the vendor's research programme.
-->

---
layout: two-cols
title: "The rules keep moving: the Digital Omnibus"
---

::header::
###### L · Law

# The rules keep moving: the Digital Omnibus

::left::

### Status

- **Law since 27 Jul 2026:** the Digital Omnibus on AI (Regulation (EU) 2026/1744) moved the high-risk deadlines to Dec 2027 and Aug 2028
- **Still a proposal:** the Digital Omnibus on data (proposed 19 Nov 2025)
    - the Commission proposed narrowing the definition of personal data
    - the Council's mandate (21 Oct 2026) keeps the definition, adds a pseudonymisation rule and a research definition
    - the Parliament's position is pending

::right::

### Two readings

- **Simplification:** lower compliance costs, legal certainty, EU competitiveness (the Commission's case)
- **Erosion:** the EDPB and EDPS warned that the definition change would significantly narrow the concept of personal data (Joint Opinion 2/2026)

Discussion: simplification, or "ethics lobbying"?

Check current status: EUR-Lex, the EDPB, the AI Act Service Desk.

<!--
Both readings have their advocates; the useful skill is checking what is law today.
This slide reflects the situation in November 2026.
-->

---
layout: section
color: dark
hexText: "BREAK"
class: title-middle
---

# Break: 10 minutes

---
layout: section
color: dark
hexText: "T"
class: title-middle
---

# T. Technology

D · E · L · <span class="delti-on">T</span> · I — turning principles into technical measures

---
layout: default
title: "Data protection by design starts with what you collect"
---

###### T · Technology

# Data protection by design starts with what you collect

- **Art 25:** data protection by design and by default
- **Before collection:** collect features, not raw streams (daily sleep duration, not raw accelerometer data); coarsen location; avoid free text
- **At ingestion:** pseudonymise; keep the key separate; give each person the least access they need
- **During analysis:** approved storage and compute, e.g. secure processing environments for health data
- **Before release:** run the anonymity test; release aggregates or controlled access; document every release
- **Throughout:** a privacy notice in plain language that names vendors and transfers; a DPIA when risk is high

<!--
Art 25 is "data protection by design and by default". "Large scale" has no fixed threshold such as a number of participants.
-->

---
layout: default
title: "Anonymity is a risk judgement, not a technique"
---

###### T · Technology

# Anonymity is a risk judgement, not a technique

EDPB Guidelines 02/2026 (version for consultation): data are anonymous only if, for **each relevant entity**, all three criteria hold.

<div class="grid-3">
<div class="card">

**No record isolation**

No record is unique to one person.

</div>
<div class="card">

**No linkage**

Records cannot be linked to other data about the same person.

</div>
<div class="card">

**No inference**

No specific, meaningful conclusion about an identifiable person can be drawn.

</div>
</div>

- The likelihood of identification must be **insignificant**, not zero (para 22)
- Risk tends to rise over time: **reassess** (para 35)
- Anonymising is itself processing and needs a **legal basis** (para 38)
- Access controls alone do **not** make data anonymous (para 90)

<!--
The draft guidelines were open for consultation until 30 October 2026; check for the final version.
-->

---
layout: default
title: "Removing names is not anonymisation"
---

###### T · Technology

# Removing names is not anonymisation

<div class="spectrum">
  <div class="sp-top"><p><strong>Raw personal data</strong></p><p>Direct identifiers present</p></div>
  <div class="sp-top"><p><strong>Pseudonymised</strong></p><p>Identifiers replaced by codes; key kept (Art 4(5))</p></div>
  <div class="sp-top"><p><strong>De-identified, masked</strong></p><p>Identifiers removed; rich records kept</p></div>
  <div class="sp-top"><p><strong>Aggregated or noisy release</strong></p><p>Counts, statistics, differential privacy</p></div>
  <div class="sp-top"><p><strong>Synthetic data, trained models</strong></p><p>No real records released</p></div>
  <div class="sp-arrow" aria-hidden="true"></div>
  <div class="sp-bottom"><p><strong>Identifiable by anyone with access</strong></p></div>
  <div class="sp-bottom"><p><strong>Personal data for whoever can re-identify</strong></p></div>
  <div class="sp-bottom"><p><strong>Usually still personal: isolation and linkage remain</strong></p></div>
  <div class="sp-bottom"><p><strong>Anonymous only if the three criteria pass</strong></p></div>
  <div class="sp-bottom"><p><strong>Can still leak: test before claiming anonymity</strong></p></div>
</div>

Pseudonymised data stay personal data for the key holder (EDPB Guidelines 01/2025); for a recipient without reasonable means to re-identify, they may not be (CJEU C-413/23 P).

<div class="ref-bottom">Deeper look at minimisation and anonymisation: <a href="https://zenodo.org/records/10649060" target="_blank" rel="noopener">https://zenodo.org/records/10649060</a></div>

<style>
/* Five steps from identifiable to possibly anonymous data, over a dark-to-light arrow */
.spectrum { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0 1rem; margin-top: 1rem; }
.spectrum p { margin: 0 0 0.3rem; }
.sp-top { align-self: start; }
.sp-arrow { grid-column: 1 / -1; height: 2.6rem; margin: 1.2rem 0; background: linear-gradient(90deg, #434343, #9FC5E8); clip-path: polygon(0 25%, calc(100% - 2.6rem) 25%, calc(100% - 2.6rem) 0, 100% 50%, calc(100% - 2.6rem) 100%, calc(100% - 2.6rem) 75%, 0 75%); }
</style>

<!--
Common misconceptions: "impossible to re-identify" is not the legal test; masking is still pseudonymisation; aggregates and synthetic data are not anonymous by default; differential privacy describes how a result is released, not a dataset.
-->

---
layout: default
title: "Aggregates, synthetic data and models can still leak"
---

###### T · Technology

# Aggregates, synthetic data and models can still leak

- **Reconstruction:** published census tables allowed individual records to be reconstructed; the US Census Bureau adopted differential privacy for the 2020 census
- **Membership inference:** an attacker can tell whether a person's record was in the training data
- **Memorisation:** language models can reproduce training data verbatim when prompted
- **EDPB:** AI models trained on personal data cannot in all cases be considered anonymous (Opinion 28/2024); inference from aggregates, synthetic data and models counts against anonymity (Guidelines 02/2026, paras 17, 77, 82)

<div class="ref-bottom">Jarmul, K. (2023). Practical Data Privacy, ch. 2 and 4. · Glerean, E. (2025). Fundamentals of Secure AI Systems with Personal Data, ch. 7.</div>

<!--
The practical consequence: a model trained on the study data may itself be personal data, which matters when the spin-out takes it.
-->

---
layout: default
title: "Privacy-enhancing technologies trade risk for utility and effort"
---

###### T · Technology

# Privacy-enhancing technologies trade risk for utility and effort

<div class="small compact">

| **Technique** | **Protects against** | **Main cost** | **In a wearable study** |
| --- | --- | --- | --- |
| **Pseudonymisation** | Casual identification | Key management; data stay personal | Codes instead of names at ingestion |
| **Differential privacy** | Inference from released statistics or models | Noise lowers accuracy; privacy budget | Release group averages with calibrated noise |
| **Federated learning** | Central collection of raw data | Engineering; updates can leak without DP | Train on phones, share only model updates |
| **Secure processing environment** | Uncontrolled copies and exports | Access procedures, less flexibility | Analyse inside, export only checked aggregates |
| **Synthetic data** | Sharing real records | Fidelity and leakage must be tested | Share synthetic data for method development |
| **Homomorphic encryption, secure multiparty computation** | Exposure during computation | Slow; specialist skills | Joint analysis across hospitals without pooling data |

</div>

<div class="ref-bottom">Jarmul (2023), ch. 2, 5–7. · Glerean (2025), ch. 5.</div>

<!--
No technique is a free pass: each moves risk somewhere else. Combine them, and document why the combination is enough.
-->

---
layout: default
title: "Sending participant data to an LLM is a data protection decision"
---

###### T · Technology

# Sending participant data to an LLM is a data protection decision

Before you paste or upload:

1. **Is it personal data?** Prompts and files count, pseudonymised or not
2. **Who is the provider?** A processor under an Art 28 agreement, or a company that also uses inputs for its own purposes?
3. **Where is it processed?** Transfers outside the EU/EEA need a basis, e.g. the EU–US Data Privacy Framework
4. **Is the tool approved** by your organisation for this class of data?
5. **Were participants told** in the privacy notice, and does the DPIA cover it?
6. **Can the output** contain personal data or new health inferences?

Lecture 5 showed what LLMs can do with phenotyping data; this is the checklist before you do it.

<!--
Never use a consumer chatbot with participants' data. Institutional tools exist for a reason: contracts, location and no training on inputs.
-->

---
layout: default
title: "Security failures harm individuals directly: Vastaamo"
---

###### T · Technology

# Security failures harm individuals directly: Vastaamo

- Vastaamo, a Finnish psychotherapy provider, kept its patient database on a server reachable from the internet without a firewall from 2017 to 2019
- Attackers took therapy records; in 2020 the patients themselves received extortion demands
- **Finnish DPA, 7 Dec 2021:** €608,000 fine for failing to secure the data and to notify the breach (Art 5(1)(f), 32, 33, 34); the company went bankrupt
- For health data, security is not a technical detail: it is the main duty you owe participants

<div class="ref-bottom"><a href="https://www.edpb.europa.eu/news/national-news/2022/administrative-fine-imposed-psychotherapy-centre-vastaamo-data-protection_en" target="_blank" rel="noopener">EDPB: administrative fine imposed on psychotherapy centre Vastaamo (2022)</a></div>

<!--
The "I" of DELTI in its starkest form: tens of thousands of people whose therapy notes were used against them.
Back to the 2×2: unlawful and unethical.
-->

---
layout: section
color: dark
hexText: "I"
class: title-middle
---

# I. Individuals

D · E · L · T · <span class="delti-on">I</span> — who is harmed, and who is responsible

---
layout: default
title: "Harms are often collective, not only individual"
---

###### I · Individuals

# Harms are often collective, not only individual

- **Inference about groups:** a model trained on volunteers predicts things about people who never joined
- **Aggregation:** Strava users each chose to share their runs; together they exposed military bases
- **Bias:** an algorithm that used health costs as a proxy for health needs underestimated how ill Black patients were (Obermeyer et al., 2019)
- **Limits of individual rights:** consent and access rights work person by person; harms from inference and aggregation do not (Solove, 2013; Wachter & Mittelstadt, 2019)

Ask in every project: **who is affected beyond the people in the dataset?**

<!--
This is the critical angle on the "I": the GDPR protects individuals one by one, but data science acts on groups.
-->

---
layout: default
title: "Five ways to look ethical without being ethical"
---

###### I · Individuals

# Five ways to look ethical without being ethical

| **Ethics risk** | **Definition** |
| --- | --- |
| **Ethics shopping** | Selecting ethical principles that justify existing practices instead of aligning with shared standards |
| **Ethics bluewashing** | Superficial or misleading claims about ethical benefits without meaningful action |
| **Ethics lobbying** | Using voluntary ethics to delay or weaken binding rules or their enforcement |
| **Ethics dumping** | Exporting unethical practices to regions with weaker rules, or importing their results |
| **Ethics shirking** | Doing less ethical work where accountability is lower |

<div class="ref-bottom">Floridi, L. (2019). Translating principles into practices of digital ethics: five risks of being unethical. Philosophy & Technology 32.</div>

<!--
"Ethics dumping" was first used in research ethics for research exported to low-resource settings; Floridi generalises it to digital ethics.
-->

---
layout: default
title: "The five risks in today's AI"
---

###### I · Individuals

# The five risks in today's AI

- **Ethics shopping:** "AI will benefit humanity" used to justify its energy use. Data centres used about 415 TWh in 2024, projected to reach about 945 TWh by 2030 ([IEA, 2025](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai))
- **Ethics bluewashing:** "open" language models that do not release training data or code ([Liesenfeld & Dingemanse, 2024](https://dl.acm.org/doi/pdf/10.1145/3630106.3659005))
- **Ethics dumping:** data labelling and content moderation outsourced to low-paid workers in the Global South ([The Guardian, 2023](https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai))
- **Ethics lobbying:** is the Digital Omnibus legitimate simplification or weakening by the back door? Argue both sides
- **Legal note:** in the EU, training on scraped content falls under the text-and-data-mining exceptions (CDSM Directive Art 3–4) and, for general-purpose AI providers, the copyright policy duty (AI Act Art 53(1)(c&#8203;)), not US "fair use"

<div class="ref-bottom">More details <a href="https://www.aalto.fi/en/services/artificial-intelligence-ai-the-ai-act-and-ai-literacy-at-aalto-university" target="_blank" rel="noopener">https://www.aalto.fi/en/services/artificial-intelligence-ai-the-ai-act-and-ai-literacy-at-aalto-university</a></div>

<style>
/* Long URLs wrap instead of running off the slide */
a { overflow-wrap: anywhere; }
</style>

<!--
In the EU, the relevant rules for training data are the text-and-data-mining exceptions, not US fair use.
-->

---
layout: default
title: "You are a data subject too"
---

###### I · Individuals

# You are a data subject too

- **Digital traces:** cookies, location history, the apps and wearables you use. Use your access right (GDPR Art 15) and, for devices, your Data Act right to see what is collected
- **Hidden metadata** in files, photos and shared links
- **Where data are stored matters:** transfers to the US rely on the EU–US Data Privacy Framework (2023), upheld by the General Court in 2025 (*Latombe*, T-553/23); an appeal is pending at the Court of Justice (C-703/25 P)
- **Your participants** did not sign your employer's contracts with cloud providers: choose tools for them, not for you
- **Basic hygiene:** multi-factor authentication, a password manager, updates, encrypted storage and transfer, end-to-end encrypted messaging for sensitive conversations

<!--
Schrems II (2020) invalidated the Privacy Shield; the Data Privacy Framework replaced it in 2023.
-->

---
layout: default
title: "A decision path for your next project"
---

###### I · Synthesis

# A decision path for your next project

<div class="grid-2">
<div>

1. Is it personal data? Is anyone identifiable by means reasonably likely?
2. Is any of it special category, including by inference?
3. Which legal basis (Art 6) and, if needed, which Art 9(2) condition?
4. Is it genuine scientific research? Which research rules apply?
5. Is ethics review mandatory? If not, who makes the ethical call?

</div>
<div>

6. Is a DPIA required?
7. Is the product a medical device? What is your role under the AI Act, and which tier?
8. Where do you compute, with which tools and processors?
9. What will you release, and does it pass the anonymity test?
10. Tell people, keep records, and revisit when something changes

</div>
</div>

<!--
This is the take-home artefact. Students can apply it to their final project in this course.
-->

---
layout: default
title: "Other EU rules that touch digital health"
---

###### I · Synthesis

# Other EU rules that touch digital health

<div class="small compact">

| **Act** | **Why it matters here** |
| --- | --- |
| **MDR 2017/745, IVDR 2017/746** | Software with a medical purpose is a device |
| **Clinical Trials Regulation 536/2014** | Trials of medicinal products, including digital endpoints |
| **Data Act 2023/2854** | Access to data from wearables and other connected products |
| **EHDS 2025/327** | People's access to health data; secondary use from 2029 |
| **Cyber Resilience Act 2024/2847** | Security of products with digital elements, e.g. wearables and apps that are not medical devices; main duties from Dec 2027 |
| **NIS2 Directive 2022/2555** | Cybersecurity duties for health care providers and other essential entities |
| **Product Liability Directive 2024/2853** | Software, including AI, counts as a product for liability |
| **Finnish Secondary Use Act 552/2019** | Access to Finnish health and social data through Findata |

</div>

The proposed AI Liability Directive and ePrivacy Regulation were withdrawn (OJ C/2025/5423). Tracker: [digibeetle.eu/legislation-tracker](https://digibeetle.eu/legislation-tracker/)

<!--
A curated list of what a digital-health data scientist meets in practice.
-->

---
layout: default
title: "Summary"
---

###### I · Synthesis

# Summary

- **Ethics is not law:** lawful is the floor, and many choices above it are yours
- **Data become health data by inference,** and sensor data identify people without names
- **Health data need two locks:** a legal basis and an Article 9 condition; consent to take part is not the legal basis
- **Research gets privileges only if it is genuine and ethical;** the AI Act exempts research until it becomes a product
- **Anonymity is a risk judgement** per entity, reassessed over time; pseudonymised data are still personal data
- **Harms can be collective:** ask who is affected beyond your participants

<!--
Each bullet maps to a block: E, D, L, L, T, I.
-->

---
layout: end
hexText: "DELTI"
---

# Thank you!

Slides and source: [github.com/eglerean/delti](https://github.com/eglerean/delti)

---
layout: section
color: dark
hexText: "UDHR"
class: title-middle
---

# Appendix: human rights and data risks

The 30 articles of the Universal Declaration of Human Rights, read through data

---
layout: default
title: "Universal declaration of human rights and data risks 1"
---

###### Appendix

# Universal declaration of human rights and data risks 1

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 1 | Right to equality and dignity. | Biased AI algorithms perpetuating inequality and discrimination. |
| 2 | Freedom from discrimination. | Unfair profiling based on personal data leading to discrimination in services or hiring. |
| 3 | Right to life, liberty, and personal security. | Surveillance systems used to monitor and restrict personal freedoms. |
| 4 | Freedom from slavery. | Trafficking networks using personal data to recruit, track and control victims. |
| 5 | Freedom from torture and degrading treatment. | AI misuse in predictive policing leading to wrongful detention or degrading treatment. |
| 6 | Right to recognition as a person before the law. | Exclusion from digital systems due to lack of data or incorrect identification. |

</div>

---
layout: default
title: "Universal declaration of human rights and data risks 2"
---

###### Appendix

# Universal declaration of human rights and data risks 2

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 7 | Right to equality before the law. | Algorithmic bias in judicial decisions disadvantaging certain groups. |
| 8 | Right to effective legal remedy for rights violations. | Inaccessibility of remedies due to opaque AI systems denying accountability. |
| 9 | Freedom from arbitrary arrest, detention, or exile. | AI-driven surveillance leading to false positives and arbitrary detentions. |
| 10 | Right to a fair and public trial. | Lack of transparency in AI decision-making affecting judicial fairness. |
| 11 | Right to be presumed innocent until proven guilty. | Predictive analytics labeling individuals as potential offenders without evidence. |
| 12 | Right to privacy and protection from attacks on honor. | Intrusive data collection violating personal privacy. |

</div>

---
layout: default
title: "Universal declaration of human rights and data risks 3"
---

###### Appendix

# Universal declaration of human rights and data risks 3

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 13 | Right to freedom of movement and residence. | Geolocation tracking used to restrict or monitor movement. |
| 14 | Right to seek asylum from persecution. | Data misuse exposing asylum seekers to risks in their home countries. |
| 15 | Right to nationality and its change. | Lack of digital identity or errors in records denying nationality rights. |
| 16 | Right to marry and found a family. | Reproductive-health data, e.g. from period-tracking apps, used to restrict reproductive choices. |
| 17 | Right to own property. | Unauthorized access to or manipulation of digital assets. |
| 18 | Right to freedom of thought, conscience, and religion. | Manipulation of beliefs through targeted misinformation. Mind-reading technology. |

</div>

---
layout: default
title: "Universal declaration of human rights and data risks 4"
---

###### Appendix

# Universal declaration of human rights and data risks 4

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 19 | Right to freedom of opinion and expression. | Censorship or suppression of opinions using AI-driven content moderation. |
| 20 | Right to peaceful assembly and association. | Surveillance and data tracking deterring assembly or targeting participants. |
| 21 | Right to participate in government and free elections. | Election manipulation through targeted disinformation campaigns. |
| 22 | Right to social security and economic, social, and cultural rights. | Denial of benefits due to flawed algorithmic eligibility assessments. |
| 23 | Right to work, equal pay, and join trade unions. | Algorithmic hiring biases excluding qualified candidates. |
| 24 | Right to rest and leisure. | Excessive data-driven monitoring of employees reducing work-life balance. |

</div>

---
layout: default
title: "Universal declaration of human rights and data risks 5"
---

###### Appendix

# Universal declaration of human rights and data risks 5

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 25 | Right to an adequate standard of living; care for mothers and children. | Data misuse in welfare systems excluding vulnerable people. |
| 26 | Right to education. | Biased educational AI tools limiting opportunities for marginalized groups. |
| 27 | Right to cultural life, to share in scientific advancement, and to authorship. | AI use of creative works without permission; exclusion from the benefits of research built on people's data. |
| 28 | Right to a social and international order upholding these rights. | Cross-border data misuse undermining global human rights efforts. |
| 29 | Duties to the community and limits on rights for public welfare. | Data collection practices used disproportionately against marginalized groups. |
| 30 | No one may use the UDHR to undermine others' rights. | Invoking security to justify surveillance that erodes other rights. |

</div>

---
layout: section
color: dark
hexText: "CASES"
class: title-middle
---

# Appendix: case exercises

Interactive exercises to work through with the students

---
layout: default
---

# Where would you place these four cases?

<div class="grid-2">
<div class="card">

**A · Mood experiment (2014).** Facebook altered the news feeds of 689,003 users for one week to test emotional contagion, then published the study. Users had accepted the data use policy.

</div>
<div class="card">

**B · Fitness heat map (2018).** Strava published a global heat map of activities that users had chosen to share. It revealed the layout of military bases.

</div>
<div class="card">

**C · Open sensor data.** A lab publishes "anonymised" smartwatch data for reproducibility. Heart-rate and location traces still single out participants.

</div>
<div class="card">

**D · Psychotherapy records (2020).** Vastaamo's patient database had been reachable from the internet. Patients then received extortion demands.

</div>
</div>

For each case: **is it ethical? is it lawful?**

<!--
Live poll, 5 minutes. Ask students to place each case before showing the next slide.
A: Kramer, Guillory & Hancock (2014), PNAS. B: Strava, January 2018. C: a composite of a common practice. D: covered in the T block.
-->

---
layout: default
---

# Ethics and law can disagree about the same data use

<div class="quad">
<svg viewBox="0 0 760 420" role="img" aria-label="Two by two map: ethics on the vertical axis, law on the horizontal axis, with the four cases placed in quadrants">
  <rect x="100" y="10" width="320" height="170" rx="10" class="q-box" />
  <rect x="430" y="10" width="320" height="170" rx="10" class="q-goal" />
  <rect x="100" y="190" width="320" height="170" rx="10" class="q-box" />
  <rect x="430" y="190" width="320" height="170" rx="10" class="q-box" />
  <text x="118" y="46" class="q-title">Ethical aim, unlawful route</text>
  <text x="118" y="90" class="q-case">C · open "anonymised"</text>
  <text x="118" y="118" class="q-case">sensor data</text>
  <text x="448" y="46" class="q-title">Aligned: the goal</text>
  <text x="448" y="90" class="q-case">Our running case,</text>
  <text x="448" y="118" class="q-case">done well</text>
  <text x="118" y="226" class="q-title">Neither</text>
  <text x="118" y="270" class="q-case">D · Vastaamo</text>
  <text x="448" y="226" class="q-title">Lawful, ethically contested</text>
  <text x="448" y="270" class="q-case">A · Facebook mood study</text>
  <text x="448" y="298" class="q-case">B · Strava heat map</text>
  <text x="70" y="95" class="q-axis" transform="rotate(-90 70 95)">ethical</text>
  <text x="70" y="275" class="q-axis" transform="rotate(-90 70 275)">unethical</text>
  <text x="30" y="185" class="q-axis-title" transform="rotate(-90 30 185)">Ethics</text>
  <text x="260" y="388" class="q-axis">unlawful</text>
  <text x="590" y="388" class="q-axis">lawful</text>
  <text x="425" y="414" class="q-axis-title">Law</text>
</svg>
</div>

Each block ends by asking where the running case sits, and what moves it up and to the right.

<style>
.quad { display: flex; justify-content: center; margin: 0 0 0.5rem; }
.quad svg { width: 540px; height: auto; }
.q-box { fill: #fff; stroke: #000; stroke-width: 1.5; }
.q-goal { fill: #C9DAF8; stroke: #1155CC; stroke-width: 3; }
.q-title { font-size: 21px; font-weight: 700; fill: #000; }
.q-case { font-size: 19px; fill: #000; }
.q-axis { font-size: 17px; fill: #444; text-anchor: middle; }
.q-axis-title { font-size: 20px; font-weight: 700; fill: #000; text-anchor: middle; }
</style>

<!--
"Lawful" for A and B means lawful where and when it happened: A was US-based and pre-GDPR; in B users had opted in to public sharing.
C has an ethical aim (reproducibility) but data that still single people out remain personal data, and publishing them needs a legal basis (EDPB Guidelines 02/2026).
D: unlawful security failures and unethical treatment of the most vulnerable patients.
-->

---
layout: default
---

# Our running case: a sleep-and-mood study that becomes an app

<div class="grid-2">
<div class="card">

### Phase 1: the study (university)

- 200 student volunteers
- Smartwatch: heart rate, sleep, steps
- Phone: GPS, screen time
- Daily mood questionnaire
- Data synced through the watch vendor's cloud
- Goal: predict low-mood days from sensor data

</div>
<div class="card">

### Phase 2: the app (spin-out)

- Model trained on the study data
- Stress-coaching app for students
- Offered to universities as a well-being service
- An LLM writes personal feedback

</div>
</div>

In every block: **Is it ethical? Is it lawful? Where do they diverge? How do we resolve it?**

<!--
The case is invented but close to digital-phenotyping studies from lecture 4 (e.g. mood and sleep sensing).
It touches every topic: inferred health data, ethics review, legal basis, the emotion-recognition ban in education, device rules, anonymisation and LLM use.
-->

---
layout: default
title: "Case check: which of the study's data are health data?"
---

###### D · Case check

# Case check: which of the study's data are health data?

<div class="compact">

| Data | Personal data? | Special category? |
| --- | --- | --- |
| Heart rate, sleep | Yes | Yes: health |
| Steps | Yes | Once used to assess health, yes |
| GPS traces | Yes | Can reveal religion or health through places visited |
| Screen time | Yes | Not on its own |
| Daily mood ratings | Yes | Yes: mental health |
| Model output "low-mood day" | Yes | Yes: inferred health data |

</div>

Where is the study on the 2×2 so far? Lawful only if we treat almost everything as health data.

<!--
Let students answer before revealing the table. The debatable rows (steps, GPS, screen time) are the useful ones: context and purpose decide.
-->

---
layout: default
title: "Case check: who reviews the study, and who reviews the app?"
---

###### E · Case check

# Case check: who reviews the study, and who reviews the app?

<div class="grid-2">
<div class="card">

### The study

- Probably **non-medical** research: observational, no intervention
- University ethics review only if a TENK condition applies, e.g. a risk of mental harm from daily mood questions
- Power imbalance: do not let teachers recruit their own students
- If the aim becomes diagnosis, ask whether it is medical research

</div>
<div class="card">

### The app

- **No** mandatory ethics review
- A DPIA is required (health data, systematic monitoring)
- MDR conformity assessment if it makes medical claims
- The ethical judgement sits with the company, and with you if you build it

</div>
</div>

<!--
Quadrant check: the study can sit top-right with review and safeguards; the app risks drifting to "lawful, ethically contested".
-->

---
layout: default
title: "Pair task: the study versus the app"
---

###### L · Pair task (8 min)

# Pair task: the study versus the app

<div class="compact">

| **Question** | **Study (university)** | **App (spin-out)** |
| --- | --- | --- |
| Legal basis (Art 6)? | | |
| Article 9 condition? | | |
| Ethics review? | | |
| Medical device? | | |
| AI Act: out of scope, prohibited, high-risk, transparency? | | |
| How would you show it works, and for whom? | | |

</div>

Work in pairs. The answers differ between the two columns, and that is the point.

<!--
Give 8 minutes, then take two or three answers before showing the next slide.
-->

---
layout: default
title: "One possible answer"
---

###### L · Pair task

# One possible answer

<div class="small compact">

| **Question** | **Study (university)** | **App (spin-out)** |
| --- | --- | --- |
| **Legal basis** | Public interest: Art 6(1)(e) + Data Protection Act s. 4(3) | Consent or contract for app users; reusing study data needs its own basis and an agreement |
| **Article 9 condition** | 9(2)(j) + Data Protection Act s. 6(1)(7), with safeguards | 9(2)(a) explicit consent of app users |
| **Ethics review** | Only if a TENK condition applies | None mandatory; DPIA required |
| **Medical device** | No: research without medical claims | Depends on claims: "stress coaching" is wellness, "detects depression" is medical (class IIa or higher) |
| **AI Act** | Out of scope (Art 2(6)) | Prohibited if a university uses it to infer students' emotions from biometric data, unless for medical or safety reasons; high-risk if it is a device needing a notified body; transparency duties for the LLM feedback (Art 50) |
| **Evidence it works** | Validate sensor features against a reference; test the model on new participants and across groups; report with TRIPOD+AI | Clinical evaluation if it is a device; a trial before effectiveness claims; check performance and uptake across groups |

</div>

<!--
Accept other well-argued answers. The key learning: the same model moves through different legal regimes as it moves from research to product.
The last row covers evaluating tools built on patient-generated data. Compliance does not show that a tool works: that needs evidence, and the bar rises with the claims.
- Sensor measures: the V3 framework (verification, analytical validation, clinical validation; Goldsack et al., 2020).
- Prediction models: report development and validation with TRIPOD+AI (Collins et al., BMJ 2024); external validation on new people matters more than accuracy on the training cohort.
- Interventions: early clinical evaluation of AI with DECIDE-AI (Vasey et al., 2022); trials with SPIRIT-AI and CONSORT-AI (2020).
- Health systems' evidence bars: NICE Evidence Standards Framework for digital health technologies (UK); DiGA in Germany, which requires evidence of a positive care effect for reimbursement.
- For whom: performance, engagement and drop-out can differ by age, skin tone, device model or digital literacy; report subgroup results (justice, slide 17; bias, slide 55).
-->

---
layout: default
title: "Live demo: re-identify, then add noise"
---

###### T · Live demo (10 min)

# Live demo: re-identify, then add noise

```python
import numpy as np
import pandas as pd

df = pd.read_csv("toy_wearable.csv")  # synthetic data, no names
qi = ["birth_year", "sex", "postcode", "watch_model"]
unique = df.groupby(qi).size().eq(1).sum()
print(f"{unique} of {len(df)} participants are unique on {qi}")

# A differentially private count with the Laplace mechanism
epsilon = 1.0                       # privacy budget
true_count = (df["sleep_h"] < 6).sum()
noisy_count = true_count + np.random.laplace(scale=1 / epsilon)
```

For real releases, use a vetted library (e.g. OpenDP, diffprivlib), not hand-written noise.

<!--
The toy dataset is synthetic. Uniqueness grows as quasi-identifiers are added; the noisy count changes with epsilon.
A count has sensitivity 1, so the Laplace scale is 1/epsilon.
-->

---
layout: default
title: "Case check: can we publish the dataset, and can we send it to an LLM?"
---

###### T · Case check

# Case check: can we publish the dataset, and can we send it to an LLM?

<div class="grid-2">
<div class="card">

### Publish?

- Raw or pseudonymised: **no**, still personal data
- Per-participant daily features: likely fail no record isolation and no linkage
- Group statistics with differential privacy, or tested synthetic data: **possibly**, with a documented assessment
- Alternative: controlled access through a secure environment

</div>
<div class="card">

### Send to an LLM?

- Only an approved tool, under a processor agreement
- Processed in the EU, or with a valid transfer basis
- Covered by the privacy notice and the DPIA
- Never a consumer chatbot

</div>
</div>

<!--
Quadrant check: publishing "anonymised" daily features moves the study to "ethical aim, unlawful route". Controlled access keeps it top-right.
-->

---
layout: default
title: "Back to the case: what moves it up and to the right"
---

###### I · Synthesis

# Back to the case: what moves it up and to the right

<div class="grid-2">
<div class="card">

### The study

- **Lawful:** public-interest basis, Art 9(2)(j), DPIA, processor agreement with the vendor
- **Ethical:** recruitment free of power imbalance, minimised features, secure environment, controlled release, honest information about vendors and LLMs

</div>
<div class="card">

### The app

- **Lawful:** explicit consent, its own DPIA, device assessment if it makes medical claims, no emotion inference in education without a medical purpose
- **Ethical:** claims backed by evidence, no reuse of study data beyond what participants were told, performance tested across groups

</div>
</div>

<!--
Ask students to move each phase on the 2×2 from the hook. Most will put the study top-right and the app bottom-right unless the safeguards above are in place.
-->

---
layout: default
title: "Exit ticket"
---

###### I · Exit ticket (3 min)

# Exit ticket

1. Name one way the study and the app differ **legally**, and one way they differ **ethically**.
2. Which legal basis and Article 9 condition would you use for the study, and why not consent?
3. A colleague says the dataset is anonymous because names were removed. Which **two questions** do you ask?

<!--
One question per learning outcome. Collect answers on paper or with a quick form; they show what to fix next year.
-->
