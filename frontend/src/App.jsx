import { useState } from 'react'
import './App.css'

const classements = {
  principal: {
    titre: 'Rôle principal',
    profil: 'Femme, 25–35 ans',
    candidats: [
      ['Amira Ben Salem', '96', 'Interprétation', 'Voix'],
      ['Yasmine Trabelsi', '93', 'Présence caméra', 'Expression'],
      ['Nour Gharbi', '91', 'Interprétation', 'Émotion'],
      ['Meriem Kallel', '89', 'Expression', 'Voix'],
      ['Sarra Mansour', '87', 'Présence caméra', 'Interprétation'],
    ],
  },
  secondaire: {
    titre: 'Second rôle',
    profil: 'Homme, 30–45 ans',
    candidats: [
      ['Adam Jaziri', '95', 'Interprétation', 'Voix'],
      ['Youssef Ben Amor', '92', 'Présence caméra', 'Expression'],
      ['Malek Saidi', '90', 'Voix', 'Interprétation'],
      ['Fares Haddad', '88', 'Expression', 'Émotion'],
      ['Ali Mzoughi', '86', 'Présence caméra', 'Voix'],
    ],
  },
  figuration: {
    titre: 'Figuration',
    profil: 'Tous profils',
    candidats: [
      ['Rim Chaabane', '94', 'Disponibilité', 'Expression'],
      ['Sami Dridi', '91', 'Présence caméra', 'Disponibilité'],
      ['Lina Bouaziz', '89', 'Expression', 'Profil'],
      ['Omar Ferjani', '87', 'Disponibilité', 'Profil'],
      ['Ines Khemiri', '85', 'Présence caméra', 'Expression'],
    ],
  },
}

const criteres = [
  {
    numero: '01',
    titre: 'Analyse des auditions',
    description: 'Les prestations vidéo sont examinées à partir de critères définis pour le rôle : interprétation, expression, présence caméra et autres critères pertinents.',
  },
  {
    numero: '02',
    titre: 'Notation et classement',
    description: 'Chaque candidature reçoit une note globale et peut être comparée aux autres profils postulant au même rôle.',
  },
  {
    numero: '03',
    titre: 'Top 15 par rôle',
    description: 'Le producteur retrouve en priorité les quinze candidatures les mieux notées pour chaque rôle et garde la décision finale.',
  },
]

