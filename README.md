![AI Song of Ice and Fire Logo](./ai_song_of_ice_and_fire_logo.svg)

George R. R. Martin's popular series "A Song of Ice and Fire" completed with AI large language models.

*CAUTION: The materials folder contains SPOILERS for A Song of Ice and Fire.*

*Disclaimer: This is NOT an attempt to "replace" George R. R. Martin's work. It's an experiment to see how AI writes extensive texts. I respect writers, and am not trying to push the idea that AI can replace them.*

The final books can be viewed here:
- [The Winds of Winter](https://liamswayne.github.io/wow.html)
- [A Dream of Spring](https://liamswayne.github.io/dos.html)

Self-imposed rules:
- No human writing other than the prompts.
- No paid tools.
- No prior knowledge of the events that take place in books 1-5, which would enable unnaturally guided generation.

Tools used:
- ChatGPT: Outline generation and expansion. Writing.
- ChatGPT to Markdown [chrome extension](https://chrome.google.com/webstore/detail/chatgpt-to-markdown/adghjpdmpbcmppeafpodcjpagmegdpci): Exporting chats and feeding them back in for outline expansion.
- Keyboard Maestro: Automating the feeding of thousands of prompts into ChatGPT (free trial).

I recorded a [demo](https://github.com/LiamSwayne/AI-song-of-ice-and-fire/assets/108629034/b6b4f455-62a6-4cb9-8029-afad2bb78a6e) of Keyboard Maestro auto-prompting ChatGPT. The Keyboard Maestro program runs for all 2037 prompts. The program is also capable of using the "continue generating" button when it appears, but it isn't shown in this video. Outside of this demo the program has an 80 second minimum time between prompts so it doesn't breach the hourly generation limit for ChatGPT. This limit was later increased to 130 seconds as OpenAI decreased the maximum tokens per hour.

ChatGPT is capable of keeping track of a massive web of characters over the course of the novel. For example, you can see in this screenshot that Illyrio phases in and out of the story, doesn't appear for hundreds of pages, but is still kept in the back of the mind of the AI for when the character is needed:

<img width="600" alt="Screen Shot 2023-06-18 at 3 49 15 PM" src="https://github.com/LiamSwayne/AI-song-of-ice-and-fire/assets/108629034/21ad1d18-1cd8-4480-a650-1de278c82e3c">

Can the writing be detected as written by an AI? Sometimes. OpenAI's official AI detection software stated that the generated text was "very unlikely" to be written by an AI (tested on June 19, 2023).

<img width="600" alt="Screen Shot 2023-06-19 at 8 21 37 PM" src="https://github.com/LiamSwayne/AI-song-of-ice-and-fire/assets/108629034/ce527587-5f89-4ee3-8112-64e0f41d7518">

Draft 2 (the expansion of draft 1, which was itself an expansion of the outline) was so big that it was split into four chats. At some point OpenAI decided to start gradually decreasing the maximum length of chats. As a result, draft 2 was split into progressively shorter chat sessions. The four chats ([1](./materials/draft_2_chat_1.md), [2](./materials/draft_2_chat_2.md), [3](./materials/draft_2_chat_3.md), [4](./materials/draft_2_chat_4.md)) are accessible in the materials folder, as well as a [unified version](./materials/draft_2_temporary_unformatted.md) which contains the entire draft without the prompts.

One of the chats used in the third draft ran into an error message regarding the token limit that I haven't seen anywhere else:

<img width="600" alt="chatGPT_token_limit" src="https://github.com/LiamSwayne/AI-Song-Of-Ice-And-Fire/assets/108629034/fdcbcdde-fcad-48f6-9acb-75ec2cd31019">

Fully understanding this message would require knowledge of the inner workings of ChatGPT. The message preceding this error was not the longest message I gave to ChatGPT, and the chat it was sent through was far from the longest chat created for the project.

Some of the chats are so long that they crash ChatGPT when generating a shared link, but some of the shorter ones are listed below:
- https://chat.openai.com/share/81946f53-2231-454c-9a72-3cc56d0c7eed
- https://chat.openai.com/share/c78a1e31-c14f-4bdf-8bd2-0b0f422f6270
- https://chat.openai.com/share/140ac0fb-62ad-4304-8a80-5cddf6208665
