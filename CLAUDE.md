# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Reference architecture for cybersecurity technology — documenting security controls, framework mappings, and technology patterns across an enterprise security program.

## Repository Structure

- `architecture/` — Architecture diagrams and narrative descriptions (draw.io, Mermaid, or Markdown)
- `controls/` — Security controls organized by domain (identity, network, endpoint, data, cloud)
- `frameworks/` — Mappings between frameworks (NIST CSF 2.0, NIST 800-53, ISO 27001, MITRE ATT&CK, CIS Controls)
- `technologies/` — Technology evaluations, capability matrices, and integration patterns
- `templates/` — Reusable configuration, policy, and deployment templates

## Conventions

- Use Markdown for all documentation
- Diagrams: prefer Mermaid (renders in GitHub) for architecture diagrams; store draw.io source files alongside exported PNGs
- Framework mappings: use tables with columns for control ID, control name, and implementation notes
- Keep technology evaluations vendor-neutral; note vendor-specific implementations separately
