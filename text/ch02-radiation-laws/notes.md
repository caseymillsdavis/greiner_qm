# Chapter 2 — Radiation Laws
*(Strahlungsgesetze)*

> Source: Walter Greiner, *Quantum Mechanics: An Introduction*, Chapter 2.
> Screenshots: [`source/p12.jpg`](source/) – [`source/p36.jpg`](source/).

**Theme of the chapter.** Classical physics gave *two* mutually contradictory
formulas for the energy density $\varrho(\omega,T)$ of black-body radiation: the
**Rayleigh–Jeans** law (right at low frequencies, but diverging at high ones —
the "ultraviolet catastrophe") and **Wien's** law (right at high frequencies).
By introducing a new constant $h$, **Planck** found a single law interpolating
between them — and, in doing so, was forced to assume that energy is exchanged
between matter and radiation only in discrete quanta $E = h\nu$. Historically,
this is the birth of quantum mechanics. This chapter builds the black-body
problem from scratch, derives all four laws, and works through Stefan–Boltzmann,
Wien's displacement law, and the cosmic microwave background.

<!-- source: source/p12.jpg -->

---

## 2.1 Preliminaries: radiation from bodies
*(Vorbetrachtung über die Strahlung von Körpern)*

<!-- source: source/p13.jpg, source/p14.jpg -->

### Reflection, and what "black" means

When radiation hits a body it can be **reflected**, **absorbed**, or
**transmitted**. Reflection is *regular* (specular) when incoming and outgoing
rays make equal angles in one plane; it is *diffuse* when the reflected light
goes equally into all directions (a surface that reflects all light diffusely
looks **grey**, or **white** if nothing is absorbed). A body that **absorbs all
incident radiation**, reflecting and transmitting nothing, is called **black**.

### Emissive power and Lambert's cosine law

Let a surface element $dF$ emit (or reflect) radiation into the solid angle
$d\Omega$ at angle $\vartheta$ to its normal. The emitted light current is

$$
J(\omega,T)\cos\vartheta  dF  d\Omega
$$

The quantity $J(\omega,T)$ — the **emissive power** (*Emissionsvermögen* /
*Strahldichte*, radiance) — is the same in all directions for a black surface.
The $\cos\vartheta$ factor is **Lambert's cosine law**: the brightness is
proportional to the *projected* area $dF\cos\vartheta$ seen from the viewing
direction. A glowing black body therefore looks **equally bright from every
angle**, because both the emitted current and the apparent area scale the same
way with $\cos\vartheta$.

---

## 2.2 Cavity (black-body) radiation
*(Hohlraumstrahlung)*

<!-- source: source/p13.jpg, source/p14.jpg, source/p15.jpg, source/p16.jpg -->

**Definition.** Consider a closed cavity whose walls are perfectly black (or
perfectly reflecting) and held at temperature $T$. The radiation field that
builds up inside is **cavity radiation** (*Hohlraumstrahlung*), also called
**black-body radiation**.

### What thermodynamics alone tells us

Without knowing any details of how the walls emit, several conclusions follow
from the **second law of thermodynamics**:

1. After a short time the field reaches **thermal equilibrium** with the walls
   and no longer changes in time.
2. The field is **isotropic and homogeneous**: $J(\omega,T)$ depends only on the
   temperature $T$, not on direction, position, or the material/shape of the
   walls. (If two cavities at the same $T$ had different emissive powers
   $J(\omega,T)$, connecting them would let energy flow from one to the other
   with no temperature difference — a perpetual-motion machine of the second
   kind.)

### Linking emissive power to energy density

We need a relation between two distinct quantities:

- the **emissive power** $J(\omega,T)$ — energy radiated per unit area, per unit
  time, per unit frequency, *per unit solid angle* (i.e. the radiance), and
- the **energy density** $\varrho(\omega,T)$ — energy *stored* per unit volume,
  per unit frequency, summed over all directions and both polarizations.

The bridge between "energy flowing" and "energy stored" is the **Poynting
vector** $\vec S$, the energy flux of an electromagnetic wave: the energy
crossing unit area per unit time (units: power/area). For a wave travelling at
speed $c$, all the energy contained in a column of length $c  dt$ and unit
cross-section pours through the end face in time $dt$, so the flux is simply the
energy density carried forward at speed $c$:

$$
|\vec S| = c  e \qquad\Longleftrightarrow\qquad e = \frac{|\vec S|}{c}
$$

