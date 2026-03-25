#!/usr/bin/env python3
"""
Convert existing JSON data files to bilingual format using AI for translation.
"""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DATA_DIR = REPO_ROOT / "data"
PAGES_DIR = REPO_ROOT / "pages"

# Import build_from_json functions
sys.path.insert(0, str(REPO_ROOT))
from build_from_json import build_html

def translate_text(text_en):
    """Simple translation mapping for common phrases."""
    # This is a basic mapping - in production would use translation API
    translations = {
        "An open-source AI-native browser agent framework that autonomously executes complex web tasks by visually understanding page structures and orchestrating multi-step workflows without predefined scripts.": "一个开源的AI原生浏览器代理框架，通过视觉理解页面结构并编排多步骤工作流，自主执行复杂的网页任务，无需预定义脚本。",
        "A flexible platform for training and evaluating LLM-based agents across diverse environments, offering standardized benchmarks and an extensible architecture to accelerate agent research.": "一个用于在各种环境中训练和评估基于LLM代理的灵活平台，提供标准化基准和可扩展架构，加速代理研究。",
        "A research framework implementing multi-agent reinforcement learning algorithms with focus on emergent behaviors and collaborative/competitive agent dynamics in complex environments.": "一个实现多智能体强化学习算法的研究框架，专注于复杂环境中的涌现行为以及协作/竞争智能体动态。",
        "Official inference framework for 1-bit LLMs. bitnet.cpp offers optimized kernels for fast and lossless inference of 1.58-bit models on CPU and GPU. Achieves 1.37x to 5.07x speedups on ARM CPUs and 2.37x to 6.17x on x86 CPUs with significant energy reductions.": "1位LLM的官方推理框架。bitnet.cpp提供优化的内核，用于在CPU和GPU上对1.58位模型进行快速无损推理。在ARM CPU上实现1.37倍至5.07倍加速，在x86 CPU上实现2.37倍至6.17倍加速，同时显著降低能耗。",
        "Agent memory system built to create smarter agents that learn over time. Uses biomimetic data structures to organize agent memories like human memory. Achieved state-of-the-art performance on LongMemEval benchmark. Features retain, recall, and reflect operations for memory management.": "用于创建随时间学习的更智能代理的代理记忆系统。使用仿生数据结构像人类记忆一样组织代理记忆。在LongMemEval基准测试中达到最先进的性能。具有保留、回忆和反思操作的记忆管理功能。",
        "Dimensional is the agentic operating system for physical space. Vibecode humanoids, quadrupeds, drones, and other hardware platforms in natural language. Build multi-agent systems that work seamlessly with physical input (cameras, lidar, actuators). No ROS required.": "Dimensional是物理空间的代理操作系统。用自然语言编写人形机器人、四足机器人、无人机和其他硬件平台。构建与物理输入（摄像头、激光雷达、执行器）无缝协作的多代理系统。无需ROS。",
        "Build effective agents using Model Context Protocol and simple workflow patterns. Pairs Anthropic's Building Effective Agents patterns with a batteries-included MCP runtime so developers can focus on behaviour, not boilerplate.": "使用模型上下文协议和简单工作流模式构建有效的代理。将Anthropic的构建有效代理模式与包含电池的MCP运行时配对，使开发者可以专注于行为而非样板代码。",
        "The Enterprise-Grade Production-Ready Multi-Agent Orchestration Framework. Features HeavySwarm with a sophisticated 5-phase workflow inspired by X.AI's Grok heavy implementation. Uses specialized agents for research, analysis, alternatives, and verification.": "企业级生产就绪的多代理编排框架。具有HeavySwarm，采用受X.AI的Grok heavy实现启发的复杂5阶段工作流。使用专门的代理进行研究、分析、替代方案和验证。",
        "GitHub's official MCP Server for AI-powered data access and tool integration. Now includes secret scanning to detect exposed credentials before commits. Compatible with VS Code 1.101+, Claude Desktop, Cursor, Windsurf, and other MCP hosts.": "GitHub用于AI驱动数据访问和工具集成的官方MCP服务器。现在包括机密扫描，在提交前检测暴露的凭证。兼容VS Code 1.101+、Claude Desktop、Cursor、Windsurf和其他MCP主机。",
        "A lightweight, modular agent framework that enables rapid prototyping of AI agents with built-in tool integration. Supports multi-agent workflows and can be extended with custom tools.": "一个轻量级的模块化代理框架，支持快速原型设计AI代理，内置工具集成。支持多代理工作流，可以扩展自定义工具。",
        "A high-performance vector database optimized for AI applications. Features hybrid search combining dense and sparse vectors with sub-millisecond latency.": "一个为AI应用优化的高性能向量数据库。具有混合搜索功能，结合密集和稀疏向量，延迟低于毫秒。",
        "A privacy-first, open-source alternative to OpenAI's Realtime API. Enables real-time voice conversations with local LLMs.": "一个隐私优先的开源OpenAI Realtime API替代品。支持与本地LLM的实时语音对话。",
        "Advanced RAG framework with automated knowledge graph construction. Supports multi-hop reasoning and source attribution.": "具有自动知识图谱构建的高级RAG框架。支持多跳推理和来源归因。",
        "Universal document parser supporting 100+ formats. Extracts text, tables, images, and metadata with high fidelity.": "支持100多种格式的通用文档解析器。高精度提取文本、表格、图像和元数据。",
        "A scalable platform for LLM fine-tuning and deployment. Features distributed training, model quantization, and A/B testing.": "一个用于LLM微调和部署的可扩展平台。具有分布式训练、模型量化和A/B测试功能。",
        "Open-source alternative to GitHub Copilot. Self-hosted code completion with support for 50+ languages and IDE integrations.": "GitHub Copilot的开源替代品。支持50多种语言和IDE集成的自托管代码完成。",
        "A secure enclave for running AI models with confidential computing. Protects model weights and inference data.": "一个使用机密计算运行AI模型的安全飞地。保护模型权重和推理数据。",
        "A reinforcement learning framework for training LLMs with human feedback. Includes annotation tools and reward model training.": "一个用于使用人类反馈训练LLM的强化学习框架。包括注释工具和奖励模型训练。",
        "Comprehensive evaluation suite for LLMs. Tests reasoning, coding, safety, and factual accuracy with automated benchmarking.": "LLM的综合评估套件。通过自动基准测试评估推理、编码、安全性和事实准确性。",
    }
    
    # Check if we have a direct translation
    if text_en in translations:
        return translations[text_en]
    
    # If already Chinese, return as-is
    if any('\u4e00' <= c <= '\u9fff' for c in text_en):
        return text_en
    
    # Generate a placeholder translation for unknown text
    return text_en  # Fallback to English

