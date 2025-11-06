---
title: Agents
template: pages.html
---

<div class="icon-def-1" style="text-align: center; border: 0.1rem dotted; width: 5%; float: right; padding: 0px; margin: 0px; font-size: 0.9rem; border-radius: 10px;">
  <a onclick="toggleAnimations()" title="Toggle Animations" style="cursor: pointer;">
    <p style="padding: 0px; margin: 0px;"><i class="mdi mdi-sine-wave"></i></p>
  </a>
</div>

# :material-robot-excited-outline:{ .icon-def-0 } Agents

!!! tl-dr "TL;DR"
    Learn how to create different chatbot and agent builds :material-robot-outline:{ .icon-def-0 } as well as easy to use web UIs to facilitate interactions :material-monitor-shimmer:{.icon-def-0}. Dive into the tutorials below to check them out, or keep scrolling to learn more :material-arrow-down-bold-outline:{ .icon-def-0 }.

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 90%; margin: 0 auto;"> 

<div class="grid cards" markdown>

-   :material-chat-processing-outline:{ .icon-def-0 } Chatbot

    ---

    Create a simple chatbot without any memory.

    [:material-arrow-right-thin: Get started building a chatbot][chatbot]

-   :material-memory:{ .icon-def-0 } Agent with Memory

    ---

    Create an agent with awareness of past conversation history.

    [:material-arrow-right-thin: Get started building an agent with memory][agent-memory]

-   :material-bookshelf:{ .icon-def-0 } Document Agent

    ---

    Give your agent a tool to retrieve info from your personal docs.

    [:material-arrow-right-thin: Get started building a doc agent][doc-agent]

-   :material-file-code-outline:{ .icon-def-0 } Code Agent

    ---

    Tweak your agent build so that it's specialized to help with your coding needs

    [:material-arrow-right-thin: Get started building a code agent][code-agent]

</div>

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 90%; margin: 0 auto;"> 

## :material-flask-round-bottom:{ .icon-def-0 } What will we create?

[Remember where we started][servers]. We created all these local servers that house latent potential :material-volcano-outline:{ .icon-def-0 } to do some crucial work for our agents. Now, we can start passing them over to see how they fit :material-puzzle-outline:{ .icon-def-0 } and what we can make with them (turns out some really fun, interesting, and useful AI assistants :material-robot-love-outline:{ .icon-def-0 }). 

<h4 style="text-align: center;">Chatbot</h4>

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 30%; margin: 0 auto;"> 

First is the :material-chat-processing-outline:{ .icon-def-0 } [chatbot](chatbot.md) without any memory or tools. This will be the local :simple-ollama:{ .icon-def-0 } [Ollama][ollama]{.blank} server that [we created][ollama-tutorial] in :simple-docker:{ .icon-def-0 } [Docker][docker]{.blank} connected to a chat model in :simple-langchain:{ .icon-def-0 } [LangChain][langchain]{.blank} and all packaged up in an easy to interact with :simple-gradio:{ .icon-def-0 } [Gradio][gradio]{.blank} web UI. 

This one will be a blank slate, it'll have no recollection of any conversation history :material-robot-confused-outline:{ .icon-def-0 }. This kind of assistant is impractical, but it does serve as a good learning opportunity :material-wizard-hat:{.icon-def-0} for how to use an Ollama server with LangChain and display the results in a user friendly manner with Gradio :material-tag-faces:{ .icon-def-0 }. 

<h4 style="text-align: center;">Agent with Memory</h4>

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 30%; margin: 0 auto;"> 

Next is the :material-memory:{ .icon-def-0 } [agent with memory][agent-memory]. This will be the same as the :material-chat-processing-outline:{ .icon-def-0 } [chatbot][chatbot], but instead of a chat model in LangChain, we're going to use an agent in :simple-langgraph:{ .icon-def-0 } [LangGraph][langgraph]{.blank}. Also, we're going to give our agent *memory* so that it'll have access to our conversation history :material-clipboard-text-clock-outline:{ .icon-def-0 }. This is much more practical and is going to serve as a clean base for all of our more advanced agent builds :material-monitor-shimmer:{ .icon-def-0 }. 

We're also going to package this one up in a Gradio web UI but this time we'll add more functionality to accomodate our more complex agent :material-robot-excited-outline:{ .icon-def-0 }. Specifically, we'll see how to setup individual chat threads that can be managed and selected, so that we can easily have different conversation topics stored and ready for future use :material-cards-outline:{ .icon-def-0 }. Finally, we'll learn tricks to building code that runs faster and more efficiently :material-flash:{ .icon-def-0 }.

<h4 style="text-align: center;">Document Agent</h4>

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 30%; margin: 0 auto;"> 

This is where we'll learn how to pass our agents tools and what it looks like when our agents use them: the :material-bookshelf:{ .icon-def-0 } [doc agent](doc-agent.md). This will be the :material-memory:{ .icon-def-0 } [agent with memory][agent-memory] equipped with a tool that can be used to query a :simple-milvus:{ .icon-def-0 } [Milvus][milvus]{.blank} vectorstore [that we created][milvus-tutorial] in Docker. We'll use our Gradio web UI to upload :simple-markdown:{ .icon-def-0 } [Markdown][markdown]{.blank} documents that we want to be analyzed :material-upload-outline:{ .icon-def-0 }, then interact with our agent to gain information about them :material-book-open-outline:{ .icon-def-0 }. 