(the same statement as $I_0 = c\varrho$ used in Exercise 2.1 below). Carrying
this through the directional averaging — collecting all waves in $d\omega$,
averaging the flux over propagation directions, and counting both polarizations
— gives the cavity relation

$$
\varrho(\omega,T)  d\omega = \frac{8\pi}{c}  J(\omega,T)  d\omega
\qquad\Longrightarrow\qquad
\boxed{J(\omega,T) = \frac{c}{8\pi} \varrho(\omega,T)} \qquad (2.1)
$$

**Where the $8\pi$ comes from.** It is $8\pi = 2 \times 4\pi$: the $4\pi$ is the
total solid angle (steradians) over which the isotropic radiation is spread, and
the $2$ counts the **two independent polarizations** of light. (In Greiner's
bookkeeping $J$ is the radiance *per polarization*, so the light current sent
into a cone is $2J\cos\vartheta  d\omega  dF  d\Omega$, the $2$ being the
polarization factor; integrating $J$ over the full $4\pi$ then produces the
$8\pi$.) Exercise 2.1 reproduces the same coefficient by working the geometry out
directly.

### Exercise 2.1 — energy density vs. intensity (the $c/8\pi$ factor)

<!-- source: source/p16.jpg, source/p17.jpg, source/p18.jpg -->

Let us see explicitly where the $c/8\pi$ in Eq. (2.1) comes from. The geometry
is worth doing slowly.

**Step 1 — one wave: flux equals energy density times $c$.** Take a single plane
wave filling a cylinder of length $l$ and cross-section $F$ (volume $V = lF$).
All the energy it holds, $E = \varrho V = \varrho l F$, streams out through the
end face in the time $t = l/c$ it takes light to cross the cylinder. The
intensity (power per unit area) is therefore

$$
I_0 = \frac{P}{F} = \frac{E}{F t} = \frac{\varrho  l F}{F (l/c)} = c \varrho
$$

This is the $|\vec S| = c  e$ relation again, now in words: a beam's intensity
is its energy density carried forward at speed $c$.

**Step 2 — isotropic field: share the waves over all directions.** Real cavity
radiation is **isotropic**: it travels equally in every direction. Model it as
$N$ identical plane waves whose propagation directions $\vec k$ are spread
uniformly over the full sphere. "Uniformly over the sphere" is the crucial idea,
so let us be careful about solid angles.

The element of solid angle in spherical coordinates is

$$
d\Omega = \sin\vartheta  d\vartheta  d\varphi, \qquad
\int d\Omega = \int_0^\pi\int_0^{2\pi}\sin\vartheta  d\varphi  d\vartheta = 4\pi
$$

The waves heading into a thin cone at polar angle $\vartheta$ (any azimuth
$\varphi$) form a ring. Doing the azimuthal integral $\int_0^{2\pi} d\varphi =
2\pi$ collapses that ring to the solid angle $2\pi\sin\vartheta  d\vartheta$, and
the **fraction** of the $N$ waves lying in it is its share of the full $4\pi$:

$$
\frac{n_i}{N} = \frac{d\Omega_i}{\Omega}
 = \frac{2\pi\sin\vartheta_i  d\vartheta_i}{4\pi}
 = \tfrac{1}{2}\sin\vartheta_i  d\vartheta_i
$$

The $\sin\vartheta$ is purely geometric: there is very little solid angle near
the poles ($\vartheta\approx 0$) and a lot near the equator
($\vartheta\approx\pi/2$), so most directions point "sideways," not straight
along the axis. This is the factor the text writes down in one line — it is just
the area of a ring on the unit sphere, normalized to the whole sphere.

**Step 3 — power through the aperture (Lambert again).** A wave arriving at angle
$\vartheta_i$ to the surface normal pushes its energy through only the
*projected* opening $F\cos\vartheta_i$, so it contributes the power

$$
P_{0i} = I_0  F\cos\vartheta_i
$$

Each of the $n_i$ waves in the ring contributes this. Summing over rings and
turning the sum into an integral over the **forward hemisphere**
($0 \le \vartheta \le \pi/2$ — the half whose waves actually leave through the
aperture):

$$
I_{\text{ges}} = \frac{P_{\text{ges}}}{F}
 = \sum_i \frac{n_i}{N}  N I_0 \cos\vartheta_i
 = \frac{N I_0}{2}\int_0^{\pi/2}\sin\vartheta\cos\vartheta  d\vartheta
 = \frac{1}{4} N I_0
$$

