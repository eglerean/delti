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
keywords: data ethics, GDPR, AI Act, personal data, privacy, research ethics, Enrico Glerean, https://eglerean.github.io/
layout: cover
class: no-footer
hexText: "DATA\nETHICS"
hexSeed: 7
---

# Data, ethics, law, technologies, individuals

::presenter::
**Dr. Enrico Glerean**, Staff Scientist and Data Agent at Aalto University, 2026

<div class="license-line"><CcBy /> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a> · <a href="https://github.com/eglerean/delti" target="_blank" rel="noopener" class="gh-link" title="Slides on GitHub" aria-label="Slides on GitHub"><carbon-logo-github class="gh-icon" /></a></div>

<style>
h1 { font-size: 2.5rem !important; line-height: 1.1 !important; }
p { font-size: 0.95rem; }
.cover-presenter p { font-size: 0.85rem; }
.license-line { margin-top: 0.45rem; font-size: 0.75rem; white-space: nowrap; }
.gh-icon { vertical-align: -0.2em; width: 1.15em; height: 1.15em; }
.license-line a.gh-link { border-bottom: none; text-decoration: none; color: inherit; }
</style>

---
layout: two-cols
---

::header::
# Outline: data, ethics, law, technology, individuals

::left::

1. Ethics and law
2. Privacy
3. Device regulations
4. Tools and techniques for working with (patient generated) health data
5. Reflections on privacy, data protection, AI, ethics

::right::

### Learning outcomes

- How to identify ethical principles for working with data from individuals
- Getting familiar with the principles of GDPR and AI Act
- Awareness of new technologies and risks they bring

---
layout: default
---

# Briefly about the speaker

**Enrico Glerean, DSc.**

- **Staff scientist and data agent** (background in neuroimaging), helping and training researchers with handling personal data (anonymization, secure computing), medical images, clinical trials/FINDATA, research ethics and research integrity (AI and new technologies), statistics
- Other affiliations/COI: **CodeRefinery** (Nordic network to teach computational reproducibility), **Finnish Reproducibility Network** (National network to raise awareness in reproducibility), Support Pool of Experts at the **European Data Protection Board** (open training materials on personal data, AI, and cybersecurity)

---
layout: default
---

# Context for this audience: Digital Health and Human Behaviour course

- You might become a **researcher** in academia or a company working with data from human participants
- You might become a **data scientist** in a company or a manager of a team of developers building applications that process **personal data**
- You most likely won’t need to worry about “***data governance***” and ”***lawfulness of personal data processing***” as the company you will work for will have a legal expert and a **data protection officer**
- However, **it is beneficial to understand what you can ethically and legally do with data from individuals**
- **Only very high-risk applications are truly prohibited**, often **cybersecurity** and **transparency towards the data subjects** is all you need to build your application

---
layout: section
color: dark
hexText: "ETHICS"
class: title-middle
---

# 1. Ethics

Fundamental principles and the requirements for research

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
---

# The four principles of ethics

| **Principle** | **Definition** | **Example** |
| --- | --- | --- |
| **Beneficence** | Do only good: Acting to promote the well-being of individuals or society and to do good. | A teacher offering extra support to a struggling student to help them succeed academically. |
| **Nonmaleficence** | Do no harm: Avoiding harm or minimizing potential risks to individuals or society | A doctor refraining from prescribing medication with severe side effects when a safer alternative exists. |
| **Autonomy** | Respecting individuals’ right to make informed decisions about their lives. | Allowing someone to refuse a blood transfusion based on their religious beliefs. |
| **Justice** | Ensuring fairness in the distribution of benefits, risks, and resources | Providing equal access to clean water for all members of a community, regardless of their income.. |

---
layout: default
---

# Ethics in business and research

<br>

