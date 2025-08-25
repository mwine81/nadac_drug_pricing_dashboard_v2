# Copilot Instructions for nadac_drug_pricing_dashboard_v2

## Project Overview
This project is a modular Python dashboard for NADAC drug pricing analysis. It is organized by feature and UI responsibility, with clear separation between data, UI, and helper logic.

## Architecture & Key Components
- `app.py`: Main entry point. Orchestrates app startup and layout.
- `components/`: Reusable UI widgets (badges, dropdowns, containers, social media links).
- `ui/`: Page-level UI structure (header, footer, layout, chart, controls, legend, help).
- `figures/`: Chart and figure generation logic.
- `helpers.py`: Utility functions for data processing and app logic.
- `config.py`: Centralized configuration (constants, environment, etc.).
- `assets/`: Static files (e.g., logo.png).

## Developer Workflows
- **Run the app:**
  ```bash
  uv run app.py
  ```
- **Dependencies:**
  - Managed via `requirements.txt` and/or `project.toml`.
- **No explicit test suite** detected. Add tests in a `tests/` folder if needed.

## Project Conventions
- **Component Structure:**
  - UI and logic are separated: `components/` for widgets, `ui/` for layout and orchestration.
  - Each UI or component file typically defines a single class or function for clarity.
- **Imports:**
  - Use relative imports within packages (e.g., `from .badges import ...`).
- **Configuration:**
  - All environment/config values should be set in `config.py`.
- **Static Assets:**
  - Place images and static files in `assets/`.

## Integration & Data Flow
- Data flows from `helpers.py` and `figures/` into UI components.
- UI is composed in `app.py` using elements from `ui/` and `components/`.
- Charts are generated via `figures/generate_chart.py` and rendered in the UI.

## Examples
- To add a new chart: implement logic in `figures/`, create a UI wrapper in `ui/chart.py`, and add to the layout in `ui/layout.py` and/or `app.py`.
- To add a new UI widget: add to `components/`, import and use in relevant `ui/` or `app.py` files.

## Tips for AI Agents
- Always check `config.py` for settings before hardcoding values.
- Follow the existing modular structure for new features.
- Use existing components as templates for new UI elements.
- Keep business logic out of UI files—place in `helpers.py` or `figures/`.

---
_If any conventions or workflows are unclear, please request clarification or examples from the user._
