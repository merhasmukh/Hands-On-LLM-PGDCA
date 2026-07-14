# 10. Evaluation of Large Language Models

Evaluating LLMs is challenging because language quality is subjective.

---

## BLEU Score

**Bilingual Evaluation Understudy**

Measures similarity between generated text and reference text.

Used in:

* Machine Translation

Higher BLEU = Better Translation Quality

---

## ROUGE Score

**Recall-Oriented Understudy for Gisting Evaluation**

Measures overlap between generated summaries and reference summaries.

Used in:

* Text Summarization

Higher ROUGE = Better Summary Quality

---

## Perplexity

Measures how well a model predicts text.

Lower Perplexity = Better Language Model

Formula:

Perplexity = Inverse Probability of Test Data

---

## Human Evaluation

Humans assess outputs based on:

* Accuracy
* Fluency
* Relevance
* Coherence
* Helpfulness

---

## Evaluation Metrics Summary

| Metric           | Purpose             | Application         |
| ---------------- | ------------------- | ------------------- |
| BLEU             | Translation Quality | Machine Translation |
| ROUGE            | Summary Quality     | Summarization       |
| Perplexity       | Language Modeling   | LLM Evaluation      |
| Human Evaluation | Overall Quality     | Chatbots            |

---

[Next Topic: Challenges and Limitations](./11-challenges-and-limitations.md)
