# Codex instructions

- Treat this as a learning project. Build a small, command-line-only GPT-style language model that the reader can trace from text to generated tokens. Use Python in VS Code by default. Introduce C++ only when requested for a specific learning goal.
- Implement one requested milestone at a time. Keep a flat layout while it remains clear. Prefer straightforward functions and classes, descriptive names, explicit tensor operations, and short comments on tensor shapes or non-obvious math. Avoid premature abstractions and optimization.
- Use the Python standard library for text processing and PyTorch for tensors, automatic differentiation, and optimization. Write causal attention, the Transformer block, and the training and generation loops explicitly. Use tiny CPU-friendly examples and train from randomly initialized weights.
- Verify each new milestone by running one small, documented CLI example. Keep input handling focused on ordinary use. Add automated tests only if the user requests them or a specific correctness regression needs one. Keep CI, coverage tooling, deployment, containers, GUIs, and service APIs out of scope unless requested.
- Cite borrowed ideas in the code or accompanying documentation and link them to `REFERENCES.md` with a section or timestamp. Track licenses and notices for adapted code and training data.
- Keep the public GitHub repository easy to navigate. Maintain the README, LICENSE with the chosen copyright holder, roadmap, and references. Keep local environments and generated checkpoints out of Git.

## Privacy and public GitHub

- Never push personal information to GitHub under any circumstances. Before pushing, review all outgoing commits for personal information in file contents, commit messages, and author and committer metadata. Use a GitHub-provided no-reply address and check the author and committer names too.
- If you are unsure whether anything is personal information, stop and ask the user before pushing.
- Keep downloaded literature and videos in `local-references/`. Never commit or force-add those files. Put citations and source links in `REFERENCES.md`.

- `FlanelCat` and `Patrick Edlund` are approved for public use. The privacy rule still applies to other personal information.
