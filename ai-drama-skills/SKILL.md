# AI Drama Skills Pack

Muse-adapted routing pack from the Douyin post by @荔枝的AI折腾日常, "做AI漫剧，看这6个Skill" (2378 likes, 3424 saves in the screenshot).
Source post is a carousel, not a single repo. Three of the six slugs were verified on GitHub; two are flagged below as unverified, do not present them as verified repos.

Use when 帅东 wants an AI comic / short drama, including rest-time work on 《拾愿者》. Route by the step he is stuck on, not by running all six at once. Paid generation, account login and external upload always need his provider, assets and spending limit first.

1. Make a motion comic — make-motion-comic
   Source: ToBeWin/make-motion-comic (GitHub, low-cost motion comics: AI keyframes, Mandarin Edge TTS, anti-jitter FFmpeg rendering).
   Use: keyframes + dubbing,合成 video. For Muse: draft keyframe list and dubbing script first, then hand the render to a local tool / Codex with FFmpeg; Muse alone does not render the video.

2. Storyboard — drama-director
   Source: kianaliang-dev/drama-director-skill (GitHub, GPT Image 2 + Seedance 2.0 comic-drama workflow).
   Use: nine-panel storyboard, then a short sample. For Muse: output the nine panels with shot, action, camera, sound, and continuity notes before any generation.

3. Script review — no slug in the post, no repo verified
   Post description only: "内容负责人编制审稿，找开头、人物和逻辑问题".
   Use as a role, not a repo: check opening hook, character consistency, logic / rule consistency, and whether each episode's hook is answered next episode. For 《拾愿者》, also check its frozen rules: rewriting reality costs the memory most related to the wish, and key lines about cost and "记得" must not be changed to fit a prompt.

4. Full short drama — dramake
   Source: xixihhhh/ai-short-drama-skill (GitHub, "Dramake", for Codex / Claude Code / WorkBuddy: script, storyboard, Wan 3 / Seedance / MiniMax H3, dubbing, editing, QC, for Douyin / Hongguo short drama, vertical and horizontal).
   Use: end-to-end pipeline only when the user actually wants a full episode, not for a single test clip.

5. Write video prompts — byted-sol-seedance-prompt
   Post description only: "写清动作、运镜和声音". No matching GitHub repo was found for this exact slug, so do not cite it as a verified repo.
   Muse substitute already installed: seedance-director (custom-skills/seedance-director), based on Emily2040/seedance-2.0. Prompt formula to follow: subject + motion + environment + camera + aesthetics + audio, one primary camera move, named sounds, dialogue language named before the line. Seedance 2.0 numbers must not be restated for 2.5.

6. Manage a serial — phase-ai-anime-skill
   Source: gggwjuy/phase-ai-anime-skill (GitHub, small repo, no stars at check time).
   Use: save characters, assets and production progress across episodes. For Muse: keep that state in the project file, not in chat memory alone: character / armour reference, scene list, episode status, what failed before.

Order for 《拾愿者》 sample work: script review (3) -> storyboard (2) -> prompt (5) -> motion comic or full drama (1 or 4) -> serial management (6). Stop at the step the user asked for; do not run the whole pipeline unasked.