using $\int_0^{\pi/2}\sin\vartheta\cos\vartheta  d\vartheta = \tfrac{1}{2}$. The
two angular factors — the $\tfrac{1}{2}\sin\vartheta$ from counting directions and
the $\cos\vartheta$ from the Lambert projection — together produce the famous
**factor of $\tfrac{1}{4}$** that links energy density to emitted flux.

**Step 4 — assemble.** With $\varrho = N\varrho_0$ and $I_0 = c\varrho_0$ this is

$$
\boxed{\text{emittance} = I_{\text{ges}} = \frac{c}{4} \varrho} \qquad (2.2)
$$

— the total power radiated per unit area from a black surface (used for the
Stefan–Boltzmann law in §2.6). Finally, since this power leaves into a
**hemisphere** of solid angle $\Omega_H = 2\pi$, the intensity *per unit solid
angle* is

$$
I = \frac{1}{2\pi}  I_{\text{ges}} = \frac{1}{2\pi}\cdot\frac{c}{4} \varrho
 = \frac{c}{8\pi} \varrho
$$

— exactly the coefficient in Eq. (2.1), reached here purely from the geometry.

---

## 2.3 The Rayleigh–Jeans law: counting the cavity modes
*(Rayleigh–Jeanssches Strahlungsgesetz — die Eigenschwingungen des Hohlraums)*

<!-- source: source/p19.jpg, source/p20.jpg, source/p21.jpg, source/p22.jpg -->

**Strategy.** The radiation in the cavity is the electromagnetic field; its
allowed frequencies are the **standing-wave modes** (*Eigenschwingungen*). We
(i) count how many modes lie in $d\omega$, then (ii) give each mode its
classical thermal energy $k_B T$.

### Setting up the modes

Take a cube of side $a$ with perfectly reflecting walls, and ask which
electromagnetic fields can persist inside it.

**The wave equation.** In the empty cavity (no charges or currents) Maxwell's
equations imply that the field propagates as a wave at speed $c$. Working with
the vector potential $\vec A$ (in the Coulomb gauge) for convenience, each of its
components obeys

$$
\nabla^2 \vec A - \frac{1}{c^2}\frac{\partial^2 \vec A}{\partial t^2} = 0
$$

The operator on the left — the Laplacian minus $1/c^2$ times the second time
derivative — is the **d'Alembertian** (wave operator), often abbreviated
$\Box\vec A = 0$. In words: the way the field curves in space, $\nabla^2\vec A$,
is locked to how it accelerates in time, $\partial^2\vec A/\partial t^2$, and the
proportionality constant $1/c^2$ is exactly what makes the disturbance travel at
speed $c$. (The electric and magnetic fields obey the same equation; using
$\vec A$ just keeps the algebra short. Here $\nabla^2 = \Delta$ is the Laplacian.)

**The potential and the Coulomb gauge.** A word on "$\vec A$ in the Coulomb
gauge," since we lean on it twice. The measurable fields are $\vec E$ and
$\vec B$; they can always be written through a scalar potential $\phi$ and a
vector potential $\vec A$ as $\vec B = \nabla\times\vec A$ and
$\vec E = -\nabla\phi - \partial\vec A/\partial t$. But the potentials are **not
unique**: the replacement $\vec A \to \vec A + \nabla\chi$,
$\phi \to \phi - \partial\chi/\partial t$ — for *any* function $\chi(\vec r,t)$ —
leaves $\vec E$ and $\vec B$, and hence all physics, completely unchanged. This
built-in redundancy is **gauge freedom**, and to *choose a gauge* is to impose
one extra condition on $\vec A$ that pins the freedom down. The **Coulomb gauge**
is the choice

$$
\nabla\cdot\vec A = 0
$$

(also called the *transverse* or *radiation* gauge). In a source-free region it
buys us exactly the two things we use: the scalar potential can be taken as
$\phi = 0$, so $\vec A$ alone carries the field and obeys the clean wave equation
above; and $\nabla\cdot\vec A = 0$ forces the waves to be **transverse** — for a
plane wave $\vec A \propto e^{-i\vec k\cdot\vec r}$ the condition becomes
$\vec A\cdot\vec k = 0$, i.e. $\vec A$ is perpendicular to the propagation
direction $\vec k$. That transversality is what leaves **two** independent
polarizations for each $\vec k$ (two directions perpendicular to it) — the factor
of $2$ we keep meeting.

**Why we can separate off the time.** The wave equation is *linear* and its
coefficients do not depend on time. That lets us look for solutions that oscillate
**harmonically** at a single frequency $\omega$ — the **normal modes** (standing
waves) of the cavity:

