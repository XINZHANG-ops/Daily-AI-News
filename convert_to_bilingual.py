#!/usr/bin/env python3
"""
Convert existing JSON data files to bilingual format (EN/ZH).
Then rebuild all HTML pages and push to git.
"""

import json
import subprocess
from pathlib import Path
import sys

# Add parent directory to path to import build_from_json
sys.path.insert(0, str(Path(__file__).parent))

REPO_ROOT = Path(__file__).parent
DATA_DIR = REPO_ROOT / "data"
PAGES_DIR = REPO_ROOT / "pages"

def translate_repo_description(desc_en):
    """Simple mapping for common terms - in production this would use translation API."""
    translations = {
        "An open-source AI-native browser agent framework that autonomously executes complex web tasks by visually understanding page structures and orchestrating multi-step workflows without predefined scripts.": "一个开源的AI原生浏览器代理框架，通过视觉理解页面结构并编排多步骤工作流，自主执行复杂的网页任务，无需预定义脚本。",
        "A flexible platform for training and evaluating LLM-based agents across diverse environments, offering standardized benchmarks and an extensible architecture to accelerate agent research.": "一个用于在各种环境中训练和评估基于LLM代理的灵活平台，提供标准化基准和可扩展架构，加速代理研究。",
        "A research framework implementing multi-agent reinforcement learning algorithms with focus on emergent behaviors and collaborative/competitive agent dynamics in complex environments.": "一个实现多智能体强化学习算法的研究框架，专注于复杂环境中的涌现行为以及协作/竞争智能体动态。",
        "A high-performance inference engine for LLMs optimized for edge devices, featuring quantized model support and memory-efficient attention mechanisms.": "一个为边缘设备优化的高性能LLM推理引擎，支持量化模型和内存高效注意力机制。",
        "An open-source visual programming environment for AI workflows, enabling non-technical users to build complex agent pipelines through drag-and-drop interfaces.": "一个用于AI工作流的开源可视化编程环境，使非技术用户能够通过拖放界面构建复杂的代理流程。",
        "A comprehensive toolkit for building conversational AI assistants with built-in memory management, context handling, and multi-turn dialogue capabilities.": "一个用于构建对话式AI助手的综合工具包，内置内存管理、上下文处理和多轮对话能力。",
        "Real-time speech-to-text library optimized for low-latency applications, supporting 100+ languages with automatic punctuation and speaker diarization.": "一个为低延迟应用优化的实时语音转文本库，支持100多种语言，具有自动标点符号和说话人分离功能。",
    }
    return translations.get(desc_en, desc_en)

def translate_news_title(title_en):
    """Translate news titles to Chinese."""
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
    }
    return translations.get(title_en, title_en)

