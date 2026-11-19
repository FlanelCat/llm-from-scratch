# References and reading order

The book draft and papers below are free to read and download. Open the PDFs in Safari on your iPad and save them to Books or Files.

| Source | Where to start | Project connection |
| --- | --- | --- |
| Dan Jurafsky and James H. Martin, [Speech and Language Processing, 3rd ed. draft](https://web.stanford.edu/~jurafsky/slp3/) | Chapters 1–3, then 5 and 7. Chapter 6 is a neural-network refresher. The site offers individual PDFs and a complete PDF. | Tokenization, bigrams, embeddings, training, and decoding. |
| Ashish Vaswani et al. (2017), [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Sections 3.2.1–3.2.2 and 3.3 | Scaled dot-product attention, multiple heads, and the feed-forward layer. |
| Alec Radford et al. (2019), [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language-models.pdf) | Sections 2 and 2.3 | Next-token objective and GPT-2 architecture. |
| Sebastian Raschka, [Build a Large Language Model (From Scratch) companion notebooks](https://github.com/rasbt/LLMs-from-scratch) | Chapters 2–5. The notebooks are free. The published book is sold separately. | Training windows, attention, model assembly, and pretraining in Python. |
| Andrej Karpathy, [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY) | Watch after implementing the bigram baseline. Self-attention starts around 1:02:00. | An end-to-end walkthrough from a bigram model to a decoder-only Transformer. |

## Implementation citations

As each idea is implemented, record the source, exact section or timestamp, the idea used, and the file or function that uses it. Put a brief citation beside the relevant code. For adapted code, record the upstream file and version and retain the required license and notices. For external training text, record its source and reuse terms.
