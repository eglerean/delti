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
color: sand
class: no-footer
hexText: "DATA\nETHICS\nLAW\nTECH"
hexSeed: 7
---
###### CS-E4150 - Digital Health and Human Behavior

# Data, Ethics, Law, Technologies, Individuals
Applied data ethics for digital health research and innovation

::presenter::
**Dr. Enrico Glerean**, Staff Scientist, Aalto University, November 2026

<div class="license-line"><CcBy /> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a> · <a href="https://github.com/eglerean/delti" target="_blank" rel="noopener" class="gh-link" title="Slides on GitHub" aria-label="Slides on GitHub"><carbon-logo-github class="gh-icon" /> GitHub</a> · <a href="https://eglerean.github.io/delti/Glerean_2026_DataEthicsLawTechnology.pdf" target="_blank" rel="noopener" class="gh-link" title="Slides as PDF" aria-label="Slides as PDF"><carbon-document-pdf class="gh-icon" /> PDF</a></div>

<style>
h1 { font-size: 2.5rem !important; line-height: 1.1 !important; }
/* Red eyebrow on the yellow cover, same red as the eyebrows on the other slides */
h6, h6:not(.opacity-100) { color: #E8413E !important; }
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

1. <b>D</b>ata about individuals: when does it become health data?
2. <b>E</b>thics in research and in innovation
3. <b>L</b>aw - governing data and digital systems
4. <b>T</b>echnology - privacy and AI
5. <b>I</b>ndividuals - we are all study participants
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

# Context for this audience
###### Digital Health and Human Behaviour course

- You might become a **researcher** in academia or a company working with data from human participants
- You might become a **data scientist** in a company or a manager of a team of developers building applications that process **personal data**
- You most likely won’t need to worry about “***data governance***” and ”***lawfulness of personal data processing***” as the company you will work for will have a legal expert and a **data protection officer**
- However, **it is beneficial to understand what you can ethically and legally do with data from individuals**
- **Only very high-risk applications are truly prohibited**, often **cybersecurity** and **transparency towards the data subjects** is all you need to build your application

---
layout: section
color: dark
hexText: "D"
class: title-middle
---

# D. Data about individuals

<span class="delti-on">D</span> · E · L · T · I
<br>What makes data personal? And when does it become health data?

---
layout: default
title: "Personal data is any information relating to an identifiable person"
---

###### D · Data about individuals

# What is personal data?

- **Personal data** is a broad concept under the EU’s **General Data Protection Regulation**
- **Personal data** is information relating to an identified or identifiable natural person  (GDPR Art 4(1))
- **Identifiable** by any means *reasonably likely* to be used, by the **controller** or by anyone else (GDPR Recital 26)
- **Practical rule:** if you collect information **from** or **about** people, treat it as personal data

Exceptions:
- The same dataset can be personal data for one holder and not for another (CJEU C-413/23 P, *EDPS v SRB*, 2025)
- **Out of scope:** truly anonymous data, and data of deceased persons (Recital 27), although national law may still protect them, e.g. patient records


---
layout: default
title: "Identifiers come in degrees, and sensor data are among them"
---

# PD: direct and indirect identifiers (quasi-identifier)

1. **Direct identifiers:** information which is **sufficient on its own to identify an individual**<br>- e.g. a person’s name, email address (containing the person’s name), personal identification number, fingerprints, a facial image, a person's voice, video, brain scan images, dental records, DNA
2. **Strong indirect identifiers :** information which **can be used to identify an individual fairly easily**<br>- e.g. a postal address, a phone number, a vehicle registration number, bibliographic citation of a publication, an email address not in the form of the personal name, an unusual job title, a very rare disease, a job position held by only one person at a time, a student ID number, a bank account number, IP address of a computer, cookie identifier, RFID tags, location data
3. **Indirect identifiers:** information that on its own is not enough to identify someone but, when **linked with other available information, could be used to deduce the identity of a person:**<br>- e.g. age, gender, education, status in employment, economic activity and occupational status, socio-economic status, household composition, income, marital status, mother tongue, ethnic background, place of work or study, postal code, municipality, major region.

##### Sensor and other digital traces are direct identifiers
Many type of raw sensor data (EGC and heart-rate time series, gait from accelerometers, sleep data) and other digital traces (location, typing time series, internet history) should be treated as **direct identifiers** since with enough data, it is possible to build a fingerprint. 


---
layout: default
title: "Sensor data identify people even without names"
---


# Digital traces and re-identification examples

- **Four location-time points re-identify 95% of population:** in 15 months of mobile phone records of 1.5 million subjects ([de Montjoye et al., 2013](https://doi.org/10.1038/srep01376))
- **Fifteen Simple background factors re-identify 99% of population:** 15 demographic attributes (postal code, birth date, gender, number of children) can correctly re-identify 99.98% of Americans in any dataset, even a small sample ([Rocher et al., 2019](https://doi.org/10.1038/s41467-019-10933-3))
- **Eight public movie ratings are enough:** movie ratings with approximate dates singled out 99% of the <i>"anonymised"</i> Netflix Prize users, by matching them with public IMDb reviews ([Narayanan & Shmatikov, 2008](https://doi.org/10.1109/SP.2008.33))
- **Aggregated data can also be sensitive:** the outlines of military bases where identified in Strava (an app for sharing sports tracking routes) global heat map of users  ([The Guardian, 2018](https://www.theguardian.com/world/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-army-bases))

<div class="ref-bottom">Jarmul, K. (2023). Practical Data Privacy, ch. 4. O'Reilly. · Glerean, E. (2025). Fundamentals of Secure AI Systems with Personal Data, ch. 4. EDPB Support Pool of Experts.</div>


---
layout: default

---

# Health data: measured and inferred

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

**Inference counts as health data**

- Data that **indirectly reveal** a special category ([CJEU C-184/20, *OT*, 2022](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62020CJ0184))
- Online orders of pharmacy-only medicines are health data ([CJEU C-21/23, *Lindenapotheke*, 2024](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0021))
- A model that predicts low mood or insomnia from sleep and activity **creates** health data (GPS and phone use predict depressive symptoms: [Saeb et al., 2015](https://doi.org/10.2196/jmir.4273))
- Repeated GPS visits to a place of worship or a clinic can reveal religion or health (case [FTC v. Kochava, 2022](https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-sues-kochava-selling-data-tracks-people-reproductive-health-clinics-places-worship-other))

</div>
</div>

---
layout: section
color: dark
hexText: "E"
class: title-middle
---

# E. Ethics

D · <span class="delti-on">E</span> · L · T · I
<br>Research ethics principles, and risk mitigation

---
layout: default
---

# Ethics

<br>

- 1 a: a set of **moral principles** : a theory or system of moral values<br>—often used in plural but singular or plural in constructionan elaborate ethics
  - b: the principles of conduct governing an individual or a group
  - c: a consciousness of moral importance
  - d: a guiding philosophy
- 2 ethics: a set of **moral issues or aspects** (such as rightness)
- 3 ethics: the **discipline** dealing with what is good and bad and with moral duty and obligation

<div class="ref-bottom">Source: <a href="https://www.merriam-webster.com/dictionary/ethics?utm_campaign=sd&utm_medium=serp&utm_source=jsonld" target="_blank" rel="noopener">Merriam-Webster</a></div>

---
layout: default
---

# Ethics is not law

<div class="venn">
<svg viewBox="0 0 700 342" role="img" aria-label="Venn diagram: two partly overlapping circles, Ethics and Law">
  <circle cx="346" cy="171" r="171" class="v-ethics" />
  <circle cx="432" cy="171" r="171" class="v-law" />
  <text x="113" y="171" class="v-label" style="fill: #990000">Ethics</text>
  <text x="585" y="171" class="v-label" style="fill: #1155CC">Law</text>
</svg>
</div>

- In the ideal case they overlap
- Different countries have different overlap
- Things can be **ethical but illegal** (giving humanitarian help without permission), or **legal but unethical** (exploiting loopholes to avoid paying taxes)

<style>
.venn { display: flex; justify-content: center; margin: 0.25rem 0 1rem; }
.venn svg { width: 520px; height: auto; }
.v-ethics { fill: #F4CCCC; fill-opacity: 0.45; }
.v-law { fill: #C9DAF8; fill-opacity: 0.46; }
.v-label { font-size: 44px; font-weight: 700; text-anchor: middle; dominant-baseline: middle; }
</style>

---
layout: default
---

# Ethics and the Normative Cascade

<div class="cascade">
<svg viewBox="-6 -6 670 288" role="img" aria-label="Normative cascade: Ethics leads to Law, Law to Business, Business to Customers, and Customers loop back to Ethics">
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

- **Ethics** is not **law:** in the ideal case they overlap, in practice they never do.
- **People** decide in what kind of society they want to live and drive ethical principles which are at the base of law
- You can also replace “business” with “government” and “customers” with “citizens”.

<div class="ref-bottom">Reference: Floridi, L. (2023). The ethics of artificial intelligence: Principles, challenges, and opportunities.</div>

<style>
.cascade { margin: 0 0 0.75rem; }
.cascade svg { width: 480px; height: auto; display: block; }
.nc-oval { fill: #fff; stroke: #000; stroke-width: 1.5; }
.nc-label { font-size: 20px; text-anchor: middle; dominant-baseline: middle; fill: #000; }
.nc-line { fill: none; stroke: #000; stroke-width: 2; }
.nc-dash { stroke-dasharray: 7 5; }
.nc-head { fill: #000; }
</style>

---
layout: default
title: "Five principles: four from bioethics, one added for AI"
---

# Five principles of ethics
Four from bioethics (Beauchamp, T. & Childress, J. (2019). Principles of Biomedical Ethics, 8th ed.) and one added for AI (Floridi, L. (2023). The Ethics of Artificial Intelligence)

<div class="compact">

| **Principle** | **Meaning** | **In digital health** |
| --- | --- | --- |
| **Beneficence** | Do only good: Promote well-being of individuals and society | Sensor-based early warning of a depressive relapse |
| **Nonmaleficence** | Do no harm: avoid harm and minimize risks (e.g. privacy and security) | Store daily distance instead of raw GPS traces |
| **Autonomy** | Respect individuals' rights to make informed decisions about their lives | Participants can stop sharing watch data at any time, without penalty |
| **Justice** | Ensure fairness in the distribution of benefits, risks, and resources | Check that the model works as well for groups under-represented in training |
| **Explicability** | Make AI understandable and accountable | Users and clinicians can see why a "low-mood day" was mis-classified |

</div>


---
layout: default
title: "Ethics review starts with listing the issues"
---

###### E · Ethics

# Research ethics requires pre-evaluation of risks before conducting research that can cause harm

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
---

###### E · Ethics

# Ethical pre-review in Finland

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
- **<a href="https://www.pnas.org/doi/10.1073/pnas.1320040111">Facebook, 2014</a>:** news feeds of 689,003 users were altered for one week to test emotional contagion. Consent relied on the data use policy; the journal later added an editorial expression of concern
- Possible solutions: risks mitigation in EU:
    - **Data Protection Impact Assessment** (GDPR Art 35)
    - **Fundamental Rights Impact Assessment** for some deployers of high-risk AI (AI Act Art 27)
    - **Conformity assessment** for regulated products
    - internal review boards, staff, reputation

<div class="card dark small">

**Note:** companies that claim "scientific research" for GDPR's research rules must match the six factors ([EDPB Guidelines 1/2026](https://www.edpb.europa.eu/documents/guideline/guidelines-12026-on-processing-of-personal-data-for-scientific-research_en)):

1. **Methodical and systematic approach** 
2. **Adherence to ethical standards** 
3. **Verifiability and transparency**
4. **Autonomy and independence**
5. **Objectives of the research**
6. **Potential to contribute to scientific knowledge**

</div>

<style>
.card.dark { font-size: 0.8rem; line-height: 1.35; margin-top: 0.6rem; }
.card.dark p { margin-bottom: 0.3rem; }
.card.dark ol { margin: 0; }
</style>

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

D · E · <span class="delti-on">L</span> · T · I
<br>From fundamental rights to the GDPR, the AI Act, and other legislations

---
layout: two-cols
title: "From human rights to law"
---

::header::
###### L · Law

# From human rights to law

::left::

### Universal Declaration of Human Rights (1948)

- Adopted by the United Nations; not binding law
- 30 articles; "all human beings are born free and equal in dignity and rights"
- **Art 12:** privacy
- **Art 27:** the right to share in scientific advancement and its benefits
- [Read all 30 at least once](https://www.un.org/en/about-us/universal-declaration-of-human-rights)

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

###### L · Law - GDPR

# The GDPR in one slide

- **Regulation (EU) 2016/679:** adopted in 2016, (applied from 25 May 2018), with national specifications (Finland: Data Protection Act 1050/2018)
- **Scope:** organisations in the EU, and organisations elsewhere that offer services to people in the EU or monitor them (Art 3)
- **Roles:** the **controller** governs the personal data; a **processor** acts on behalf of the controller and **joint controllers** decide together
- **Typical case in university:** the university is the controller of the study, some external service (e.g. wearable watch vendor) is a processor if it processes the data for your study.
- **Authority in Finland:** Office of the Data Protection Ombudsman ([tietosuoja.fi](https://tietosuoja.fi/en/home))
- **Fines:** up to €20 million or 4% of worldwide annual turnover (Art 83(5))


---
layout: default
title: "The principles of the GDPR, applied to research"
---

###### L · Law - GDPR

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

###### L · Law - GDPR

# Consent to take part ≠ GDPR consent legal basis

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
- GDPR consent legal basis (Art 6(1)(a)) only if freely given, specific, informed, unambiguous and withdrawable: hard with power imbalances
- Withdrawing GDPR consent stops processing based on it

</div>
</div>

You can ask for both when needed, but keep the two requests **clearly separated** (EDPB Guidelines 1/2026).


---
layout: default
title: "Six legal bases, used differently in academia and industry"
---

###### L · Law - GDPR

# Six legal bases  in academia and industry

<div class="compact">

| **Legal basis (Art 6(1))** | **Typical in academia** | **Typical in industry** |
| --- | --- | --- |
| **(a) Consent** | Possible but stricter with withdrawals | Common for apps; must be freely given |
| **(b) Contract** | Rarely | Providing the service the user signed up for; not for research |
| **(c&#8203;) Legal obligation** | Statutory reporting | Tax, product vigilance |
| **(d) Vital interests** | Emergencies only | Emergencies only |
| **(e) Public interest** | Most used legal basis for Finnish universities (Data Protection Act s. 4(3)) | Only if a law gives the company that task |
| **(f) Legitimate interests** | Limited for public bodies performing their tasks (Art 6(1), last subparagraph) | Common for commercial research, with a documented balancing test (EDPB Guidelines 1/2024; 1/2026) |

</div>


---
layout: default
title: "Health data need two locks: a legal basis and an Article 9 condition"
---

###### L · Law - GDPR

# Health data need two locks

- **Lock 1:** a legal basis under [GDPR Art 6](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (previous slide)
- **Lock 2:** an exception to the [Art 9(1)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) prohibition. Common ones in research:
    - **(a)** explicit consent
    - **(j)** scientific research based on EU or national law, with Art 89(1) safeguards
    - **(h), (i)** health care and public health
- **Finland:** [Data Protection Act](https://www.finlex.fi/en/legislation/translations/2018/eng/1050) s. 6(1)(7) allows research processing, with suitable and specific safeguards (s. 6(2))
- **Registry data:** secondary use of Finnish health and social data goes through the [Secondary Use Act (552/2019)](https://www.finlex.fi/fi/lainsaadanto/2019/552) and [Findata](https://findata.fi/en/)
- **From 2029:** the [EHDS](https://eur-lex.europa.eu/eli/reg/2025/327/oj) adds an EU-wide route for secondary use (later in this block)
- **If approved:** the [Digital Omnibus proposal](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0837) (Nov 2025) would add a new Art 9(2)(k) exception for residual special-category data in the development and operation of AI.

<div class="ref-bottom"><a href="https://www.edpb.europa.eu/documents/guideline/guidelines-12026-on-processing-of-personal-data-for-scientific-research_en" target="_blank" rel="noopener">EDPB Guidelines 1/2026 on processing of personal data for scientific research purposes</a> (version for consultation, April 2026).</div>

<!--
Member States may add conditions for genetic, biometric or health data (Art 9(4)).
Digital Omnibus status (Nov 2026): the Council agreed its negotiating mandate on 21 October 2026 and narrowed the exception to incidental processing of residual data that the controller did not intend to process; the Parliament has not adopted its position yet, so trilogues have not concluded. Critics argue it weakens Art 9 (European Law Blog). Check the status before teaching.
-->

---
layout: default
title: "Three assessments ask three different questions"
---

###### L · Law - GDPR

# Tools for risk mitigation

<div class="compact">

| **Assessment** | **Question** | **Required when** | **Who** |
| --- | --- | --- | --- |
| **Ethics review** | Should we do this study, and is it fair to participants? | Medical research; TENK conditions; funder rules | Ethics committee |
| **DPIA** (GDPR Art 35) | What are the risks to people's rights, and how do we reduce them? | Likely high risk, e.g. health data with systematic monitoring | Controller, advised by the DPO |
| **Conformity assessment** (MDR, AI Act) | Is the product safe, and does it meet its requirements? | Medical devices; high-risk AI systems | Manufacturer or provider, often a notified body |
| **FRIA** (AI Act Art 27) | What does deploying this high-risk AI do to fundamental rights? | Public bodies and some private deployers of high-risk AI | Deployer |

</div>


<!--
Students often assume an ethics approval covers data protection, or the reverse. Different questions, different owners, different documents.
-->

---
layout: default
title: "The data protection impact assessment"
---

###### L · Law - GDPR

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
  <svg viewBox="-2 -2 504 414" role="img" aria-label="DPIA risk matrix: severity of impact (minimal, some, serious) against likelihood of harm (remote, reasonable possibility, more likely than not). Serious harm is high risk when reasonably possible or more likely; some impact is medium risk when reasonably possible and high risk when more likely than not; everything else is low risk.">
    <!-- risk cells: columns remote / reasonable / likely, rows serious / some / minimal -->
    <rect x="140" y="0"   width="120" height="100" class="r-low" />
    <rect x="260" y="0"   width="120" height="100" class="r-high" />
    <rect x="380" y="0"   width="120" height="100" class="r-high" />
    <rect x="140" y="100" width="120" height="100" class="r-low" />
    <rect x="260" y="100" width="120" height="100" class="r-med" />
    <rect x="380" y="100" width="120" height="100" class="r-high" />
    <rect x="140" y="200" width="120" height="100" class="r-low" />
    <rect x="260" y="200" width="120" height="100" class="r-low" />
    <rect x="380" y="200" width="120" height="100" class="r-low" />
    <text x="200" y="50"  class="r-cell">Low risk</text>
    <text x="320" y="50"  class="r-cell">High risk</text>
    <text x="440" y="50"  class="r-cell">High risk</text>
    <text x="200" y="150" class="r-cell">Low risk</text>
    <text x="320" y="140" class="r-cell">Medium</text>
    <text x="320" y="162" class="r-cell">risk</text>
    <text x="440" y="150" class="r-cell">High risk</text>
    <text x="200" y="250" class="r-cell">Low risk</text>
    <text x="320" y="250" class="r-cell">Low risk</text>
    <text x="440" y="250" class="r-cell">Low risk</text>
    <!-- row labels: severity -->
    <text x="95" y="40"  class="r-lab">Serious</text>
    <text x="95" y="62"  class="r-lab">harm</text>
    <text x="95" y="140" class="r-lab">Some</text>
    <text x="95" y="162" class="r-lab">impact</text>
    <text x="95" y="240" class="r-lab">Minimal</text>
    <text x="95" y="262" class="r-lab">impact</text>
    <!-- column labels: likelihood -->
    <text x="200" y="335" class="r-lab">Remote</text>
    <text x="320" y="324" class="r-lab">Reasonable</text>
    <text x="320" y="346" class="r-lab">possibility</text>
    <text x="440" y="324" class="r-lab">More likely</text>
    <text x="440" y="346" class="r-lab">than not</text>
    <!-- grid lines -->
    <path d="M50 0H500M50 100H500M50 200H500M50 300H500M140 370H500M50 0V300M140 0V370M260 0V370M380 0V370M500 0V370" class="r-grid" />
    <!-- axis titles -->
    <text x="0" y="0" transform="translate(28 150) rotate(-90)" class="r-axis">Severity of impact</text>
    <text x="320" y="396" class="r-axis">Likelihood of harm</text>
  </svg>
  <p class="small"><a href="https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/data-protection-impact-assessments-dpias/how-do-we-do-a-dpia/" target="_blank" rel="noopener">Derived from this source</a></p>
</div>
</div>

<style>
.dpia { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 0.8fr); gap: 1.5rem; align-items: start; }
.dpia-fig svg { display: block; width: 100%; height: auto; }
.r-low { fill: #DDF0C4; }
.r-med { fill: #FFC9A8; }
.r-high { fill: var(--aalto-red); }
.r-grid { fill: none; stroke: currentColor; stroke-width: 1.5; }
.r-cell { font-size: 19px; font-weight: 700; fill: #000; text-anchor: middle; dominant-baseline: middle; }
.r-lab { font-size: 17px; fill: currentColor; text-anchor: middle; dominant-baseline: middle; }
.r-axis { font-size: 19px; font-weight: 700; fill: currentColor; text-anchor: middle; dominant-baseline: middle; }
.dpia-fig p { text-align: right; margin-top: 0.3rem; }
</style>

<!--
The running case ticks 3, 4, 6 and 7 (students can be vulnerable when the researchers are their teachers): a DPIA is clearly needed.
-->



---
layout: two-cols
title: "The AI Act regulates AI by risk, and its dates have moved"
---

::header::
###### L · Law - EU AI Act

# The EU AI Act 

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

###### L · Law - EU AI Act

# EU AI Act research exemption

- **Art 2(6):** AI systems or models developed and put into service **for the sole purpose** of scientific research and development are out of scope
- **Art 2(8):** research, testing and development **before** placing on the market or putting into service are out of scope; **testing in real-world conditions is not**
- It covers applied research and company R&D, not only basic research
- It exempts from the AI Act only: the GDPR, ethics review and the MDR still apply
- **AI literacy (Art 4)** applies to providers and deployers, e.g. a university that deploys AI tools for its staff

<div class="card blue">
<b>Example:</b> a research study's machine learning model is out of scope; but the spin-out's app is in scope.
</div>

<!--
The exemption is not limited to basic research, and it ends when the system is placed on the market or put into service.
-->

---
layout: default
title: "Some AI practices have been banned since February 2025"
---

###### L · Law - EU AI Act

# Prohibited AI systems (February 2025)

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

**Example**

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
###### L · Law - EU AI Act

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

###### L · Law - Medical device regulation

# Medical devices

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
###### L · Law - Other medical regulations

# Other regulations related to medical applications

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
###### L · Law - Future

# Changes in the law: the Digital Omnibus

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

# Privacy by design

<div class="pbd">
<div>

- **Art 25:** data protection by design and by default
- **Before collection:** collect features, not raw streams (daily sleep duration, not raw accelerometer data); coarsen location; avoid free text
- **At ingestion:** pseudonymise; keep the key separate; give each person the least access they need
- **During analysis:** approved storage and compute, e.g. secure processing environments for health data
- **Before release:** run the anonymity test; release aggregates or controlled access; document every release
- **Throughout:** a privacy notice in plain language that names vendors and transfers; a DPIA when risk is high

</div>
<div class="card yellow">

**The 7 principles of privacy by design** <span class="small">([Cavoukian, 2009](https://en.wikipedia.org/wiki/Privacy_by_design))</span>

<div class="small">

1. **Proactive not reactive;** preventive not remedial
2. **Privacy as the default** setting
3. **Privacy embedded** into design
4. **Full functionality:** positive-sum, not zero-sum
5. **End-to-end security:** full lifecycle protection
6. **Visibility and transparency:** keep it open
7. **Respect for user privacy:** keep it user-centric

</div>
</div>
</div>

<style>
.pbd { display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr); gap: 1.5rem; align-items: start; }
</style>

<!--
Art 25 is "data protection by design and by default". "Large scale" has no fixed threshold such as a number of participants.
-->

---
layout: image-right
image: /images/pets-landscape.png
class: fit-image
title: "Privacy Enhancing Technologies (PETs)"
---

###### T · Technology - Privacy Enhancing Technologies 

# Privacy Enhancing Technologies (PETs)

Broadly two families:

- Techniques that **transform the data**
- Techniques that **harden the computing environment**

Embedded in the security of all other components.

<p class="pets-caption">Figure 5.1 from <a href="https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf">Glerean 2025</a>. The landscape of PETs solutions. Various techniques can be combined to ensure the privacy of the entire system by altering the data or by improving security of storage, communication, and computations. The image is an evolution of Garrido et al. (2022).</p>

<style>
.slidev-layout .pets-caption { position: absolute; left: 3.5rem; right: 2rem; bottom: 3.2rem; font-size: 0.66rem !important; line-height: 1.3 !important; opacity: 0.8; }
</style>

---
layout: default
title: "Privacy-enhancing technologies trade risk for utility and effort"
---

###### T · Technology - Privacy Enhancing Technologies 

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
title: "Anonymity is a risk judgement, not a technique"
---

###### T · Technology - Privacy Enhancing Technologies 

# Anonymous data

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

<div class="ref-bottom"><a href="https://www.edpb.europa.eu/public-consultations/guidelines-022026-on-anonymisation_en" target="_blank" rel="noopener">EDPB Guidelines 02/2026 on anonymisation</a> (version for public consultation).</div>

<!--
The draft guidelines were open for consultation until 30 October 2026; check for the final version.
-->

---
layout: default
title: "Removing names is not anonymisation"
---

###### T · Technology - Privacy Enhancing Technologies 

# From personal to anonymous data

<div class="spectrum">
  <div class="sp-top"><p><strong>Personal data with direct identifiers</strong></p></div>
  <div class="sp-top"><p><strong>Pseudonymisation</strong></p><p class="sp-tech">Replacing strong identifiers: tokenization, hashing, encryption</p></div>
  <div class="sp-top"><p><strong>Masking</strong></p><p class="sp-tech">Suppression / removal of strong identifiers</p></div>
  <div class="sp-top"><p><strong>Anonymisation</strong></p><p class="sp-tech">K-anonymity, l-diversity, t-closeness, perturbation, data swapping, differential privacy</p></div>
  <div class="sp-top"><p><strong>Anonymisation</strong></p><p class="sp-tech">Aggregation, data synthesis</p></div>
  <div class="sp-ends"><span class="sp-personal">Personal data</span><span class="sp-anon">Anonymous data</span></div>
  <div class="sp-arrow" aria-hidden="true"></div>
  <div class="sp-bottom"><p><strong>Easy to re-identify</strong></p></div>
  <div class="sp-bottom"><p><strong>Can be re-identified with the key</strong></p><p class="sp-crit">Still personal data for the key holder</p></div>
  <div class="sp-bottom"><p><strong>The key is lost but other data (will) exist, and it can be reasonably likely to re-identify</strong></p><p class="sp-crit">Usually fails isolation and linkage</p></div>
  <div class="sp-bottom"><p><strong>Re-identification is not reasonably likely, but data is still data from individuals</strong></p><p class="sp-crit">Anonymous only if isolation, linkage and inference all pass</p></div>
  <div class="sp-bottom"><p><strong>Re-identification is not reasonably likely, and data is not related to any individual</strong></p><p class="sp-crit">Still test: small counts, outliers and memorised records can fail the criteria</p></div>
</div>

Pseudonymised data stay personal data for the key holder (EDPB Guidelines 01/2025); for a recipient without reasonable means to re-identify, they may not be (CJEU C-413/23 P).

<div class="ref-bottom">Figure adapted from <a href="https://fundamentals-of-secure-ai-systems-with-personal-data-9cd9e2.pages.code.europa.eu/images/src/FIGS2.2_anon_spectrum.svg" target="_blank" rel="noopener">Glerean, E. (2025). Fundamentals of Secure AI Systems with Personal Data, fig. S2.2</a>. Deeper look at minimisation and anonymisation: <a href="https://zenodo.org/records/10649060" target="_blank" rel="noopener">https://zenodo.org/records/10649060</a></div>

<style>
/* Five steps from personal to anonymous data, over an orange-to-teal arrow (wording from Glerean 2025, fig. S2.2) */
.spectrum { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0 1rem; margin-top: 0.6rem; }
.spectrum p { margin: 0 0 0.2rem; font-size: 0.9rem; line-height: 1.2; }
.sp-top { align-self: start; }
.spectrum .sp-tech { font-size: 0.65rem; font-style: italic; }
.spectrum .sp-crit { font-size: 0.65rem; color: var(--asc-muted); }
.sp-ends { grid-column: 1 / -1; display: flex; justify-content: space-between; margin-top: 0.5rem; padding-right: 3rem; font-style: italic; font-weight: 700; }
.sp-personal { color: #F07F5C; }
.sp-anon { color: #2F6B6B; }
.sp-arrow { grid-column: 1 / -1; height: 2.2rem; margin: 0.1rem 0 0.6rem; background: linear-gradient(90deg, #F07F5C, #2F6B6B); clip-path: polygon(0 25%, calc(100% - 2.6rem) 25%, calc(100% - 2.6rem) 0, 100% 50%, calc(100% - 2.6rem) 100%, calc(100% - 2.6rem) 75%, 0 75%); }
</style>

<!--
The grey lines under each step map it to the three EDPB criteria (isolation, linkage, inference).
The book figure says "impossible to re-identify"; the slide uses "not reasonably likely" because the legal test is an insignificant likelihood, not zero.
Common misconceptions: masking is still pseudonymisation; aggregates and synthetic data are not anonymous by default; differential privacy describes how a result is released, not a dataset.
-->

---
layout: default
title: "Aggregates, synthetic data and models can still leak"
---

###### T · Technology - Privacy Enhancing Technologies  

# Leaks from aggregates, synthetic data, and models

- **Reconstruction:** the US Census Bureau rebuilt person-level records (block, age, sex, race) from its own published 2010 census tables, and matched many of them to commercial data. It adopted differential privacy for the 2020 census ([Garfinkel et al., 2019](https://doi.org/10.1145/3287287))
- **Membership inference:** an attacker can tell whether a person's record was in the data. Even summary allele frequencies from a genomic study revealed whether a given person had taken part ([Homer et al., 2008](https://doi.org/10.1371/journal.pgen.1000167)); the same works against trained models ([Shokri et al., 2017](https://doi.org/10.1109/SP.2017.41))
- **Memorisation:** language models can reproduce training data verbatim when prompted; names, phone numbers and email addresses were extracted from GPT-2 ([Carlini et al., 2021](https://arxiv.org/abs/2012.07805))
- **EDPB:** AI models trained on personal data cannot in all cases be considered anonymous ([Opinion 28/2024](https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en)); inference from aggregates, synthetic data and models counts against anonymity ([Guidelines 02/2026](https://www.edpb.europa.eu/public-consultations/guidelines-022026-on-anonymisation_en), paras 17, 77, 82)

<div class="ref-bottom">Jarmul, K. (2023). Practical Data Privacy, ch. 2 and 4. · Glerean, E. (2025). Fundamentals of Secure AI Systems with Personal Data, ch. 7.</div>

<!--
The practical consequence: a model trained on the study data may itself be personal data, which matters when the spin-out takes it.
-->

---
layout: default
title: "Sending participant data to an LLM is a data protection decision"
---

###### T · Technology - Cloud computing and remote AI endpoints

# Personal data processed on the cloud

<div class="cloud">
<div>

The cloud is someone else's computer: **confidentiality can be lost**

- **Provider access:** data are decrypted while processed; admins, subprocessors and abuse-monitoring staff may see them
- **Retention you do not control:** prompts and outputs are logged; in 2025 a US court ordered OpenAI to keep even deleted ChatGPT chats ([NYT v. OpenAI](https://simonwillison.net/2025/Jun/5/openai-court-order/))
- **Training on inputs:** consumer plans of US LLM providers such as OpenAI and Anthropic may train on chats unless you opt out ([Anthropic, 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms)); business and API terms usually do not
- **Foreign access:** the US [CLOUD Act](https://www.congress.gov/bill/115th-congress/house-bill/4943) lets US authorities compel US providers to hand over data, even from EU data centres; US surveillance law is why Privacy Shield fell ([Schrems II, 2020](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0311))
- **Fragile transfer basis:** the EU–US Data Privacy Framework was upheld in 2025 (Latombe), but an [appeal is pending](https://eur-lex.europa.eu/eli/C/2025/6610/oj) (C-703/25 P)
- **Safer options:** approved enterprise contracts (no training, limited retention), EU-hosted or local open-weight models, encryption keys you hold; the EU is investing in its own cloud and AI capacity ([Tech Sovereignty Package, 2026](https://digital-strategy.ec.europa.eu/en/news/commission-proposes-tech-sovereignty-package-strengthen-europes-digital-autonomy-and-resilience))

</div>
<div class="card yellow">

**Sending participant data to an LLM**

<div class="small">

Before you paste or upload:

1. **Is it personal data?** Prompts and files count, pseudonymised or not
2. **Who is the provider?** A processor under an Art 28 agreement, or a company that also uses inputs for its own purposes?
3. **Where is it processed?** Transfers outside the EU/EEA need a basis, e.g. the EU–US Data Privacy Framework
4. **Is the tool approved** by your organisation for this class of data?
5. **Were participants told** in the privacy notice, and does the DPIA cover it?
6. **Can the output** contain personal data or new health inferences?

</div>
</div>
</div>

<style>
.cloud { display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); gap: 1.5rem; align-items: start; }
.cloud li { font-size: 0.9rem; line-height: 1.2; }
.cloud .small li { font-size: inherit; }
</style>

<!--
Status checks before teaching: the OpenAI preservation order was lifted for new chats in October 2025; Anthropic's consumer training opt-out dates from August 2025; the CJEU appeal on the Data Privacy Framework (C-703/25 P) was pending in late 2025.
-->


---
layout: default
title: "Cybersecurity threats"
---

###### T · Technology - cybersecurity

# Cybersecurity threats

- **Health data are a prime target:** healthcare breaches remain the costliest of any sector, on average $6.64M each ([IBM Cost of a Data Breach 2026](https://www.chiefhealthcareexecutive.com/view/cost-of-breaches-healthcare-still-leads-all-sectors-and-ai-is-used-in-more-attacks))
- **Scale:** the 2024 ransomware attack on Change Healthcare exposed data on about 193 million people ([HHS](https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html))
- **The harm lands on people:** Vastaamo, a Finnish psychotherapy provider, left its patient database reachable from the internet; in 2020 patients were blackmailed one by one with their therapy notes. €608,000 fine (Art 5(1)(f), 32–34); the company went bankrupt ([EDPB](https://www.edpb.europa.eu/news/national-news/2022/administrative-fine-imposed-psychotherapy-centre-vastaamo-data-protection_en))
- **Usual causes:** stolen credentials and phishing, unpatched software, misconfigured servers and cloud storage, breaches at vendors
- **AI agents make leaks more likely:** agents now find exploitable vulnerabilities on their own ([Google Big Sleep](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html)), and an attacker used an AI coding agent to break into and extort at least 17 organisations, including healthcare ([Anthropic, 2025](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)). More flaws found faster means less time to patch


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
title: "You are a data subject too"
---

###### I · Individuals

# You are a data subject too

- **Digital traces:** cookies, location history, the apps and wearables you use. Use your access right (GDPR Art 15) and, for devices, your Data Act right to see what is collected
- **Hidden metadata** in files, photos and shared links
- **Where data are stored matters:** transfers to the US rely on the EU–US Data Privacy Framework (2023), upheld by the General Court in 2025 (*Latombe*, T-553/23); an appeal is pending at the Court of Justice (C-703/25 P)
- **Your participants** did not sign your employer's contracts with cloud providers: choose tools for them, not for you
- **Basic data hygiene:** multi-factor authentication, a password manager, updates, encrypted storage and transfer, end-to-end encrypted messaging for sensitive conversations



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

<div class="small">

| **Ethics risk** | **Definition** | **In today's AI** |
| --- | --- | --- |
| **Ethics shopping** | Selecting ethical principles that justify existing practices instead of aligning with shared standards | "AI will benefit humanity" justifies its energy use: data centres used ~415 TWh in 2024, ~945 TWh projected by 2030 ([IEA, 2025](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)) |
| **Ethics bluewashing** | Superficial or misleading claims about ethical benefits without meaningful action | "Open" language models that do not release training data or code ([Liesenfeld & Dingemanse, 2024](https://dl.acm.org/doi/pdf/10.1145/3630106.3659005)) |
| **Ethics lobbying** | Using voluntary ethics to delay or weaken binding rules or their enforcement | The Digital Omnibus: simplification or weakening by the back door? Argue both sides |
| **Ethics dumping** | Exporting unethical practices to regions with weaker rules, or importing their results | Data labelling and content moderation outsourced to low-paid workers in the Global South ([The Guardian, 2023](https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai)) |
| **Ethics shirking** | Doing less ethical work where accountability is lower | |

</div>

<div class="ref-bottom">Floridi, L. (2019). Translating principles into practices of digital ethics: five risks of being unethical. Philosophy & Technology 32. · More on AI at Aalto: <a href="https://www.aalto.fi/en/services/artificial-intelligence-ai-the-ai-act-and-ai-literacy-at-aalto-university" target="_blank" rel="noopener">aalto.fi AI services</a></div>

<style>
table th:nth-child(1) { width: 18%; }
table th:nth-child(2) { width: 36%; }
</style>

<!--
"Ethics dumping" was first used in research ethics for research exported to low-resource settings; Floridi generalises it to digital ethics.
Legal note: in the EU, training on scraped content falls under the text-and-data-mining exceptions (CDSM Directive Art 3–4) and, for general-purpose AI providers, the copyright policy duty (AI Act Art 53(1)(c)), not US "fair use".
-->

---
layout: section
color: dark
hexText: "WRAP\nUP"
class: title-middle
---

# Conclusions

---
layout: default
---

###### Conclusions

# A checklist for your next digital health project

1. Is it **personal data**? Is anyone identifiable by means reasonably likely?
2. Is any of it **special category**, including by inference?
3. Which **legal basis** (Art 6) and, if needed, which Art 9(2) condition?
4. Is it genuine **scientific research**? Which research rules apply?
5. Is **ethics review** mandatory? If not, who makes the ethical self-assessment?
6. Is a **DPIA** required?
7. **Other legislations**: Is the product a medical device? What is your role under the AI Act, and which level of risk?
8. Where and howdo you **store** your data and run your **computations**? With which **tools** and **processors**?
9. What will you **release**, and does it pass the anonymity test?
10. During all steps: **Tell people, keep records, and revisit** when something changes.

---
layout: default
title: "Other EU rules that touch digital health"
---

###### Conclusions

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

Tracker: [digibeetle.eu/legislation-tracker](https://digibeetle.eu/legislation-tracker/)

---
layout: default
title: "Summary"
---

###### Conclusions

# Summary

- **Ethics is not law:** 
- **Data become health data by inference** and digital traces identify people without names
- **Health data need two locks:** a legal basis and an Article 9 condition; consent to take part is not the legal basis
- **Research gets privileges only if it is genuine and ethical** 
- **Anonymity is challenging** case-by-case and reassessed over time; pseudonymised data are still personal data
- **Harms can be collective:** ask who is affected beyond your participants, protect also your own data
- **Consider all laws that might apply**


---
layout: end
hexText: "DELTI"
---

# Thank you!

Slides and source: [github.com/eglerean/delti](https://github.com/eglerean/delti)