$$
\vec A(\vec r,t) = \vec A(\vec r)  e^{i\omega t}
$$

(equally $\vec A(\vec r)\sin\omega t$ or $\cos\omega t$; the complex exponential
is just convenient bookkeeping). This is **separation of variables**: we assume
the space- and time-dependence factorize into a product
$\vec A(\vec r)\cdot(\text{function of }t)$. It costs no generality, because
linearity guarantees that the most general field is a superposition (a Fourier
sum) of such single-frequency pieces — so it is enough to understand one
frequency at a time. Physically, a closed cavity "rings" at a discrete set of
frequencies, exactly like an organ pipe or a drumhead; each ringing pattern is
one mode.

**The Helmholtz equation.** Substitute the separated form into the wave equation.
The time derivative gives $\partial^2_t e^{i\omega t} = -\omega^2 e^{i\omega t}$,
and the common factor $e^{i\omega t}$ cancels, leaving a purely *spatial*
equation for $\vec A(\vec r)$:

$$
\nabla^2 \vec A(\vec r) + \frac{\omega^2}{c^2}\vec A(\vec r) = 0
$$

Introducing the wavenumber $k = \omega/c$, this is the **Helmholtz equation**

$$
\left(\Delta + \frac{\omega^2}{c^2}\right)\vec A(\vec r)
 = (\Delta + k^2)\vec A(\vec r) = 0, \qquad k=\frac{\omega}{c}
$$

The Helmholtz equation is simply the time-independent ("stationary") form of the
wave equation: an **eigenvalue problem** for the Laplacian, asking which spatial
patterns reproduce themselves — up to the constant factor $-k^2$ — under
$\nabla^2$. Which values of $k$ (and hence which frequencies $\omega = ck$) are
allowed is then decided entirely by the **boundary conditions** at the walls.
That is the standing-wave condition we impose next; it is the three-dimensional
version of the rule that fixes the allowed pitches of a vibrating string.

Two physical constraints fix the modes:

- **Transversality** (Coulomb gauge $\nabla\cdot\vec A=0$, i.e.
  $\vec A\cdot\vec k=0$): each $\vec k$ carries **two** independent polarizations.
- **Reflecting walls**: the tangential field must vanish on the faces, forcing
  $\sin(k_x a)=\sin(k_y a)=\sin(k_z a)=0$, hence

$$
k_x = n_x\frac{\pi}{a}, \quad k_y = n_y\frac{\pi}{a}, \quad k_z = n_z\frac{\pi}{a},
\qquad n_x,n_y,n_z = 1,2,3,\dots
$$

The $n_i$ are positive (standing waves only). Each allowed mode is one lattice
point in $n$-space, so the number of modes in $(dn_x  dn_y  dn_z)$ is just that
volume.

### Counting in $k$-space

Switch to spherical coordinates with $n^2 = n_x^2+n_y^2+n_z^2$. Only the **first
octant** counts (all $n_i>0$), giving a shell volume
$\tfrac{1}{8}\cdot 4\pi n^2  dn = \tfrac{1}{2}\pi n^2  dn$. Using
$n = (a/\pi)k$ and then $k=\omega/c$:

$$
\frac{1}{2}\pi n^2  dn = \frac{1}{2}\pi\left(\frac{a}{\pi}\right)^3 k^2  dk
 = \frac{V}{2\pi^2 c^3} \omega^2  d\omega = dN'(\omega)
$$

with $V=a^3$. Including the **two polarizations** doubles this, giving the
**density of electromagnetic modes**:

$$
\boxed{\frac{dN(\omega)}{d\omega} = \frac{V}{\pi^2 c^3} \omega^2} \qquad (2.3)
$$

### From mode count to the law

In classical statistical mechanics each oscillator (each mode) carries a mean
energy $k_B T$ — *not* $\tfrac{1}{2}k_B T$: an oscillator has $\tfrac{1}{2}k_B T$
in kinetic **and** $\tfrac{1}{2}k_B T$ in potential energy (virial theorem).
Multiplying the mode density by $k_B T$ and dividing by $V$ gives the
**Rayleigh–Jeans law**:

$$
\boxed{\varrho(\omega,T) = \frac{k_B T}{\pi^2 c^3} \omega^2} \qquad (2.4)
$$

and via Eq. (2.1), $J(\omega,T) = \dfrac{k_B T}{8\pi^3 c^2} \omega^2$.

