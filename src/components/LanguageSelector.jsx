import './LanguageSelector.css';

export default function LanguageSelector({ currentLanguage, onLanguageChange }) {
  return (
    <div className="language-selector">
      <button 
        className={`language-button ${currentLanguage === 'en' ? 'active' : ''}`}
        onClick={() => onLanguageChange('en')}
      >
        🇬🇧 EN
      </button>
      <button 
        className={`language-button ${currentLanguage === 'es' ? 'active' : ''}`}
        onClick={() => onLanguageChange('es')}
      >
        🇪🇸 ES
      </button>
    </div>
  );
}
