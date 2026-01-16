import { translations } from '../translations';
import './Timeline.css';

export default function Timeline({ timeline, showYears, language }) {
  const t = translations[language];

  if (timeline.length === 0) {
    return (
      <div className="timeline empty">
        <p>{t.noSongs}</p>
      </div>
    );
  }

  // Group songs by year
  const groupedByYear = [];
  let currentGroup = [timeline[0]];
  
  for (let i = 1; i < timeline.length; i++) {
    if (timeline[i].year === timeline[i - 1].year) {
      currentGroup.push(timeline[i]);
    } else {
      groupedByYear.push(currentGroup);
      currentGroup = [timeline[i]];
    }
  }
  groupedByYear.push(currentGroup);

  return (
    <div className="timeline">
      {groupedByYear.map((group, groupIndex) => (
        <div key={groupIndex} className="timeline-year-group">
          <div className="year-group-container">
            {group.map((song, songIndex) => (
              <div key={songIndex} className="song-card">
                <div className="song-info">
                  <div className="song-title">{song.title}</div>
                  <div className="song-artist">{song.artist}</div>
                  {showYears && <div className="song-year">{song.year}</div>}
                </div>
              </div>
            ))}
          </div>
          {groupIndex < groupedByYear.length - 1 && (
            <div className="timeline-arrow">→</div>
          )}
        </div>
      ))}
    </div>
  );
}
