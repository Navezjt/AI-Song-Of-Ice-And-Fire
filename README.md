![AI Song of Ice and Fire Logo](./ai_song_of_ice_and_fire_logo.svg)

George R. R. Martin's popular series "A Song of Ice and Fire" completed with AI large language models.

*CAUTION: The materials folder contains SPOILERS for A Song of Ice and Fire!*

*Disclaimer: This is NOT meant to "replace" George R. R. Martin's work. It's an experiment to see how AI writes extensive texts. I respect writers, and am not trying to push the idea that AI can replace them.*

Self-imposed rules:
- No human writing other than the prompts, obviously.
- No paid tools.
- I am not allowed to read any of the books in A Song of Ice and Fire, as I would be able to unnaturally guide the generation.

Tools used:
- ChatGPT: Outline generation and expansion. Writing.
- ChatGPT to Markdown [chrome extension](https://chrome.google.com/webstore/detail/chatgpt-to-markdown/adghjpdmpbcmppeafpodcjpagmegdpci): Exporting chats and feeding them back in for outline expansion.
- Keyboard Maestro: automating the feeding of thousands of prompts into ChatGPT (free trial).


Here's a [demo](https://github.com/LiamSwayne/AI-song-of-ice-and-fire/assets/108629034/b6b4f455-62a6-4cb9-8029-afad2bb78a6e) of me using Keyboard Maestro to auto-prompt ChatGPT. The Keyboard Maestro program runs for all 2037 prompts. The program is also capable of using the "continue generating" button when it appears, but it isn't shown in this video. Outside of this demo the program has an 80 second minimum time between prompts so it doesn't breach the hourly generation limit for ChatGPT.

ChatGPT is keeping track of a massive web of characters over the course of the novel. For example, you can see in this screenshot that Illyrio phases in and out of the story, doesn't appear for hundreds of pages, but is still kept in the back of the mind of the AI for when he is needed:
<img width="1117" alt="Screen Shot 2023-06-18 at 3 17 19 PM" src="https://github.com/LiamSwayne/AI-song-of-ice-and-fire/assets/108629034/cf582ce7-b61a-4468-9c5f-63ba85781e4e">
