---
title: Tutorials
template: pages.html
---

<div class="icon-def-1" style="text-align: center; border: 0.1rem dotted; width: 5%; float: right; padding: 0px; margin: 0px; font-size: 0.9rem; border-radius: 10px;">
  <a onclick="toggleAnimations()" title="Toggle Animations" style="cursor: pointer;">
    <p style="padding: 0px; margin: 0px;"><i class="mdi mdi-sine-wave"></i></p>
  </a>
</div>

# :material-robot-excited-outline:{ .icon-def-0 } Agents 

!!! tl-dr "TL;DR"
    Learn how to build your own `AI agents` :material-robot-outline:{ .icon-def-0 } and interact with them via easy to use web UIs. Dive into the tutorials below or keep scrolling to learn more :material-arrow-down-bold-outline:{ .icon-def-0 }.

<hr class="icon-def-1 tertiary-icon", style="width: 90%;"> 

<div class="grid cards" markdown>

-   :material-server:{ .icon-def-0 } Servers

    ---

    Setup the servers you need to power your agents.

    [:material-arrow-right-thin: Get started with servers][servers]

-   :material-robot-excited-outline:{ .icon-def-0 } Agents

    ---

    Create builds from simple chatbots to specialized agents.

    [:material-arrow-right-thin: Get started with agents][agents]

</div>

<hr class="icon-def-1 tertiary-icon", style="width: 90%;"> 

## :material-hammer-wrench:{ .icon-def-0 } What goes into building an AI agent?

An AI agent, first and foremost, needs a brain: a `language model` :material-head-cog-outline:{ .icon-def-0 }. These LMs are what allow our agents to reflect on what to do, make decisions, and generate responses. Without them, our agents wouldn't be able to take any actions :material-head-dots-horizontal-outline:{ .icon-def-0 }. 

However, LMs are built on static stores of knowledge. Their most recent information only goes up to a certain date :material-calendar-month-outline:{ .icon-def-0 }. Also, LMs are great at generating information :material-text-box-multiple-outline:{ .icon-def-0 }, but we may want our agents to be able to perform more specialized tasks :material-wizard-hat:{ .icon-def-0 }.

We can bypass these limitations by also giving our agents `tools` :material-hammer-wrench:{ .icon-def-0 } which will enhance both their knowledge store from which to retrieve and generate information :material-telescope:{ .icon-def-0 } as well as their ability to perform actions that uniquely fit our needs :material-rocket-launch-outline:{ .icon-def-0 }. 

<hr class="icon-def-1 primary-icon", style="width: 60%;"> 

<a id="how-power"></a>

## :material-generator-portable:{ .icon-def-0 } How will we power our agents?

<div class="grid cards" markdown style="text-align: center; font-size: 2rem; width: 22rem; margin: 0 auto;">

-   
    :simple-ollama:{ .icon-def-1 style="color: var(--md-accent-fg-color);" } :simple-searxng:{ .icon-def-1 style="color: var(--md-accent-fg-color);" } :simple-milvus:{ .icon-def-1 style="color: var(--md-accent-fg-color);" } :simple-docker:{ .icon-def-1 style="color: var(--md-accent-fg-color);" } :simple-langchain:{ .icon-def-1 style="color: var(--md-accent-fg-color);" } :simple-langgraph:{ .icon-def-1 style="color: var(--md-accent-fg-color);" } :simple-gradio:{ .icon-def-1 style="color: var(--md-accent-fg-color);" }

</div>

I like to host :material-server:{ .icon-def-0 } [local servers][servers] for the LMs and tools that my agents will need, then pass these servers over to the proper agents using :simple-langchain:{ .icon-def-0 } [LangChain][langchain]{.blank} and :simple-langgraph:{ .icon-def-0 } [LangGraph][langgraph]{.blank}. This method is highly customizable :material-palette:{ .icon-def-0 }. I can create different agents and give them the right tools for particular purposes (e.g. a coding assistant or a journal analyst) :material-wizard-hat:{ .icon-def-0 }. 

For the LMs and tools to pass to the agent, I chose solutions that were able to be :material-laptop:{ .icon-def-0 } `locally served` and were easy to setup and use. I also wanted to learn how to build tools that I would want to give to multiple types of agents :material-shape-plus:{ .icon-def-0 }. I found that the most useful tools for all my agent builds were those that enhanced the knowledge of the LM through either a `web search` or a `personal document search` :material-magnify:{ .icon-def-0 }. 

In the end, my favorite picks for the LM and tool servers are an :simple-ollama:{ .icon-def-0 } [Ollama][ollama]{.blank} server for the [LMs][ollama-tutorial], a :simple-searxng:{ .icon-def-0 } [SearXNG][searxng]{.blank} server for a [metasearch engine tool][searxng-tutorial] [^metasearch], and a :simple-milvus:{ .icon-def-0 } [Milvus][milvus]{.blank} server for a [data retrieval tool][milvus-tutorial] that can be used on my personal documents. We'll learn how to create and run each of these servers in turn :material-robot-excited-outline:{.icon-def-0}.

<hr class="icon-def-1 primary-icon", style="width: 60%;"> 

## :material-stairs:{ .icon-def-0 } What tutorials should we follow?

