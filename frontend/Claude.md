# CLAUDE.md

# Mond Frontend Engineering Guide

## Project

Project Name: Mond

Mond is an open-source metadata validation platform for books.

Contributors submit mappings between Anna's Archive books and Open Library editions.

Moderators review submissions before approval.

The frontend communicates with an existing FastAPI backend.

Do not redesign the application's workflow.

---

# Tech Stack

Framework:
- SvelteKit

Language:
- TypeScript

Styling:
- Tailwind CSS

UI Components:
- Bits UI

Icons:
- Lucide Svelte

HTTP:
- Axios

Backend:
- FastAPI

Authentication:
- Supabase Auth

---

# Philosophy

Mond should feel like:

- Moonlight
- Quiet
- Elegant
- Trustworthy
- Research software
- Modern open-source tooling

Avoid:

- Cyberpunk
- Neon
- Gaming UI
- Bright gradients
- Overly playful interfaces

The UI should resemble a premium productivity application.

---

# Design Language

Theme:
Dark

Visual Style:

- Deep charcoal backgrounds
- Indigo & violet accents
- Soft borders
- Large whitespace
- Glass-inspired cards
- Smooth transitions
- Clean typography

---

# Color Palette

Background:
#09090B

Surface:
#18181B

Card:
#202024

Border:
#27272A

Primary:
#8B5CF6

Secondary:
#6366F1

Accent:
#A5B4FC

Text:
#F4F4F5

Muted:
#A1A1AA

Success:
#22C55E

Warning:
#F59E0B

Danger:
#EF4444

Never invent additional primary colors.

---

# Typography

Use modern sans-serif typography.

Headings should feel spacious.

Avoid decorative fonts.

Maintain a clear visual hierarchy.

---

# Layout

The authenticated application always uses:

Sidebar

Top Navigation

Content Area

Pages must never implement their own sidebar.

---

# Sidebar Navigation

Dashboard

Submit Mapping

History

Moderator (only for moderators)

Settings

Logout

Sidebar must support collapse.

---

# Components

Components should be:

Reusable

Accessible

Strongly typed

Small

Composable

Split components if they become too large.

---

# Cards

Use:

rounded-xl

subtle border

clean spacing

soft shadow

optional glass effect

---

# Buttons

Support:

Primary

Secondary

Ghost

Danger

Maintain consistent sizing.

---

# Forms

Always include:

Labels

Placeholders

Validation messages

Keyboard accessibility

Proper focus states

---

# Tables

Tables should support:

Loading state

Empty state

Hover state

Responsive layout

---

# Icons

Only use Lucide Svelte.

Do not mix icon libraries.

---

# Animations

Keep animations subtle.

Allowed:

Fade

Scale

Hover

Opacity

Avoid:

Bounce

Spin

Flash

Heavy motion

---

# Accessibility

Use semantic HTML.

Support keyboard navigation.

Use ARIA where appropriate.

Maintain good contrast.

---

# Folder Structure

src/lib/components

src/lib/api

src/lib/stores

src/lib/types

src/lib/utils

src/lib/assets

Pages belong in:

src/routes

---

# Backend Integration

The FastAPI backend already exists.

Do NOT invent backend endpoints.

Do NOT invent request schemas.

Do NOT hardcode business logic.

Keep API logic inside:

src/lib/api

Components should receive data through props whenever practical.

Forms should mirror backend request models.

Tables should mirror backend response models.

---

# TypeScript

Always use strict typing.

Avoid any.

Create reusable interfaces.

---

# Responsiveness

Desktop

Tablet

Mobile

Desktop-first is acceptable.

---

# Code Style

Use Tailwind only.

No inline CSS.

Prefer composition.

Avoid duplication.

Keep components readable.

---

# When Generating Code

Always:

Return complete files.

Specify the destination path.

Explain any required dependencies.

Think about reusable components before writing code.

Separate presentation from data fetching.

Design pages so they can later connect to the FastAPI backend with minimal changes.

# Compatibility Requirements

Always target:

- Latest SvelteKit
- Latest Svelte 5
- Latest Tailwind CSS
- Latest TypeScript

Never use deprecated APIs.

Never guess package exports.

Only use imports that are confirmed to exist.

If uncertain, omit the feature instead of generating code that may not compile.