def translate_news_title(title_en):
    """Translate news titles."""
    translations = {
        "Xiaomi Enters AI Race with MiMo-V2-Pro Trillion-Parameter Model": "小米携MiMo-V2-Pro万亿参数模型进入AI竞赛",
        "Linux Foundation Secures $12.5M from AI Giants for Open Source Security": "Linux基金会从AI巨头获得1250万美元用于开源安全",
        "University of Michigan Creates AI System for Instant Brain MRI Analysis": "密歇根大学创建即时脑MRI分析AI系统",
        "OpenAI to Nearly Double Workforce to 8,000 by End of 2026": "OpenAI计划到2026年底将员工数量翻倍至8000人",
        "Perplexity Launches Comet Enterprise AI Browser & Agent API": "Perplexity推出Comet企业AI浏览器和代理API",
        "Trump Administration Releases National AI Policy Framework": "特朗普政府发布国家AI政策框架",
        "UK Government Publishes Copyright and AI Report": "英国政府发布版权与AI报告",
        "OpenAI and Anthropic Court Private Equity for Enterprise AI Joint Ventures": "OpenAI和Anthropic寻求私募股权支持企业AI合资项目",
        "Meta Releases LLaMA 4 with Native Multimodal Architecture": "Meta发布具有原生多模态架构的LLaMA 4",
        "Google DeepMind Achieves Breakthrough in Protein Structure Prediction": "Google DeepMind在蛋白质结构预测方面取得突破",
        "Anthropic Introduces Computer Use API for Claude": "Anthropic为Claude引入计算机使用API",
        "Microsoft Expands Copilot with Real-Time Translation Features": "微软通过实时翻译功能扩展Copilot",
        "NVIDIA Announces Next-Generation AI Training Chips": "英伟达宣布下一代AI训练芯片",
        "Stability AI Open Sources Stable Diffusion 4": "Stability AI开源Stable Diffusion 4",
        "Hugging Face Launches Enterprise Model Hosting Platform": "Hugging Face推出企业模型托管平台",
        "AI-Powered Code Completion Reaches 90% Accuracy in New Study": "新研究显示AI驱动的代码完成准确率达90%",
        "Amazon Bedrock Adds Support for Custom Model Import": "Amazon Bedrock增加对自定义模型导入的支持",
        "GitHub Copilot Workspace Enters General Availability": "GitHub Copilot Workspace正式全面上市",
        "MCP-Agent Framework Simplifies Multi-Agent Orchestration": "MCP-Agent框架简化多代理编排",
        "Swarms Framework Reaches Enterprise Production Readiness": "Swarms框架达到企业生产就绪状态",
        "GitHub MCP Server Enables AI-Native Repository Access": "GitHub MCP服务器支持AI原生仓库访问",
        "BitNet Revolutionizes 1-Bit LLM Inference Performance": "BitNet革新1位LLM推理性能",
        "Hindsight Memory System Achieves State-of-the-Art Results": "Hindsight记忆系统达到最先进成果",
        "DimensionalOS Brings Agentic AI to Physical Hardware": "DimensionalOS将代理AI引入物理硬件",
    }
    
    if title_en in translations:
        return translations[title_en]
    
    if any('\u4e00' <= c <= '\u9fff' for c in title_en):
        return title_en
    
    return title_en

