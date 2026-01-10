# Hitster Game

A music guessing game where teams build timelines by placing songs in chronological order.

## 🎮 How to Play

1. **Setup Teams**: Choose 2-6 teams and set a winning score (5, 10, 15, or 20 songs)
2. **Listen**: Each turn, a team hears a mystery song
3. **Guess**: Place the song in your timeline (before, between, or after existing songs)
4. **Build**: Correct placements add the song to your timeline
5. **Win**: First team to reach the target number of songs wins!

## 🎵 Song Library

The game includes 35 curated iconic songs from 1960-2025:
- 1960s: The Beatles, Bob Dylan, Aretha Franklin, The Beach Boys
- 1970s: Queen, Led Zeppelin, Eagles, Bee Gees, John Lennon
- 1980s: Michael Jackson, Guns N' Roses, Madonna, The Police
- 1990s: Nirvana, Oasis, Spice Girls, TLC, Britney Spears
- 2000s: Beyoncé, OutKast, Amy Winehouse, Rihanna, The Killers
- 2010s: Adele, Bruno Mars, Pharrell, Ed Sheeran, Billie Eilish
- 2020s: The Weeknd, Dua Lipa, Olivia Rodrigo, Taylor Swift, Miley Cyrus

## 🚀 Getting Started

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open browser to http://localhost:5173
```

## 🛠 Tech Stack

- **React** - UI framework
- **Vite** - Build tool
- **YouTube Embeds** - Audio playback
- **CSS3** - Styling with modern gradients

## 📝 Features

- ✅ Turn-based gameplay for multiple teams
- ✅ Configurable winning conditions
- ✅ Hidden song playback (no spoilers!)
- ✅ Play/Pause controls
- ✅ Visual timeline display
- ✅ Immediate feedback on correct/incorrect placements
- ✅ Winner announcement with full timeline
- ✅ Modern dark theme UI

## 🎨 Customization

To add more songs, edit `src/data/songs.js`:

```javascript
{
  id: 36,
  title: "Your Song Title",
  artist: "Artist Name",
  year: 2024,
  youtubeId: "youtube_video_id"
}
```

## 📦 Project Structure

```
src/
├── components/
│   ├── GameSetup.jsx       # Team configuration
│   ├── GameBoard.jsx       # Main game logic
│   ├── Timeline.jsx        # Timeline display
│   ├── SongPlayer.jsx      # Audio player
│   └── PlacementButtons.jsx # Placement controls
├── data/
│   └── songs.js            # Curated song library
└── App.jsx                 # Root component
```

## 🎯 No API Keys Required!

This version uses a curated song list - just clone and play!

---

Enjoy the game! 🎵
