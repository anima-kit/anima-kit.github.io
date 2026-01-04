---
title: About
template: pages.html
hide:
  - navigation
  - toc
---

# :material-dna:{ .md-icon } About

---

!!! tl-dr "TL;DR"
    I like building AI projects and I want to learn more and contribute to the field :material-robot-excited-outline:{ .md-icon }. So, I'm distilling what I've been learning and packaging it for anyone that wants to learn with me :material-wizard-hat:{ .md-icon }.

## :material-robot-love-outline:{ .md-icon } What's anima-kit about?    

When I realized that I wanted to be a part of the AI field, I didn't really know anyone that was in it :material-head-dots-horizontal-outline:{ .md-icon } and my biggest assets in learning were online tutorials :material-search-web:{ .md-icon } :material-bookshelf:{ .md-icon }. Before that, I had been working to get my PhD in physics for the past several years and I was almost done with my thesis :material-school-outline:{ .md-icon }. I worked mostly on theoretical models of dark matter :material-telescope:{ .md-icon } :material-ghost-outline:{ .md-icon } which required nothing but something to write with :material-pencil-outline:{ .md-icon }, something to write on :material-note-outline:{ .md-icon }, and stamina :material-run:{ .md-icon }. Almost all calculations could be done without any help from a computer, which is to say, almost all functions of the theories I worked on could be solved exactly :material-equal:{ .md-icon }. 

However, there *were* some numerical calculations that could be done :material-desktop-classic:{ .md-icon }, specifically in regards to how certain theoretical, cosmological clouds form :material-cloud-question-outline:{ .md-icon }. With respect to this, the idea of a reinforcement learning project got floated around and even though it didn't pan out, it marked the beginning of my gravitation towards learning AI and towards learning how to create code in general :material-file-code-outline:{ .md-icon }. 

!!! memory-bubble "Memory"

    *Training an agent in a custom environment using the [A2C][a2c]{.blank} method with [Stable Baselines 3][stable-baselines]{.blank}*

Ah, very fond memories of these times :material-heart-outline:{ .md-icon }. It was one of the first that I had taken other people's code and tried to create something new with it :material-creation-outline:{ .md-icon }. I was starting to see how I could build some really cool things if I started to embrace this field. I wanted to get my hands dirty :material-hammer-wrench:{ .md-icon } and build something that I could use in my everyday life :material-account-hard-hat-outline:{ .md-icon }. The shock of AI, its sheer practicality and the promise of hours of entertainment struggling through debugs :material-bug-outline:{ .md-icon }, was so much that I haven't been able to take my eyes off it since :material-head-heart-outline:{ .md-icon }.

<hr class="primary-icon", style="width: 30%;"> 

Around this time, I started to notice that generative AI :material-generator-portable:{ .md-icon } had been popping up through open source models and libraries. I began playing around with [an early precursor][sd-early]{.blank} to the :material-image-multiple-outline:{ .md-icon } [Stable Diffusion][stability-ai]{.blank} models using :simple-huggingface:{ .md-icon } [Huggingface Diffusers][diffusers]{.blank}. I didn't have a viable :material-expansion-card-variant:{ .md-icon } GPU at the time so I was paying for Google GPUs, going through every tutorial I could find :material-bookshelf:{ .md-icon }. There was a community of people that were sharing their work, explaining how to use image generation models and how they worked :material-gift-outline:{ .md-icon }. 

I learned how to [fine-tune][fine-tune]{.blank} text-to-image models, how to create [LoRAs][lora]{.blank}, and how to generate images through different pipelines :material-pipe:{ .md-icon } for different outcomes :material-shape-plus:{ .md-icon }. I was burning up Google resources using [kohya-ss's SD scripts][sd-scripts]{.blank} and [automatic1111's SD web UI][sd-webui]{.blank} (a pioneer for one of my favorite tools, [ComfyUI][comfyui]{.blank}). It was so fun, and I was sure of one thing. I *really* wanted a GPU with lots of [VRAM][vram]{.blank} :material-head-heart-outline:{ .md-icon }.

Soon after, I started to play around with [text-generation models][models-text-gen]{.blank} (i.e. the designation for early LLMs [^multi-modal]) and I began to notice the existence of AI agent frameworks that utilized these models to power agents, such as [ChatDev][chatdev]{.blank} and [AutoGen][autogen]{.blank}. At the time, I could do some of the quickstart tutorials for these repos :material-checkbox-marked-outline:{ .md-icon }, but I couldn't get my agents to do anything very useful for me :material-robot-confused-outline:{ .md-icon }. It seemed they were either still in the early stages or I didn't understand how to use them. Either way, I felt something immense was on the precipice :material-volcano-outline:{ .md-icon } and I wanted to join in :material-crowd:{ .md-icon } and learn more :material-robot-excited-outline:{ .md-icon }.