In the :material-server:{ .icon-def-0 } [servers series][servers], I discuss how to build each of our local servers with :simple-docker:{ .icon-def-0 } [Docker][docker]{.blank}. Then, in the :material-robot-excited-outline:{ .icon-def-0 } [agents tutorials][agents], I show how to pass these servers to our agents and implement :simple-gradio:{ .icon-def-0 } [Gradio][gradio]{.blank} web UIs to facilitate interactions. 

For each of the tutorials, there will be a :simple-github:{ .icon-def-0 } [Github repo][animakit] with :material-file-code-outline:{ .icon-def-0 } `all the source code included`, so you can check out any of the tutorials as standalone lessons. However, they do tend to build off of each other nicely :material-stairs:{ .icon-def-0 }.

I suggest starting with the :material-server:{ .icon-def-0 } [servers tutorials][servers] and working your way through to the :material-robot-excited-outline:{ .icon-def-0 } [agent examples][agents] after that. You can then check out more advanced techniques to get your agents to retrieve relevant information with the :material-bookshelf:{ .icon-def-0 } [RAG tutorials][rag]. While taking a break from any of these, you can also brush up your AI knowledge with the :material-shape-plus:{ .icon-def-0 } [fundamentals][odds-ends].

Check out any of the tutorials above to get started :material-arrow-up-bold-outline:{ .icon-def-0 }. You can also keep reading to see what software you may need or want in order to follow along :material-arrow-down-bold-outline:{ .icon-def-0 }.

<hr class="icon-def-1 primary-icon", style="width: 60%;"> 

## :material-checkbox-multiple-marked-outline:{ .icon-def-0 } What will we need?

For most tutorials, we'll be using :simple-python:{ .icon-def-0 } [Python][python]{.blank} and :simple-docker:{ .icon-def-0 } [Docker][docker]{.blank}. You can just simply install these tools and use them right away. To my knowledge, there shouldn't be any special setup that needs to be done for these :material-flash:{ .icon-def-0 }. 

You may also want something to view, edit, and manage code :material-file-code-outline:{ .icon-def-0 } as well as to execute commands in a :material-console:{ .icon-def-0 } CL. This isn't *strictly necessary*, but will be enormously helpful in following along with the tutorials and seeing for yourself what the code does :material-puzzle-check-outline:{ .icon-def-0 }. In my opinion, the GOAT is :simple-vscodium:{.icon-def-0} [VSCodium][vscodium]{.blank}. All the code management and execution in these tutorials can be performed with this software, no problem :material-creation-outline:{ .icon-def-0 }. 

I've also heard good things about :simple-neovim:{.icon-def-0} [NeoVim][neovim]{.blank} and :simple-pycharm:{ .icon-def-0 } [PyCharm][pycharm]{.blank}. If you don't mind Microsoft telemetry and licensing, you can also try the *Microsofted* version of VSCodium called [VSCode][vscode]{.blank}. 

---

All other third-party libraries, etc., that are needed to follow along will be explicitly covered in the tutorials :material-checkbox-marked-outline:{ .icon-def-0 }. 

<hr class="icon-def-1 primary-icon", style="width: 30%;"> 

I made these lessons so that they could be used by a wide variety of people; whether you want to just quickly take the code and use it without having to understand what it does :material-invoice-text-fast-outline:{ .icon-def-0 }, or you want to dive into the code and try to understand how it all works :material-wizard-hat:{ .icon-def-0 }, or you want something in between :material-head-cog-outline:{ .icon-def-0 }. As long as you have a desire to build :material-robot-excited-outline:{ .icon-def-0 } AI agents or the :material-server:{ .icon-def-0 } servers necessary to power these agents, or you just want to learn about AI :material-school-outline:{ .icon-def-0 }, these tutorials were made for you! :material-hand-heart:{ .icon-def-0 }  


<!-- FOOTNOTES -->
[^metasearch]: A metasearch engine takes a query, gets various web search results, performs some actions on the results like ranking them in order of relevancy :material-podium-silver:{ .icon-def-0 }, then outputs some information based on these results :material-newspaper-variant-multiple-outline:{ .icon-def-0 }. The :simple-searxng:{.icon-def-0} SearXNG server that we'll create takes our queries and searches the web through various engines, then outputs some final results. How these steps are performed will depend on how we setup our server in :simple-docker:{.icon-def-0} Docker. 


<!-- LINKS -->
[agents]: agents/index.md
[animakit]: https://github.com/anima-kit
[docker]: https://www.docker.com/
[gradio]: https://www.gradio.app/
[langchain]: https://www.langchain.com/
[langgraph]: https://www.langchain.com/langgraph/
[milvus]: https://milvus.io/
[milvus-tutorial]: servers/milvus.md
[neovim]: https://neovim.io/
[odds-ends]: ../../fundamentals/index.md
[ollama]: https://ollama.com/
[ollama-tutorial]: servers/ollama.md
[pycharm]: https://www.jetbrains.com/pycharm/
[python]: https://www.python.org/
[rag]: ../rag/index.md
[searxng]: https://github.com/searxng/searxng/
[searxng-tutorial]: servers/searxng.md
[servers]: servers/index.md
[vscode]: https://code.visualstudio.com/
[vscodium]: https://vscodium.com/