def translate_news_desc(desc_en):
    """Translate news descriptions to Chinese."""
    translations = {
        "Xiaomi officially unveiled its flagship AI model MiMo-V2-Pro, a trillion-parameter model that ranks #3 globally on agent benchmarks, right behind Claude Opus 4.6. The model was previously tested anonymously as 'Hunter Alpha' on OpenRouter and is now free for limited time.": "小米正式发布了其旗舰AI模型MiMo-V2-Pro，这是一个万亿参数模型，在代理基准测试中全球排名第三，仅次于Claude Opus 4.6。该模型此前曾以'Hunter Alpha'的化名在OpenRouter上进行匿名测试，现在限时免费。",
        "Seven major AI companies including Anthropic, AWS, GitHub, Google, Google DeepMind, Microsoft, and OpenAI collectively contributed $12.5 million in grants to strengthen open source security through Alpha-Omega and OpenSSF initiatives.": "包括Anthropic、AWS、GitHub、Google、Google DeepMind、Microsoft和OpenAI在内的七家主要AI公司共同出资1250万美元，通过Alpha-Omega和OpenSSF计划加强开源安全。",
        "Researchers developed an AI system that can interpret brain MRI scans in seconds, accurately identifying neurological conditions and determining which cases need urgent care, significantly accelerating diagnostic workflows.": "研究人员开发了一种AI系统，可以在几秒钟内解读脑部MRI扫描，准确识别神经系统疾病并确定哪些病例需要紧急护理，显著加快诊断工作流程。",
        "OpenAI plans to expand its workforce from approximately 4,000 to 8,000 employees by year-end 2026, following a funding round that valued the company at $840 billion.": "在最新一轮估值达8400亿美元的融资后，OpenAI计划到2026年底将其员工从约4000人扩展到8000人。",
        "Perplexity released Comet Enterprise, an AI browser for organizations with CrowdStrike security integration, and expanded its Agent API availability for developers building autonomous task execution systems.": "Perplexity发布了Comet Enterprise，这是一款面向组织的AI浏览器，集成了CrowdStrike安全功能，并扩展了Agent API的可用性，供开发者构建自主任务执行系统。",
        "The White House released a national AI policy framework urging Congress to adopt a federally unified, innovation-oriented regime centered on preemption principles.": "白宫发布了国家AI政策框架，敦促国会采用以优先权原则为核心的联邦统一、以创新为导向的治理体制。",
        "The UK published its 'Report on Copyright and Artificial Intelligence' under the Data (Use and Access) Act 2025, examining AI training data practices and setting policy options for the relationship between copyright and AI.": "英国根据《2025年数据（使用和访问）法》发布了《版权与人工智能报告》，审查AI训练数据实践并设定版权与AI关系的政策选项。",
        "OpenAI is offering private-equity firms a sweeter deal than rival Anthropic as both companies court buyout firms to form joint ventures aimed at raising fresh capital and accelerating enterprise AI adoption.": "OpenAI向私募股权公司提供比竞争对手Anthropic更优惠的条件，因为两家公司都在寻求与收购公司组建合资企业，以筹集新资金并加速企业AI采用。",
        "Meta's latest LLaMA model features seamless integration of text, image, and video understanding with improved reasoning capabilities and reduced hallucination rates.": "Meta最新的LLaMA模型实现了文本、图像和视频理解的无缝集成，具有改进的推理能力和降低的幻觉率。",
        "AlphaFold 4 demonstrates 50% improvement in accuracy for complex protein interactions, opening new pathways for drug discovery and disease treatment.": "AlphaFold 4在复杂蛋白质相互作用的准确性方面显示出50%的改进，为药物发现和疾病治疗开辟了新途径。",
        "New API allows Claude to control computers, browse the web, and execute tasks autonomously, competing directly with OpenAI's Operator.": "新API允许Claude控制计算机、浏览网页并自主执行任务，直接与OpenAI的Operator竞争。",
        "Real-time translation now supports 40+ language pairs with context-aware processing and industry-specific terminology support.": "实时翻译现在支持40多种语言对，具有上下文感知处理和行业特定术语支持。",
        "Blackwell Ultra chips promise 4x performance improvement for training large AI models while reducing energy consumption by 25%.": "Blackwell Ultra芯片承诺将训练大型AI模型的性能提高4倍，同时降低25%的能耗。",
        "Latest version features improved photorealism, better text rendering, and 8K resolution support with training data increased by 300%.": "最新版本具有改进的照片级真实感、更好的文本渲染和8K分辨率支持，训练数据增加了300%。",
        "New platform offers dedicated GPU clusters, fine-tuning capabilities, and enterprise-grade security for hosting proprietary AI models.": "新平台为托管专有AI模型提供专用GPU集群、微调功能和企业级安全。",
        "Researchers at MIT demonstrate that AI pair programmers can now match human accuracy across multiple programming languages and frameworks.": "麻省理工学院的研究人员证明，AI结对程序员现在可以在多种编程语言和框架中达到与人类相当的准确性。",
        "Businesses can now import and deploy their own fine-tuned models alongside foundation models in the Bedrock platform.": "企业现在可以在Bedrock平台中导入和部署自己的微调模型，与基础模型一起使用。",
        "New environment enables full-stack application development through natural language prompts, integrating planning, coding, and deployment workflows.": "新环境支持通过自然语言提示进行全栈应用开发，集成规划、编码和部署工作流程。",
    }
    return translations.get(desc_en, desc_en)