!!! memory-bubble "Memory"
    *Scratch that. Life's throwing you something that requires your utmost presence and emotional stability. Better find your lodestone and better find it quick.*

Nothing quite like difficult life experiences to strengthen one's resolve, endurance, and faith in oneself :material-weight-lifter:{ .md-icon }. Throughout this experience, I couldn't dedicate very much time to the field and I started to lose touch :material-head-question-outline:{ .md-icon }. But, when I was able to put my feet back down on solid ground :material-sprout-outline:{ .md-icon } and come back to my learning, I found that AI agent frameworks had become quite good and were the marks in my sight :material-bullseye-arrow:{ .md-icon }. I could easily make the agents that I had been wanting to make since I realized frameworks like this existed :material-robot-love-outline:{ .md-icon }. 

I sure did find my lodestone during this time :material-magnet-on:{ .md-icon } :material-compass-outline:{ .md-icon } and trying to contribute to the field of AI is a part of it. So, [let's go][tutorials]! :material-rocket-launch-outline:{ .md-icon }   

---

## :material-flask-round-bottom:{ .md-icon } Why tutorials?

I'm not a developer (yet) :material-flag-triangle:{ .md-icon }. I didn't learn how to code in an organized, systematic way like in a classroom :material-school-outline:{ .md-icon }. I taught myself how through wanting to build things :material-robot-outline:{ .md-icon }, then searching the internet (or chatting with LLMs) for solutions :material-magnify:{ .md-icon }. 

When I first started learning how to code and how to use AI :material-sprout-outline:{ .md-icon }, it felt like starting to learn physics all over again. It's pretty difficult to understand what's going on when everyone uses words that you've never heard :material-head-question-outline:{ .md-icon }, and I'm all too familiar with how it feels to try to join a field that you're completely alien to :material-alien-outline:{ .md-icon } :material-ufo-outline:{ .md-icon }. 

First, it can be difficult to find good teachers :material-map-marker-question-outline:{.md-icon}, especially for technical concepts. Everyone's different in how they learn and it's a big challenge to tailor lessons to fit lots of various learners :material-head-question-outline:{ .md-icon }  [^personal-ai]. To top off the mounting difficulties of learning a new field and trying to find good teachers :material-image-filter-hdr-outline:{ .md-icon }, the field of AI is so vast and moves so ridiculously fast :material-rocket-launch-outline:{ .md-icon }. There's always a new app, or repo, or technique and everyone's using something different :material-shape-plus:{ .md-icon }. At some point, I almost gave up on trying to join the field because it's so daunting :material-emoticon-dead-outline:{ .md-icon }. I felt like, how could I ever actually keep up?

But, what helped me (and still helps me) is trying to take it all one step at a time :material-stairs:{.md-icon}, one unknown word :material-puzzle-outline:{ .md-icon }, one bug :material-bug-outline:{.md-icon}, one demo :material-laptop:{.md-icon} at a time. As I started to learn more, I became more confident and just couldn't keep away. It's too fun, it's too useful. The thrill in learning and building something is too powerful :material-volcano-outline:{ .md-icon }.

It also helps that I've learned a thing or two about *how to learn* from the teachers that took the time to not only try to teach the subject material, but how to learn it :material-creation-outline:{ .md-icon }. These rare :material-clover-outline:{ .md-icon } individuals and organizations that try to make learning accessible are greatly appreciated and they inspire me to follow in their footsteps :material-hiking:{ .md-icon }. I'm not sure that I'm a very good teacher for this subject material yet. But I do love it :material-heart-outline:{ .md-icon } and the more I teach others, the more I distill my own knowledge :material-flask-round-bottom:{ .md-icon }. 

<hr class="primary-icon", style="width: 30%;"> 

Now, my learning technique for this subject material has been to figure out how to build something :material-magnify:{ .md-icon }, get it to work :material-hammer-wrench:{ .md-icon }, then dive into the code to understand it better :material-diving-scuba:{ .md-icon }. I've learned a lot this way, by trying to understand and build on other people's code :material-robot-happy-outline:{ .md-icon } :material-wizard-hat:{ .md-icon }. But, when I started cleaning all the projects that I had accumulated over my course of learning :material-monitor-shimmer:{ .md-icon }, I realized *how confused I still was* :material-head-question-outline:{ .md-icon }. So, I started making tutorials with an audience of non-experts in mind :material-crowd:{ .md-icon }. Because that's what I am, a non-expert trying to learn the field :material-puzzle-outline:{ .md-icon }, and it was *definitely* what I was when I started learning and needed the tutorials of others to get a jump start :material-hand-heart:{ .md-icon }.

---

## :material-gift-open-outline:{ .md-icon } What are the tutorials like?

I've structured my tutorials similarly to the way that I originally learned the material. Show how to get something to work :material-monitor-shimmer:{ .md-icon }, then show why it does :material-file-code-outline:{ .md-icon }. This way, if anyone wants to just take the code and get it working without learning anything about it :material-invoice-text-fast-outline:{ .md-icon }, they can. Whoever wants to dive into how the code works afterwards can then follow along with the rest of the tutorial :material-book-open-variant-outline:{ .md-icon }. 

It's probably pretty obvious by now that I like to use code that I can open up to check out the gears if I need to :material-cog-outline:{ .md-icon }. So, much of the code that we'll use from other libraries will be available to view in all their full glory on :simple-github:{ .md-icon } [Github][github]{.blank}. I also like to use libraries and platforms that are free to use :material-currency-usd-off:{ .md-icon }. No need for a paywall. Just plug into your code and play :material-controller-classic-outline:{ .md-icon }. 

<hr class="primary-icon", style="width: 30%;"> 

I originally set out to create these tutorials so that I would better understand the subject material :material-head-sync-outline:{ .md-icon } and gain the necessary skills to create clean and easily digestible, yet highly complex, AI projects :material-robot-love-outline:{ .md-icon }. But, through teaching myself I now feel compelled to teach others :material-bookshelf:{ .md-icon }. 

These projects :material-file-code-outline:{ .md-icon }, these tutorials :material-bookshelf:{ .md-icon }, are proof that someone with very limited knowledge of AI and coding can learn the field enough to build something for themselves and others :material-robot-excited-outline:{ .md-icon }. It seems that it's never been easier for any given human to learn any given subject than it is in our day and age :material-wizard-hat:{ .md-icon }. A ridiculous amount of information is at our fingertips in a moment's notice :material-flash:{ .md-icon }. To distill it into something useful :material-flask-round-bottom:{ .md-icon }, we just need curiosity, enduring effort, and proper aim :material-bullseye-arrow:{ .md-icon }.

So, if you want to [learn about AI][tutorials] :material-head-cog-outline:{ .md-icon }, here's my knowledge! :material-hand-heart:{ .md-icon }

<!-- FOOTNOTES -->
[^multi-modal]: Nowadays, LLMs are becoming increasingly [multi-modal][multi-modal]{.blank} and aren't prohibited to only generating text, or even taking text as an input for that matter :material-multimedia:{ .md-icon }. These [any-to-any][models-any-to-any]{.blank} models can take in other forms of information and generate through other mediums like audio :material-music-note:{ .md-icon } and images :material-image:{ .md-icon }. At some point, I want to learn how to use these models for agentic purposes, and I'll most likely feel compelled to create tutorials in order to distill my learning :material-wizard-hat:{ .md-icon } :material-flask-round-bottom:{ .md-icon }.

[^personal-ai]: But AI can help! One great thing about LLMs is that they can be used to create highly personalized tutors :material-cast-education:{ .md-icon }. 

<!-- LINKS -->
[a2c]: https://arxiv.org/pdf/1602.01783
[agents]: tutorials/applications/agents/agents/index.md
[animakit]: https://github.com/anima-kit
[autogen]: https://github.com/microsoft/autogen
[chatdev]: https://github.com/OpenBMB/ChatDev
[comfyui]: https://www.comfy.org/
[diffusers]: https://huggingface.co/docs/diffusers/en/index
[fine-tune]: https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)
[github]: https://github.com/
[langchain]: https://www.langchain.com/
[langgraph]: https://www.langchain.com/langgraph
[lora]: https://huggingface.co/docs/diffusers/en/training/lora
[models-any-to-any]: https://huggingface.co/models?pipeline_tag=any-to-any&sort=trending
[models-text-gen]: https://huggingface.co/models?pipeline_tag=text-generation&sort=trending
[multi-modal]: https://en.wikipedia.org/wiki/Multimodal_learning
[sd-early]: https://huggingface.co/blog/stable_diffusion
[sd-scripts]: https://github.com/kohya-ss/sd-scripts
[sd-webui]: https://github.com/AUTOMATIC1111/stable-diffusion-webui
[stable-baselines]: https://stable-baselines3.readthedocs.io/en/master/
[stability-ai]: https://huggingface.co/stabilityai/collections
[tutorials]: tutorials/index.md
[vram]: https://en.wikipedia.org/wiki/Video_random-access_memory