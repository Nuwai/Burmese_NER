# **Burmese_NER**

## **Named Entity Recognition (NER) for Burmese**

**Project Overview**

This project implements a NER system for the Burmese language. While many NER solutions exist for high-resource languages (such as English), Burmese remains a low-resource language for which there are very few annotated corpora and off-the-shelf tools.
The purpose of this project is to explore data collection, annotation, and deep learning model architectures (including transformer-based models / transfer learning) for Burmese NER — and thereby lay a foundation for future NLP workflows in Burmese.

**Problem Statement**

Natural Language Processing (NLP) and Named Entity Recognition (NER) are key enablers for a wide range of intelligent applications: information extraction, document classification, search engine enhancement, recommendation systems, social media monitoring, etc.

NER identifies and classifies entities in text into categories like PERSON, ORGANIZATION, LOCATION, DATE, etc.

For high-resource languages there are robust tools (e.g., SpaCy, Stanford NER, Flair). For Burmese:

- Annotated corpora are scarce or non-standardised

- No widely accepted labelling guidelines are in place

- Pretrained language resources are limited

- Burmese text presents additional challenges (lack of explicit word boundaries, complex morphology, context-sensitive tokens)

Example (Burmese):

“ရန်ကုန်မြို့ရှိ ရန်ကုန်တက္ကသိုလ်တွင် တက္ကသိုလ်ကျောင်းသားများ စုပေါင်းဆန္ဒပြခဲ့သည်။”
Here “ရန်ကုန်မြို့” = LOCATION; “ရန်ကုန်တက္ကသိုလ်” = ORGANIZATION. A strong Burmese NER system must distinguish these despite token overlap.

Without such a tool, many organisations (law-firms, media agencies, government offices) must resort to manual, time-consuming, error-prone document review.

In short: Burmese NER is not just a research challenge, but a linguistic and societal necessity as Myanmar becomes more digitally connected.

**Objectives**

This project aims to:

- Build or curate a Burmese NER dataset (annotated sentences) with a consistent label schema.

- Experiment with different model architectures: from baseline sequence models (e.g., BiLSTM-CRF) to transformer models (e.g., mBERT / XLM-R) with transfer learning.

- Evaluate performance using standard metrics (Precision, Recall, F1-score per entity type) and analyse which entity types are most challenging.

- Identify key limitations (tokenisation issues, label imbalance, ambiguous entities) and propose improvements for future iterations.

Provide a proof-of-concept research dataset and modelling workflow that can be extended into production-level Burmese NLP tools in the future.

---

📂 Dataset

The corpus comprises ~70,000+ Burmese sentences collected from public websites (e.g., BBC Burmese news, government announcements, entertainment & sports sites) and combined with ~20,000+ sentences from an open-source corpus (Asian Language Treebank).

Annotation categories:

Label	Description	Example (Burmese)
LOCATION	Geographical places (cities, countries)	ရန်ကုန်မြို့၊ မြန်မာနိုင်ငံ
PERSON	Individual person names	ဒေါ်အောင်ဆန်းစုကြည်
ORGANIZATION	Companies, institutions, agencies	ရန်ကုန်တက္ကသိုလ်၊ WHO
DATE	Specific dates, months or years	ဇူလိုင် ၁၂၊ ၂၀၂၅
NUMBERS	Quantities, measurements, monetary values	၁၀၀၀ ကျပ်၊ ၁၅ ဦး

Tokens outside these categories are annotated as O (Outside) using the BIO tagging format. (Support for BIOES format may be considered in advanced experiments.)

🛠 Model & Annotation Workflow

Annotation is done using Label Studio (or equivalent annotation tool) to mark entities according to the schema above.

Data preprocessing steps include tokenisation (special handling for Burmese), clean-up of raw text, and conversion into the required input format for modelling.

Modelling workflow:

Baseline: BiLSTM + CRF

Transformer-based: e.g., mBERT / XLM-R fine-tuned for Burmese NER

Transfer learning: leveraging multilingual models, adapting to Burmese domain

Evaluation: Models are trained and validated on splits of the dataset (train/dev/test). Metrics include Accuracy, Precision, Recall, F1-score (overall and per-entity).

Expectation: At least 75% overall accuracy, with strong F1-scores for major entity types (though some imbalance bias may exist in LOCATION and ORGANIZATION due to dataset nature).

Getting Started

Clone the repository:

git clone https://github.com/Nuwai/Burmese_NER.git
cd Burmese_NER


Install dependencies:

pip install -r requirements.txt


Tagging Format

BIO (Begin-Inside-Outside) format is the primary annotation scheme:

B-XXX = Beginning of entity type XXX

I-XXX = Inside entity type XXX

O = Outside any entity

Optionally, BIOES (Begin-Inside-Outside-End-Single) may be supported for more granular tagging:

S-XXX = Single-token entity of type XXX

E-XXX = End of a multi-token entity of type XXX

**Potential Use Cases**

Legal document review in Myanmar: automatically extract client names, dates, organizations, locations.

Media monitoring & social listening: identify named entities in Burmese news, blogs, and social media.

Knowledge graph construction: feed extracted entities into larger graph pipelines (relations, events).

Multilingual NLP system expansion: serve as a blueprint for other low-resource languages.

🎓 Next Steps & Roadmap

Improve dataset balance (under-represented entity types) and expand annotation size beyond ~70k sentences.

Explore more advanced tokenisation strategies (for Burmese).

Fine-tune and compare a wider range of transformer architectures (with domain adaptation).

Release a lightweight Burmese-NER library or API for community use.

Extend from NER → relation extraction → event detection → knowledge graph.
