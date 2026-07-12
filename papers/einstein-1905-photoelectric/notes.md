# Einstein (1905) — "On a Heuristic Point of View about the Creation and Conversion of Light"

> Source: A. Einstein, *Annalen der Physik* **17**, 132–148 (1905). Received
> 18 March 1905. German title: *Über einen die Erzeugung und Verwandlung des
> Lichtes betreffenden heuristischen Gesichtspunkt*.
> English text followed here: the Arons–Peppard translation, *Am. J. Phys.*
> **33**, 367 (1965) — "Concerning an Heuristic Point of View Toward the
> Emission and Transformation of Light" — a copy of which is kept in
> [`source/`](source/). The
> [Wikisource translation](https://en.wikisource.org/wiki/Translation:On_a_Heuristic_Point_of_View_about_the_Creation_and_Conversion_of_Light)
> is a freely readable alternative with slightly different wording.
> Companion reading for Greiner ch. 1
> ([notes](../../text/ch01-quantization-of-physical-quantities/notes.md), §1.1
> on the photoelectric effect) and ch. 2
> ([notes](../../text/ch02-radiation-laws/notes.md), the radiation laws).

These notes walk through the paper **section by section**, in the order you
will meet the material on the page. Each section gets: what Einstein is doing
and *why he is doing it there*, the argument unpacked with the skipped algebra
filled in, the common sticking points, and a "with modern eyes" gloss for a
technical (but non-physicist) reader. Equation labels like (4.5) are mine —
the original numbers almost nothing — and Einstein's own notation is kept
throughout (see the [notation dictionary](#notation-dictionary) below).

---

## 0. How to read this paper — a roadmap

**It is not really "the photoelectric paper."** The photoelectric effect
occupies about a page and a half near the end (§8 of 9). Calling it the
photoelectric paper is like calling *Moby-Dick* a book about a boat. What the
paper actually argues is far more radical: that **light itself, while it flies
through empty space, behaves as a collection of discrete, indivisible packets
of energy** — what we now call photons. The photoelectric effect is one of
three quick experimental applications bolted on at the end as evidence.

**The architecture.** The paper is a single sustained argument with three
movements:

| § | Topic (abridged heading) | Role in the argument |
|---|---|---|
| Intro | The manifesto | States the hypothesis and its scope |
| 1 | A difficulty in black-body radiation theory | Classical physics, taken seriously, *forces* a radiation law that is catastrophically wrong |
| 2 | Planck's determination of the elementary quanta | Salvage operation: which parts of Planck's work can still be trusted, and why |
| 3 | The entropy of radiation | Builds the tool: an entropy function for radiation out of equilibrium |
| 4 | Entropy of dilute monochromatic radiation | The tool applied: that entropy depends on volume exactly like an ideal gas's |
| 5 | Entropy and volume for gases and dilute solutions | Boltzmann's principle: the logarithmic volume law *counts independent particles* |
| 6 | Interpretation via Boltzmann's principle | The punchline: dilute radiation behaves as n independent quanta of energy each equal to Rβν/N |
| 7 | Stokes' rule | Application 1: photoluminescence |
| 8 | Cathode rays from illuminated solids | Application 2: the photoelectric effect — the famous equation |
| 9 | Ionisation of gases by ultraviolet light | Application 3: photo-ionisation and a quantitative bound |

The engine of the paper is §§3–6, and it is pure **thermodynamics plus
statistics**: no model of atoms, no model of how light interacts with matter,
just the measured black-body spectrum and Boltzmann's link between entropy and
probability. That is Einstein's signature move (his 1902–1904 papers had been
exactly about the statistical foundations of thermodynamics), and it is why
the paper spends four sections on entropy before saying a word about
experiments.

**Why "heuristic"?** The word in the title is a hedge and a precision
instrument at once. Einstein does not claim to *derive* light quanta from a
deeper theory, and he knows perfectly well that the wave theory explains
interference and diffraction magnificently. A "heuristic point of view" is a
working picture: adopt it, see what it predicts, judge it by its fruits. The
paper never explains how quanta reconcile with interference — that tension
stayed open for twenty years and became wave–particle duality. Einstein knew
exactly how big a bomb he was tossing: in a May 1905 letter to his friend
Conrad Habicht he called this paper — not special relativity! — "very
revolutionary" (*sehr revolutionär*). It was the only one of his 1905 papers
he described that way, and it was the last major claim of his to be accepted
(essentially not until the Compton effect, 1923).

**Title translation note.** You will see the title rendered variously:
"emission and transformation of light" (Arons–Peppard — the AJP translation
in `source/`), "creation and conversion of light" (Wikisource), "production
and transformation of light" (ter Haar). Same German words (*Erzeugung und
Verwandlung*). The choice of words matters for reading the
paper: Einstein's hypothesis is explicitly about how light is **emitted,
absorbed, and transformed** — not, or at least not necessarily, about how it
propagates. Keep that in mind; it is stated carefully in the introduction and
is the paper's escape hatch from the interference objection.

---

## 0.1 The stage in 1905 — what every reader already knew

To feel the force of the paper you need the 1905 background it assumes.

**Light was settled science.** Maxwell's electromagnetic theory (1860s),
confirmed spectacularly by Hertz's generation of radio waves (1887), had ended
the centuries-old particle-vs-wave debate in favor of waves. Interference,
diffraction, polarization, reflection — everything optical was quantitatively
explained by continuous electromagnetic fields. Proposing granular light in
1905 was roughly as contrarian as proposing today that energy conservation
fails.

**Black-body radiation was the hot problem.** A cavity held at temperature
$T$ fills with radiation whose spectrum — how much energy sits at each
frequency — is, by a classic argument of Kirchhoff (1859), a **universal
function** of frequency and temperature only, independent of the cavity's
material. Universal functions smell like fundamental physics, so measuring
and deriving this spectrum became a flagship program, driven by superb
measurements at the Physikalisch-Technische Reichsanstalt in Berlin
(Lummer–Pringsheim, Rubens–Kurlbaum). Wien's law (1896) fit the
high-frequency data; by 1900 the measurements had pushed to lower frequencies
(longer wavelengths) and Wien's law visibly failed there. In October 1900
Planck produced an interpolation formula — Planck's law — that fit everything,
and in December 1900 he manufactured a derivation for it. The derivation
required a strange bookkeeping step: the material oscillators in the cavity
walls could apparently only take up energy in chunks of size $h\nu$. Planck
regarded this as a formal device concerning **matter** — he emphatically did
*not* claim the free radiation field is grainy, and he resisted that idea for
another decade. (Greiner ch. 2 covers all of this; see §2.3–2.5 of the
[ch. 2 notes](../../text/ch02-radiation-laws/notes.md).)

**The photoelectric effect was a fresh anomaly.** Hertz noticed in 1887 —
ironically, during the very experiments confirming Maxwell — that ultraviolet
light helps a spark gap fire. By 1899–1902 it was established (J.J. Thomson,
Lenard) that UV light knocks **electrons** out of metal surfaces, and Philipp
Lenard's careful 1902 study found something baffling: the *energy* of the
ejected electrons does not depend on the light's intensity at all — only on
its color — while the *number* of electrons tracks the intensity. On the wave
picture, a brighter wave carries more energy and should eject faster
electrons. It doesn't.

**Atoms themselves were still contested.** Influential physicists and
chemists (Mach, Ostwald and the "energetics" school) regarded atoms as a
convenient fiction. Avogadro's number $N$ — the count of molecules in a mole
— was the battleground constant: every independent measurement of $N$ that
agreed with the others was evidence that matter really is made of countable
units. Watch how often $N$ appears in this paper: Einstein keeps writing the
quantum of energy as $(R/N)\beta\nu$ instead of inventing new constants,
deliberately keeping the molecular constant $N$ front and center. (His
dissertation and the Brownian-motion paper, both also 1905, were direct
attacks on the same question.)

**Einstein's own position:** 26 years old, examining patents in Bern, outside
academia, with three prior publications (1902–04) on the statistical
mechanics of heat — from which he had independently rebuilt much of Gibbs'
and Boltzmann's machinery. Those papers are the toolkit this one runs on.

---

## Notation dictionary

Einstein's notation predates the modern conventions; nothing here is hard,
but a translation table saves constant friction. Planck's constant $h$
**never appears in the paper** — Einstein works with the empirical constants
$\alpha$ and β from the radiation law and with the gas constants $R$ and $N$.

| Symbol in the paper | Modern equivalent | Meaning |
|---|---|---|
| $R$ | $R$ | universal gas constant, about 8.31 J per mol per K |
| $N$ | $N_A$ | Avogadro's number; Einstein's value 6.17e23, modern 6.022e23 |
| $R/N$ | $k_B$ | Boltzmann's constant: gas constant per single molecule |
| $L$ | $c$ | speed of light |
| $\rho$ or $\rho_\nu$ | $u(\nu,T)$ | spectral energy density of radiation: energy per volume per frequency interval |
| $\alpha$ | $8\pi h/c^3$ | prefactor in Wien's and Planck's laws |
| β | $h/k_B$ | constant in the exponential; Einstein quotes 4.866e-11 s K, modern value 4.799e-11 s K |
| $(R/N)\beta\nu$ | $h\nu$ | **the energy quantum** — check: $k_B \cdot (h/k_B)\cdot\nu = h\nu$ |
| $E$ | $E$ | total energy of the radiation being considered |
| $S$, $\varphi$ | $S$, $s(\nu)$ | entropy; entropy per unit volume per unit frequency |
| $W$ | $W$ | "probability" of a state in Boltzmann's principle (a relative statistical weight) |
| $\Pi$ | $V_s$ | stopping potential in the photoelectric section |
| $\varepsilon$ | $e$ | elementary charge |
| $P$, $P'$ | $W_0$ | escape work, today called the work function; $P$ is per electron, and $P'$ is the same quantity per gram-equivalent of electrons, expressed as a potential |

Keep the one identity $(R/N)\beta\nu = h\nu$ in your pocket; it converts every
formula in the paper to its textbook form instantly.

Three further trip-hazards of the paper's notation:

- Volumes are written lowercase, $v$ and $v_0$; these notes use $V$ and $V_0$.
- The bar in §1's average energy refers to **one linear component** of a
  three-dimensional oscillator (Einstein resolves the bound electron's motion
  into three perpendicular components and works per component).
- In §8 the letter $E$ gets reused for the **charge of a gram-equivalent of
  monovalent ions** — the Faraday constant, quoted as $9.6\times 10^3$ in the
  paper's electromagnetic units — not for an energy. Watch for it.

---

## The Introduction — the manifesto

<!-- source: source/einstein1905-arons-peppard-ajp33.pdf, pp. 1-2 -->

**What he is doing.** In four paragraphs Einstein states the deepest version
of the problem, carves out exactly the territory where the wave theory can be
challenged, states his hypothesis, and lists the phenomena he will explain.
Almost every sentence is load-bearing.

**The "profound formal difference."** The opening observation: physics in
1905 describes matter and radiation in structurally incompatible ways. The
state of a body is a sum over a **finite number** of atoms and electrons —
its energy is parceled into countable carriers, and cannot be subdivided
below one atom's share. The electromagnetic field, by contrast, is described
by **continuous functions of space**, and its energy can be diced arbitrarily
finely: half of any amount of field energy is a perfectly good amount of
field energy. Why lead with this abstraction rather than with an experiment?
Because it frames everything that follows as a *structural* clash, not a
puzzle about one effect. Any theory that couples grainy matter to continuous
radiation has to negotiate this seam — and §1 will show the negotiation fails
catastrophically at equilibrium.

**The time-average escape hatch.** Next comes the paper's most careful
epistemological move. The wave theory "has proved itself excellently" for
diffraction, reflection, refraction, dispersion — and, Einstein says, "will
probably never be replaced by another theory." But: **optical observations
refer to time averages, not to instantaneous values.** A light wave at
visible frequencies oscillates about 10^15 times per second; every detector
available (the eye, a photographic plate, a bolometer) integrates over at
least milliseconds — a trillion cycles. All the triumphs of wave optics are
therefore triumphs about *averaged* quantities, and it is logically possible
that the instantaneous, elementary events — **emission and absorption** — are
governed by something entirely different. This is why the title says
*creation and conversion* of light: the hypothesis targets the events, not
(necessarily) the propagation.

**The hypothesis.** Paraphrasing the key sentence closely: when a light ray
spreads from a point source, its energy is *not* distributed continuously
over ever-growing volumes; it consists of a **finite number of energy quanta,
localised at points of space, which move without dividing and can only be
produced and absorbed as complete units.** Note the three separate claims
packed in: (i) spatial localisation, (ii) indivisibility in flight, (iii)
all-or-nothing production and absorption. The thermodynamic argument of §§3–6
will support the "as if" version of (i)–(ii) for dilute radiation; the
applications in §§7–9 test (iii).

**Sticking points.**

- *Isn't this just Newton's corpuscles again?* No. Newton's particles carried
  no frequency; Einstein's quanta have an energy fixed by the **frequency** —
  a wave property. From its first sentence the light quantum is a hybrid
  object, which is why the hypothesis could not have been guessed before
  Planck's law existed.
- *Doesn't interference immediately refute localised quanta?* This is the
  objection every physicist of 1905 raised, and Einstein's only defense here
  is the time-average argument: interference experiments measure averages,
  and the hypothesis is about elementary events. He is deliberately not
  offering a theory of propagation. The full reconciliation is quantum field
  theory: the field is continuous and wavelike, but its energy exchanges with
  matter are quantised. In 1905 that is decades away; the honest tension is
  the price of the word "heuristic."
- *How does Planck fit in?* Curiously, the introduction frames the light
  quantum as compatible-with-but-independent-of Planck. In 1905 Einstein
  actually believed his hypothesis *contradicted* Planck's theory (he says
  Planck's law "seems to be in contradiction" with the results of §1, and he
  builds his own case on Wien's law instead, precisely where it is *not*
  Planck-specific). Only in 1906 did Einstein show that Planck's derivation
  secretly *requires* energy quantisation. Don't let hindsight ("Einstein
  extended Planck") flatten the actual logic: this paper distrusts Planck's
  derivation and routes around it.

