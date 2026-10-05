<img src="./assets/hero.svg" alt="Maitry Parikh — Software Engineer and Product Builder. I turn messy product problems into simple, reliable software." width="100%">

<p align="center">
  <sub><b><a href="#work">WORK</a></b> &nbsp;&nbsp;/&nbsp;&nbsp; <b><a href="#thinking">THINKING</a></b> &nbsp;&nbsp;/&nbsp;&nbsp; <b><a href="#stack">STACK</a></b> &nbsp;&nbsp;/&nbsp;&nbsp; <b><a href="#contact">CONTACT</a></b></sub>
</p>

## Work

‼️Three projects. If you only open one: <b>02 — RunBait</b>.

<br>

<img src="./assets/noodle.svg" alt="Noodle architecture: User, Flutter, WebSocket, FastAPI, Gemini and TTS, Response, Discard." width="100%">

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <b>❓WHAT IT IS</b><br><br>
      A voice companion with opinions and zero memory. You talk, it answers back (sarcastically), and the exchange is gone. Flutter handles the real-time voice UX; a FastAPI service streams each turn over WebSockets to Gemini and TTS.
    </td>
    <td width="50%" valign="top">
      <b>THE INTERESTING CONSTRAINT</b><br><br>
      No conversation history, by design. The privacy requirement became the architecture: a stateless request path where audio and text exist only for the length of a turn.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <sub><b>STACK</b></sub> &nbsp; <code>Flutter</code> <code>Riverpod</code> <code>GoRouter</code> <code>Hive</code> <code>FastAPI</code> <code>WebSockets</code> <code>Gemini</code> <code>Docker</code>
      &nbsp;&nbsp;·&nbsp;&nbsp; <a href="https://github.com/maitry4/noodle"><b>SOURCE ↗</b></a>
    </td>
  </tr>
</table>

<br>

<img src="./assets/runbait.svg" alt="RunBait pipeline: PR diff, understand repo, affected journeys, generate flows, run in Playwright, capture evidence, AI evaluates, structured verdict." width="100%">

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <b>❓WHAT IT IS</b><br><br>
      A PR QA agent that tests the change, not the whole codebase. It reads the diff, works out which user journeys are affected, writes targeted browser flows, runs them in Playwright, and judges the captured evidence.
    </td>
    <td width="50%" valign="top">
      <b>THE INTERESTING CONSTRAINT</b><br><br>
      Never let the model grade its own guess.<br>
      <b>AI decides what to test. The browser determines what happened. Evidence determines the verdict.</b>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <sub><b>PROOF</b></sub> &nbsp; Run against a fork of Razorpay's open-source website, it caught a runtime issue in the changed feature.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <sub><b>STACK</b></sub> &nbsp; <code>Next.js</code> <code>React</code> <code>Tailwind</code> <code>FastAPI</code> <code>Supabase / Postgres</code> <code>GitHub OAuth</code> <code>GitHub Actions</code> <code>Playwright</code> <code>Cloudflare AI</code> <code>Pydantic</code>
      &nbsp;&nbsp;·&nbsp;&nbsp; <a href="https://github.com/maitry4/runbait"><b>SOURCE ↗</b></a>
    </td>
  </tr>
</table>

<br>

<img src="./assets/layered.svg" alt="Layered: Presentation, Domain, Data architecture and a four-step level generator that avoids an expensive solver." width="100%">

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <b>❓WHAT IT IS</b><br><br>
      A fully offline, cross-platform Flutter puzzle game with 100 levels, built on a strict Presentation → Domain → Data split.
    </td>
    <td width="50%" valign="top">
      <b>THE INTERESTING CONSTRAINT</b><br><br>
      Good levels, generated cheaply. Instead of running an expensive solver on every candidate, the generator combines controlled scrambling, valid-move constraints, deadlock detection and homogeneity scoring.
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <sub><b>STACK</b></sub> &nbsp; <code>Flutter</code> <code>Dart</code> <code>BLoC / Cubit</code> <code>Hive</code> <code>Firebase Analytics</code>
      &nbsp;&nbsp;·&nbsp;&nbsp; <a href="https://github.com/maitry4/layered"><b>SOURCE ↗</b></a>
    </td>
  </tr>
</table>

## Thinking

<img src="./assets/thinking.svg" alt="How I work: problem, simplify, find the constraint, design the system, ship, observe, iterate." width="100%">

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <sub><b>01 — SIMPLE UX</b></sub><br>
      Complexity should live underneath the product.
    </td>
    <td width="50%" valign="top">
      <sub><b>02 — CONSTRAINT FIRST</b></sub><br>
      Cost, latency, reliability and privacy shape architecture.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><b>03 — EVIDENCE OVER ASSUMPTIONS</b></sub><br>
      If something matters, measure it or observe it.
    </td>
    <td width="50%" valign="top">
      <sub><b>04 — SHIP</b></sub><br>
      A technically beautiful system nobody uses is still unfinished.
    </td>
  </tr>
</table>

## Stack

<sub>Grouped by the problem they solve, not by logo.</sub>

<table width="100%">
  <tr>
    <td width="130" valign="top"><sub><b>BACKEND</b></sub></td>
    <td><code>Python</code> <code>FastAPI</code> <code>PostgreSQL</code> <code>SQLite</code> <code>REST</code> <code>WebSockets</code></td>
  </tr>
  <tr>
    <td valign="top"><sub><b>MOBILE</b></sub></td>
    <td><code>Flutter</code> <code>Dart</code> <code>Android</code> <code>JNI</code> <code>C++</code> <code>BLE</code> <code>Offline-first</code></td>
  </tr>
  <tr>
    <td valign="top"><sub><b>AI / SYSTEMS</b></sub></td>
    <td><code>LLMs</code> <code>On-device AI</code> <code>Playwright</code> <code>GitHub Actions</code> <code>AI orchestration</code></td>
  </tr>
  <tr>
    <td valign="top"><sub><b>PRODUCT</b></sub></td>
    <td><code>UX thinking</code> <code>Prototyping</code> <code>Performance</code> <code>System design</code></td>
  </tr>
</table>

## Contact

<p align="center">
  <a href="https://www.linkedin.com/in/maitry4"><code>LinkedIn</code></a>
  &nbsp;
  <a href="https://github.com/maitry4"><code>GitHub</code></a>
  &nbsp;
  <a href="mailto:maitryparikh23@gmail.com"><code>Email</code></a>
</p>

