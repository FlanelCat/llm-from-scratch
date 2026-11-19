# Build a small language model from scratch

## Original prompt

> I want to create my own LLM as learning experience. The base criteria is that it should be:
>
> - Command-line only
> - Written in C++ and/or Python
> - Using VSCode
> - No specific focus on testing and input/output verification
> - Code should be written and oriented for ease of understanding and reading, instead of optimization
> - This project should aim for functionality and provide examples of all layers and connections in a basic LLM structure
> - References and citations to sources from articles, books, sites, and YouTube videos should given as often as possible and always when specifically borrowing an idea or theory from literature/videos
> - This project should be stored on GitHub with all applicable files (i.e., readme, copyright, etc) and should be public from the start
>
> Please provide me with a starting point setting up the Github project, but first:
>
> - Give a short starting roadmap for accomplishing the above
> - Point me to literature that I can read for free on my IPad to make me more knowledgeable about creating a basic LLM

## Proposed approach

Build a small decoder-only GPT-style model in Python. Use PyTorch for tensors, automatic differentiation, and optimization. Write the attention calculation, model connections, training loop, and generation loop explicitly. Start with a tiny original text corpus and train on CPU from randomly initialized weights.

| Milestone | Deliverable |
| --- | --- |
| 1. Text to tokens | Encode `hello` as character IDs, decode it, and print `hell` and `ello` as a training input and its next-token targets. This example needs only the standard library. |
| 2. Bigram baseline | Learn next-token logits with cross-entropy and generate a short continuation in the terminal. |
| 3. One Transformer block | Trace token and position embeddings, query/key/value projections, scaled dot-product attention, the causal mask, multiple heads, residual connections, layer normalization, and the feed-forward network. |
| 4. Train and generate | Stack blocks, add final normalization and a vocabulary projection, and save and reload a checkpoint. Use separate CLI commands for training and sampling one token at a time. |
| 5. Document the model | Trace one prompt from characters to token IDs, through each layer, and back to generated text. Include tensor shapes and cite the implementation sources. |

Try two blocks, two heads, embedding width 64, and a 64-token context. Consider byte-pair encoding once the character-level pipeline works.

## GitHub and VS Code

With GitHub CLI authenticated as `FlanelCat`, create and clone the public repository from `~/Projects`.

```bash
cd ~/Projects
gh repo create FlanelCat/llm-from-scratch --public \
  --description "A readable, command-line GPT-style language model built for learning" \
  --add-readme --gitignore Python --license MIT --clone
cd llm-from-scratch
python3 -m venv .venv
code-oss .
```

Select `.venv/bin/python` with **Python: Select Interpreter**. Check the copyright holder in `LICENSE`. Put this roadmap, [REFERENCES.md](REFERENCES.md), and [AGENTS.md](AGENTS.md) at the repository root. Link the roadmap and references from the README. The first code file can be `tokenizer.py`. Introduce PyTorch at the bigram milestone.

For further reading and video, see [REFERENCES.md](REFERENCES.md). [GitHub CLI setup reference](https://cli.github.com/manual/gh_repo_create) · [VS Code Python environments](https://code.visualstudio.com/docs/python/environments)