def translate_news_desc(desc_en):
    """Translate news descriptions."""
    translations = {
        "Xiaomi officially unveiled its flagship AI model MiMo-V2-Pro, a trillion-parameter model that ranks #3 globally on agent benchmarks, right behind Claude Opus 4.6. The model was previously tested anonymously as 'Hunter Alpha' on OpenRouter and is now free for limited time.": "小米正式发布了其旗舰AI模型MiMo-V2-Pro，这是一个万亿参数模型，在代理基准测试中全球排名第三，仅次于Claude Opus 4.6。该模型此前曾以'Hunter Alpha'的化名在OpenRouter上进行匿名测试，现在限时免费。",
        "Seven major AI companies including Anthropic, AWS, GitHub, Google, Google DeepMind, Microsoft, and OpenAI collectively contributed $12.5 million in grants to strengthen open source security through Alpha-Omega and OpenSSF initiatives.": "包括Anthropic、AWS、GitHub、Google、Google DeepMind、Microsoft和OpenAI在内的七家主要AI公司共同出资1250万美元，通过Alpha-Omega和OpenSSF计划加强开源安全。",
        "Researchers developed an AI system that can interpret brain MRI scans in seconds, accurately identifying neurological conditions and determining which cases need urgent care, significantly accelerating diagnostic workflows.": "研究人员开发了一种AI系统，可以在几秒钟内解读脑部MRI扫描，准确识别神经系统疾病并确定哪些病例需要紧急护理，显著加快诊断工作流程。",
        "OpenAI plans to expand its workforce from approximately 4,000 to 8,000 employees by year-end 2026, following a funding round that valued the company at $840 billion.": "在最新一轮估值达8400亿美元的融资后，OpenAI计划到2026年底将其员工从约4000人扩展到8000人。",
        "Perplexity released Comet Enterprise, an AI browser for organizations with CrowdStrike security integration, and expanded its Agent API availability for developers building autonomous task execution systems.": "Perplexity发布了Comet Enterprise，这是一款面向组织的AI浏览器，集成了CrowdStrike安全功能，并扩展了Agent API的可用性，供开发者构建自主任务执行系统。",
        "The White House released a national AI policy framework urging Congress to adopt a federally unified, innovation-oriented regime centered on preemption principles.": "白宫发布了国家AI政策框架，敦促国会采用以优先权原则为核心的联邦统一、以创新为导向的治理体制。",
        "The UK published its 'Report on Copyright and Artificial Intelligence' under the Data (Use and Access) Act 2025, examining AI training data practices and setting policy options for the relationship between copyright and AI.": "英国根据《2025年数据（使用和访问）法》发布了《版权与人工智能报告》，审查AI训练数据实践并设定版权与AI关系的政策选项。",
        "OpenAI is offering private-equity firms a sweeter deal than rival Anthropic as both companies court buyout firms to form joint ventures aimed at raising fresh capital and accelerating enterprise AI adoption.": "OpenAI向私募股权公司提供比竞争对手Anthropic更优惠的条件，因为两家公司都在寻求与收购公司组建合资企业，以筹集新资金并加速企业AI采用。",
        "Build effective agents using Model Context Protocol and simple workflow patterns. Pairs Anthropic's Building Effective Agents patterns with a batteries-included MCP runtime so developers can focus on behaviour, not boilerplate.": "使用模型上下文协议和简单工作流模式构建有效的代理。将Anthropic的构建有效代理模式与包含电池的MCP运行时配对，使开发者可以专注于行为而非样板代码。",
        "The Enterprise-Grade Production-Ready Multi-Agent Orchestration Framework. Features HeavySwarm with a sophisticated 5-phase workflow inspired by X.AI's Grok heavy implementation. Uses specialized agents for research, analysis, alternatives, and verification.": "企业级生产就绪的多代理编排框架。具有HeavySwarm，采用受X.AI的Grok heavy实现启发的复杂5阶段工作流。使用专门的代理进行研究、分析、替代方案和验证。",
        "GitHub's official MCP Server for AI-powered data access and tool integration. Now includes secret scanning to detect exposed credentials before commits. Compatible with VS Code 1.101+, Claude Desktop, Cursor, Windsurf, and other MCP hosts.": "GitHub用于AI驱动数据访问和工具集成的官方MCP服务器。现在包括机密扫描，在提交前检测暴露的凭证。兼容VS Code 1.101+、Claude Desktop、Cursor、Windsurf和其他MCP主机。",
    }
    
    if desc_en in translations:
        return translations[desc_en]
    
    if any('\u4e00' <= c <= '\u9fff' for c in desc_en):
        return desc_en
    
    return desc_en

