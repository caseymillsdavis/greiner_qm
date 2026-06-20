# Chapter 1 — The Quantization of Physical Quantities
*(Die Quantelung physikalischer Größen)*

> Source: Walter Greiner, *Quantum Mechanics: An Introduction*, Chapter 1.
> Screenshots: [`source/p01.jpg`](source/) – [`source/p11.jpg`](source/).

**Theme of the chapter.** Classical physics treats energy, momentum, and
orientation as continuous quantities that can take any value. Chapter 1 walks
through five experiments — the photoelectric effect, the Compton effect, the
Ritz combination principle, the Franck–Hertz experiment, and the Stern–Gerlach
experiment — each of which forces us to conclude that some physical quantity is
**quantized**: it comes in discrete lumps rather than a continuum. Together they
are the experimental foundation on which the rest of the book builds quantum
mechanics.

---

## 1.1 Light quanta and the photoelectric effect
*(Lichtquanten · Der photoelektrische Effekt)*

<!-- source: source/p01.jpg, source/p02.jpg, source/p03.jpg, source/p04.jpg -->

### Background: two pictures of light

Historically, two competing pictures arose to explain the phenomena of light,
both dating to the seventeenth century: Newton's **corpuscular theory** (light
as a stream of particles) and Huygens' **wave theory** (light as a wave). Some
basic properties — rectilinear propagation, reflection — could be accounted for
by either. But **interference** (in particular the striking fact that light
added to light can produce *darkness*) could only be explained by the wave
theory. The triumphs of Maxwell's electrodynamics in the nineteenth century,
which revealed light to be an electromagnetic wave, then seemed to settle the
question decisively in favour of waves.

The photoelectric effect — discovered by Hertz in 1887 — and the other
experiments of this section overturned that finality. They show that light also
has a **particle** aspect. Depending on the question one asks
(*je nach Fragestellung*), light must sometimes be described as a wave and
sometimes as a stream of particles, the **light quanta** or **photons**. This
side-by-side coexistence of the two descriptions is the **wave–particle duality
of light** (*Dualismus des Lichts*). The experiments below are precisely those
that *cannot* be described by the wave picture and *require* light quanta.

### The phenomenon