def translate_insight(insight_en):
    """Translate insight analysis to English."""
    insights = {
        "本周AI行业呈现出'巨头入场、生态整合'的显著趋势。小米以MiMo-V2-Pro强势切入大模型赛道，万亿参数规模直接对标Claude Opus，标志着中国科技公司正在从应用层向基础模型层跃迁。与此同时，Linux Foundation获得七大AI巨头联合注资，反映出行业对开源安全基础设施的共识——竞争归竞争，底层安全必须共建。值得关注的是，Agent框架持续火热，从浏览器自动化到多智能体强化学习，开发者工具生态正在快速成熟，2026年有望成为AI Agent从演示走向生产的转折点。": "This week, the AI industry shows a clear trend of 'giants entering and ecosystem integration'. Xiaomi's MiMo-V2-Pro marks a strong entry into the large model race with trillion-parameter scale directly competing with Claude Opus, signaling Chinese tech companies' leap from application layer to foundation model layer. Meanwhile, the Linux Foundation receiving joint funding from seven major AI giants reflects industry consensus on open-source security infrastructure—competition aside, underlying security must be built together. Notably, Agent frameworks continue to boom, from browser automation to multi-agent reinforcement learning, with developer tool ecosystems rapidly maturing. 2026 is poised to be the turning point where AI Agents move from demos to production.",
        "本周AI行业呈现出'基础模型迭代、应用层创新'的双轮驱动格局。Meta发布LLaMA 4带来原生多模态能力，标志着开源模型正在快速缩小与闭源模型的差距；同时GitHub Copilot Workspace的全面上市，显示出AI编程助手正在从代码补全向端到端开发演进。值得注意的是，本周多个Agent框架发布，从浏览器自动化到多智能体协作，2026年AI Agent的元年特征愈发明显。": "This week, the AI industry shows a dual-wheel drive pattern of 'foundation model iteration and application layer innovation'. Meta's LLaMA 4 brings native multimodal capabilities, marking that open-source models are rapidly closing the gap with closed-source models; meanwhile, GitHub Copilot Workspace's general availability shows AI coding assistants evolving from code completion to end-to-end development. Notably, multiple Agent frameworks were released this week, from browser automation to multi-agent collaboration—the characteristics of 2026 as the year of AI Agents become increasingly evident.",
        "本周AI行业呈现出'硬件突破、应用深化'的并进态势。英伟达Blackwell Ultra芯片的发布代表着AI训练基础设施的重大升级，4倍性能提升将直接加速下一代大模型的研发进程。与此同时，AI在医疗领域的应用取得实质性进展——密歇根大学的脑MRI分析系统能在数秒内完成诊断，这种从小时级到秒级的效率跃迁，正是AI技术价值的最佳体现。此外，OpenAI的人员扩张计划反映出行业对人才和算力的持续饥渴，8400亿美元的估值也预示着AI赛道的资本热度短期内不会消退。": "This week, the AI industry shows parallel progress in 'hardware breakthroughs and application deepening'. NVIDIA's Blackwell Ultra chip release represents a major upgrade to AI training infrastructure, with 4x performance improvement directly accelerating the R&D of next-generation large models. Meanwhile, AI applications in healthcare have made substantial progress—the University of Michigan's brain MRI analysis system can complete diagnoses in seconds, representing exactly the kind of efficiency leap from hours to seconds that best embodies AI's value. Additionally, OpenAI's workforce expansion plans reflect the industry's continued hunger for talent and compute power, and the $840 billion valuation indicates that capital enthusiasm for the AI sector won't cool down in the near term.",
    }
    return insights.get(insight_en, insight_en)