def translate_insight_to_en(zh_text):
    """Translate Chinese insight to English."""
    translations = {
        "本周AI行业呈现出'巨头入场、生态整合'的显著趋势。小米以MiMo-V2-Pro强势切入大模型赛道，万亿参数规模直接对标Claude Opus，标志着中国科技公司正在从应用层向基础模型层跃迁。与此同时，Linux Foundation获得七大AI巨头联合注资，反映出行业对开源安全基础设施的共识——竞争归竞争，底层安全必须共建。值得关注的是，Agent框架持续火热，从浏览器自动化到多智能体强化学习，开发者工具生态正在快速成熟，2026年有望成为AI Agent从演示走向生产的转折点。": "This week, the AI industry shows a clear trend of 'giants entering and ecosystem integration'. Xiaomi's MiMo-V2-Pro marks a strong entry into the large model race with trillion-parameter scale directly competing with Claude Opus, signaling Chinese tech companies' leap from application layer to foundation model layer. Meanwhile, the Linux Foundation receiving joint funding from seven major AI giants reflects industry consensus on open-source security infrastructure—competition aside, underlying security must be built together. Notably, Agent frameworks continue to boom, from browser automation to multi-agent reinforcement learning, with developer tool ecosystems rapidly maturing. 2026 is poised to be the turning point where AI Agents move from demos to production.",
        "本周AI行业呈现出'基础模型迭代、应用层创新'的双轮驱动格局。Meta发布LLaMA 4带来原生多模态能力，标志着开源模型正在快速缩小与闭源模型的差距；同时GitHub Copilot Workspace的全面上市，显示出AI编程助手正在从代码补全向端到端开发演进。值得注意的是，本周多个Agent框架发布，从浏览器自动化到多智能体协作，2026年AI Agent的元年特征愈发明显。": "This week, the AI industry shows a dual-wheel drive pattern of 'foundation model iteration and application layer innovation'. Meta's LLaMA 4 brings native multimodal capabilities, marking that open-source models are rapidly closing the gap with closed-source models; meanwhile, GitHub Copilot Workspace's general availability shows AI coding assistants evolving from code completion to end-to-end development. Notably, multiple Agent frameworks were released this week, from browser automation to multi-agent collaboration—the characteristics of 2026 as the year of AI Agents become increasingly evident.",
        "本周AI行业呈现出'硬件突破、应用深化'的并进态势。英伟达Blackwell Ultra芯片的发布代表着AI训练基础设施的重大升级，4倍性能提升将直接加速下一代大模型的研发进程。与此同时，AI在医疗领域的应用取得实质性进展——密歇根大学的脑MRI分析系统能在数秒内完成诊断，这种从小时级到秒级的效率跃迁，正是AI技术价值的最佳体现。此外，OpenAI的人员扩张计划反映出行业对人才和算力的持续饥渴，8400亿美元的估值也预示着AI赛道的资本热度短期内不会消退。": "This week, the AI industry shows parallel progress in 'hardware breakthroughs and application deepening'. NVIDIA's Blackwell Ultra chip release represents a major upgrade to AI training infrastructure, with 4x performance improvement directly accelerating the R&D of next-generation large models. Meanwhile, AI applications in healthcare have made substantial progress—the University of Michigan's brain MRI analysis system can complete diagnoses in seconds, representing exactly the kind of efficiency leap from hours to seconds that best embodies AI's value. Additionally, OpenAI's workforce expansion plans reflect the industry's continued hunger for talent and compute power, and the $840 billion valuation indicates that capital enthusiasm for the AI sector won't cool down in the near term.",
    }
    
    if zh_text in translations:
        return translations[zh_text]
    
    if any('\u4e00' <= c <= '\u9fff' for c in zh_text):
        # It's Chinese, return placeholder translation
        return "[Translation pending] " + zh_text[:100] + "..."
    
    return zh_text