**With modern eyes.** The granularity is invisible in daily life because the
grains are tiny and torrentially numerous: a green photon carries about
$4\times 10^{-19}$ J (2.5 eV), so a 1 mW laser pointer emits roughly $10^{15}$
photons per second. A continuous description of such a flood is as good as a
continuous description of water from a fire hose. The quantum shows itself
only where **one grain matters**: very faint light, or — Einstein's cases —
processes where a single molecule or electron does business with the field.

---

## §1. Concerning a Difficulty with Regard to the Theory of Blackbody Radiation

**What he is doing.** Before proposing anything new, Einstein demonstrates
that *orthodox* physics — Maxwell's electrodynamics plus the kinetic theory
of gases, each applied exactly where its proponents insist it is valid —
predicts a black-body spectrum that is not merely wrong in detail but
absurd: it puts infinite energy into the cavity. The failure is structural
and cannot be patched.

**The setup.** A cavity with perfectly reflecting walls contains (a) gas
molecules, (b) free electrons, and (c) electrons elastically bound to points
— harmonic oscillators of natural frequency $\nu$, Planck's "resonators."
The resonators talk to both worlds: they exchange energy with the gas by
collisions (mechanics) and with the radiation by emitting and absorbing
(electrodynamics). At equilibrium, both conversations must balance
simultaneously. That double bookkeeping is the trap.

**Step 1 — mechanics fixes the resonator's average energy.** Kinetic theory's
equipartition theorem: at temperature $T$, thermal agitation gives each
quadratic degree of freedom the average energy $\frac{1}{2}(R/N)T$. Einstein
resolves the bound electron's motion into three perpendicular linear
components and works per component; one component has two such terms
(kinetic + potential, equal on time average), so its mean energy is

$$
\bar E = \frac{R}{N} T. \qquad (1.1)
$$

Here $R/N$ — gas constant divided by Avogadro's number — is the "per
molecule" unit of thermal energy, our $k_B$. Einstein glosses (1.1) as
"two-thirds the kinetic energy of a free monatomic gas particle" — check:
a free particle carries $\frac{3}{2}(R/N)T$ of kinetic energy, and
two-thirds of that is $(R/N)T$. His argument that (1.1) *must* hold in
equilibrium is a driftwood argument: if radiation somehow held the
oscillators above or below $\bar E$ on average, collisions with the gas
would systematically pump heat into or out of the gas, and the gas
temperature would drift — contradiction with equilibrium. (A footnote
remarks that the underlying assumption — free electrons and molecules have
equal mean kinetic energy — is the same one Drude used to explain the ratio
of thermal to electrical conductivity of metals; Einstein is flagging that
it has independent experimental credit.)

The crucial feature of (1.1): it is **independent of the frequency** $\nu$.
Equipartition is temperature-blind to how stiff the spring is; a slow floppy
oscillator and a fast stiff one soak up the same average energy. Hold that
thought — it is the exact point where classical physics dies.

**Step 2 — electrodynamics ties the resonator to the field.** Planck had
shown (1900, by an entirely classical calculation of a small damped
oscillating charge driven by random radiation) that at equilibrium the
resonator's mean energy and the spectral energy density $\rho_\nu$ of the
surrounding radiation must satisfy — and note this is *not* Planck's
radiation law, which enters only in §2; it is a temperature-free statement
of classical electrodynamics —

$$
\bar E_\nu = \frac{L^3}{8\pi\nu^2}\rho_\nu, \qquad (1.2)
$$

with $L$ the speed of light. Read it as: the field at frequency $\nu$ acts
as a bath that both shakes and damps the resonator, and (1.2) is the unique
balance point. Its derivation uses nothing but Maxwell; the resonator's
charge, mass, and damping all cancel out — which means **no tinkering with
the model of matter can change it**.

**Step 3 — collision.** Insert (1.1) into (1.2):

$$
\rho_\nu = \frac{8\pi\nu^2}{L^3}\frac{R}{N}T. \qquad (1.3)
$$

This is the Rayleigh–Jeans law (Greiner derives it by counting cavity modes
in §2.3 of ch. 2 — same law, different route; Einstein's resonator route
sidesteps any argument about what "modes of the field" mean). It agrees
beautifully with experiment at low frequency. But integrate over all
frequencies:

$$
\int_0^\infty \rho_\nu d\nu = \frac{8\pi R T}{L^3 N}\int_0^\infty \nu^2 d\nu = \infty. \qquad (1.4)
$$

The equilibrium energy density is infinite. Physically: since equipartition
demands the *same* energy per oscillator at every frequency, and there is no
highest frequency, matter would keep pumping energy into ever-bluer radiation
without end — a cavity at room temperature should blast X-rays. Equilibrium
between matter and radiation is impossible in classical physics.

**Sticking points.**

- *Why is this inescapable?* Because each ingredient is used in its home
  territory: equipartition is the core of the kinetic theory that explains
  gases; relation (1.2) is straight Maxwell. There is no third theory in 1905
  to blame. Either mechanics or electrodynamics (or both) must fail somewhere.
- *"Why bother with equipartition at all — doesn't Planck's expression
  already show the high-frequency problem?"* A name collision trips many
  readers here: two different things called "Planck" are in play. Equation
  (1.2) is Planck's **resonator–field relation** — classical electrodynamics
  — and is *not* Planck's radiation law (that is (2.1), which enters only in
  §2). The relation contains no temperature: it is one equation linking two
  unknowns, saying only that resonator energy and field density sit in a
  fixed ratio at equilibrium. It cannot say how much energy either has at
  temperature $T$. And Planck's radiation *law* shows no problem at high
  frequency — it is finite, integrable, and fits the data everywhere; it is
  the answer, not the problem. The divergence appears only when you ask what
  *classical theory predicts* for the resonator energy at temperature $T$,
  and classical statistical mechanics has exactly one answer: equipartition,
  $(R/N)T$ per oscillator, blind to frequency. That mechanical input is the
  load-bearing — and guilty — ingredient. Relation (1.2) then merely
  converts "same energy at every frequency" into the $\nu^2 T$ spectrum,
  and the integral (1.4) blows up. Equipartition is not garnish; it is the
  only thermodynamic anchor classical physics can supply.
- *"Doesn't the argument secretly need thermal energy per field mode?
  Einstein never says that."* Correct — and deliberately so. Assigning $k_B T$ to
  each electromagnetic mode is the Rayleigh–Jeans route (Greiner §2.3).
  Einstein instead applies equipartition only to a **material oscillator** —
  a bound electron colliding with gas molecules — where kinetic theory's
  authority was beyond dispute. He never assigns energy to field modes,
  never counts them, and never has to defend treating the ether's infinitely
  many degrees of freedom as equipartition recipients — a genuinely
  contested move in 1905 (Jeans, for one, tried to escape the catastrophe by
  arguing that the high-frequency modes simply never reach equilibrium).
  One resonator per frequency is enough — hence Einstein's aside that
  oscillators "of all the relevant frequencies" must be present — because
  each resonator, through the purely electrodynamic relation (1.2), pins the
  field density at its own frequency. The per-mode structure is *hidden
  inside (1.2)*: its factor $8\pi\nu^2/L^3$ is exactly the field's mode
  density. So the result reads as if every mode carried $(R/N)T$ — but in
  Einstein's version that is a corollary, not an assumption. This is what
  upgrades §1 from a calculation with disputable inputs to an indictment:
  to dodge the conclusion you must break either kinetic gas theory or
  Maxwell's electrodynamics; there is no third assumption to sacrifice.
