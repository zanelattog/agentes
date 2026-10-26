<p align="center"><a href="README.md">Português</a> · <b>English</b></p>

# AI Agents

Eleven agents for development, content, prospecting and delivery coordination. I put this selection together to plan, build and review projects in Codex, with role-specific procedures and a simple installer.

**[↓ Download the agents](https://github.com/zanelattog/agentes/archive/refs/heads/main.zip)** · [Installation](docs/installation.en.md) · [Token usage](docs/tokens.en.md)

## Meet the team

| Agent | How it helps |
| --- | --- |
| **[Atlas](agents/atlas.toml)** | Plans the solution and next steps. |
| **[Luna](agents/luna.toml)** | Builds screens, forms and interactions. |
| **[Nexo](agents/nexo.toml)** | Handles APIs, business rules and data. |
| **[Iris](agents/iris.toml)** | Reviews code for bugs and regressions. |
| **[Cora](agents/cora.toml)** | Examines access, inputs and security risks. |
| **[Vero](agents/vero.toml)** | Tests the delivery and checks what actually works. |
| **[Pixel](agents/pixel.toml)** | Plans and produces images using available tools. |
| **[Frame](agents/frame.toml)** | Prepares video scripts, cuts and editing. |
| **[Nilo](agents/nilo.toml)** | Researches and qualifies leads; drafts outreach. |
| **[Maia](agents/maia.toml)** | Creates content, campaign copy and presentations. |
| **[Otto](agents/otto.toml)** | Organizes priorities, dependencies and deliverables. |

![Edited Habblaud example showing Atlas, Luna, Nexo, Iris, Cora and Vero with their roles](assets/habblaud-equipe.png)

<sub>Illustration of the original six technical agents, before expansion to eleven. Edited from an official screenshot of <a href="https://github.com/marmottajr/habblaud">Habblaud by Márcio Junior</a>. Names and roles were changed to present this team. This is not a capture of our agents running. The application labels in this image are in Portuguese. <a href="docs/imagens.md">Source and editing details</a>.</sub>

## How to call the agents

**You do not need to memorize names or call everyone for each request.** Choose a specialist or ask Codex to choose:

| You want… | You can say… |
| --- | --- |
| Codex to choose | “Use the agents needed for this task and explain how you divided the work.” |
| A code review | “Ask Iris to review this code without editing files.” |
| A screen built and checked | “Ask Luna to implement the screen, then ask Vero to test it.” |

If you prefer deciding before using additional agents, start the chat with:

> Handle simple tasks directly. When specialists would help, suggest which ones and ask me before calling them.

This instruction applies to the conversation; repeat it in a new chat or save it in project instructions. Installing profiles makes them available; it does not automatically run all eleven. [More examples](docs/usage.en.md).

## Five new specialists in practice

- **Pixel:** “Prepare a cover for this project. Generate it if a suitable tool is available, then inspect the result.”
- **Frame:** “Plan a 30-second app demo with cuts and subtitles.”
- **Nilo:** “Define the ideal customer and research matching companies with sources. Do not contact anyone.”
- **Maia:** “Turn this demo into a LinkedIn post without inventing metrics.”
- **Otto:** “Organize these tasks by priority, dependencies and completion criteria.”

Image and video production require accessible media tools. Without them, profiles deliver plans and disclose the limitation. Lead research depends on available sources; drafting does not authorize sending.

## What I adapted from Vibe Coding Toolkit

Verify actual state before acting, investigate failures using evidence, preserve local changes and resume without blindly trusting old handoffs. These practices are embedded in **all eleven profiles**, with credit to Matheus Gomes. [Adaptation details](docs/toolkit.en.md).

## Get started

1. Click **Download the agents** and extract the ZIP.
2. Open the folder and double-click **Instalar.command**.
3. Wait for **Done**, then start a new Codex chat. Recognized previous versions are upgraded with backups; personal edits are preserved.
4. Request an agent by name:

> Use `iris` to review this change. Report issues with evidence and do not edit files. Respond in English.

The same installer supports Intel and Apple Silicon Macs. Downloading does not run it automatically. [Full instructions and troubleshooting](docs/installation.en.md).

## The Habblaud office

Habblaud helps you see who is working or waiting for your attention. It assigns its own characters: **installing these profiles does not automatically apply the names in the image**. [Character names and Codex integration](docs/habblaud.en.md).

Watching the dashboard does not require a new AI response. Working agents still consume tokens.

## What to expect

Each profile defines procedures, checks and boundaries. **Paired test: a tie on all eleven exercises.** Expanded profiles passed the checks, but did not outperform the previous versions in this sample and used 4.04% more tokens. [Results and limitations](docs/evaluation.en.md).

[Understand token usage](docs/tokens.en.md) · [Validation status](docs/evaluation.en.md) · [Original catalog's visual installer](docs/installation.en.md#original-catalog-agency-agents-app)

---

Selected and adapted by **Gabriel (@zanelattog)** with Codex assistance. Based on **Agency Agents by Michael Sitarzewski and contributors**, with practices from **Vibe Coding Toolkit by Matheus Gomes**. [Credits](CREDITOS.md) · [MIT](LICENSE).