Shine light on a metal surface and electrons are knocked out — the
**photoelectric effect** (Lenard's experiment). The measurement setup: light
strikes a metal plate, ejected electrons fly to a collector plate, and the
resulting current is read off a meter.

![Photoelectric measurement apparatus](figures/fig-1.1-photoelectric-apparatus.png)

<!-- figure: cropped from source/p02.jpg -->
Principle of the measurement: light frees electrons from a metal plate; they
travel to a collector plate, and the resulting current is read on the meter.

The experimental facts that classical wave theory **cannot** explain:

1. **The energy of the ejected electrons is set by the *frequency* of the
   light, not its intensity.** Monochromatic light produces electrons of a
   single, definite energy.
2. **Raising the intensity ejects *more* electrons but leaves their energy
   unchanged.** Classically this is paradoxical: in a wave, the energy is
   carried by the intensity, so a brighter wave should hand each electron more
   energy.
3. There is a **threshold frequency** $\omega_A$ below which *no* electrons are
   emitted, no matter how intense the light.

### The quantitative law

Doing the experiment with monochromatic light of various frequencies gives a
**linear** relation between the electron energy and the frequency:

$$
E \sim (\omega - \omega_A)
$$

![Energy versus frequency of the photoelectrons](figures/fig-1.1-energy-frequency.png)

<!-- figure: cropped from source/p03.jpg -->
The kinetic energy $E$ of the photoelectrons grows linearly with the light's
frequency $\omega$, meeting the axis at the threshold $\omega_A$.

The proportionality constant — read off as the slope of the line — is **Planck's
quantum of action** $h$ (or $\hbar = h/2\pi$):

$$
\boxed{E = \hbar(\omega - \omega_A) = h(\nu - \nu_A)} \qquad (1.1)
$$

with

$$
h = 2\pi\hbar = 6.6\times 10^{-34}\ \text{W·s}^2 = 6.6\times 10^{-34}\ \text{J·s}
$$

**Symbols.**
- $\omega = 2\pi\nu$ — angular frequency of the light; $\nu$ — ordinary frequency.
- $\omega_A,\ \nu_A$ — **threshold** angular / ordinary frequency.
- $E$ — kinetic energy of the ejected electron.
- $\hbar$ — reduced Planck constant; $h$ — Planck constant.

The quantity $W_A \equiv \hbar\omega_A$ is the **work function**
(*Austrittsarbeit*): the minimum energy needed to lift an electron out of the
metal surface. Crucially, the threshold $\omega_A$ — equivalently $W_A$ — is a
**property of the particular metal**: different metals bind their conduction
electrons with different energies, so each has its own threshold frequency.
Below the threshold ($\omega < \omega_A$) a single light quantum simply does not
carry enough energy to free an electron, which is why piling on more intensity
(more quanta) cannot help.

### Einstein's interpretation: light comes in quanta

Einstein (1905) explained this by proposing that light of frequency $\omega$
consists of discrete **light quanta (photons)**, each carrying energy

$$
\boxed{E_{\text{photon}} = \hbar\omega} \qquad (1.2)
$$

A single photon ejects a single electron: it spends $W_A=\hbar\omega_A$ on
freeing the electron and the remainder, $\hbar\omega - \hbar\omega_A$, becomes
the electron's kinetic energy — exactly Eq. (1.1). Increasing the intensity
means delivering *more photons per second*, hence more ejected electrons, but
each photon still carries the same energy $\hbar\omega$, so the per-electron
energy is unchanged. This is in **direct contradiction to classical wave
theory**, and it is what the experiment confirms.

> **Intuition.** Think of light not as a continuous stream of energy but as a
> hail of identical "energy pellets." A bigger hail (more intensity) means more
> pellets, not heavier pellets. The energy of each pellet depends only on the
> color (frequency).

### The momentum of a photon

A light quantum **moves at the speed of light** $c$. This is not an extra
assumption about some new fast-moving particle: the photon *is* light. Light in
vacuum propagates at $c$ (Maxwell's electrodynamics, confirmed by countless
experiments), so the discrete energy packets that make up a light wave must
travel at $c$ as well.

A finite-energy object moving at $c$ is forced to be **massless**. In special
relativity the total energy and momentum of a particle obey

$$
E^2 = (m_0 c^2)^2 + p^2 c^2 \qquad (1.3)
$$

and the total energy of a *massive* particle is $E = m_0 c^2/\sqrt{1-\beta^2}$
with $\beta = v/c$. As $v \to c$ this diverges — *unless* $m_0 = 0$. Since the
photon has the perfectly finite energy $\hbar\omega$ yet travels at $c$, its
**rest mass must vanish**, $m_0 = 0$. Equation (1.3) then collapses to the
massless relation $E = pc$, i.e. $\hbar\omega = pc$. Writing the frequency
through the wavenumber, $\omega = c k$ (with $k = 2\pi/\lambda$), gives

$$
\boxed{p = \hbar k}\qquad\text{or, as a vector}\qquad \vec p = \hbar \vec k \qquad (1.4)
$$

the direction of the momentum coinciding with the propagation direction of the
light. So a photon carries both energy $\hbar\omega$ **and** momentum
$\hbar\vec k$. The next experiment makes this momentum directly visible.

> **What "dispersion relation" means.** A *dispersion relation* is the rule
> linking a wave's frequency to its wavenumber, $\omega(k)$ — equivalently a
> particle's energy to its momentum, $E(p)$. For the photon, $E = pc$ together
> with $E=\hbar\omega,\ p=\hbar k$ gives the simple **linear** law $\omega = ck$;
> we call it *massless* because it is the form $E=pc$ obeyed by any massless
> particle. A *massive* particle instead has $E^2=(pc)^2+(m_0c^2)^2$, i.e.
> $\omega = \sqrt{c^2k^2 + (m_0c^2/\hbar)^2}$, which is not linear.

---

## 1.2 The Compton effect
*(Der Compton-Effekt)*

<!-- source: source/p04.jpg, source/p05.jpg, source/p06.jpg, source/p07.jpg -->

### The phenomenon

When X-rays scatter off electrons, the scattered radiation is **shifted to a
longer wavelength**, and the size of the shift depends on the scattering angle
$\vartheta$. This was discovered by Compton in 1923 (and independently by
Debye). Classical electrodynamics predicts **no** wavelength change when an
electromagnetic wave scatters — so the shift is a genuine puzzle for the wave
picture, and a clean test of the photon picture.

### Setup and conservation laws

Treat the collision as a relativistic two-body problem: an incoming photon of
energy $\hbar\omega$ and momentum $\hbar\vec k$ strikes an electron that is
**at rest and unbound** before the collision. Afterwards the photon flies off
with energy $\hbar\omega'$ and momentum $\hbar\vec k'$ at angle $\vartheta$,
while the electron recoils with speed $v$ at angle $\varphi$ (write
$\beta = v/c$).

![Compton scattering kinematics](figures/fig-1.2-compton-kinematics.png)

<!-- figure: cropped from source/p05.jpg -->
Kinematics of Compton scattering: the incoming photon $\hbar\vec k$ scatters to
$\hbar\vec k'$ through angle $\vartheta$, while the electron recoils with
momentum $\vec p$ at angle $\varphi$.

**Energy conservation:**

$$
\hbar\omega + m_0 c^2 = \hbar\omega' + \frac{m_0 c^2}{\sqrt{1-\beta^2}} \qquad (1)
$$

**Momentum conservation:**

$$
\hbar\vec k = \hbar\vec k' + \frac{m_0\vec v}{\sqrt{1-\beta^2}} \qquad (2)
$$

Here $m_0$ is the electron rest mass and $m_0/\sqrt{1-\beta^2}$ its relativistic
mass. The photon's massless dispersion relation $k = \omega/c$ is used
throughout.

### Reducing the equations

Resolve the vector equation (2) into components **parallel** and
**perpendicular** to the incident direction (using $k=\omega/c$):

$$
\hbar\frac{\omega}{c} = \hbar\frac{\omega'}{c}\cos\vartheta
      + \frac{m_0 v}{\sqrt{1-\beta^2}}\cos\varphi \qquad (2\parallel)
$$

$$
\hbar\frac{\omega'}{c}\sin\vartheta = \frac{m_0 v}{\sqrt{1-\beta^2}}\sin\varphi \qquad (2\perp)
$$

**Step 1 — eliminate the electron angle $\varphi$.** Move the photon terms to
the left in $(2\parallel)$, then square both component equations and add. Since
$\cos^2\varphi+\sin^2\varphi=1$ the recoil angle drops out:

$$
\frac{m_0^2 v^2}{1-\beta^2}
 = \frac{\hbar^2}{c^2}\Big(\omega^2 + \omega'^2 - 2\omega\omega'\cos\vartheta\Big) \qquad (\ast)
$$

**Step 2 — eliminate the electron speed $v$ using energy conservation.** Square
Eq. (1) written as $\dfrac{m_0c^2}{\sqrt{1-\beta^2}} = \hbar(\omega-\omega') + m_0c^2$:

$$
\frac{m_0^2 c^4}{1-\beta^2}
 = \hbar^2(\omega-\omega')^2 + 2\hbar(\omega-\omega') m_0 c^2 + m_0^2 c^4 \qquad (\ast\ast)
$$

Now use the relativistic identity (valid for any speed)

$$
\frac{m_0^2 c^4}{1-\beta^2} - c^2 \frac{m_0^2 v^2}{1-\beta^2} = m_0^2 c^4
$$

which follows because $\dfrac{m_0^2 c^2(c^2 - v^2)}{1-\beta^2} = m_0^2 c^2\cdot
c^2 \dfrac{1-\beta^2}{1-\beta^2} = m_0^2 c^4$. Substituting $(\ast)$ and
$(\ast\ast)$ into this identity, the $m_0^2 c^4$ terms cancel and so do
$\omega^2,\ \omega'^2$:

$$
2\hbar(\omega-\omega') m_0 c^2 = 2\hbar^2 \omega\omega' (1-\cos\vartheta)
$$

Dividing by $2\hbar m_0 c^2$ and using $1-\cos\vartheta = 2\sin^2(\vartheta/2)$:

$$
\boxed{\omega - \omega' = \frac{2\hbar}{m_0 c^2} \omega\omega' \sin^2\frac{\vartheta}{2}} \qquad (1.5)
$$

### The Compton scattering formula

Convert frequencies to wavelengths with $\omega = 2\pi c/\lambda$. Then
$\omega-\omega' = 2\pi c \dfrac{\lambda'-\lambda}{\lambda\lambda'}$ and
$\omega\omega' = (2\pi c)^2/(\lambda\lambda')$; the common factor
$2\pi c/(\lambda\lambda')$ cancels, leaving the **Compton scattering formula**:

$$
\boxed{\lambda' - \lambda = 4\pi \frac{\hbar}{m_0 c} \sin^2\frac{\vartheta}{2}
 = \frac{2h}{m_0 c}\sin^2\frac{\vartheta}{2}} \qquad (1.6)
$$

The wavelength shift depends **only on the scattering angle** $\vartheta$, not
on the incident wavelength. In the collision the photon loses energy, so
$\lambda' > \lambda$ always. The combination

$$
\lambda_c \equiv \frac{2\pi\hbar}{m_0 c} = \frac{h}{m_0 c}
$$

is the **Compton wavelength** of a particle of mass $m_0$ (here the electron,
$\lambda_c \approx 2.43\times10^{-12}$ m).

> **Why the Compton wavelength is a "size."** It marks the length scale below
> which a particle can no longer be treated as a simple point object. To pin a
> particle down to within a distance $\Delta x$, you must probe it with light of
> wavelength $\sim \Delta x$, i.e. with photons of energy $\sim \hbar c/\Delta x$.
> As $\Delta x$ shrinks toward the (reduced) Compton wavelength
> $\hbar/(m_0 c)$, that probe energy approaches $m_0 c^2$ — enough to create a
> brand-new particle–antiparticle pair of the same mass. At that point you no
> longer have *one* well-defined particle, and single-particle quantum mechanics
> must hand over to quantum field theory. So $\lambda_c$ is the natural quantum
> "extent" of a particle: roughly the smallest region in which it still makes
> sense to speak of a single particle of mass $m_0$. In terms of it,
> $\lambda'-\lambda = 2\lambda_c \sin^2(\vartheta/2)$.

### Kinetic energy of the recoil electron

The electron carries away the energy the photon lost:

$$
T = \hbar\omega - \hbar\omega' = 2\pi\hbar c\left(\frac{1}{\lambda}
       - \frac{1}{\lambda'}\right)
$$

Substituting $\lambda' = \lambda + 2\lambda_c\sin^2(\vartheta/2)$ and using
$\hbar\omega = 2\pi\hbar c/\lambda$:

$$
\boxed{T = \hbar\omega
\frac{2\lambda_c \sin^2(\vartheta/2)}{\lambda + 2\lambda_c \sin^2(\vartheta/2)}} \qquad (1.7)
$$

![Energy distribution of photons and electrons versus scattering angle](figures/fig-1.2-compton-energy-distribution.png)

<!-- figure: cropped from source/p07.jpg -->
Energy carried by the scattered photon (upper vectors, $\hbar\omega$) and by
the recoil electron (lower vectors, $\frac{m}{2}v^2$) as the scattering angle
runs from forward (direction 1, no deflection and no energy transfer) to
backward (direction 10, maximum energy handed to the electron).

### Why it matters

The recoil energy is **directly proportional to the photon energy**
$\hbar\omega$, so the Compton effect is only appreciable at **short
wavelengths** (X-rays, $\gamma$-rays); for visible light the shift is utterly
negligible. Crucially, classical electrodynamics forbids any frequency change
in scattering — only the picture of light quanta carrying momentum $\hbar\vec k$
and energy $\hbar\omega$ reproduces Eq. (1.6). The Compton effect is therefore a
direct experimental confirmation of the **photon** and of energy–momentum
conservation in light–matter interactions.

> **What is measured — and why the "Compton line" has a width.** At a fixed
> scattering angle one records the *intensity of the scattered X-rays as a
> function of their wavelength*. The result is a peak — a spectral **line** —
> centred on the shifted wavelength $\lambda'$; this peak is the **Compton
> line**. (One usually also sees an *unshifted* peak at $\lambda$, from photons
> that scatter off tightly bound inner electrons, where the whole heavy atom
> recoils and the shift $\propto 1/m_{\text{atom}}$ is negligible.)
>
> Our derivation assumed the target electron is **at rest**. Real atomic
> electrons are *bound and in motion*, with a spread of momenta — a **momentum
> distribution** (*Impulsverteilung der Elektronen*). An electron moving toward
> or away from the incoming photon contributes an extra Doppler-like shift on
> top of the Compton shift, so averaging over the distribution of electron
> momenta smears the scattered wavelengths and gives the Compton line a finite
> **width** instead of a sharp spike. The width therefore *encodes* the
> electrons' momentum distribution — and indeed measured Compton profiles are
> used to map electron momentum distributions in atoms and solids.

---

## 1.3 The Ritz combination principle
*(Das Ritzsche Kombinationsprinzip)*

<!-- source: source/p08.jpg -->

### The phenomenon

The light emitted by atoms consists of characteristic, discrete **spectral
lines**, which fall into regular **series** (e.g. the Balmer series of
hydrogen). Ritz (1908) noticed an arithmetic regularity: **new spectral lines
can be obtained by additively or subtractively combining the frequencies of
known lines.**

> **How does an atom emit light in the first place?** An atom radiates when it
> is in an **excited** state — an electron occupying a higher energy level — and
> then drops to a lower level, carrying off the energy difference as a single
> photon of frequency $\omega_{ln} = (E_l - E_n)/\hbar$. So yes, the atom must
> first be excited: by heating, by an electric discharge, or by particle
> collisions (exactly the mechanism of the Franck–Hertz experiment in §1.4).
> Absorption is the reverse process — the atom swallows a photon of the right
> energy and jumps *up* to a higher level.

### Explanation from energy levels

Spectral lines mean the atom makes **transitions between discrete energy
states**. Combined with the frequency condition $E = \hbar\omega$, the Ritz
principle is immediate. For a transition from level $E_l$ to level $E_n$,
inserting an intermediate level $E_m$:

$$
\hbar\omega_{ln} = E_l - E_n = (E_l - E_m) + (E_m - E_n)
$$

so the frequencies simply add:

$$
\boxed{\omega_{ln} = \omega_{lm} + \omega_{mn}} \qquad (1.8)
$$

![Energy-level scheme illustrating the Ritz combination principle](figures/fig-1.3-ritz-levels.png)

<!-- figure: cropped from source/p08.jpg -->
A transition $E_l \to E_n$ (frequency $\omega_{ln}$) viewed through an
intermediate level $E_m$: it equals $E_l \to E_m$ plus $E_m \to E_n$, so the
frequencies add, $\omega_{ln} = \omega_{lm} + \omega_{mn}$.

The various spectral series arise from transitions from different higher levels
down to a common lower ("ground") level $E_n$.

> **Why this matters.** The very existence of sharp spectral lines, organized so
> that their frequencies add, is strong evidence that an atom possesses **only
> discrete energy levels** and that energy is absorbed or emitted only in
> quanta of fixed size $\hbar\omega$.

---

## 1.4 The Franck–Hertz experiment
*(Der Franck-Hertz-Versuch)*

<!-- source: source/p09.jpg, source/p10.jpg -->

### The phenomenon

Franck and Hertz (1913) demonstrated the quantization of *energy* directly. An
electron tube is filled with **mercury vapour**; electrons are accelerated
through it and the current is measured as a function of the accelerating
voltage, giving a current–voltage characteristic.

![Franck–Hertz current–voltage characteristic](figures/fig-1.4-franck-hertz.png)

<!-- figure: cropped from source/p10.jpg -->
The current $J$ rises, then drops sharply each time the electrons gain just
enough energy (a further 4.9 eV) to excite a mercury atom, producing regular
maxima and minima at multiples of 4.9 V (4.9, 9.8, 14.7 eV).

### What the characteristic shows

- As long as the electron energy stays **below 4.9 eV**, electrons cross the
  tube without energy loss — they undergo only **elastic** collisions with the
  Hg atoms, and the current rises steadily with voltage.
- The moment the electron energy reaches **4.9 eV**, a collision can transfer
  this exact energy to a mercury atom (an **inelastic** collision). The
  electron is left with almost no kinetic energy, can no longer reach the
  anode, and the **current drops sharply**.
- The excited Hg atom then radiates the absorbed energy as light of wavelength
  $\lambda = 2537\ \text{Å}$ — consistent with $E = \hbar\omega = hc/\lambda
  \approx 4.9\ \text{eV}$.
- At still higher voltages the electron can re-accelerate after a collision and
  the process repeats, producing **regular maxima and minima** in the current
  at multiples of 4.9 V (≈ 4.9, 9.8, 14.7 eV).

### Why it matters

The Franck–Hertz electron-collision experiment is **direct** evidence of a
**discrete energy level** (energy quantization) in the mercury atom: the atom
will only accept energy in a fixed lump of 4.9 eV, never less.

> **"Direct" — in contrast to what?** The spectroscopic evidence of §1.3 is
> *indirect*: the Ritz principle infers discrete levels from the pattern of
> emitted spectral lines, and only by *assuming* the relation $E = \hbar\omega$.
> Franck and Hertz instead measure the energy lost by the electrons themselves —
> reading the level spacing straight off an electrical current — with no
> assumption about light at all. The same number, 4.9 eV, also matches the
> 2537 Å emission line, tying the two kinds of evidence together.

---

## 1.5 The Stern–Gerlach experiment
*(Der Stern-Gerlach-Versuch)*

<!-- source: source/p10.jpg, source/p11.jpg -->

### Force on a magnetic moment

In their 1921 experiment, Stern and Gerlach demonstrated the splitting of an
atomic beam in an **inhomogeneous magnetic field**. An atom with magnetic
moment $\vec m$ in a field $\vec H$ feels not only a torque but, because the
field is non-uniform, also a net **force**. Its potential energy is

$$
V = -\vec m \cdot \vec H
$$

and the force is the negative gradient,

$$
\vec F = -\nabla V = \nabla(\vec m\cdot\vec H) \qquad (1.9)
$$

A uniform field would exert only a torque; the **gradient** is what deflects the
atom, by an amount that depends on the orientation of $\vec m$ relative to the
field.

### The result

A beam of **neutral silver atoms** was sent through the inhomogeneous field and
the distribution of atoms after passing through was measured.

- **Classically**, $\vec m$ could point in any direction, so the beam should
  merely **broaden** into a continuous smear.
- **Observed**: the beam splits into **two distinct sub-beams**.

![Intensity distribution of the silver-atom beam](figures/fig-1.5-stern-gerlach.png)

<!-- figure: cropped from source/p11.jpg -->
Intensity of the silver-atom beam on the detector. Without the field
(ohne Feld) it is a single peak; with the inhomogeneous field (mit Feld) the
beam splits into two — the signature of space quantization.

This means the magnetic moment of the silver atom **cannot take an arbitrary
orientation** relative to the field — only **two opposite settings** are
allowed.

### Why it matters: space quantization

The quantization seen in the atomic world is not restricted to energy and
momentum; it also constrains other physical quantities — here, **orientation**.
The effect is called **space quantization** or **directional quantization**
(*Richtungsquantelung*): it is the quantization of **angular momentum**.

> **Cross-references (Greiner).** The detailed treatment is deferred: the
> angular-momentum operator appears in **Ch. 4** (*Drehimpulsoperator*), and a
> full discussion of the Stern–Gerlach experiment in **Ch. 12**.

---

## Chapter summary

| Experiment | Quantized quantity | Key relation |
|---|---|---|
| Photoelectric effect | energy of light (photons) | $E = \hbar(\omega - \omega_A)$, $E_{\text{ph}}=\hbar\omega$ |
| Compton effect | momentum of light | $\vec p = \hbar\vec k$; $\lambda'-\lambda = \dfrac{2h}{m_0c}\sin^2\frac{\vartheta}{2}$ |
| Ritz combination principle | atomic energy levels | $\omega_{ln} = \omega_{lm} + \omega_{mn}$ |
| Franck–Hertz | atomic energy levels (Hg) | excitation in fixed lump $\approx 4.9$ eV |
| Stern–Gerlach | orientation / angular momentum | beam splits in two; force $\vec F = \nabla(\vec m\cdot\vec H)$ |

The recurring lesson: quantities that classical physics assumes are continuous
— energy, momentum, orientation — are found experimentally to be **discrete**.
Planck's constant $\hbar$ sets the scale of the lumps.