### The ultraviolet catastrophe

Equation (2.4) matches experiment only at **low** frequencies. It cannot be
right at high $\omega$: $\varrho \propto \omega^2$ grows without bound, and the
total energy $\int_0^\infty \varrho  d\omega$ **diverges**. Physically absurd —
the classical equipartition of energy over infinitely many high-frequency modes
is the culprit.

> **Why this matters.** The divergence is not a small discrepancy but a
> catastrophe built into classical physics. Its resolution *requires* abandoning
> the idea that a mode can hold any amount of energy.

---

## 2.4 Planck's radiation law (Einstein's derivation)
*(Das Plancksche Strahlungsgesetz)*

<!-- source: source/p23.jpg, source/p24.jpg, source/p25.jpg, source/p26.jpg -->

Rather than counting modes classically, Einstein's later derivation tracks the
**photons** through emission and absorption between two atomic levels
$E_m > E_n$, with $\omega = (E_m - E_n)/\hbar$. Three processes occur, each for a
photon of polarization $\alpha$ into solid angle $d\Omega$:

| Process | Probability |
|---|---|
| Spontaneous emission | $dW_e' = a^n_{m\alpha}  d\Omega$ |
| Induced emission | $dW_e'' = b^n_{m\alpha}  \varrho_\alpha  d\Omega$ |
| Absorption | $dW_a = b^m_{n\alpha}  \varrho_\alpha  d\Omega$ |

Here $\varrho_\alpha(\omega,T,\Omega)$ is the spectral energy density **for one
polarization, per unit solid angle**, so that $\varrho_\alpha = \tfrac{1}{8\pi}\varrho$
(two polarizations $\times\ 4\pi$ steradians). Induced emission and absorption
are proportional to $\varrho_\alpha$ (more photons present → more transitions);
spontaneous emission is not.

### The equilibrium condition

