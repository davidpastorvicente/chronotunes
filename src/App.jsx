import { useState } from 'react'
import GameSetup from './components/GameSetup'
import GameBoard from './components/GameBoard'
import LanguageSelector from './components/LanguageSelector'
import './App.css'

function App() {
  const [gameStarted, setGameStarted] = useState(false)
  const [teams, setTeams] = useState([])
  const [winningScore, setWinningScore] = useState(10)
  const [language, setLanguage] = useState('es')
  const [songSet, setSongSet] = useState('everything')

  const handleStartGame = (teamNames, targetScore, selectedSongSet) => {
    setTeams(teamNames)
    setWinningScore(targetScore)
    setSongSet(selectedSongSet)
    setGameStarted(true)
  }

  return (
    <div className="app">
      <LanguageSelector currentLanguage={language} onLanguageChange={setLanguage} />
      {!gameStarted ? (
        <GameSetup onStartGame={handleStartGame} language={language} />
      ) : (
        <GameBoard teams={teams} winningScore={winningScore} language={language} songSet={songSet} />
      )}
    </div>
  )
}

export default App
