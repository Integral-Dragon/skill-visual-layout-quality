# Hopper Ideas

## 1. Rust helper utilities for higher-speed layout tooling

Explore building Rust helper utilities that start as supplements to the Python tools and only replace them if profiling shows a real speed win.

Possible targets:

- SVG preflight helpers
- rendered-asset QA helpers
- PDF/image processing utilities
- batch-oriented inspection pipelines

Why it matters:

- asset generation and validation time will matter more as quality expectations rise
- if the skill grows into more rendering, rasterization, or batch-inspection work, execution speed could become a practical bottleneck
- starting as supplements is safer than rewriting the current Python scripts on faith

Current Dex read:

- this is more compelling for future rendered-QA helpers than for the current lightweight preflight scripts
- the present Python scripts are small enough that a full rewrite would probably not pay off yet
- the right trigger is profiling evidence, not language preference

Scores:

- Effort: `4`
- Uncertainty: `4`
- Impact: `3`