In equilibrium the number of upward transitions equals the number of downward
ones, $N_m(dW_e' + dW_e'') = N_n  dW_a$:

$$
N_m\big(a^n_{m\alpha} + b^n_{m\alpha}\varrho_\alpha\big)
 = N_n  b^m_{n\alpha} \varrho_\alpha
$$

The level populations follow the **Boltzmann distribution**,

$$
\frac{N_n}{N_m} = \frac{e^{-E_n/k_B T}}{e^{-E_m/k_B T}} = e^{\hbar\omega/k_B T}
$$

Solving for $\varrho_\alpha$ and demanding that $\varrho_\alpha\to\infty$ as
$T\to\infty$ (where the exponential $\to 1$) forces the **detailed-balance
relation** $b^n_{m\alpha} = b^m_{n\alpha}$. The result is

$$
\varrho_\alpha(\omega,T,\Omega)
 = \frac{a^n_{m\alpha}}{b^n_{m\alpha}}\cdot\frac{1}{e^{\hbar\omega/k_B T}-1}
$$

### Fixing the coefficient ratio

The ratio $a/b$ is a property of the atom, so we may pin it down in any
convenient limit. For small $\omega$, expanding
$1/(e^{\hbar\omega/k_BT}-1)\approx k_B T/\hbar\omega$ and matching to
Rayleigh–Jeans, Eq. (2.4) (remembering $\varrho_\alpha = \varrho/8\pi$), gives

$$
\frac{a^n_{m\alpha}}{b^n_{m\alpha}} = \frac{1}{8\pi^3}\frac{\hbar\omega^3}{c^3}
$$

Substituting back and summing over both polarizations and all solid angles
($\varrho = 8\pi\varrho_\alpha$) yields **Planck's radiation law**:

$$
\boxed{\varrho(\omega,T) = \frac{\hbar\omega^3}{\pi^2 c^3}\cdot
\frac{1}{e^{\hbar\omega/k_B T}-1}} \qquad (2.5)
$$

and the corresponding emissive power

$$
J(\omega,T)  d\omega = \frac{\hbar\omega^3}{8\pi^3 c^2}\cdot
\frac{1}{e^{\hbar\omega/k_B T}-1}  d\omega \qquad (2.6)
$$

### The two classical limits

- **Low frequency** ($\hbar\omega \ll k_B T$): $e^{\hbar\omega/k_BT}-1\approx
  \hbar\omega/k_B T$, recovering Rayleigh–Jeans, Eq. (2.4).
- **High frequency** ($\hbar\omega \gg k_B T$): $e^{\hbar\omega/k_BT}-1\approx
  e^{\hbar\omega/k_BT}$, giving **Wien's law**

$$
\varrho(\omega,T) = \frac{\hbar\omega^3}{\pi^2 c^3}  e^{-\hbar\omega/k_B T}
\qquad (\hbar\omega \gg k_B T) \qquad (2.7)
$$

Planck's single formula thus contains both classical laws as limiting cases.

### Wave vs. particle character (a number-density argument)

<!-- source: source/p26.jpg, source/p27.jpg -->

Comparing the photon **number densities** of the Wien and Rayleigh–Jeans regimes
at two frequencies $\omega_2 \gg \omega_1$ gives

$$
\frac{dN_W}{dN_{RJ}} = \frac{e^{-\hbar\omega_2/k_B T} \hbar\omega_2^2}{k_B T \omega_1}
\ll 1
$$

So the **wave** character of light dominates where there are **many low-energy
photons** (Rayleigh–Jeans regime), while the **particle** character shows up for
**few high-energy photons** (Wien regime).

---

## 2.5 Planck's own derivation (Exercise 2.2)
*(Die Ableitung des Planckschen Strahlungsgesetzes nach Planck)*

<!-- source: source/p27.jpg, source/p28.jpg, source/p29.jpg -->

Planck's historical route differs from Einstein's and shows exactly where the
quantum enters. Using the same mode density, Eq. (2.3), the energy density is

$$
\varrho(\omega,T) = \frac{1}{V}\frac{dN}{d\omega} \bar\varepsilon(\omega,T)
 = \frac{1}{\pi^2 c^3} \omega^2 \bar\varepsilon(\omega,T)
$$

where $\bar\varepsilon$ is the **mean energy of a mode** at temperature $T$.
Classical equipartition sets $\bar\varepsilon = k_B T$, reproducing
Rayleigh–Jeans — and its catastrophe.

**Planck's hypothesis.** Instead, let a harmonic mode of frequency $\omega$ take
only the **discrete** energies

$$
\varepsilon_n = n \hbar\omega, \qquad n = 0,1,2,\dots
$$

The mean energy in thermal equilibrium is then a Boltzmann-weighted sum, neatly
written with the **partition function** $Z=\sum_n e^{-\beta\varepsilon_n}$,
$\beta = 1/k_B T$:

$$
\bar\varepsilon = \frac{\sum_n \varepsilon_n e^{-\beta\varepsilon_n}}
{\sum_n e^{-\beta\varepsilon_n}} = -\frac{d}{d\beta}\ln Z
$$

The geometric series sums to $Z=\sum_n (e^{-\beta\hbar\omega})^n
= \dfrac{1}{1-e^{-\beta\hbar\omega}}$, and so

$$
\boxed{\bar\varepsilon = \frac{\hbar\omega}{e^{\hbar\omega/k_B T}-1}} \qquad (2.8)
$$

Inserting this gives Planck's law again, Eq. (2.5) — identical to the Einstein
derivation. The limits reproduce $\bar\varepsilon = k_B T$ for small $\omega/T$
(classical) and $\bar\varepsilon = \hbar\omega  e^{-\hbar\omega/k_B T}$ for large
$\omega/T$ (Wien).

> **Reading $\bar\varepsilon$.** The factor $1/(e^{\hbar\omega/k_BT}-1)$ is the
> **mean number of photons** $\bar n$ in a mode of energy $\hbar\omega$; the mode
> energy is then $\bar\varepsilon = \bar n \hbar\omega$. Quantizing the
> oscillator energy is what tames the high-frequency modes: when
> $\hbar\omega \gg k_B T$, even one quantum is too expensive thermally, so those
> modes are effectively frozen out and the sum over modes converges.

---

## 2.6 The Stefan–Boltzmann law (Exercise 2.3)
*(Strahlung eines schwarzen Körpers — Gesamtenergie $\propto T^4$)*

<!-- source: source/p30.jpg, source/p31.jpg, source/p32.jpg -->

### Planck's law as Bose–Einstein statistics

Photons are **spin-1 bosons**; the mean occupation of a state of energy
$E=\hbar\omega$ at temperature $T$ is the **Bose–Einstein distribution**
$f_{BE} = (e^{\hbar\omega/k_B T}-1)^{-1}$. Multiplying the mode density by
$f_{BE}$ and by the photon energy $\hbar\omega$ reproduces Planck's law directly:

$$
\frac{1}{V}\frac{dE}{d\omega} = \frac{1}{V}\frac{dN}{d\omega} f_{BE} \hbar\omega
 = \frac{\hbar\omega^3}{\pi^2 c^3}\frac{1}{e^{\hbar\omega/k_B T}-1}
$$

### Integrating over all frequencies

The total energy density is

$$
\frac{E}{V} = \int_0^\infty \frac{\hbar\omega^3}{\pi^2 c^3}
\frac{d\omega}{e^{\hbar\omega/k_B T}-1}
 = \frac{(k_B T)^4}{\pi^2 c^3 \hbar^3}\int_0^\infty \frac{q^3  dq}{e^q-1}
$$

using the substitution $q=\hbar\omega/k_B T$. The dimensionless integral is

$$
\int_0^\infty \frac{q^3}{e^q-1}  dq
 = \sum_{n=0}^\infty \int_0^\infty q^3 e^{-(n+1)q}  dq
 = 6\sum_{n=0}^\infty \frac{1}{(n+1)^4} = \frac{\pi^4}{15}
$$

(expanding $1/(e^q-1)=\sum e^{-(n+1)q}$ and using
$\sum 1/n^4 = \pi^4/90$). Therefore the **Stefan–Boltzmann law**:

$$
\boxed{\frac{E}{V} = a  T^4, \qquad a = \frac{\pi^2 k_B^4}{15 \hbar^3 c^3}
\approx 7.56\times 10^{-15}\ \frac{\text{erg}}{\text{cm}^3 \text{K}^4}} \qquad (2.9)
$$

### From energy density to radiated power

Using the emittance relation, Eq. (2.2), a black surface radiates

$$
\varepsilon(T) = \frac{c}{4}\frac{E}{V} = \sigma T^4, \qquad
\sigma = \frac{c}{4}a \approx 5.4\times 10^{-5}\ \frac{\text{erg}}{\text{cm}^2 \text{s} \text{K}^4}
$$

(The factor $c/4$ comes from integrating $K\cos\vartheta$ over the forward
hemisphere: $\varepsilon = \pi K = \tfrac{c}{4}\tfrac{E}{V}$.)

### Application: the temperature of the Sun

Stars radiate approximately as black bodies. With the Sun's radius
$R = 0.7\times 10^{11}$ cm, the total emitted power is
$4\pi R^2\sigma T^4 = 3.34\times 10^{18}  T^4\ \text{erg/s}$. Spread over a
sphere of radius equal to the Earth–Sun distance $1.5\times 10^{13}$ cm, the flux
at Earth is $0.96\times 10^{-9}  T^4\ \text{erg/cm}^2\text{s}$. Setting this
equal to the measured **solar constant** ($1.94\ \text{cal/cm}^2\text{min}
= 1.36\times 10^6\ \text{erg/cm}^2\text{s}$) gives

$$
T^4 = 1.52\times 10^{15}\ \text{K}^4 \quad\Longrightarrow\quad T \approx 6000\ \text{K}
$$

---

## 2.7 Wien's displacement law (Exercise 2.4)
*(Das Wiensche Verschiebungsgesetz)*

<!-- source: source/p33.jpg, source/p34.jpg -->

**Goal.** Find the wavelength $\lambda_{\max}$ at which the spectral density
peaks, and show $\lambda_{\max} T = \text{const}$.

Maximize Planck's density in $\omega$ by setting $d\varrho/d\omega = 0$. With
$x = \hbar\omega/k_B T$ this reduces to the transcendental equation

$$
3 - \frac{\hbar\omega}{k_B T} \frac{e^{\hbar\omega/k_B T}}{e^{\hbar\omega/k_B T}-1} = 0
\qquad\Longleftrightarrow\qquad e^x = \left(1 - \frac{x}{3}\right)^{-1}
$$

Besides the trivial $x=0$ (a minimum), this has one positive root
$x_{\max}\approx 2.82$ (solved graphically/numerically). Hence
$\hbar\omega_{\max}/k_B T = x_{\max}$, i.e. $\omega_{\max} \propto T$.

> **A subtlety worth flagging.** The peak location depends on *which variable*
> you bin by. The maximum of the density per unit **frequency** $\varrho(\omega)$
> sits at $x\approx 2.82$; converting that frequency to a wavelength via
> $\omega = 2\pi c/\lambda$ gives $\lambda T \approx 0.51\ \text{cm·K}$. But the
> maximum of the density per unit **wavelength** $\varrho(\lambda)$ sits at a
> *different* point (the Jacobian $|d\omega/d\lambda|\propto\lambda^{-2}$ shifts
> it), namely $y\approx 4.965$, giving the standard Wien constant

$$
\boxed{\lambda_{\max}  T \approx 0.29\ \text{cm·K} = 2.9\times 10^{-3}\ \text{m·K}} \qquad (2.10)
$$

For the Sun ($T\approx 6000$ K) this gives $\lambda_{\max} = 0.29/6000\ \text{cm}
\approx 4800\ \text{Å}$ — yellow visible light. The estimate lands within ~20% of
the exact value. The law says the hottest bodies glow at the shortest
wavelengths (red-hot → white-hot → blue), and lets one read a star's temperature
from the colour of its peak.

---

## 2.8 Energy emitted in a spectral band (Exercise 2.5)
*(Emittierte Energien eines schwarzen Strahlers)*

<!-- source: source/p34.jpg -->

**Problem.** For a black body at $T = 2000$ K, compare the energy emitted in two
$100\ \text{Å}$-wide bands, one centred at $\lambda_1 = 5000\ \text{Å}$ (visible),
one at $\lambda_2 = 50000\ \text{Å}$ (infrared).

Converting Planck's law to a *per-wavelength* density with $\omega = 2\pi c/\lambda$:

$$
\left|\frac{dE}{d\lambda}\right| = \frac{8\pi h c}{\lambda^5}
\left(e^{hc/k_B T\lambda}-1\right)^{-1}
$$

Since the bands are narrow, the ratio is just the ratio of $|dE/d\lambda|$ at the
two centres. With $hc = 12400\ \text{eV·Å}$ and $k_B = 8.62\times 10^{-5}\ \text{eV/K}$,

$$
W = \frac{dE/d\lambda\big|_{\lambda_2}}{dE/d\lambda\big|_{\lambda_1}} = 5.50
$$

i.e. at 2000 K the body radiates several times more in this infrared band than in
the visible one — **only a small fraction of the energy comes out as visible
light**.

---

## 2.9 The cosmic microwave background (Exercise 2.6)
*(Kosmische Schwarzkörperstrahlung)*

<!-- source: source/p35.jpg, source/p36.jpg -->

Black-body radiation regained prominence with cosmology. The **Big Bang**
("Urknall") model (Gamow; Alpher, Bethe, Gamow) predicts that the intense
radiation from the early universe should survive today as a black-body field at
a few kelvin. After unreliable early estimates (~25 K), **Penzias and Wilson**
(1964) detected a strong, isotropic thermal "noise" with their radio antenna;
the group around **Dicke** (with Peebles, Roll, Wilkinson) interpreted it as
relic cavity radiation at $T = 2.65 \pm 0.09\ \text{K}$ (modern value
$\approx 2.7$ K). Its near-perfect black-body spectrum is among the strongest
pieces of evidence for the Big Bang. Tiny anisotropies also reveal our motion
relative to this radiation field: the Solar System drifts at less than
$\approx 300\ \text{km/s}$ relative to the CMB.

---

## Chapter summary

| Law | Result | Validity |
|---|---|---|
| Emissivity ↔ energy density | $J = \dfrac{c}{8\pi}\varrho$ | always (cavity) |
| Mode density | $\dfrac{dN}{d\omega} = \dfrac{V}{\pi^2c^3}\omega^2$ | cavity eigenmodes |
| Rayleigh–Jeans | $\varrho = \dfrac{k_B T}{\pi^2c^3}\omega^2$ | low $\omega$; diverges at high $\omega$ |
| Wien | $\varrho = \dfrac{\hbar\omega^3}{\pi^2c^3}e^{-\hbar\omega/k_BT}$ | high $\omega$ |
| **Planck** | $\varrho = \dfrac{\hbar\omega^3}{\pi^2c^3}\dfrac{1}{e^{\hbar\omega/k_BT}-1}$ | all $\omega$ |
| Stefan–Boltzmann | $E/V = aT^4$, $\varepsilon = \sigma T^4$ | total energy |
| Wien displacement | $\lambda_{\max}T \approx 0.29$ cm·K | peak wavelength |

**The lesson.** The classical mistake was equipartition — handing every mode
$k_B T$, no matter how high its frequency. Planck's quantization
$\varepsilon_n = n\hbar\omega$ makes high-frequency modes thermally
unaffordable, cutting off the ultraviolet catastrophe and producing a finite,
correct spectrum. The constant $h$ introduced here to "interpolate" between two
classical laws turned out to be the cornerstone of all of quantum mechanics.