function App() {
  const [roleActif, setRoleActif] = useState('principal')
  const classement = classements[roleActif]

  return (
    <div className="site-shell">
      <header className="site-header">
        <a className="brand" href="#accueil" aria-label="Cast IA, accueil">
          <span className="brand-mark">C</span>
          <span>CAST<span className="brand-accent"> IA</span></span>
        </a>
        <nav className="main-nav" aria-label="Navigation principale">
          <a href="#fonctionnement">Fonctionnement</a>
          <a href="#classement">Classement IA</a>
          <a href="#producteurs">Producteurs</a>
        </nav>
        <a className="header-cta" href="#classement">Voir le concept <span>↗</span></a>
      </header>

      <main>
        <section className="hero-section" id="accueil">
          <div className="hero-copy">
            <p className="eyebrow"><span className="live-dot" /> CASTING INTELLIGENT · AIDE À LA SÉLECTION</p>
            <h1>Le bon rôle.<br /><em>Le bon talent.</em><br />Sans passer à côté.</h1>
            <p className="hero-description">
              Cast IA aide les producteurs à évaluer les candidatures, comparer les auditions et repérer rapidement les profils les mieux adaptés à chaque rôle.
            </p>
            <div className="hero-actions">
              <a className="button button-primary" href="#classement">Découvrir le classement <span>→</span></a>
              <a className="text-link" href="#fonctionnement">Comment ça marche ?</a>
            </div>
            <div className="hero-footnote"><span className="foot-line" /> L’IA assiste la sélection. Le choix final reste au producteur.</div>
          </div>

          <div className="ranking-preview" id="classement">
            <div className="preview-topline">
              <span className="preview-kicker">ESPACE PRODUCTEUR</span>
              <span className="preview-status"><i /> APERÇU DU CLASSEMENT</span>
            </div>
            <div className="preview-heading">
              <div><p className="preview-overline">PROJET · LONG MÉTRAGE</p><h2>Les candidatures</h2></div>
              <span className="film-icon">▣</span>
            </div>
            <div className="role-tabs" role="tablist" aria-label="Choisir un rôle">
              {Object.entries(classements).map(([key, value]) => (
                <button key={key} type="button" role="tab" aria-selected={roleActif === key} className={roleActif === key ? 'role-tab active' : 'role-tab'} onClick={() => setRoleActif(key)}>
                  {value.titre}
                </button>
              ))}
            </div>
            <div className="role-summary">
              <div><strong>{classement.titre}</strong><span>{classement.profil}</span></div>
              <div className="top-count"><strong>TOP 15</strong><span>meilleures notes</span></div>
            </div>
            <div className="candidate-list">
              {classement.candidats.map((candidat, index) => (
                <div className="candidate-row" key={candidat[0]}>
                  <span className={index === 0 ? 'candidate-rank first' : 'candidate-rank'}>{String(index + 1).padStart(2, '0')}</span>
                  <span className="candidate-avatar">{candidat[0].split(' ').map(part => part[0]).slice(0, 2).join('')}</span>
                  <span className="candidate-info"><strong>{candidat[0]}</strong><small>{candidat[2]} · {candidat[3]}</small></span>
                  <span className="candidate-score">{candidat[1]}<small>/100</small></span>
                </div>
              ))}
            </div>
            <div className="preview-bottom"><span>5 profils affichés sur 15</span><span>Exemple fictif · notes simulées</span></div>
          </div>
        </section>

        <section className="value-strip">
          <p>UNE AIDE CONCRÈTE AU CASTING</p>
          <h2>Moins de tri manuel. Plus de temps pour <em>choisir les talents.</em></h2>
        </section>

        <section className="workflow-section" id="fonctionnement">
          <div className="section-intro">
            <p className="eyebrow">DU DOSSIER AU TOP 15</p>
            <h2>Une présélection pensée<br />pour <em>chaque rôle.</em></h2>
            <p>Un processus lisible pour aider l’équipe de production à passer d’un grand volume de candidatures à une sélection ciblée.</p>
          </div>
          <div className="workflow-grid">
            {criteres.map((item) => (
              <article className="workflow-card" key={item.numero}>
                <span className="workflow-number">{item.numero}</span>
                <div className="workflow-mark">{item.numero === '01' ? '◉' : item.numero === '02' ? '↗' : '✳'}</div>
                <h3>{item.titre}</h3>
                <p>{item.description}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="producer-section" id="producteurs">
          <div className="producer-copy">
            <p className="eyebrow">POUR LES PRODUCTEURS</p>
            <h2>La décision vous appartient.<br /><em>Le tri devient plus clair.</em></h2>
            <p>Pour chaque rôle, Cast IA a pour ambition de fournir une liste ordonnée des quinze candidats les mieux notés, avec des éléments d’évaluation consultables pour éclairer la présélection.</p>
          </div>
          <div className="producer-note">
            <span className="note-symbol">✦</span>
            <strong>L’IA est un assistant, pas un décideur.</strong>
            <p>Les notes doivent rester explicables, liées aux exigences du rôle et vérifiables par l’équipe de casting. Le producteur conserve le dernier mot.</p>
          </div>
        </section>

        <section className="prototype-banner">
          <div><span className="eyebrow">ÉTAT DU PROJET</span><h2>Cast IA est en cours de développement.</h2><p>Cette page présente le fonctionnement visé. L’analyse automatique des auditions, la notation IA et le classement réel des quinze meilleurs candidats restent à implémenter et à valider.</p></div>
          <a className="prototype-pill" href="https://github.com/ismailkrid957-dot/spider-el-3ankabout" target="_blank" rel="noopener noreferrer" aria-label="Voir le dépôt GitHub de Cast IA">Prototype ↗</a>
        </section>
      </main>

      <footer className="site-footer">
        <a className="brand" href="#accueil"><span className="brand-mark">C</span><span>CAST<span className="brand-accent"> IA</span></span></a>
        <p>© {new Date().getFullYear()} Cast IA · Projet académique</p>
        <a href="#accueil">Retour en haut ↑</a>
      </footer>
    </div>
  )
}

export default App
