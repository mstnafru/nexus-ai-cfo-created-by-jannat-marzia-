# NEXUS — Autonomous Crypto CFO

> **From raw crypto data to explainable decisions.**

NEXUS is an AI-style crypto portfolio intelligence agent built for the **Binance Agent OS — Data & Analysis** track.

It transforms market and portfolio data into:

- 📊 Market intelligence
- 🛡️ Portfolio risk analysis
- 🧠 Explainable decisions
- 🎯 Actionable recommendations
- 🔗 Workflow-ready actions for Trading, Payment, and Onchain agents

## How NEXUS Works

Market Data
↓
Risk Engine
↓
AI CFO Reasoning
↓
Decision
↓
Workflow Action

## Core Analysis

NEXUS analyzes:

- Current price
- Market volatility
- Price trend
- Drawdown from recent highs
- Portfolio concentration
- Portfolio-level risk

## Example

Instead of simply saying:

"ETH volatility is 7%."

NEXUS explains:

"ETH represents 47% of the portfolio, above the configured 40% concentration limit. The position is therefore the highest-priority portfolio risk."

### Recommendation

Consider reducing ETH exposure toward the configured target.

### Workflow

`CREATE_REBALANCE_PLAN`

## Track

**Primary:** Data & Analysis

**Future extensions:**

- Trading workflows
- Payment workflows
- Onchain workflows

## Demo

Run the offline demo:

```bash
pip install -r requirements.txt
python -m nexus.agent --config config.yaml --demo