def convert_json_to_bilingual(json_path):
    """Convert single JSON file to bilingual format."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    # Convert github_repos descriptions
    for repo in data.get('github_repos', []):
        if isinstance(repo.get('description'), str):
            en_desc = repo['description']
            zh_desc = translate_repo_description(en_desc)
            repo['description'] = {'en': en_desc, 'zh': zh_desc}
            modified = True
    
    # Convert ai_news titles and descriptions
    for news in data.get('ai_news', []):
        if isinstance(news.get('title'), str):
            en_title = news['title']
            zh_title = translate_news_title(en_title)
            news['title'] = {'en': en_title, 'zh': zh_title}
            modified = True
        
        if isinstance(news.get('description'), str):
            en_desc = news['description']
            zh_desc = translate_news_desc(en_desc)
            news['description'] = {'en': en_desc, 'zh': zh_desc}
            modified = True
    
    # Convert insight_analysis
    if isinstance(data.get('insight_analysis'), str):
        zh_insight = data['insight_analysis']
        # Check if it's already Chinese (contains Chinese characters)
        if any('\u4e00' <= char <= '\u9fff' for char in zh_insight):
            en_insight = translate_insight(zh_insight)
        else:
            en_insight = zh_insight
            zh_insight = zh_insight  # Keep as is if English
        data['insight_analysis'] = {'en': en_insight, 'zh': zh_insight}
        modified = True
    
    if modified:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Converted {json_path.name}")
    else:
        print(f"  Skipped {json_path.name} (already bilingual)")
    
    return data

def rebuild_html_page(json_path):
    """Rebuild HTML page from JSON using build_from_json.py."""
    import subprocess
    result = subprocess.run(
        ['python3', 'build_from_json.py', str(json_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"  ✓ Rebuilt {json_path.stem}.html")
    else:
        print(f"  ✗ Failed to rebuild {json_path.stem}.html: {result.stderr}")

def git_push():
    """Run git add, commit, and push."""
    from datetime import datetime
    
    # Git add
    result = subprocess.run(['git', 'add', '-A'], cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"✗ git add failed: {result.stderr}")
        return False
    
    # Check if there are changes
    result = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=REPO_ROOT)
    if result.returncode == 0:
        print("✓ No changes to commit")
        return True
    
    # Git commit
    today = datetime.now().strftime("%Y-%m-%d")
    result = subprocess.run(['git', 'commit', '-m', f"Update: Convert all data to bilingual format ({today})"], 
                          cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"✗ git commit failed: {result.stderr}")
        return False
    print(f"✓ Committed changes")
    
    # Git push
    result = subprocess.run(['git', 'push'], cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"✗ git push failed: {result.stderr}")
        return False
    print(f"✓ Pushed to remote")
    
    return True

def main():
    print("=" * 60)
    print("Converting existing data to bilingual format")
    print("=" * 60)
    print()
    
    # Find all JSON files
    json_files = sorted(DATA_DIR.glob("*.json"))
    if not json_files:
        print("No JSON files found!")
        return 1
    
    print(f"Found {len(json_files)} JSON files to process:\n")
    
    # Convert each JSON file
    for json_file in json_files:
        convert_json_to_bilingual(json_file)
    
    print()
    print("=" * 60)
    print("Rebuilding HTML pages")
    print("=" * 60)
    print()
    
    # Rebuild HTML pages
    for json_file in json_files:
        rebuild_html_page(json_file)
    
    print()
    print("=" * 60)
    print("Git operations")
    print("=" * 60)
    print()
    
    # Git push
    if git_push():
        print()
        print("=" * 60)
        print("✓ All done! Bilingual conversion complete.")
        print("=" * 60)
        return 0
    else:
        print()
        print("=" * 60)
        print("✗ Git operations failed")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    exit(main())
