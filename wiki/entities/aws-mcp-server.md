---
title: "AWS MCP Server"
slug: aws-mcp-server
type: product
last_updated: 2026-05-13
---

# AWS MCP Server

## What It Is
The AWS MCP Server is Amazon's managed remote Model Context Protocol server that reached general availability on May 6, 2026. It provides AI agents secure access to 15,000+ AWS API operations with IAM integration using context keys, sandboxed script execution, and a new "Skills" feature that replaces traditional Agent SOPs with curated AWS best practices.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Amazon Web Services |
| Launch Date | 2026-05-06 (GA) |
| API Operations | 15,000+ |
| Authentication | IAM integration with context keys |
| Execution | Sandboxed script execution |
| Key Feature | "Skills" replacing Agent SOPs |

## Significance
AWS joining the MCP ecosystem with a first-class managed server validates Anthropic's protocol as the de facto industry standard for AI-tool integration. The 15,000 API operations coverage is comprehensive — this is not a curated subset but the full AWS surface, meaning agents can theoretically manage any AWS resource through a single protocol interface.

The "Skills" feature is the subtle but important innovation: instead of agents learning how to use AWS through trial and error, AWS packages its tribal knowledge as reusable primitives. This shifts the burden from the agent developer to the service provider — AWS knows how AWS should be used, and now encodes that knowledge as structured capabilities agents can invoke.

The timing is strategically significant: the same week as HuggingFace Transformers 5.8.0 added DeepSeek-V4 support and IBM launched Watsonx Orchestrate, MCP is becoming the connective tissue of the AI infrastructure stack. When the largest cloud provider, the largest model hub, and the oldest enterprise AI platform all converge on the same protocol, it signals protocol consolidation rather than fragmentation.

On May 13, 2026, the AWS MCP Server's general availability with sandboxed Python execution was contextualized alongside GitHub MCP Server's secret scanning GA and new open-source agent projects (frona, Agenvoy) launching with MCP support. Cloud providers are now racing to become the "default backend" for AI agents, betting that agent workflows will drive compute consumption. The sandboxed Python execution is the killer feature — most MCP servers just query APIs, but AWS lets agents actually run code in their environment.

## Connections
- [[entities/mcp-protocol]] — AWS MCP Server validates MCP as enterprise-grade infrastructure; 15,000 API operations is the most comprehensive MCP implementation to date and addresses the supply chain security concerns that the April 21 vulnerability exposed
- [[sources/ibm]] — IBM's Watsonx Orchestrate launched the same week as AWS MCP Server GA; both are enterprise control planes for agent infrastructure, but AWS provides the cloud resource layer while IBM provides governance — complementary infrastructure converging on MCP
- [[topics/agentic_ai]] — 15,000 AWS APIs accessible through MCP means agents can now manage cloud infrastructure, databases, networking, and security at scale; the "Skills" feature replacing SOPs is the infrastructure layer for reliable agent-cloud interaction
- [[ideas/agent-economy-infrastructure]] — AWS MCP Server provides the cloud resource pillar that agent economy infrastructure was missing; alongside Stripe (payments), IBM (governance), and OpenAI (deployment), AWS completes the operational stack for agents as economic participants
- [[entities/ibm-sovereign-core]] — AWS MCP Server's IAM integration with context keys is a security model that complements IBM Sovereign Core's runtime policy embedding; together they show enterprise agent security being built at both the cloud access layer and the governance layer
- [[ideas/boring-infrastructure-shift]] — AWS MCP Server GA is the definition of boring infrastructure: not a breakthrough capability but the plumbing that makes agents reliably manage enterprise cloud resources; the 15,000 API coverage means this is comprehensive plumbing, not a demo