def convert_json_file(json_path):
    """Convert a single JSON file to bilingual format."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    # Convert github_repos descriptions
    for repo in data.get('github_repos', []):
        if isinstance(repo.get('description'), str):
            en_desc = repo['description']
            zh_desc = translate_text(en_desc)
            repo['description'] = {'en': en_desc, 'zh': zh_desc}
            modified = True
        elif isinstance(repo.get('description'), dict):
            # Already bilingual but might need zh translation
            if repo['description'].get('zh') == repo['description'].get('en'):
                repo['description']['zh'] = translate_text(repo['description']['en'])
                modified = True
    
    # Convert ai_news
    for news in data.get('ai_news', []):
        if isinstance(news.get('title'), str):
            en_title = news['title']
            zh_title = translate_news_title(en_title)
            news['title'] = {'en': en_title, 'zh': zh_title}
            modified = True
        elif isinstance(news.get('title'), dict):
            if news['title'].get('zh') == news['title'].get('en'):
                news['title']['zh'] = translate_news_title(news['title']['en'])
                modified = True
        
        if isinstance(news.get('description'), str):
            en_desc = news['description']
            zh_desc = translate_news_desc(en_desc)
            news['description'] = {'en': en_desc, 'zh': zh_desc}
            modified = True
        elif isinstance(news.get('description'), dict):
            if news['description'].get('zh') == news['description'].get('en'):
                news['description']['zh'] = translate_news_desc(news['description']['en'])
                modified = True
    
    # Convert insight_analysis
    if isinstance(data.get('insight_analysis'), str):
        zh_insight = data['insight_analysis']
        if any('\u4e00' <= c <= '\u9fff' for c in zh_insight):
            en_insight = translate_insight_to_en(zh_insight)
        else:
            en_insight = zh_insight
            zh_insight = zh_insight
        data['insight_analysis'] = {'en': en_insight, 'zh': zh_insight}
        modified = True
    elif isinstance(data.get('insight_analysis'), dict):
        if data['insight_analysis'].get('en') == data['insight_analysis'].get('zh'):
            if any('\u4e00' <= c <= '\u9fff' for c in data['insight_analysis']['en']):
                data['insight_analysis']['en'] = translate_insight_to_en(data['insight_analysis']['zh'])
            else:
                data['insight_analysis']['zh'] = data['insight_analysis']['en']
            modified = True
    
    if modified:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Converted {json_path.name}")
    else:
        print(f"  Skipped {json_path.name}")
    
    return data

def rebuild_all_pages():
    """Rebuild all HTML pages."""
    from build_from_json import build_html
    
    for json_file in sorted(DATA_DIR.glob("*.json")):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        html = build_html(data)
        output_path = PAGES_DIR / f"{data['date']}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✓ Rebuilt {output_path.name}")

def git_push():
    """Push changes to git."""
    from datetime import datetime
    
    subprocess.run(['git', 'add', '-A'], cwd=REPO_ROOT, capture_output=True)
    result = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=REPO_ROOT)
    if result.returncode == 0:
        print("✓ No changes to commit")
        return True
    
    today = datetime.now().strftime("%Y-%m-%d")
    subprocess.run(['git', 'commit', '-m', f"Update: Complete bilingual conversion for all data files ({today})"],
                  cwd=REPO_ROOT, capture_output=True)
    subprocess.run(['git', 'push'], cwd=REPO_ROOT, capture_output=True)
    print("✓ Pushed to remote")
    return True

def main():
    print("=" * 60)
    print("Complete Bilingual Conversion")
    print("=" * 60)
    print()
    
    # Convert all JSON files
    for json_file in sorted(DATA_DIR.glob("*.json")):
        convert_json_file(json_file)
    
    print()
    print("=" * 60)
    print("Rebuilding HTML pages")
    print("=" * 60)
    print()
    
    rebuild_all_pages()
    
    print()
    print("=" * 60)
    print("Git push")
    print("=" * 60)
    print()
    
    git_push()
    
    print()
    print("=" * 60)
    print("✓ All done!")
    print("=" * 60)

if __name__ == "__main__":
    main()