- **Ethics is not a necessary driving principle for *most* companies**
  - Google used to have the *“Don’t be evil”* motto, which was then replaced with *“Do the right thing”* ([ref](https://en.wikipedia.org/wiki/Don%27t_be_evil))
- **Ethics** is a mandatory requirements in **research that can cause harm to study participants, communities, minorities, society at large, and the environment**

---
layout: default
---

# Research ethics requires pre-evaluation of risks before conducting research that can cause harm

**Horizon Europe** considers 9 cases that might require ethical pre-review ([ref](https://www.aalto.fi/en/for-personnel-highlights-and-support-for-your-work/different-perspectives-to-research-ethics-how-to-make-an-ethics-self-assessment-in-research-projects))

1. **Medical research** with human participants, human organs, tissues and cells
2. **Non-medical research** with human participants
3. **Processing of personal data**
4. Research with **animals**
5. Research in **non-EU countries**, global south/developing countries
6. **Environment** & **safety**
7. **Artificial Intelligence**
8. **Dual use** items
9. Potential **misuse of results**

---
layout: default
---

# Ethical pre-review in Finland

<div class="prereview">
<div>

**For researchers (and for companies):**

Depending on the nature of your study, you might be required to request ethical pre-evaluation **before starting the research work.**

1. If the study is **medical** (medical research, research on clinical devices, research based on tissue and biobank acts) you need to apply for [ethical pre-review from HUS](https://www.hus.fi/tutkimus-ja-opetus/tutkijan-palvelut/sahkoiset-palvelut-tutkijalle) or for companies running clinical trials [Valvira Tukija](https://tukija.fi/en/frontpage)
2. If the study is **non-medical** and if one of these below is true ([TENK 2019](https://www.tenk.fi/sites/tenk.fi/files/Ihmistieteiden_eettisen_ennakkoarvioinnin_ohje_2019.pdf)), then you need to apply to ethical pre-review from a University Institutional Review Board ([e.g. at Aalto](https://www.aalto.fi/en/services/research-ethics-review-research-ethics-committee))
    1. Study deviates from **informed consent**
    2. Study intervenes on **physical integrity**
    3. Study involved **minors** under 15
    4. Study uses exceptionally **strong stimuli**
    5. Study can cause **mental harm**
    6. Study can be a **threat to safety** of participants or researchers

</div>
<div class="card yellow warning-card">
  <img src="/images/warning.svg" alt="Warning icon">
  <p><strong>When ethical review is not mandatory, companies might find a legal loophole to justify the lawfulness of their unethical work</strong></p>
</div>
</div>

<style>
.prereview { display: grid; grid-template-columns: minmax(0, 3fr) minmax(0, 1fr); gap: 1.5rem; align-items: end; }
.warning-card img { width: 64px; height: 64px; border-radius: 0; margin-bottom: 0.5rem; }
</style>

---
layout: section
color: dark
hexText: "AI"
class: title-middle
---

# 2. Ethics and data intensive technologies

The case of Artificial Intelligence

---
layout: default
---

# (Human) Data intensive technologies: Artificial Intelligence

<br>

- Large scale processing of data from individuals can raise ethical concerns
- Artificial intelligence is a technology that comes with ethical issues.
- AI Act Article 3 (I):<br>‘AI system’ means a machine-based system that is designed to operate with **varying levels of autonomy**, and that may exhibit **adaptiveness** after deployment, and that, **for explicit or implicit objectives**, **infers**, from the input it receives, how to **generate outputs** such as predictions, content, recommendations, or decisions that can **influence physical or virtual environments;**
- Each element marked in **bold** in the definition highlights the **risk of individuals not being in control of the technology**
- More broadly, any **automated individual decision making, including profiling** (GDPR Art 22) puts individuals at risk of harm, even without the use of AI

---
layout: default
---

# Unified framework of five principles for ethical AI

<div class="ref-line">Floridi, L. (2023). The ethics of artificial intelligence: Principles, challenges, and opportunities.</div>

<div class="compact">

| **Principle** | **Definition** | **Example of (risky) AI system** |
| --- | --- | --- |
| **Beneficence** | Do only good: Promote well-being, preserve dignity, and sustain the environment. | AI that enhances healthcare diagnostics to improve human welfare, ensuring accuracy and ethical use. |
| **Nonmaleficence** | Do no harm: Avoid harm by ensuring privacy, security, and preventing negative societal impacts. | AI systems used in surveillance or remote facial recognition |
| **Autonomy** | Preserve human decision-making: Balance AI’s independence with human control. | Autonomous weapons that bypass human intervention, potentially causing unaccountable harm. |
| **Justice** | Promote fairness and solidarity: Ensure equitable AI outcomes and avoid discrimination. | AI in hiring that reinforces bias, leading to unfair employment practices based on race or gender. |
| **Explicability** | Ensure transparency and accountability: Make AI decisions understandable and responsible. | AI used in legal sentencing without explainability, leading to opaque decision-making that impacts individuals’ lives. |

</div>


---
layout: default
---

# Unified framework of five principles for ethical AI

<div class="five-principles">
  <img src="/images/unified-five-principles.png" alt="Diagram: traditional bioethics principles lead to Beneficence, Non-maleficence, Autonomy and Justice; a new enabling principle for AI leads to Explicability">
</div>

<div class="ref-bottom">Floridi, L. (2023). The ethics of artificial intelligence: Principles, challenges, and opportunities.</div>

<style>
.five-principles { display: flex; justify-content: center; margin-top: 3rem; }
.five-principles img { width: 100%; max-width: 820px; height: auto; }
</style>

---
layout: section
color: dark
hexText: "RIGHTS"
class: title-middle
---

# 3. From ethics to law (focus on humans)

Fundamental rights of individuals

---
layout: default
---

# Universal declaration of human rights

<br>

- Adopted by the United Nations on 10/Dec/1948
- **30 articles** on individuals’ basic rights and fundamental freedoms
- UDHR recognizes all humans as being "**born free and equal in dignity and rights**" regardless of "nationality, place of residence, sex, national or ethnic origin, colour, religion, language, or any other status”
- It is worth reading the 30 articles at least once in your lifetime [https://www.un.org/en/about-us/universal-declaration-of-human-rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights)
- Also noteworthy: “**Charter of Fundamental Rights of the European Union**” (which is legally binding in Europe)

---
layout: default
---

# Universal declaration of human rights and data risks 1

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 1 | Right to equality and dignity. | Biased AI algorithms perpetuating inequality and discrimination. |
| 2 | Freedom from discrimination. | Unfair profiling based on personal data leading to discrimination in services or hiring. |
| 3 | Right to life, liberty, and personal security. | Surveillance systems used to monitor and restrict personal freedoms. |
| 4 | Freedom from slavery. | Exploitation of individuals through data-driven manipulation or trafficking networks. |
| 5 | Freedom from torture and degrading treatment. | AI misuse in predictive policing leading to wrongful detention or degrading treatment. |
| 6 | Right to recognition as a person before the law. | Exclusion from digital systems due to lack of data or incorrect identification. |

</div>

---
layout: default
---

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
---

# Universal declaration of human rights and data risks 3

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 13 | Right to freedom of movement and residence. | Geolocation tracking used to restrict or monitor movement. |
| 14 | Right to seek asylum from persecution. | Data misuse exposing asylum seekers to risks in their home countries. |
| 15 | Right to nationality and its change. | Lack of digital identity or errors in records denying nationality rights. |
| 16 | Right to marry and found a family. | Unethical use of genetic data impacting reproductive rights. |
| 17 | Right to own property. | Unauthorized access to or manipulation of digital assets. |
| 18 | Right to freedom of thought, conscience, and religion. | Manipulation of beliefs through targeted misinformation. Mind-reading technology. |

</div>

---
layout: default
---

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
---

# Universal declaration of human rights and data risks 5

<div class="compact">

| **Art.** | **Key Right** | **Risks from Data Misuse** |
| --- | --- | --- |
| 25 | Right to an adequate standard of living. Motherhood and childhood assistance. | Data misuse in welfare systems excluding vulnerable populations. |
| 26 | Right to education. | Biased educational AI tools limiting opportunities for marginalized groups. |
| 27 | Right to participate in cultural life and protection of authorship. | Unauthorized use or replication of creative works via AI systems. |
| 28 | Right to a social and international order upholding these rights. | Cross-border data misuse undermining global human rights efforts. |
| 29 | Duties to the community and limits on rights for public welfare. | Data collection practices used disproportionately against marginalized groups. |
| 30 | No one may use the UDHR to undermine others' rights. | Ethics bluewashing. |

</div>

---
layout: default
---

# Considering these data-related risks, what should we do?

<br>

- **Implement a data protection legislation** to ensure the safety of the personal data of individuals
  - In Europe this is implemented in the **General Data Protection Regulation**
- **Implement a legislation that minimises the risks when using AI systems**
  - In Europe this is implemented in the Artificial Intelligence Act
- Implement other data- or product-related legislations that protect basic rights of individuals (cybersecurity, health data, medical device regulation, etc…)

---
layout: section
color: dark
hexText: "GDPR"
class: title-middle
---

# 4. The general data protection regulation (GDPR)

Protecting the personal data of individuals in Europe

---
layout: default
---

# What is the GDPR?

<br>

Established in 2018, **the General Data Protection Regulation (GDPR)** is a **groundbreaking data protection regulation** that revolutionized the way **personal data** is handled in the EU, granting individuals greater **control** over their information and holding organizations **accountable** for responsible data processing.

[https://tietosuoja.fi/en/home](https://tietosuoja.fi/en/home)

---
layout: default
---

# What is personal data?

<br>

- **Personal data is a broad concept under the EU’s General Data Protection Regulation**
- **“Personal data” is any data about living people from which they can be identified**
  - If you collect information **from** or **of** persons, consider it as **personal data**
  - Exception: **anonymous data**

---
layout: default
---

# Personal data: direct and indirect identifiers (quasi-identifier)

1. **Direct identifiers:** information which is **sufficient on its own to identify an individual**<br>- e.g. a person’s name, email address (containing the person’s name), personal identification number, fingerprints, a facial image, a person's voice, video, brain scan images, dental records, DNA
2. **Strong indirect identifiers :** information which **can be used to identify an individual fairly easily**<br>- e.g. a postal address, a phone number, a vehicle registration number, bibliographic citation of a publication, an email address not in the form of the personal name, an unusual job title, a very rare disease, a job position held by only one person at a time, a student ID number, a bank account number, IP address of a computer, cookie identifier, RFID tags, location data
3. **Indirect identifiers:** information that on its own is not enough to identify someone but, when **linked with other available information, could be used to deduce the identity of a person:**<br>- e.g. age, gender, education, status in employment, economic activity and occupational status, socio-economic status, household composition, income, marital status, mother tongue, ethnic background, place of work or study, postal code, municipality, major region.

---
layout: default
---

# Special categories of personal data (art. 9)

- personal data revealing **racial or ethnic origin**
- personal data revealing **political opinions**
- personal data revealing **religious or philosophical beliefs**
- personal data revealing **trade union membership**
- **genetic data, biometric data (where used for identification purposes)**
- data concerning **health**
- data concerning a person’s **sex life** and data concerning a person’s **sexual orientation**

<br>

It is not prohibited to process these categories of personal data, but it comes with extra requirements for the **data processor** and **data controller**.

---
layout: default
---

# The principles of the GDPR

<div class="small compact">

| **GDPR Principle** | **Practical Actions in Research Projects** |
| --- | --- |
| **1. Lawfulness, fairness, and transparency** | Obtain and manage informed consent from research participants<br>Clearly explain data processing activities, purposes, and potential risks to participants<br>Maintain transparency in data sharing, storage, and access policies |
| **2. Purpose limitation** | Specify the research objectives and data processing purposes before collecting personal data<br>Use collected data only for the stated purposes<br>Obtain additional consent or establish a new legal basis if the purpose changes |
| **3. Data minimization** | Collect only the minimum amount of personal data necessary to achieve research objectives<br>Employ data anonymization or pseudonymization techniques to reduce the scope of identifiable information |
| **4. Accuracy** | Implement processes to ensure the accuracy and up-to-date nature of personal data<br>Allow research participants to rectify inaccurate or incomplete information<br>Regularly review and update collected data as needed |
| **5. Storage limitation** | Establish retention periods for personal data based on research objectives and legal requirements<br>Regularly delete or anonymize personal data when it is no longer necessary for the stated purpose or when the retention period ends |
| **6. Integrity and confidentiality** | Use appropriate security measures to protect personal data from unauthorized access, disclosure, or misuse<br>Train research team members on data protection and privacy practices<br>Implement access controls and encryption for data storage and transfer |
| **7. Accountability** | Document data processing activities, legal bases, and compliance measures<br>Appoint a data protection officer (DPO) when required<br>Conduct data protection impact assessments (DPIAs) for high-risk processing activities<br>Demonstrate adherence to GDPR principles and requirements in research practices |

</div>

---
layout: default
---

# The legal basis of the GDPR (art 6)

<div class="small">

| **Legal Basis** | **Applicability in Research and Other Contexts** |
| --- | --- |
| **1. Consent** | Obtaining explicit and informed consent from research participants for data collection and processing<br>Marketing activities<br>Consent can be withdrawn at any time; Reusing data for new purposes may require obtaining new consent |
| **2. Contract** | Processing personal data in the context of a contract (e.g., employment, service provision)<br>Limited to the specific terms and purposes outlined in the contract |
| **3. Legal Obligation** | Processing personal data to comply with legal requirements (e.g., tax reporting, anti-money laundering regulations)<br>Must be based on a specific legal obligation under EU or national law |
| **4. Vital Interests** | Processing personal data to protect the life or health of an individual (e.g., emergency medical situations)<br>Rarely applicable in research settings |
| **5. Public Task** | Public authorities processing personal data for official tasks or public interest<br>Research conducted for public interest<br>Must be based on EU or national law. Greater flexibility for data reuse in scientific or archival purposes |
| **6. Legitimate Interests** | Processing personal data when necessary for the legitimate interests of the organization or a third party (e.g., fraud prevention)<br>Must be balanced against the rights and interests of data subjects. Rarely applicable in research settings |

</div>

---
layout: default
---

# Rights of the data subject

According to the General Data Protection Regulation (GDPR), **data subjects have the right:**

- to **obtain information** on the processing of their personal data
- of **access** to their data
- to **rectification** of their data
- to the **erasure** of their data and to be forgotten
- to **restrict the processing** of their data
- to data **portability**
- to **object to the processing** of their data
- not to be subject to a decision based **solely on automated processing**

---
layout: section
color: dark
hexText: "PETs"
class: title-middle
---

# 5. Privacy enhancing technologies

How to put GDPR principles and data-subjects rights into practice

---
layout: default
---

# Measures to ensure data protection

<br>

- **Informing** the data subjects (**privacy notice or privacy policy**)
- Data **minimisation** (*pseudonymisation*, *anonymisation*)
- **Privacy by default**
- **Secure data processing strategies** when minimisation is not possible or **risks are high** (hundreds of subjects, minors (DPIA)) or when **required by legislation** (secondary use of health data)

---
layout: default
---

# Measures to ensure data protection

<div class="spectrum">
  <div class="sp-top"><p><strong>Personal data with direct identifiers and no minimisation</strong></p></div>
  <div class="sp-top"><p><strong>Pseudonymisation</strong></p><p>Replacing strong identifiers: tokenization, hashing, encryption</p></div>
  <div class="sp-top"><p><strong>Masking</strong></p><p>Suppression of strong identifiers</p></div>
  <div class="sp-top"><p><strong>Anonymisation</strong></p><p>K-anonymity, l-diversity, t-closeness, perturbation (data swapping, differential privacy)</p></div>
  <div class="sp-top"><p><strong>Anonymisation</strong></p><p>Aggregation, data synthesis</p></div>
  <div class="sp-arrow" aria-hidden="true"></div>
  <div class="sp-bottom"><p><strong>Easy to re-identify</strong></p></div>
  <div class="sp-bottom"><p><strong>Can be re-identified with the key</strong></p></div>
  <div class="sp-bottom"><p><strong>The key is lost, but other data (will) exist</strong></p></div>
  <div class="sp-bottom"><p><strong>Impossible to re-identify, but still related to an individual</strong></p></div>
  <div class="sp-bottom"><p><strong>Impossible to re-identify and not related to an individual anymore</strong></p></div>
</div>

<div class="ref-bottom">Deeper look at minimisation and anonymisation: <a href="https://zenodo.org/records/10649060" target="_blank" rel="noopener">https://zenodo.org/records/10649060</a></div>

<style>
/* Five steps from identifiable to anonymous data, over a dark-to-green arrow (as in the original slide) */
.spectrum { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0 1rem; margin-top: 1rem; }
.spectrum p { margin: 0 0 0.3rem; }
.sp-top { align-self: start; }
.sp-arrow { grid-column: 1 / -1; height: 2.6rem; margin: 1.2rem 0; background: linear-gradient(90deg, #434343, #00FF00); clip-path: polygon(0 25%, calc(100% - 2.6rem) 25%, calc(100% - 2.6rem) 0, 100% 50%, calc(100% - 2.6rem) 100%, calc(100% - 2.6rem) 75%, 0 75%); }
</style>

---
layout: default
---

# The Data Protection Impact Assessment

<div class="dpia">
<div>

A tool for evaluating the risks related to PD processing.

Aalto guidelines as an example:<br>**DPIA if 2 or more are true**

<div class="small">

1. processing of personal data for evaluation or **scoring** purposes
2. processing of personal data for **automated decision-making** with legal or similar significant effect
3. processing of personal data for **systematic monitoring**
4. processing of **special categories of personal data** or personal data that is confidential by law (sensitive data)
5. personal data is processed on a **large scale** at the regional, national or  international level
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

---
layout: section
color: dark
hexText: "AI ACT"
class: title-middle
---

# 6. The case of AI

The European AI Act: product liability mixed with protection of fundamental rights

---
layout: default
---

# The European AI Act

<br>

- Into force since 1st of August 2024. Over the next two years it is being implemented.
- Risk based classification of AI systems: **Prohibited, high-risk, medium or low risk**
- It does not apply to basic research, **unless the research becomes a product**
- It is being criticised as it is not compatible with fundamental human rights (e.g. law enforcement can use prohibited systems like **remote biometric identification,** see “[AI Act fails to adequately protect human rights](https://www.aegee.org/ai-act-fails-to-adequately-protect-human-rights/)” by AEGEE European Student’s forum)

---
layout: default
---

# The European AI Act: Prohibited AI system

<br>

- Subliminal / manipulative or deceptive techniques
- Exploiting vulnerabilities (e.g. age, disability, social/economic situation)
- Social scoring
- Predictive criminal risk assessments based on profiling
- Facial recognition databases through untargeted scraping
- Emotional inference in workplace or education
- Biometric categorisation that infers sensitive data
- Real-time remote biometric identification for law enforcement

---
layout: three-cols
---

::header::
# The European AI Act: High-risk AI systems

::left::

### Product safety (products)

- Machinery
- Explosives
- PPE
- Toys
- Radio equipment
- Gas-fuelled appliances
- Watercraft
- Pressure equipment
- Medical devices
- Lifts
- Cableways

::center::

### Product safety (vehicles)

- Civil aviation
- Rail systems
- Motor vehicles and trailers
- 2/3-wheel vehicles
- Agricultural/forestry vehicles
- Unmanned aircrafts/drones
- Marine equipment

::right::

### Fundamental rights

- Biometrics
- Essential services and benefits
- Critical infrastructures
- Law enforcement
- Educational and vocational training
- Migration, asylum, border control
- Employment
- Justice, democracy

---
layout: section
color: dark
hexText: "RISKS"
class: title-middle
---

# 7. The ethical risks of AI

The grey area of legal loopholes

---
layout: default
---

# From legislations back to ethics risks

- Floridi defines also ***ethics risks***: where companies exploit ethical standards and legal loopholes potentially causing harm to individuals

| **Ethics Risk** | **Definition** |
| --- | --- |
| **Ethics Shopping** | Selecting ethical principles that justify pre-existing practices instead of aligning with universal standards. |
| **Ethics Bluewashing** | Making superficial or misleading claims about AI’s ethical benefits without meaningful actions. |
| **Ethics Lobbying** | Exploiting ethics to delay or avoid necessary legislation or to weaken legal enforcement. |
| **Ethics Dumping** | Exporting or importing unethical AI practices to regions with weaker regulations or standards. |
| **Ethics Shirking** | Reducing ethical responsibilities in regions or situations where accountability is less enforced. |

---
layout: default
---

# AI Ethics risks

- **Ethics shopping:** large AI companies have scraped the internet under the principle of ”fair use” (**Fair use** is a doctrine in United States law that permits limited use of copyrighted material without having to first acquire permission from the copyright holder.)
- **Ethics shopping**: justifying any unsustainable practices (e.g. towards the environment) in the search for AGI (Artificial General Intelligence, AI that matches or surpasses human cognitive capabilities across a wide range of cognitive tasks) for the benefit of mankind<br>( it is estimated that the electricity consumption of AI will increase in the order of the [yearly amount consumed by a country like Sweden](https://www.thedailybeast.com/ai-may-soon-gobble-up-as-much-power-as-sweden-each-year)) [[see also this](https://www.theatlantic.com/technology/archive/2024/03/nvidia-chips-gpu-generative-ai/677664/)]
- **Ethics bluewashing:** open source large language models are actually not open at all<br>[https://dl.acm.org/doi/pdf/10.1145/3630106.3659005](https://dl.acm.org/doi/pdf/10.1145/3630106.3659005) (Figure 2)
- **Ethics dumping:** on stage of training large language model is ”reinforcement learning from human feedback” which became exploitations of workers from the global south:<br>[https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai](https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai)

<div class="ref-bottom">More details <a href="https://www.aalto.fi/en/services/artificial-intelligence-ai-the-ai-act-and-ai-literacy-at-aalto-university" target="_blank" rel="noopener">https://www.aalto.fi/en/services/artificial-intelligence-ai-the-ai-act-and-ai-literacy-at-aalto-university</a></div>

<style>
/* Long URLs wrap instead of running off the slide */
a { overflow-wrap: anywhere; }
</style>

---
layout: section
color: dark
hexText: "YOU"
class: title-middle
---

# 8. Reflection on you as a data subject

Awareness on your own privacy

---
layout: default
---

# Understand data protection with your own data

Understand your own privacy, your personal data, evaluate the risks that you expose yourself to. Europe is the best place to be!

- **Digital traces** of personal data you leave around (cookies, GPS trackers, the apps you use)
- **(hidden) metadata in files or links you share:** sometimes it is not just what you see
- **Where data are stored matters**: Schrems vs FISA (Foreign Intelligence Surveillance Act)
  - Consider the perspective that as an employee of an organization you have accepted that some of your data is transferred overseas, however your study participants did not sign any agreement with third parties
- **Know your rights about your data**
- Familiarize yourself with (and adopt!) **encryption**, **secure connectivity (MFA, SSH keys, https, never use free wifi)**, **secure file sharing and communication** (funet, Signal)

---
layout: section
color: dark
hexText: "SUM"
class: title-middle
---

# 9. Summary

---
layout: default
---

# Summary

<br>

- Working with personal data (as a company or as a researcher) comes with **ethical and legal responsibilities**
- **Ignorance is not an excuse**: every  other day companies are being fined for not respecting privacy of individuals. With AI systems becoming more popular, more risks of illegal (or unethical) practices will emerge.
- **The GDPR and the AI Act** are two important legislations that data scientists working with personal data in Europe should be aware of, however there is more to that depending on specific context.

---
layout: default
---

# Other data/privacy legislations in EU

<br>

European Health Data Space Regulation, AI Liability Directive, Product Liability Directive, Platform Work Directive, Directive on Combating Violence Against Women and Domestic Violence, Cyber Resilience Act, Transparency and Targeting of Political Advertising Regulation, Cyber Solidarity Act, Data Protection Regulation for EU institutions, Law Enforcement Directive, Data Governance Act, Data Act, Digital Services Act, Digital Markets Act, Interoperable Europe Act, NIS2 Directive, Cybersecurity Act, Digital Operational Resilience Act, ePrivacy Regulation, Market Surveillance and Compliance of Products Regulation.

**Links and more information at [https://digibeetle.eu/legislation-tracker/](https://digibeetle.eu/legislation-tracker/)**
