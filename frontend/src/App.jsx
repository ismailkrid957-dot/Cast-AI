import './App.css'

const fonctionnalites = [
  {
    numero: '01',
    titre: 'Gestion des scénarios',
    description:
      'Les directeurs de casting peuvent publier et organiser les scénarios des auditions.',
  },
  {
    numero: '02',
    titre: 'Espace candidat',
    description:
      'Les candidats disposent d’un espace dédié pour découvrir les opportunités et participer aux auditions.',
  },
  {
    numero: '03',
    titre: 'Analyse assistée par IA',
    description:
      'Le projet prévoit des outils d’intelligence artificielle pour assister l’analyse des prestations.',
  },
]

function App() {
  return (
    <div className="site-shell">
      <header className="site-header">
        <a className="brand" href="#accueil" aria-label="Cast IA, accueil">
          <span className="brand-mark">C</span>
          <span>cast<span className="brand-accent">ia</span></span>
        </a>

        <nav className="main-nav" aria-label="Navigation principale">
          <a href="#accueil">Accueil</a>
          <a href="#fonctionnalites">Fonctionnalités</a>
          <a href="#apropos">À propos</a>
        </nav>

        <a className="header-link" href="#fonctionnalites">
          Découvrir le projet <span aria-hidden="true">↗</span>
        </a>
      </header>

      <main>
        <section className="hero-section" id="accueil">
          <div className="hero-copy">
            <div className="eyebrow">
              <span className="status-dot" />
              LE CASTING À L’ÈRE DE L’INTELLIGENCE ARTIFICIELLE
            </div>
            <h1>
              Le talent mérite
              <br />
              <span>le premier rôle.</span>
            </h1>
            <p className="hero-description">
              Cast IA simplifie l’organisation des auditions et explore le
              potentiel de l’intelligence artificielle pour accompagner
              l’évaluation des performances.
            </p>
            <div className="hero-actions">
              <a className="button button-primary" href="#fonctionnalites">
                Explorer la plateforme <span aria-hidden="true">→</span>
              </a>
              <a className="text-link" href="#apropos">
                En savoir plus
              </a>
            </div>
            <div className="hero-note">
              <span className="note-line" />
              Une nouvelle approche du processus de casting
            </div>
          </div>

          <div className="hero-visual" aria-label="Illustration abstraite de Cast IA">
            <div className="visual-glow" />
            <div className="visual-orbit orbit-one" />
            <div className="visual-orbit orbit-two" />
            <div className="visual-core">
              <span className="core-letter">C</span>
              <span className="core-caption">CAST IA</span>
            </div>
            <div className="floating-card card-top">
              <span className="floating-icon">✦</span>
              <span>
                <strong>Intelligence</strong>
                <small>au service du casting</small>
              </span>
            </div>
            <div className="floating-card card-bottom">
              <span className="floating-icon">◎</span>
              <span>
                <strong>Talent d’abord</strong>
                <small>Une expérience centralisée</small>
              </span>
            </div>
            <span className="visual-index">01 / 03</span>
          </div>
        </section>

        <section className="intro-strip" id="apropos">
          <p className="strip-label">NOTRE OBJECTIF</p>
          <p className="strip-copy">
            Rassembler les acteurs du casting dans une plateforme claire,
            accessible et pensée pour évoluer avec les outils d’IA.
          </p>
        </section>

        <section className="features-section" id="fonctionnalites">
          <div className="section-heading">
            <div>
              <p className="eyebrow">LA PLATEFORME</p>
              <h2>Un processus plus <span>simple.</span></h2>
            </div>
            <p>
              Une première base pour connecter les directeurs de casting,
              les candidats et les futurs outils d’analyse.
            </p>
          </div>

          <div className="feature-grid">
            {fonctionnalites.map((fonctionnalite) => (
              <article className="feature-card" key={fonctionnalite.numero}>
                <span className="feature-number">{fonctionnalite.numero}</span>
                <div className="feature-arrow" aria-hidden="true">↗</div>
                <h3>{fonctionnalite.titre}</h3>
                <p>{fonctionnalite.description}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="project-status">
          <div className="status-symbol">✳</div>
          <div>
            <p className="eyebrow">UN PROJET EN CONSTRUCTION</p>
            <h2>Les prochaines scènes s’écrivent maintenant.</h2>
            <p>
              Cast IA est actuellement un prototype. Cette interface présente
              la vision du projet ; les fonctionnalités seront intégrées
              progressivement.
            </p>
          </div>
          <span className="prototype-tag">Prototype</span>
        </section>
      </main>

      <footer className="site-footer">
        <a className="brand footer-brand" href="#accueil">
          <span className="brand-mark">C</span>
          <span>cast<span className="brand-accent">ia</span></span>
        </a>
        <p>© {new Date().getFullYear()} Cast IA. Projet académique et technique.</p>
        <a href="#accueil">Retour en haut ↑</a>
      </footer>
    </div>
  )
}

export default App