We'll see that in order to use the Milvus vectorstore :material-bookshelf:{ .icon-def-0 }, we'll need `embedding` models that are used to create special representations for our data :material-vector-polygon:{ .icon-def-0 } to be utilized when searching our data for a particular query :material-magnify:{ .icon-def-0 }. We can serve these embedding models with the same :simple-ollama:{ .icon-def-0 } [Ollama server][ollama-tutorial] that we built. Just as when we created the :material-chat-processing-outline:{ .icon-def-0 } [chatbot][chatbot], we can connect this server to a LangChain object which can then easily be passed to our agent for proper use :material-flash:{ .icon-def-0 }.

We'll also add functionality to our web UI so that we can upload and manage all the documents that we'll want to analyze :material-file-document-multiple-outline:{ .icon-def-0 } and we'll learn how to split our documents and store them as chunks :material-cube-unfolded:{ .icon-def-0 } so that cleaner and more relevant information is passed to our agents :material-robot-love-outline:{ .icon-def-0 }. 

Remember when we :simple-milvus:{ .icon-def-0 } [created the Milvus server][milvus-tutorial]? To demonstrate how to use a vectorstore, we performed a *full-text* search in which we scanned our documents for particular keywords :material-key-chain:{ .icon-def-0 }. In this tutorial, the document search tool that we'll pass to our agents will utilize a [more advanced search][hybrid-search]{.blank} that will allow for more nuanced relationships in the data to be captured :material-molecule:{ .icon-def-0 }, which means our agents will give us more informed results :material-notebook-edit-outline:{ .icon-def-0 }.

<h4 style="text-align: center;">Code Agent</h4>

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 30%; margin: 0 auto;"> 

Finally, in the last tutorial of the series, we're going to use LangChain to create a metasearch tool using the :simple-searxng:{ .icon-def-0 } [SearXNG][searxng]{.blank} server that [we created][searxng-tutorial] in Docker and pass this tool over to our :material-bookshelf:{ .icon-def-0 } [doc agent][doc-agent]. We're then going to tweak the agent and tool settings a bit :material-cog-outline:{ .icon-def-0 } to get specialized :material-file-code-outline:{ .icon-def-0 } [coding agents][code-agent]. 

We'll interact with our agents through our familar web UI, but we'll also add functionality to mananage different projects :material-cards-outline:{ .icon-def-0 }. Finally, we'll learn how to split Python documents into easier to digest chunks :material-cube-unfolded:{ .icon-def-0 } just as we did with Markdown documents in the [doc agent][doc-agent] tutorial.

This agent will not only serve as a workable tool to help you code in :simple-python:{ .icon-def-0 } Python, but also as an example for how to build different types of specialized agents; like a job search agent :material-briefcase-outline:{ .icon-def-0 }, or a global news analyst :material-newspaper-variant-multiple-outline:{ .icon-def-0 }, or a personal journal assistant :material-notebook-edit-outline:{ .icon-def-0 }. 

<hr class="icon-def-1", style="border-top: 0.2rem dotted; border-bottom: transparent; width: 30%; margin: 0 auto;"> 

After finishing these tutorials, we'll know how to create whatever specialized agents we like :material-robot-love-outline:{ .icon-def-0 }, as long as we can pass the proper tools and tweak the agent and tool settings to become more specialized. We'll have :simple-github:{ .icon-def-0 } [all the code available][animakit] so that it really is just that easy :material-flash:{ .icon-def-0 }!

Check out any of the tutorials above to get started :material-arrow-up-bold-outline:{ .icon-def-0 }, or get a refresher on how to create all the necessary servers to power our agents in the :material-server:{ .icon-def-0 } [servers tutorials][servers]. If you want to learn techniques for improving the information retrieval of your agents, check out the :material-bookshelf:{ .icon-def-0 } [RAG tutorials][rag]. 


<!-- LINKS -->
[agent-memory]: agent-memory.md
[animakit]: https://github.com/anima-kit
[chatbot]: chatbot.md
[code-agent]: code-agent.md
[doc-agent]: doc-agent.md
[docker]: https://www.docker.com/
[gradio]: https://www.gradio.app/
[hybrid-search]: https://milvus.io/docs/multi-vector-search.md
[langchain]: https://www.langchain.com/
[langgraph]: https://www.langchain.com/langgraph/
[markdown]: https://www.markdownguide.org/
[milvus]: https://milvus.io/
[milvus-tutorial]: ../servers/milvus.md
[ollama]: https://ollama.com/
[ollama-tutorial]: ../servers/ollama.md
[rag]: ../rag/index.md
[searxng]: https://github.com/searxng/searxng/
[searxng-tutorial]: ../servers/searxng.md
[servers]: ../servers/index.md