- *"Ultraviolet catastrophe"* — the famous name is **not** in this paper; it
  was coined by Ehrenfest in 1911. Also note the history is commonly told
  backwards: this divergence played almost no role in Planck's own path in
  1900 (he worked top-down from Wien's law and the data). Einstein's §1 is
  one of the first places where the classical prediction is stated *as a
  forced consequence* and its absurdity made central.
- *Priority trivia:* Rayleigh had suggested the $\nu^2 T$ form in June 1900
  (with an ad hoc exponential cutoff bolted on); Jeans supplied a corrected
  numerical factor in 1905, shortly after this paper. Einstein derived (1.3)
  independently here — some historians call it the Rayleigh–Jeans–Einstein
  law.
- *Why does (1.3) work at low frequencies?* Where quanta are cheap compared
  with the thermal budget — $h\nu \ll k_B T$, in modern terms — the graininess
  is unnoticeable and classical physics is an excellent approximation. That
  the classical law holds *exactly there* is the pivot of §2. The ch. 2 notes
  develop this "price-to-budget ratio" intuition at length (the variable
  $x = \hbar\omega/k_B T$).
- *The long footnote on "random" radiation:* under (1.2) Einstein appends a
  footnote spelling out what "the radiation is a completely random process"
  means — expand the field at a point in Fourier components; the radiation is
  "as disordered as conceivable" when the amplitudes and phases of different
  components are statistically independent. It reads like a throwaway, but
  notice what it is: Einstein worrying, already, about how to define
  *disorder in a continuous field* — the exact concern that matures into his
  1909 fluctuation analysis of radiation.

---

## §2. Concerning Planck's Determination of the Fundamental Constants

**What he is doing.** This section looks like a digression and confuses many
readers: Einstein is about to *reject* the general validity of the classical
theory — so why pause to praise Planck's determination of the constants? The
answer: Einstein is about to lean, throughout the rest of the paper, on the
numerical value of $R/N$ (i.e., on Avogadro's number). Planck's value of $N$
came out of his radiation-law fit, whose theoretical derivation Einstein
distrusts. So Einstein shows that **the determination of Avogadro's number is independent
of the questionable parts of Planck's theory**: it only uses the radiation
law in the regime where the classical result (1.3) is empirically correct.
The German title says *Elementarquanta* — the AJP translation renders it
"fundamental constants," Wikisource "elementary quanta." Either way it means
the *atomistic constants* — the mass of the hydrogen atom, equivalently $N$,
and with it the elementary charge — **not** light quanta. (A translation-era
trap for readers of the Wikisource wording: *Elementarquanta* was standard
for "elementary units of matter/charge.")

**The argument.** Planck's law, as an empirical fit to the black-body data:

$$
\rho_\nu = \frac{\alpha\nu^3}{e^{\beta\nu/T} - 1}, \qquad (2.1)
$$

with fitted constants quoted as $\alpha = 6.10\times 10^{-56}$ and
β $= 4.866\times 10^{-11}$ in CGS units; in modern terms
$\alpha = 8\pi h/L^3$ and β $= h/k_B$. (A heads-up if you recompute: the
printed exponent of $\alpha$ is a slip. Modern $8\pi h/c^3$ is
$6.2\times 10^{-57}$, and plugging the *printed* $\alpha$ into (2.3) below
gives $6.17\times 10^{22}$ — ten times smaller than the $N$ Einstein
correctly states. With $\alpha = 6.10\times 10^{-57}$ everything is
consistent. Even this paper has a typo; don't let it cost you an evening.)
For
$T/\nu$ large — high temperature or low frequency — expand the exponential,
$e^{\beta\nu/T} \approx 1 + \beta\nu/T$:

$$
\rho_\nu \to \frac{\alpha}{\beta}\nu^2 T. \qquad (2.2)
$$

But in exactly this regime the classical law (1.3) is experimentally right.
Matching (2.2) to (1.3):

$$
\frac{\alpha}{\beta} = \frac{8\pi}{L^3}\frac{R}{N}
\quad\Longrightarrow\quad
N = \frac{8\pi R \beta}{\alpha L^3} = 6.17\times 10^{23}. \qquad (2.3)
$$

Einstein cashes this out concretely: a hydrogen atom then weighs $1/N$ grams
$= 1.62\times 10^{-24}$ g — "exactly the value found by Herr Planck, which in
turn agrees with values found by other methods."

Two comments Einstein draws out explicitly:

1. **The higher the temperature and the longer the wavelength, the better the
   classical formula works** — but it fails utterly in general (that was §1).
   So the classical theory is a *limit*, valid where energy elements are
   small compared with thermal energies.
2. Planck's determination of the elementary quanta is therefore **to a
   certain degree independent of his theory** of black-body radiation: you
   need only the measured law in its classical corner plus the classical
   relation (1.3), both of which stand regardless of what one thinks about
   Planck's resonator-energy bookkeeping.

**Why this matters for the rest of the paper.** The value (2.3) agrees with
determinations of $N$ from kinetic gas theory (gas viscosity etc.) — cross-
confirmation that both atoms and the radiation-law constants are real and
correctly sized. From here on Einstein can use $R/N$ and β as *measured*
quantities. In particular the energy quantum $(R/N)\beta\nu$ that emerges in
§6 will be a number you can compute, not a free parameter — which is what
gives §§7–9 their quantitative teeth.

The section closes with a methodological declaration worth underlining as
you read: "In the following we shall consider the experimental facts
concerning blackbody radiation **without invoking a model for the emission
and propagation of the radiation itself**." That is the contract for §§3–6 —
no resonators, no Maxwell, no mechanism; only the measured spectrum plus
thermodynamics.

**With modern eyes.** Einstein's $N = 6.17\times 10^{23}$ is within 2.5% of
the modern $6.022\times 10^{23}$ — remarkable for 1905, and one more entry in
Einstein's lifelong hobby of extracting Avogadro's number from unlikely
places (this paper, the dissertation via sugar solutions, Brownian motion —
three independent methods in one year, all agreeing: that convergence is what
finally killed anti-atomism). Also worth savoring: equating (2.2) with (1.3)
is, in modern language, the statement $\alpha/\beta = 8\pi k_B/c^3$, i.e. the
classical limit knows only the *combination* $h/(h/k_B) = k_B$ — the
correspondence principle in embryo.

---

## §3. Concerning the Entropy of Radiation

**What he is doing.** Here begins the engine (§§3–6). The goal of this
section is a tool: given the measured spectrum, construct the **entropy** of
radiation — including radiation that is *not* in equilibrium, e.g.
monochromatic radiation confined to a volume. Why entropy? Because
Einstein's whole method is to read microstructure out of thermodynamics:
entropy is the macroscopic quantity that, via Boltzmann's principle (§5),
encodes *how many ways* a state can happen, and "how many ways" is where
particle counts hide. Ideal-gas entropy knows the gas is made of $n$
molecules; if radiation entropy has the same shape, radiation is made of
countable somethings. This section builds the entropy; §4 computes its shape;
§§5–6 do the counting. (Einstein notes the section's core result was already
found by Wien, whose thermodynamic analysis of radiation he is following, but
he re-derives it for self-containedness.)

**Setup and assumptions.** Consider radiation in a volume $V$ whose state is
fully described by the spectral density $\rho(\nu)$ — energy per volume per
frequency. Assume radiation at different frequencies is separable (no work
or heat needed to sort it — frequencies don't interact in vacuum), so the
entropy is an integral over independent frequency slices:

$$
S = V\int_0^\infty \varphi(\rho,\nu) d\nu, \qquad (3.1)
$$

where $\varphi$ is an unknown entropy density function. The whole game is to
determine $\varphi$. Two honest asides in the text are easy to miss. First,
a footnote concedes that "the state is fully described by $\rho(\nu)$" is
"an arbitrary assumption," retained as the simplest one until experiment
objects — polarization and phase relationships are being deliberately swept
under the rug. Second, Einstein mentions an alternative route he will *not*
take: one can constrain $\varphi$ by demanding that adiabatic compression of
radiation between reflecting walls leave the entropy unchanged. He skips it
and goes straight at the version that uses the measured black-body law —
characteristic of the paper's data-first strategy.

### Why the entropy has the form (3.1)

The ansatz looks innocuous — "entropy is the integral of an entropy density"
— but it quietly asserts four separate physical claims, and each one is
doing real work later in the paper. Worth peeling apart, because (3.1) is
the *only* structural input to §§3–4; everything else is the measured
spectrum.

**Claim 1 — entropy adds over frequency slices.** Entropy is additive over
subsystems that cannot exchange heat or work with each other (the same fact,
run through Boltzmann's principle in §5, is why probabilities multiply while
entropies add). Are frequency slices really non-exchanging subsystems? In
vacuum, yes: Maxwell's equations are **linear**, so waves of different
frequencies superpose and pass through each other without trading a joule —
red light never "heats" blue light. There is also a nice operational way to
see that additivity is *forced*, not just plausible: colors can be sorted
**reversibly and for free** (a prism, or in modern terms a set of dichroic
mirrors, steers each band into its own sub-cavity, and running the optics
backwards recombines them). Sorting is thus a reversible process involving
no heat and no work — Einstein's exact phrase — so it cannot change the
total entropy. But after sorting, the total entropy is manifestly the sum of
the sub-cavities' entropies. Hence the unsorted radiation's entropy must
have been that sum all along:

$$
S = \sum_{\text{slices}} S_\nu \quad\longrightarrow\quad V\int_0^\infty \varphi d\nu.
$$

(If entropy were *not* additive over colors, a prism plus the second law
would make a perpetual-motion machine.) Note what would break this:
interactions that mix frequencies. Matter does exactly that — absorb red,
re-emit blue — which is why a carbon speck lets the spectrum *equilibrate*
at all; remove the speck, and each slice's energy is separately locked in.

**Claim 2 — each slice's entropy is proportional to the volume.** This is
extensivity in volume: disordered radiation is spatially homogeneous (no
preferred location), so mentally slicing the cavity into two halves gives
two subsystems with half the energy each — and, provided correlations
between the halves are negligible, half the entropy each. "Negligible
correlations" is the fine print: it holds for thermal radiation, whose
coherence length is on the order of the wavelength, tiny compared with the
cavity. A subtlety worth heading off now, because §4 *seems* to violate
this: the result (4.5) says $S$ grows like $\ln V$, not like $V$! No
contradiction — extensivity means scaling energy *and* volume together,
$S(kE, kV) = k S(E,V)$, and the form (3.1) passes that test automatically:
scale $E$ and $V$ by the same $k$ and the density $\rho = E/(V d\nu)$ is
unchanged, while the prefactor $V$ delivers the factor $k$. What §4 does is
different: it holds $E$ *fixed* and grows $V$ alone, diluting the radiation.
The $\ln V$ lives inside $\varphi$'s dependence on $\rho$, riding on top of
the extensive prefactor. Same distinction for an ideal gas: $S$ is extensive,
*and* isothermal expansion at fixed particle number gains $n k_B \ln(V/V_0)$.

**Claim 3 — one number per frequency is enough.** This is
Einstein's footnoted "arbitrary assumption" in sharper form: the observable
state of the radiation is taken to be exhausted by one number per frequency.
What's being ignored — polarization, propagation direction, phase
relationships — is exactly what carries no information in **maximally
disordered** radiation (the state his §1 footnote took pains to define):
unpolarized, isotropic, random-phased. For such radiation the mean energy
per frequency really is the only knob, so entropy can only be a function of
it. The assumption would *fail* for structured light — a polarized beam, a
laser-like phase-coherent state — whose entropy is lower than $\varphi(\rho,\nu)$
predicts. Einstein's caveat is not false modesty; it marks a real boundary
of the formula.

**Claim 4 — no cross-frequency terms, no frequency derivatives.** A corollary of Claim 1's independence — slice $\nu_1$'s
entropy cannot know what slice $\nu_2$ contains — but worth stating because
it is what made the variational problem in the refresher above *algebraic*:
the bins don't talk, so the Euler–Lagrange equation has no derivative term
and stationarity is decided bin by bin.

Why does $\nu$ appear explicitly at all, alongside $\rho$? Because the
slices are not identical subsystems: a joule parked at high frequency is
entropically different from a joule at low frequency. The deep reason is
invisible from 1905 but beautiful with hindsight — see the aside below.

**With modern eyes: the mode count hiding inside the entropy density.** Greiner's
ch. 2 §2.3 counts $8\pi\nu^2/c^3$ electromagnetic modes per unit volume per
unit frequency. In modern statistical mechanics the entropy of the slice is
(number of modes) × (entropy per mode), where the per-mode entropy depends
only on the mean occupation $\bar n$ — the average number of photons in one
mode. Since the slice's energy is (modes) × $\bar n$ × (photon energy),
$\rho = (8\pi\nu^2/c^3) \bar n h\nu = \alpha\nu^3 \bar n$, the occupation
is $\bar n = \rho/\alpha\nu^3$ — precisely the combination that appears
inside Einstein's logarithms! And the match is quantitative. The exact
per-mode entropy of thermal light is
$s = k_B[(1+\bar n)\ln(1+\bar n) - \bar n\ln\bar n]$; in the dilute limit
$\bar n \ll 1$ this collapses to $s \approx k_B \bar n(1 - \ln\bar n)$, and
multiplying by the mode density gives

$$
\varphi = \frac{8\pi\nu^2}{c^3} k_B \bar n\left(1 - \ln\bar n\right)
= \frac{k_B \rho}{h\nu}\left(1 - \ln\frac{\rho}{\alpha\nu^3}\right),
\qquad (3.1a)
$$

which — using $k_B/h = 1/\beta$ — is *identical* to Einstein's Wien-regime
result (4.3). So the mysterious explicit $\nu$-dependence of $\varphi$ is
the mode count: the same energy at higher frequency is spread over more
modes but in bigger lumps, and the entropy knows both facts. Einstein had
none of this scaffolding — no modes, no $\bar n$, no per-mode entropy — and
recovered the exact dilute limit of it from thermodynamics plus the measured
spectrum alone. (The full expression for $s$, with its $(1+\bar n)$ term,
is what §4's caveat about non-Wien radiation was gesturing at: the extra
term is the wave/bunching contribution, negligible when $\bar n \ll 1$.)

**What each claim buys later.** Claim 1 makes the maximum-entropy problem
separable (the two-bin argument); Claim 2 plants the $V$ that becomes
$\ln(V/V_0)$ in (4.5); Claim 3 guarantees the black-body law can be *encoded
in* $\varphi$ (one number per frequency in, one number out); Claim 4 makes
the equilibrium condition algebraic. Kick out any one of them and the paper
stalls on page one of §3.

**Equilibrium as maximum entropy.** Black-body radiation is the equilibrium
state, i.e. the $\rho(\nu)$ that maximizes $S$ at fixed total energy
$E = V\int\rho d\nu$. Standard variational calculus with a Lagrange
multiplier $\lambda$: demand

$$
\delta\int_0^\infty\left(\varphi - \lambda\rho\right)d\nu = 0
\quad\Longrightarrow\quad
\frac{\partial\varphi}{\partial\rho} = \lambda \quad\text{for every } \nu. \qquad (3.2)
$$

So in the black-body state, the derivative of entropy density with respect to
energy density is **one common constant across all frequencies**. (Intuition:
if slice $\nu_1$ gained more entropy per unit energy than slice $\nu_2$,
moving energy from 2 to 1 would raise total entropy — not yet equilibrium.
Equilibrium means the "entropy price of energy" is uniform. This is the same
logic that makes temperature uniform between touching bodies.)

Einstein dispatches all of this in about three lines — his 1905 readers had
variational calculus drilled into them as the backbone of mechanics. If your
own mechanics course is a distant memory, the next subsection rebuilds the
machinery from scratch; if (3.2) already looks obvious, skip ahead to
"Identifying the constant."

### Refresher: variational calculus and the Lagrange multiplier, from scratch

**What kind of problem this is.** Ordinary calculus finds the maximum of a
function of finitely many variables. Here the unknown is an entire
*function*: the spectrum $\rho(\nu)$. Correspondingly, $S$ in (3.1) is a
**functional** — a machine that eats a whole function $\rho(\nu)$ and
returns one number. The most useful mental model: chop the frequency axis
into $M$ narrow bins of width $\Delta\nu$ centered at $\nu_1, \nu_2, \ldots$
Then the function $\rho(\nu)$ is just a long list of numbers
$\rho_1, \rho_2, \ldots, \rho_M$ (the energy density in each bin), and

$$
S \approx V \Delta\nu \sum_{i=1}^{M} \varphi(\rho_i, \nu_i)
$$

is an ordinary function of $M$ variables. Everything below is plain
multivariable calculus on this list, with $M \to \infty$ silently at the
end. Nothing about the $\delta$ symbol is deeper than that.

**What δ means.** A **variation** $\delta\rho(\nu)$ is a small, arbitrary
nudge function: replace $\rho(\nu)$ by $\rho(\nu) + \delta\rho(\nu)$
everywhere and expand to first order, exactly as you would write
$f(x + dx) \approx f(x) + f'(x) dx$:

$$
\delta S = S[\rho + \delta\rho] - S[\rho]
= V\int_0^\infty \frac{\partial\varphi}{\partial\rho} \delta\rho(\nu) d\nu
\quad + \quad \text{terms of order } (\delta\rho)^2. \qquad (3.2a)
$$

In the bin picture this is nothing but the multivariable chain rule,
$df = \sum_i (\partial f/\partial\rho_i) d\rho_i$, with the sum becoming an
integral. A function $\rho(\nu)$ is a **stationary point** (candidate
maximum) when $\delta S = 0$ for *every* admissible nudge — just as an
ordinary maximum has $df = 0$ for every direction $d\vec x$.

**Relation to the mechanics you saw.** In mechanics one demands
$\delta\int L(q, \dot q, t) dt = 0$ over paths $q(t)$. Because $L$ depends
on the *derivative* $\dot q$ as well, you must integrate by parts, and out
comes a differential equation — Euler–Lagrange,
$\frac{d}{dt}\frac{\partial L}{\partial\dot q} - \frac{\partial L}{\partial q} = 0$.
Einstein's problem has the same shape with $\nu$ playing the role of $t$ and
$\rho(\nu)$ the role of the path — but $\varphi(\rho, \nu)$ contains **no
derivative** $d\rho/d\nu$. So the integration-by-parts step never happens,
the Euler–Lagrange equation loses its derivative term, and the stationarity
condition is *algebraic*, bin by bin. This problem is strictly easier than
the ones from your mechanics class: the bins don't talk to each other.

**Why unconstrained maximization would be nonsense.** If every nudge were
allowed, $\delta S = 0$ for all $\delta\rho$ would force
$\partial\varphi/\partial\rho = 0$ at every $\nu$. (This step is the
**fundamental lemma** of the calculus of variations: if
$\int u(\nu) \delta\rho(\nu) d\nu = 0$ for *arbitrary* $\delta\rho$, then
$u \equiv 0$ — because otherwise you could choose $\delta\rho$ to be a
little bump sitting where $u \ne 0$, with the same sign as $u$, making the
integral positive.) But physically $\partial\varphi/\partial\rho = 0$ is
absurd: that derivative will turn out to be $1/T > 0$ — radiation entropy
*always* increases when you add energy, so an unconstrained maximum doesn't
exist. The maximization only makes sense **at fixed total energy**: the
cavity has a definite energy budget, and equilibrium is the entropy maximum
*on that budget*.

**How the constraint changes the game.** Fixed energy
$E = V\int\rho d\nu$ means the admissible nudges are only those that
*redistribute* energy, not create it:

$$
\int_0^\infty \delta\rho(\nu) d\nu = 0. \qquad (3.2b)
$$

Now the fundamental lemma doesn't apply — $\delta\rho$ is no longer
arbitrary — and you cannot conclude $\partial\varphi/\partial\rho = 0$.
Good: you shouldn't.

**The two-bin argument (the multiplier without the multiplier).** Here is
the cleanest way to see what stationarity under (3.2b) *does* imply. Choose
the simplest balanced nudge: take a sliver of energy $\varepsilon$ out of
the bin at $\nu_2$ and put it into the bin at $\nu_1$. This satisfies
(3.2b) by construction, and (3.2a) gives

$$
\delta S = V\varepsilon\left[
\frac{\partial\varphi}{\partial\rho}(\nu_1) -
\frac{\partial\varphi}{\partial\rho}(\nu_2)
\right].
$$

At a maximum this must vanish — if it were positive, the nudge would raise
the entropy; if negative, the *reverse* nudge would. Since $\nu_1$ and
$\nu_2$ were arbitrary, $\partial\varphi/\partial\rho$ must have the **same
value in every bin**. Call that common value $\lambda$. That is precisely
conclusion (3.2), and notice it is the "entropy price of energy is uniform"
intuition from above, now made rigorous: the derivative
$\partial\varphi/\partial\rho$ *is* the entropy gained per unit of energy
parked at frequency $\nu$, and equilibrium is the state where no
reallocation of the budget is profitable.

**The Lagrange multiplier is bookkeeping for the same idea.** Lagrange's
trick automates the two-bin argument. Instead of maximizing $S$ subject to
the constraint, make the *unconstrained* combination
$\int(\varphi - \lambda\rho) d\nu$ stationary, where $\lambda$ is a number
to be chosen later:

$$
\delta\int_0^\infty(\varphi - \lambda\rho) d\nu
= \int_0^\infty\left(\frac{\partial\varphi}{\partial\rho} - \lambda\right)\delta\rho d\nu = 0.
$$

Why is this legitimate? For nudges obeying (3.2b), the added term
$-\lambda\int\delta\rho d\nu$ is zero anyway — subtracting it changes
nothing. Its purpose is to *extend* the statement to unbalanced nudges:
$\lambda$ is tuned so that the bracket kills the one direction (uniformly
adding energy) that the constraint had removed. With the combination
stationary under **arbitrary** $\delta\rho$, the fundamental lemma applies
again and yields $\partial\varphi/\partial\rho = \lambda$ at every $\nu$ —
equation (3.2). Afterwards $\lambda$ is pinned down by requiring the
constraint itself, $\int\rho d\nu = E/V$.

If you prefer the finite-dimensional picture from multivariable calculus:
to maximize $f(\vec x)$ on the level surface $g(\vec x) = c$, note that at
the constrained maximum you cannot increase $f$ by moving *along* the
surface, so the gradient of $f$ must be perpendicular to the surface — i.e.
parallel to the gradient of $g$: the condition
$\partial f/\partial x_i = \lambda \partial g/\partial x_i$ for all $i$.
Here $f \leftrightarrow S$ with $\partial f/\partial\rho_i = \varphi'(\rho_i)$,
and $g \leftrightarrow E$ whose "gradient" components $\partial g/\partial\rho_i$
are all equal to 1 — so parallel-gradients reads $\varphi'(\rho_i) = \lambda$
in every bin.

**The multiplier is never junk — it is the physics.** In mechanics, when
you enforce a constraint with a multiplier, the multiplier turns out to be
the constraint *force* (the tension in the pendulum rod). The same thing
happens here: $\lambda$, the sensitivity of the maximized entropy to the
constrained quantity, is $\partial S/\partial E$ — and thermodynamics calls
that quantity $1/T$, as the next paragraph confirms. This is a completely
general pattern worth taking from this paper into the rest of statistical
mechanics: **the multiplier attached to each conserved quantity is its
conjugate intensive variable**. Constrain energy and the multiplier is
$1/T$; constrain particle number and it is $-\mu/T$ (the chemical
potential); constrain volume and it is $p/T$. The Boltzmann distribution,
and the Bose–Einstein occupation $1/(e^x - 1)$ that Greiner uses to rebuild
Planck's law in ch. 2 §2.6, all come out of exactly this
maximize-entropy-with-multipliers machine.

**Is it a maximum, though?** Stationarity is also satisfied by minima and
saddle points. The second-order check is concavity of $\varphi$ in $\rho$,
and (4.3) will let you verify it in the Wien regime:
$\partial^2\varphi/\partial\rho^2 = -1/(\beta\nu\rho) < 0$. Each bin's
entropy has diminishing returns in energy — which is also *why* the
"uniform price" condition picks out a maximum: with concave $\varphi$,
moving energy from a low-price bin to a high-price bin is always favorable
until the prices equalize.

**Identifying the constant with 1/T.** This is the paragraph that begins,
in the translation, "The following equation applies when the temperature of
a unit volume of blackbody radiation increases by $dT$" (in the German:
"Für die Temperaturzunahme $dT$ ..."). Einstein writes down, without
derivation,

$$
dS = \int_0^\infty \frac{\partial\varphi}{\partial\rho} d\rho d\nu, \qquad (3.3a)
$$

then pulls the frequency-independent derivative out front and compares with
thermodynamics. Let's supply the missing derivation, then rerun his
comparison.

*Where (3.3a) comes from: the chain rule along the family of black-body
spectra.* Work per unit volume ($V = 1$, as Einstein specifies). At
temperature $T$ the equilibrium spectrum is $\rho(\nu, T)$; heat the
radiation to $T + dT$ and every slice's density moves by a definite amount,

$$
d\rho(\nu) = \frac{\partial\rho(\nu,T)}{\partial T} dT
$$

— the vertical gap between the black-body curves at $T$ and at $T + dT$,
frequency by frequency. The entropy (3.1) responds through each slice.
Differentiating under the integral sign with the chain rule — and noting
that only the *first* slot of $\varphi(\rho,\nu)$ moves, since the second
slot is the integration label $\nu$, which heating does not touch —

$$
S(T) = \int_0^\infty \varphi\left(\rho(\nu,T), \nu\right) d\nu
\quad\Longrightarrow\quad
\frac{dS}{dT} = \int_0^\infty \frac{\partial\varphi}{\partial\rho} \frac{\partial\rho}{\partial T} d\nu,
$$

and multiplying through by $dT$ and recognizing
$(\partial\rho/\partial T) dT = d\rho(\nu)$ gives exactly (3.3a). In the
bin picture of the refresher above, this is bare multivariable calculus:
$S = \sum_i \varphi(\rho_i, \nu_i)\Delta\nu$ is an ordinary function of the
list $(\rho_1, \ldots, \rho_M)$; heating nudges the list by
$(d\rho_1, \ldots, d\rho_M)$; the first-order change is
$\sum_i (\partial\varphi/\partial\rho) d\rho_i \Delta\nu$. So (3.3a) is
nothing new — it is the general variation formula (3.2a), evaluated on the
one particular nudge that heating happens to produce. That also explains
the division of labor between the two kinds of "d": the **partial**
$\partial\varphi/\partial\rho$ appears because $\varphi$ has two slots and
only the first one changes; the **totals** $dS$, $dT$, $d\rho$ are actual
changes in the physical heating process. (And note the chain-rule step is
valid for *any* small perturbation of *any* spectrum; the black-body
specialization has not been used yet — it enters only in the next two
moves.)

*The comparison.* Two facts now collapse the integral. First, for
black-body radiation $\partial\varphi/\partial\rho$ has the same value in
every slice — that was the variational result (3.2) — so it pulls out
front:

$$
dS = \frac{\partial\varphi}{\partial\rho}\int_0^\infty d\rho d\nu
   = \frac{\partial\varphi}{\partial\rho} dE,
$$

where $dE = \int d\rho d\nu$ is the total energy added per unit volume.
Second, that added energy is *pure heat*, delivered *reversibly*: the
cavity walls are rigid, so no volume change and the radiation pressure does
no work ($dE$ has no $p dV$ piece to subtract); and we may imagine warming
the cavity by contact with a reservoir only infinitesimally hotter — a
quasi-static, reversible path. (Entropy is a state function, so computing
$dS$ along this one convenient path settles it for every process between
the same endpoints.) For reversible heat transfer, thermodynamics says
$dS = dE/T$. Comparing the two expressions for $dS$:

$$
\frac{\partial\varphi}{\partial\rho} = \frac{1}{T}. \qquad (3.3)
$$

**The tool, stated.** Equation (3.3) is a differential equation for
$\varphi$: if experiment tells you the equilibrium spectrum $\rho(\nu,T)$ —
i.e. tells you $T$ as a function of $\rho$ at each $\nu$ — you can integrate
$1/T$ with respect to $\rho$ and obtain the entropy density $\varphi(\rho,\nu)$
for **any** radiation, equilibrium or not. The measured black-body curve
becomes a machine for assigning entropy to arbitrary monochromatic radiation.
That inversion — spectrum in, entropy out — is the trick that makes §4 possible.

**Why "any radiation," though?** The derivation of (3.3) used black-body
radiation throughout, so the claim just made deserves a moment of
suspicion: how did equilibrium-only input buy a formula valid *out of*
equilibrium? Three ingredients.

1. *One fixed function, self-contained slices.* By the ansatz (3.1) —
   Claims 1 and 3 of the "why this form" section — a slice's entropy
   depends only on its own contents, the pair ($\rho$, $\nu$): not on what
   the rest of the spectrum looks like, and not on any "equilibrium" label.
   A slice of density $\rho$ at frequency $\nu$ carries entropy
   $\varphi(\rho,\nu) d\nu$ per unit volume whether it sits inside a full
   black-body spectrum or floats alone in a cavity (the reversible prism
   argument again: extract the slice and its entropy rides along
   unchanged). So determining $\varphi$ *anywhere* determines it for
   isolated monochromatic radiation too. Notice that the reach beyond
   equilibrium is **bought by the assumption, not derived** — which is
   exactly why Einstein's footnote conceded the ansatz is "arbitrary."
2. *The equilibrium family scans the whole domain.* At fixed $\nu$, the
   black-body density $\rho(\nu, T)$ increases monotonically with $T$, so
   each point ($\rho$, $\nu$) of the plane is *realized* by equilibrium
   radiation at exactly one temperature: invert the measured law to get
   $T(\rho, \nu)$. Equation (3.3) is therefore a statement at **every**
   point of $\varphi$'s domain — not just along one curve — and integrating
   in $\rho$ at fixed $\nu$, from $\varphi(0) = 0$, pins $\varphi$
   everywhere. (Without this coverage, equilibrium data would determine
   $\varphi$ only on a one-dimensional sliver of its domain.)
3. *A single slice is never "out of equilibrium" internally.* Its state is
   one number, $\rho$, so there is always some temperature whose black-body
   spectrum would contain exactly this slice — its **effective
   temperature**, which is what (3.3) assigns. Being out of equilibrium is
   a *relation between slices*: different effective temperatures at
   different frequencies. "Any radiation" thus means: arbitrary per-slice
   effective temperatures, total entropy the sum of per-slice pieces.

A homely analogy: measure the heat capacity of water across a range of
temperatures — equilibrium calorimetry, nothing else — and you can
thereafter assign an entropy to a bathtub that is hot at one end and cold
at the other, by integrating the local entropy density along the tub. The
equilibrium experiments determine the *function*; the function then
evaluates on non-equilibrium *configurations*. Einstein's inversion is the
same move, with frequency playing the role of position.

**Sticking points.**

- *Can pure radiation have a temperature and entropy at all?* Strictly,
  radiation in a perfectly reflecting cavity never rethermalizes on its own;
  one imagines a speck of dust or carbon that absorbs and re-emits, catalyzing
  equilibrium without changing the result (the standard caveat, cf. Greiner
  ch. 2's cavity discussion). Entropy for a *non-equilibrium* $\rho(\nu)$ is
  then defined slice by slice through $\varphi$ — legitimate because each
  monochromatic slice separately *would* be an equilibrium distribution for
  some temperature; formula (3.3) just assigns each slice its own effective $T$.
- *Why maximum entropy characterizes equilibrium:* that is the second law in
  its variational clothing — an isolated system settles into the most probable
  (= maximum entropy) macrostate compatible with its constraints.

---

## §4. Asymptotic Form for the Entropy of Monochromatic Radiation at Low Radiation Density

**What he is doing.** Now the tool from §3 gets pointed at a deliberately
chosen corner of the data: the **Wien regime** — high frequency, low
temperature, low radiation density — where Wien's law holds. Two reasons for
this choice. Tactically, Wien's law is analytically simple (a pure
exponential, no $-1$ in the denominator). Strategically — and this is the
point most readers miss — the Wien regime is **exactly the regime where
classical physics fails** (§1's classical law works at the *opposite*,
low-frequency end). Einstein is deliberately probing where the new physics
lives. With hindsight: Wien's regime is the dilute-photon limit, where quanta
are sparse and statistically independent; that independence is what will make
the ideal-gas analogy in §6 come out clean.

**Step 1 — invert Wien's law.** Wien's empirical law (which Einstein is
careful to say is "not exactly valid" in general but "fully confirmed by
experiment" for large $\nu/T$):

$$
\rho = \alpha\nu^3 e^{-\beta\nu/T}. \qquad (4.1)
$$

Solve for $1/T$:

$$
\frac{1}{T} = -\frac{1}{\beta\nu}\ln\frac{\rho}{\alpha\nu^3}. \qquad (4.2)
$$

**Step 2 — integrate (3.3) to get the entropy density.**
$\partial\varphi/\partial\rho = 1/T$ with (4.2) inserted, integrated with
respect to $\rho$:

$$
\varphi(\rho,\nu) = -\frac{\rho}{\beta\nu}\left[\ln\frac{\rho}{\alpha\nu^3} - 1\right]. \qquad (4.3)
$$

(Check by differentiating: the derivative of $-\rho[\ln(\rho/\alpha\nu^3)-1]$
with respect to $\rho$ is $-\ln(\rho/\alpha\nu^3)$, matching (4.2). The
integration constant is fixed by the condition Einstein states at the end of
§3 — $\varphi$ vanishes when $\rho = 0$: no radiation, no entropy. For the
volume comparison below only entropy *differences* matter anyway.)

**Step 3 — entropy of a monochromatic blob.** Take radiation of total energy
$E$, all within a narrow band $d\nu$ around frequency $\nu$, filling volume
$V$. Then $\rho = E/(V d\nu)$ and $S = V d\nu \cdot \varphi$:

$$
S = -\frac{E}{\beta\nu}\left[\ln\frac{E}{V d\nu \cdot \alpha\nu^3} - 1\right]. \qquad (4.4)
$$

**Step 4 — the volume dependence.** Compare the same energy $E$ in two
volumes $V$ and $V_0$ (same $\nu$, same $d\nu$). Everything cancels except
the $V$ inside the logarithm — note the awkward $d\nu$ drops out entirely:

$$
S - S_0 = \frac{E}{\beta\nu}\ln\frac{V}{V_0}. \qquad (4.5)
$$

**The punchline sentence** (close paraphrase of Einstein's): the entropy of
monochromatic radiation of sufficiently low density varies with volume
according to the **same law as the entropy of an ideal gas** or a dilute
solution. A logarithm of the volume, with a prefactor $E/\beta\nu$ — keep
your eye on that prefactor; §6 will read it as a particle count.

**Sticking points.**

- *What physical process is being described?* None yet — (4.5) compares two
  static states. But to make it vivid: imagine the radiation trapped in a box
  with mirror walls (add a grain of dust for bookkeeping), and let the box
  expand or contract without adding heat or doing frequency-changing work.
  It is a thought-experiment comparison of state functions, exactly like
  comparing a gas's entropy at two volumes.
- *Why "low density" keeps appearing:* the whole calculation lives inside
  Wien's law, i.e. requires $\beta\nu/T \gg 1$, which by (4.1) means small
  $\rho$. Einstein's result is explicitly a **limiting law**. This is not a
  defect but a feature with a future: for general Planck-law radiation the
  volume dependence acquires an extra piece, and in 1909 Einstein computed
  the corresponding energy fluctuations and found *two* terms — one
  particle-like (dominating in the Wien limit) and one wave-like (dominating
  in the Rayleigh–Jeans limit). That 1909 formula is the first precise
  statement of wave–particle duality, and the seed is exactly here. In yet
  more modern language: Wien-limit photons are so sparse that Bose bunching
  is negligible and they behave like independent classical particles.

---

## §5. Molecular-Theoretic Investigation of the Dependence of the Entropy of Gases and Dilute Solutions on the Volume

**What he is doing.** Equation (4.5) says radiation entropy looks like gas
entropy. To convert that resemblance into a *particle count*, Einstein needs
the general principle that connects entropy to statistics, stated in a form
strong enough to be run **in reverse**. This section (a) states Boltzmann's
principle, (b) grounds it operationally, and (c) shows on the ideal gas and
on dilute solutions that the logarithmic volume law is precisely the
statistical signature of "$n$ independent mobile units." It reads like a
statistical-mechanics tutorial dropped into the middle of the paper — because
in 1905 it had to be: these ideas were not yet textbook material, Boltzmann's
work was under active attack, and Einstein is also quietly correcting how the
principle should be understood.

**Boltzmann's principle.** For entropy differences:

$$
S - S_0 = \frac{R}{N}\ln W, \qquad (5.1)
$$

where $W$ is the **relative statistical probability** of the state — for
Einstein, an honest-to-goodness probability: watch the system for a very long
time and ask for the fraction of time it spends in (or near) the state in
question. Two points he takes care over, both easy to skate past:

- Only entropy **differences** are defined this way, so only probability
  *ratios* are ever needed — no fuss about normalisation or about the
  absolute size of "phase-space cells."
- The principle is meaningful **without any detailed model of the dynamics**
  ("every conceivable kinetic theory" must satisfy it, as long as states
  evolve probabilistically toward the more probable). This is exactly what
  licenses applying it to radiation, whose micro-dynamics he has pointedly
  declined to model. He opens the section with a complaint that
  molecular-theoretic calculations often use "probability" in a sense that
  isn't the probability calculus's, and promises a separate paper showing
  that his time-fraction "statistical probability" suffices and removes "a
  logical difficulty" obstructing Boltzmann's principle. (He never published
  that paper as such — the program resurfaces in his 1909–1910 fluctuation
  work.)

**Where the logarithm comes from.** The paper does not just posit (5.1); it
derives the functional form on one page, and the derivation is a small gem
worth absorbing. Take two systems that do not interact. Entropy, being
extensive, must **add**; probabilities of independent systems must
**multiply**:

$$
S = S_1 + S_2, \qquad W = W_1 W_2.
$$

If entropy is any function of probability, $S_i = \varphi_i(W_i)$, then

$$
\varphi(W_1 W_2) = \varphi_1(W_1) + \varphi_2(W_2), \qquad (5.1a)
$$

and the only solution is the logarithm: $\varphi(W) = C\ln W +$ const. The
constant $C$ appears on both sides of (5.1a) for *any* pair of systems, so it
must be one **universal** constant — measure it once, on any convenient
system, and it is fixed for all systems forever. The kinetic theory of gases
supplies the calibration: $C = R/N$. (Modern statement: $S = k_B\ln W$, and
this argument is why Boltzmann's constant is universal. Planck wrote it in
this famous form in 1900–1901; the version engraved on Boltzmann's tombstone
came later.)

**The ideal-gas computation.** Take $n$ molecules moving independently in a
volume $V_0$ (dilute: no interactions, so one molecule's position says
nothing about another's). What is the probability that, at a random instant,
all $n$ of them happen to be inside a chosen sub-volume $V$? Each
molecule is in $V$ with probability $V/V_0$; independence multiplies:

$$
W = \left(\frac{V}{V_0}\right)^{n}. \qquad (5.2)
$$

Boltzmann's principle then gives the entropy difference between "gas confined
to $V$" and "gas spread over $V_0$":

$$
S - S_0 = \frac{R}{N}\ln\left(\frac{V}{V_0}\right)^n = n\frac{R}{N}\ln\frac{V}{V_0}. \qquad (5.3)
$$

Same shape as (4.5): a logarithm of volume, prefactor = (number of
independent units) × $R/N$. Note what (5.3) does *not* depend on: the
molecules' mass, size, chemistry, or interactions with anything else. The
log-volume entropy is a pure **head count**.

**Why dilute solutions too?** Because van 't Hoff's law (1880s) showed that
dissolved sugar in water — chemically nothing like a gas — exerts osmotic
pressure obeying the ideal-gas equation. That empirical fact certifies the
head-count interpretation: the log-volume law cares only about the number of
independently roaming units, *not about what they are or what medium they
roam in*. This is the license Einstein needs — if it works for sugar in
water, why not for energy quanta in vacuum? Mentioning solutions is not
decoration; it is the universality claim without which §6 would be a mere pun.

**Closing the loop with thermodynamics.** As a consistency check Einstein
runs the logic forward to pressure (in a footnote, via the free energy
$E - TS$; equivalently): from $dE = T dS - p dV$ at constant energy (an
ideal gas's energy does not depend on volume),
$p = T(\partial S/\partial V)$, and (5.3) gives

$$
pV = \frac{n}{N} R T, \qquad (5.4)
$$

the Boyle–Gay-Lussac law and van 't Hoff's law in one line. So the chain
statistics ⇒ entropy ⇒ equation of state is verified on known ground before
being trusted on new ground.

**Sticking point — the direction of inference.** Normally one *knows* the
microphysics (molecules), computes $W$, and predicts $S$. Einstein's §6 will
run it backwards: *measure* $S$ (that was §4, from the radiation data),
deduce $W$, and infer the microstructure. The reverse direction is only as
good as the uniqueness of the reading — strictly, it is inference to the best
explanation, not a theorem. That is one more reason the paper's title says
"heuristic." (Einstein was unusually self-aware on this; he later described
the general strategy as reading the constitution of matter and radiation off
the entropy, and used it again and again — 1909 fluctuations, 1924–25
Bose–Einstein gas.)

---

## §6. Interpretation of the Expression for the Volume Dependence of the Entropy of Monochromatic Radiation in Accordance with Boltzmann's Principle

**What he is doing.** One page, one move, and the paper's central result.
Put (4.5) and (5.1) side by side and read off what radiation must be made of.

**The move.** Rewrite the radiation result (4.5) so it looks like Boltzmann's
principle. Since $x\ln y = \ln y^x$:

$$
S - S_0 = \frac{E}{\beta\nu}\ln\frac{V}{V_0}
        = \frac{R}{N}\ln\left[\left(\frac{V}{V_0}\right)^{\frac{N E}{R\beta\nu}}\right]. \qquad (6.1)
$$

Comparing with $S - S_0 = (R/N)\ln W$: the probability that all the radiation
energy $E$ is found, at a random moment, in the sub-volume $V$ of $V_0$ is

$$
W = \left(\frac{V}{V_0}\right)^{\frac{N E}{R\beta\nu}}. \qquad (6.2)
$$

But (5.2) says a power law of exactly this form, with exponent $n$, is the
fingerprint of $n$ **independently moving units**. Matching exponents:

$$
n = \frac{N E}{R\beta\nu}
\quad\Longleftrightarrow\quad
E = n\cdot\frac{R}{N}\beta\nu. \qquad (6.3)
$$

**The conclusion, in Einstein's own careful wording** (close paraphrase):
monochromatic radiation of low density (within the domain of validity of
Wien's law) **behaves thermodynamically as if it consisted of mutually
independent energy quanta** of magnitude $(R/N)\beta\nu$. With the notation
dictionary: $(R/N)\beta\nu = k_B\cdot(h/k_B)\cdot\nu = h\nu$. There it is —
$E = h\nu$ for free radiation, derived from the measured spectrum plus
statistics, with no model of matter and no use of Planck's resonator
bookkeeping.

**A closing back-of-envelope.** Before moving on, Einstein sizes his new
objects: how big is the *average* quantum of black-body radiation, compared
with the mean translational kinetic energy $\frac{3}{2}(R/N)T$ of a gas
molecule at the same temperature? Average quantum = total energy over total
number of quanta, both computed from Wien's law:

$$
\bar\epsilon
= \frac{\int_0^\infty \alpha\nu^3 e^{-\beta\nu/T} d\nu}
       {\int_0^\infty \frac{N}{R\beta\nu} \alpha\nu^3 e^{-\beta\nu/T} d\nu}
= 3\frac{R}{N}T. \qquad (6.4)
$$

(The numerator's integrand is energy per frequency slice; dividing each
slice's energy by the quantum size $R\beta\nu/N$ turns it into a *count*.
With $a = \beta/T$: the numerator integral is $6\alpha/a^4$ and the
denominator's is $(N/R\beta)\cdot 2\alpha/a^3$, and the ratio collapses to
$3R T/N$.) So a typical thermal light quantum carries $3k_B T$ — the same
scale as, and exactly twice, a gas molecule's $\frac{3}{2}k_B T$. The point
of the exercise: the quanta are **thermally sized** objects, respectable
citizens of the same statistical world as molecules — reinforcing the gas
analogy that the whole section rests on. (Hidden bonus: maximizing Wien's
$\nu^3 e^{-\beta\nu/T}$ gives $\beta\nu/T = 3$, i.e. the spectrum peaks at
$h\nu = 3k_B T$ — equation (6.4) is Wien's displacement law wearing a
statistical costume. Greiner derives the displacement law from the full
Planck law in ch. 2 §2.7, where the peak condition becomes the famous
transcendental equation with root $x \approx 2.82$; in the Wien
approximation the root is exactly 3.)

And then the bridge sentence that launches the rest of the paper: if dilute
radiation *sits there* (thermodynamically) like a gas of independent energy
quanta, it is natural to ask whether the laws of its **creation and
conversion** are also those of quanta — i.e. whether light is emitted and
absorbed one whole quantum at a time. That question is not answerable by
thermodynamics; it needs experiments. Hence §§7–9.

**Sticking points.**

- *"Behaves as if" — how strong is that?* The argument establishes a precise
  thermodynamic equivalence in the dilute limit, not a mechanical picture.
  What is genuinely established: the volume-fluctuation statistics of
  Wien-regime radiation are those of $E/h\nu$ independent grains. What is
  *not* established: anything about how the grains move, whether they have
  a size or phase, or how two of them interfere. Einstein's honesty about
  this boundary — thermodynamic behavior proven, elementary processes
  conjectured — is the paper's methodological spine.
- *Why energy proportional to frequency?* Track the derivation: the exponent
  $\beta\nu$ in Wien's law (4.1) becomes the $1/\beta\nu$ prefactor of the
  entropy (4.5), which becomes the quantum $\beta\nu\cdot R/N$ in (6.3). The
  Planck relation E-proportional-to-ν is a direct transcription of the
  *shape of the measured spectrum* — of the fact that the high-frequency
  tail falls exponentially in $\nu/T$. No spectrum-shaped input, no $h\nu$.
- *Independence is a dilute-limit artifact.* Outside the Wien regime the
  exponent-matching fails (Planck's full law does not give a clean power of
  $V/V_0$), and *that is physics, not failure*: photons in a general thermal
  state are correlated — they bunch. The full statistics had to wait for
  Bose (1924) and Einstein's extension to matter (1924–25). It is a nice
  historical loop: the 1905 argument works precisely because the Wien limit
  is where Bose statistics degenerates into Maxwell–Boltzmann independence.
- *No Planck constant anywhere.* Einstein writes the quantum as $(R/N)\beta\nu$ partly
  to stay close to measured constants, partly (historians argue) to keep his
  distance from Planck's theory, whose derivation he considered unsound. The
  quantum is presented as an experimental fact about radiation, not as an
  inheritance from Planck.

**Why this matters.** This section, not §8, is the paper's revolutionary
core, and it is why the paper unsettled people for two decades. Planck's
quanta could be (and were) read as a statement about how *matter* absorbs
and emits. Equation (6.3) is about radiation **alone, in flight, in empty
space**, with matter out of the picture entirely. That is the step nobody —
including Planck — was willing to take.

---

## §7. Concerning Stokes's Rule

**What he is doing.** First of three applications, and deliberately the
gentlest: a qualitative rule that the quantum picture explains in two lines
using only energy conservation per elementary act. The applications section
answers the obvious objection "your thermodynamic analogy is cute — does it
buy anything?" Each application also targets a phenomenon involving
*conversion* of light (photoluminescence: light in, light out; §8: light in,
electron out; §9: light in, ion out) — precisely the domain the introduction
staked out for the hypothesis.

**The rule.** Stokes' rule (G.G. Stokes, 1852): in photoluminescence — shine
light on a material, it re-emits light (fluorescence/phosphorescence) — the
emitted light's frequency is **at most** the exciting light's frequency
(equivalently, the wavelength is shifted toward the red). Empirically solid
for half a century, theoretically unexplained: on the wave picture there is
no obvious reason a material driven at frequency $\nu_1$ couldn't re-radiate
some energy at higher frequency, given enough incident intensity.

**The quantum explanation.** Assume light of frequency $\nu_1$ is absorbed
in whole quanta $(R/N)\beta\nu_1$ and emitted in whole quanta
$(R/N)\beta\nu_2$, and that in the normal case each emitted quantum draws
its energy from a *single* absorbed quantum (dilute light: quanta arrive one
at a time, and by §6 they don't act collectively). Energy conservation for
the elementary process, allowing part of the energy to be lost to heat or
other emission:

$$
\frac{R}{N}\beta\nu_2 \le \frac{R}{N}\beta\nu_1
\quad\Longrightarrow\quad
\nu_2 \le \nu_1. \qquad (7.1)
$$

That's the whole derivation. The strict *frequency* inequality — not an
intensity statement — falls out because energy is tied to frequency at the
level of single events.

**Einstein's predicted exceptions** — and this is where the section turns
from explanation to falsifiable science. The rule should fail if the
single-quantum accounting fails:

1. **Enormous excitation density**, so that one emission event can draw on
   *several* absorbed quanta. In modern language: nonlinear optics —
   two-photon absorption and upconversion, theorized by Göppert-Mayer (1931)
   and observed by Kaiser and Garrett (1961), once lasers made "enormous"
   attainable. A 56-year-early prediction of when nonlinear optics turns on.
2. **Light that is not "Wien-regime" in character** — when the incident (or
   emitted) light "is not of such a composition that it corresponds to
   blackbody radiation within the range of validity of Wien's Law," his
   example being light from a body so hot that at the relevant wavelengths
   Wien's law no longer holds. Remember what §6 actually proved: independent
   quanta *only in the Wien limit*. Outside it, all bets are off, and
   Einstein is disciplined enough to say so. He flags this case as
   commanding "especial interest": a "non-Wien radiation" of very low density
   might behave *qualitatively* differently from Wien-regime radiation — with
   hindsight, a first squint at the regime where photon correlations (Bose
   statistics, bunching) live.

(A modern relative of case 1's bookkeeping: thermally assisted anti-Stokes
emission, where the material tops up the emitted quantum from stored heat —
the per-event energy ledger survives; only the "all the energy from one
incoming quantum" clause is relaxed. Einstein's two cases are about the
*light*; this one is about the material's state — full quantum mechanics was
needed to sort out the material's side.)

He also notes the flip side: for weak excitation the quantum picture demands
the luminescence output be **proportional to the input intensity** with no
lower threshold — each arriving quantum acts alone, so halving the rate of
quanta halves the output but never switches it off. A wave-accumulation
picture would naturally expect faint light to fail entirely to excite. (This
"no intensity threshold, strict frequency threshold" signature is the common
thread of all three applications.)

**Sticking point.** Why is the energy *not* required to come out as exactly
$\nu_2 = \nu_1$? Because the elementary act may split the absorbed energy:
some to the emitted quantum, the rest to molecular vibrations (heat) — the
inequality only bounds, it does not fix. The microscopic detail (energy
levels, Kasha's rule, etc.) had to wait for full quantum mechanics; what is
impressive is how much follows from bare energy bookkeeping per quantum.

---

## §8. Concerning the Emission of Cathode Rays Through Illumination of Solid Bodies

*This is the photoelectric-effect section — the one the Nobel committee cited
— and the reason the paper is misremembered as "the photoelectric paper."
Greiner ch. 1 §1.1 presents the modern textbook version; here is where that
textbook version was born.*

**What he is doing.** The strongest application: not a qualitative rule but
a **quantitative, parameter-poor equation** plus sharp predictions that were,
in 1905, beyond the data — a genuine stick-your-neck-out forecast. ("Cathode
rays" is period vocabulary for free electrons, identified as such by
J.J. Thomson in 1897.)

**The experimental puzzle (Lenard, 1902).** Ultraviolet light on a metal
surface in vacuum ejects electrons. Lenard found:

1. The electrons' maximum kinetic energy is **independent of the light's
   intensity** — turn the arc lamp up tenfold, the electrons come out no
   faster, there are just more of them.
2. The energy appeared to **grow with the light's frequency** (qualitatively
   — his apparatus could not pin down the functional form).
3. The number of electrons is proportional to intensity.

Why this is impossible on the wave picture — the **accumulation problem**,
worth making quantitative. A wave spreads its energy uniformly over its
wavefront, so an electron can only collect energy through its tiny effective
cross-section (atomic scale, about $10^{-20}$ m²). For faint light of, say,
$10^{-6}$ W/m², the collection rate is about $10^{-26}$ W, so gathering the
observed electron-volt of energy (about $1.6\times 10^{-19}$ J) would take of
order $10^7$ seconds — **months**. Yet photoemission is observed to start
promptly (later timed at under 3 nanoseconds by Lawrence and Beams, 1928).
And in any case, a brighter wave shakes electrons harder, so intensity
*should* set the ejection energy — the opposite of finding 1.

**Einstein's elementary act.** Assume (the "simplest picture," he says) that
a light quantum gives **all** its energy to a **single** electron —
one-on-one, no sharing, no accumulation. The electron then pays an energy
toll $P$ (characteristic of the material — today's *work function*) to get
through the surface. Electrons starting deeper also lose energy on the way
out, so the surface electrons set the **maximum**:

$$
E_{\max} = \frac{R}{N}\beta\nu - P. \qquad (8.1)
$$

All three of Lenard's findings fall out instantly. Intensity = rate of
quanta, so it controls only *how many* electrons (finding 3), never how fast
(finding 1); frequency sets each quantum's size, hence the energy scale
(finding 2). Faint light ejects few electrons but promptly and at full
energy — the accumulation problem simply evaporates, because the energy was
never spread out in the first place.

**The stopping-potential form.** To measure $E_{\max}$, charge the emitting
plate to a positive potential $\Pi$ (surrounded by conductors at zero
potential) so that escaping electrons, charge $\varepsilon$, must climb a
potential hill; emission just stops when the hill exactly eats the maximum
energy:

$$
\Pi\varepsilon = \frac{R}{N}\beta\nu - P. \qquad (8.2)
$$

Einstein immediately rewrites it per gram-equivalent (per mole) of electrons
— the units his electrochemically minded readers knew by heart. Multiply
(8.2) by $N$:

$$
\Pi E = R\beta\nu - P', \qquad (8.3)
$$

where $E$ — an unfortunate reuse of the letter, here **not** an energy — is
the charge of one gram-equivalent of monovalent ions (the Faraday constant,
$9.6\times 10^3$ in the paper's electromagnetic units), and $P'$ is the
escape work per gram-equivalent expressed as a potential. A footnote covers
the case where the electron must first be torn off a neutral molecule: fine,
fold that extra work into $P'$ as a second term — the *form* of the law is
untouched, which is part of its power.

**Einstein's numerical sanity check.** Put in $\nu = 1.03\times 10^{15}$ Hz
(he takes this as the ultraviolet limit of the solar spectrum), take
$P' = 0$, and $\beta = 4.866\times 10^{-11}$: then
$\Pi \approx 4.3$ volts. (Check in modern units:
$h\nu = 6.6\times 10^{-34}\times 1.03\times 10^{15} \approx
6.8\times 10^{-19}$ J $\approx 4.3$ eV.) Lenard's measured stopping
potentials were of exactly this order — Einstein claims agreement in order
of magnitude, no more, because that is all the 1905 data could support.

**The two sharp predictions.** If (8.2) is right, then:

1. Stopping potential $\Pi$ plotted against frequency $\nu$ is a **straight
   line**.
2. Its **slope is a universal constant, identical for every material**:
   slope $= R\beta/(N\varepsilon)$, i.e. $h/e$ in modern notation. The
   material only shifts the line up and down (through $P'$); it cannot tilt it.

**Two refinements in the paper that readers often skip.** First, Einstein
shows what survives if you drop the "simplest picture" that a quantum hands
its *entire* energy to one electron: the equality degrades gracefully to

$$
\Pi E + P' \le R\beta\nu, \qquad (8.4)
$$

so the straight line becomes an upper envelope — which is in fact exactly how
the modern measurement is phrased (the *fastest* electrons define the line).
Second, he runs the process **backwards**. In cathodoluminescence — electrons
slamming into a phosphor and producing light, the workhorse of Lenard's own
tube experiments — the same ledger must read

$$
\Pi E + P' \ge R\beta\nu, \qquad (8.5)
$$

the electron must at least pay for each quantum it creates. Now the data:
Lenard's substances needed electrons accelerated through hundreds or
thousands of volts to produce visible light — quanta costing only a few
volts each. Conclusion: a single electron generates **many** light quanta.
No contradiction, and a quiet display of the hypothesis' reach — one
bookkeeping rule, running in both directions.

Nothing in 1905 could test the linearity or the universal slope — the
requisite precision was heroic (contact potentials between different metals
shift $\Pi$ and had to be tamed). Robert Millikan spent roughly a decade on
it, *expecting to refute Einstein* — he found the light-quantum hypothesis
"reckless," writing in 1916 that a localized electromagnetic disturbance
"flies in the face of the thoroughly established facts of interference."
His 1916 measurements confirmed the linear law and the universal slope
completely, and turned equation (8.2) into one of the best ways to measure
$h$ (his value was good to about 0.5%). Millikan verified the equation while
continuing, for years, to reject the hypothesis behind it — a beautiful case
study in how evidence and interpretation can come apart. Einstein's 1921
Nobel Prize (awarded 1922) cites "his discovery of the **law** of the
photoelectric effect" — the equation, pointedly not the light quantum;
Millikan's own 1923 prize cites this measurement alongside his charge
measurement.

**Sticking points.**

- *Why the maximum and not the energy?* Only electrons emitted from the very
  surface with a full quantum and no inelastic detours achieve (8.1); the
  rest populate a spectrum below it. Experiments therefore look at the
  fastest electrons (the stopping potential is where the *last* electron is
  turned back).
- $P$ vs $P'$: not two physical quantities — $P$ is the escape work per
  electron, $P'$ the same thing per gram-equivalent, expressed as a potential
  via the Faraday charge ($P' = NP$ in energy terms). The genuinely nasty
  experimental subtlety — contact potential differences between emitter and
  collector shifting the measured $\Pi$ — is *not* in the paper; taming it is
  what consumed a good part of Millikan's decade.
- *What Einstein does not claim:* any mechanism for *how* the electron
  absorbs the quantum, any statement about atomic structure (Bohr's model is
  eight years away), or that light "is particles" in flight — the argument
  needs only all-or-nothing energy delivery at absorption.
- *A modern myth to avoid:* the photoelectric effect alone, as a threshold
  phenomenon, can actually be reproduced by "semiclassical" models —
  quantised atoms in a *classical* light field (Wentzel 1927; Lamb and
  Scully 1969) — so, strictly, it does not prove photons exist. What it
  proved in 1905 was that the classical wave picture of *energy delivery*
  fails, and that Einstein's per-quantum bookkeeping gets all the phenomena
  with one constant. The clincher for the photon as a flying object came
  later: Compton scattering (1923) showed light carries momentum $h\nu/L$ in
  directed portions, and photon-antibunching experiments (1977 onward) closed
  the remaining loopholes. See the aftermath section.

---

## §9. Concerning the Ionization of Gases by Ultraviolet Light

**What he is doing.** Third application, shortest, and pushing the same
logic one step further — from "quantum ejects electron from metal" to
"quantum ionises a single gas molecule." It adds two things: a
**quantitative inequality** that the hypothesis must survive against
existing data, and (in embryo) the founding principle of photochemistry.

**The inequality.** If ionisation happens one quantum to one molecule, then
a quantum must carry at least the ionisation work of one molecule. Einstein
phrases it per gram-equivalent (per mole): with $J$ the theoretical work of
ionisation per gram-equivalent, one mole of quanta carries energy $R\beta\nu$
(that is, $N$ quanta of $(R/N)\beta\nu$ each), so

$$
R\beta\nu \ge J. \qquad (9.1)
$$

Lenard had found the largest effective wavelength for ionising air to be
about $1.9\times 10^{-5}$ cm (190 nm), i.e.
$\nu = L/\lambda \approx 1.58\times 10^{15}$ Hz, which makes the bound

$$
J \le R\beta\nu = 6.4\times 10^{12} \quad \text{erg per gram-equivalent}, \qquad (9.2)
$$

about 6.5 eV per molecule ($6.4\times 10^{12}$ erg $= 6.4\times
10^5$ J per mole; divide by $6\times 10^{23}$ and convert: about
$1.06\times 10^{-18}$ J $\approx 6.6$ eV). Then the cross-check against an
entirely independent route: ionisation potentials of rarefied gases measured
electrically. Citing Stark, the smallest observed ionisation potential for
air (at platinum anodes) is about 10 V — per gram-equivalent that is
$9.6\times 10^{12}$ erg (10 V × the Faraday charge), **another upper limit** for
$J$, "nearly equal to the value found above." Two independent upper
bounds landing within 50% of each other: the hypothesis survives a
quantitative ambush it could easily have failed. (A footnote adds the odd
detail that in the interior of gases the ionisation potential for negative
ions is about five times greater — a reminder of how murky gas-discharge
data still was.)

**The photochemical yield prediction.** Einstein then sharpens the picture
into an equation he flags as deserving experimental test "of great
importance": if *every* absorbed quantum ionises exactly one molecule, the
number of gram-molecules ionised, $j$, is tied to the absorbed light energy
$L$ by

$$
j = \frac{L}{R\beta\nu}, \qquad (9.3)
$$

valid, he specifies, only for gases that show no appreciable absorption
*without* ionisation at the relevant frequency (absorbed-but-not-ionising
channels would spoil the count). This one-quantum-one-molecule accounting is
the **photochemical equivalence law**, which Einstein formalized in 1912
(now called the Stark–Einstein law) and which underlies all quantitative
photochemistry — quantum yields, actinometry, photosynthesis efficiency
measurements, photographic sensitometry.

**With modern eyes — an instructive wrinkle.** The specific datum Einstein
leaned on was wrong: pure N₂ and O₂ ionise at 15.6 eV and 12.1 eV
respectively, needing wavelengths shorter than about 80–103 nm, not 190 nm.
The reported ionisation of air at 190 nm was an artifact (impurities,
aerosols, surface effects — sorted out over the following decades). Note
that this does not touch Einstein's logic, which was an inequality *test*
honestly applied to the best available data; and the underlying idea — a
sharp **frequency threshold** for photo-ionisation, independent of intensity
— is not only right but is now precision science (photoionisation
spectroscopy, photoelectron spectroscopy) and applied technology (UV
photodetectors, ozone-layer photochemistry). A good reminder that the paper
was real science operating on 1905-grade data, not revelation.

**Why the paper ends here.** With §9 the hypothesis has touched three
independent domains — light-to-light conversion (§7), light-to-electron in
solids (§8), light-to-ion in gases (§9) — each time with the same single
move: energy arrives in indivisible portions of size $(R/N)\beta\nu$. No
grand peroration follows; the paper simply stops (with a thanks to his
friend Michele Besso in some editions' surrounding material). The
understatement is characteristic of the whole: strong claims, carefully
fenced, left to be judged by experiment.

---

## Aftermath — what happened next, and how the paper stands today

Useful orientation for reading around the paper; also answers the natural
question "if this is so compelling, why did acceptance take twenty years?"

**Einstein doubled down.** 1906: he showed Planck's own derivation *tacitly
assumes* energy quantisation — so Planck's law, far from being an alternative
to light quanta, presupposes the quantum. 1907: he applied quantisation to
solids (specific heats), opening the second front of early quantum theory.
1909 (Salzburg lecture and papers): the fluctuation formula for full
Planck-law radiation, with its particle-like term *plus* wave-like term —
the first quantitative statement of wave–particle duality, and a direct
outgrowth of this paper's §4 caveat. 1916–17: the A and B coefficients paper,
where quanta acquire **directed momentum** $h\nu/L$ (and, as a by-product,
the theory behind the laser).

**The community said no — for years.** The light quantum was rejected by
essentially every senior physicist, *while the same people showered Einstein
with honors for everything else*. Exhibit A: the 1913 letter recommending
Einstein for the Prussian Academy, signed by Planck among others, which asks
that it not be held against him "that he may sometimes have missed the
target in his speculations, as, for example, in his hypothesis of light
quanta." Exhibit B: Millikan confirming equation (8.2) to high precision in
1916 while calling the hypothesis behind it reckless. The sticking point was
always the same: interference. Sixty years of wave optics could not see how
localized quanta produce fringes; most physicists preferred to localize the
quantum weirdness in matter (as Planck did) rather than in light.

**The turn.** Compton (1923): X-rays scattering off electrons transfer
energy *and momentum* exactly as billiard-ball collisions with quanta of
energy $h\nu$ and momentum $h\nu/L$ would (Greiner ch. 1 §1.2 works this
out). Resistance collapsed rapidly. Bose (1924) rederived Planck's law by
counting photon states — giving the statistics whose dilute limit is exactly
this paper's §6 independence — and Einstein extended the counting to atoms
(Bose–Einstein condensation, 1924–25). The word **photon** was coined by the
chemist G.N. Lewis in 1926 (for a somewhat different concept; the name stuck
to Einstein's quantum). Modern quantum optics closed the final loopholes:
since the photoelectric effect itself admits semiclassical imitations, the
cleanest proofs of field quantisation are photon antibunching
(Kimble–Dagenais–Mandel 1977) and single-photon anticorrelation at a beam
splitter (Grangier–Roger–Aspect 1986) — one photon, unlike a classical wave,
never triggers two detectors at once.

**Einstein's last word.** He never considered the photon understood. To
Besso, December 1951: "All these fifty years of conscious brooding have
brought me no nearer to the answer to the question 'What are light quanta?'
Of course today every rascal thinks he knows the answer, but he is deluding
himself." The modern answer — the photon as an excitation of a quantised
field mode, neither bullet nor ripple — vindicates both his hypothesis and
his refusal to over-interpret it.

**Where you meet this paper's physics today:** every photomultiplier, CCD,
and CMOS camera pixel (photoelectric effect); solar cells (its semiconductor
cousin); photoelectron spectroscopy as a lab workhorse (§8's equation, used
daily to measure work functions and band structures); quantum-yield
accounting throughout photochemistry and photobiology (§9); nonlinear optics'
intensity regime (§7's predicted exception); and the entire concept of the
photon budget in astronomy and quantum communication (§6).

---

## Cross-references to the Greiner notes

- **Greiner ch. 1 §1.1** ([notes](../../text/ch01-quantization-of-physical-quantities/notes.md))
  presents the photoelectric effect in modern notation, with $E = \hbar(\omega - \omega_A)$
  matching this paper's equation (8.1) under the dictionary $(R/N)\beta\nu \to \hbar\omega$
  and $P \to \hbar\omega_A$. Greiner's Compton-effect section (§1.2) is the
  1923 sequel that ended the resistance chronicled above.
- Conventions differ: Greiner uses angular frequency $\omega = 2\pi\nu$ and
  writes spectral densities per $d\omega$; this paper uses $\nu$ and
  densities per $d\nu$. All conversions ride on $h\nu = \hbar\omega$ and
  $\varrho(\omega) d\omega = \rho_\nu d\nu$.

### Mapping this paper onto Greiner ch. 2

Greiner ch. 2 ([notes](../../text/ch02-radiation-laws/notes.md)) derives
everything this paper *assumes* about radiation, so the two texts interlock
almost section by section. Reading them side by side is worth the trouble —
each fills the other's gaps.

- **The master variable is the same.** The dimensionless
  $x = \hbar\omega/k_B T$ developed at the start of the ch. 2 notes (the
  "price-to-budget ratio") is exactly Einstein's $\beta\nu/T$. Every regime
  statement in the paper translates instantly: classical/Rayleigh–Jeans
  validity (this paper's §§1–2) is $x \ll 1$; Wien validity (§§4–6) is
  $x \gg 1$. Einstein's strategy — trust the law at small $x$, mine the
  physics at large $x$ — is a walk along Greiner's opening figure from left
  to right.
- **Paper §1 vs Greiner §2.3 — two roads to Rayleigh–Jeans.** Greiner counts
  the electromagnetic **modes of the cavity** ($8\pi\nu^2/c^3$ per unit
  volume and frequency) and hands each mode the equipartition energy $k_B T$.
  Einstein instead hands $k_B T$ to each material **resonator** and imports
  Planck's resonator–field equilibrium relation (1.2) — in which the mode
  count is hiding: the $8\pi\nu^2/L^3$ in (1.2) *is* Greiner's mode density.
  Same law, same divergence; but Einstein's route needs no commitment about
  what "counting modes of the ether" means, only orthodox mechanics plus
  orthodox electrodynamics — which is what makes his §1 read as an
  indictment rather than a calculation.
- **Paper §2 vs Greiner §§2.4–2.5 — a pointed contrast in method.** Greiner
  *derives* Planck's law twice: §2.4 via Einstein's own 1917 A/B-coefficient
  argument, §2.5 via Planck's oscillator-energy counting. Einstein in 1905
  pointedly derives it **zero** times — he uses Planck's formula purely as an
  empirical fit and trusts only its classical corner. The historical arc is
  worth savoring: the 1917 derivation that Greiner teaches is the same author
  finally deriving, from quantised matter *plus his own light quanta*, the
  law he refused to lean on in 1905.
- **Wien's law's status.** In Greiner ch. 2, Wien's law appears as the
  high-frequency limit of Planck's law and as a historical stepping stone. In
  this paper it is the *load-bearing input*: §§4–6 are built entirely inside
  its domain of validity. If you've internalized Greiner's
  $\bar n = 1/(e^x - 1)$, you know *why* that domain is special: for
  $x \gg 1$ the mean occupation per mode is $\bar n \approx e^{-x} \ll 1$ —
  far less than one photon per mode. Photons that never share a mode never
  exhibit their bosonic correlations, which is exactly why Einstein's
  independent-particle reading (§6) comes out clean there, and why it *had*
  to fail (interestingly, not trivially) elsewhere.
- **Paper (6.4) vs Greiner §2.7 — the displacement law in disguise.**
  Einstein's average thermal quantum $3(R/N)T$ is the Wien-approximation
  fingerprint of Wien's displacement law: maximizing $\nu^3 e^{-\beta\nu/T}$
  gives $\beta\nu/T = 3$, while Greiner's full-Planck peak condition
  $x = 3(1 - e^{-x})$ gives $x \approx 2.82$. The 6% difference between 3
  and 2.82 is precisely the bosonic $-1$ in Planck's denominator — i.e. the
  photon bunching that the Wien regime suppresses.
- **Frequency slices, two uses.** Greiner's §2.6 (Stefan–Boltzmann) gets the
  total energy density $E/V = aT^4$ by *summing* Planck's law over all
  frequency slices (mode density × Bose–Einstein occupation × $\hbar\omega$,
  then integrate). Einstein's §§3–4 keep the slices *separate* and do
  thermodynamics on each one — entropy density $\varphi(\rho,\nu)$ per slice,
  with (3.3) as the slice-wise version of $dS = dE/T$. Integration destroys
  exactly the information Einstein needs (which frequency the energy sits
  at), which is why his equations carry a $d\nu$ that then cancels in the
  entropy *difference* (4.5). If ch. 2 left you comfortable assigning $S$ and
  $T$ to light at all, Einstein's §3 will feel natural.
- **What the paper adds that ch. 2 doesn't.** Greiner (following the
  textbook tradition) presents $E = \hbar\omega$ as Planck's postulate
  inherited by Einstein. The 1905 paper shows something stronger and rarely
  taught: the quantum of *free radiation* can be read directly out of the
  measured spectrum by thermodynamic reasoning, without Planck's postulate,
  without resonators, and without any model of matter at all. Conversely,
  ch. 2 supplies what the paper (by design) lacks: the full Planck law's
  derivation and the mode picture that eventually reconciles quanta with
  waves.
