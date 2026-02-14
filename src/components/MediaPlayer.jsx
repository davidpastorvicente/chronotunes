import SongPlayer from './SongPlayer';
import ImageHint from './ImageHint';

/**
 * MediaPlayer - Wrapper component that renders appropriate player based on media type
 * @param {object} media - Media item (song or movie object)
 * @param {string} language - Current language
 */
export default function MediaPlayer({ media, language }) {
  if (!media) {
    return null;
  }

  // Check if it's a song (has the artist parameter)
  if (media.artist) {
    return (
      <SongPlayer 
        song={media}
        language={language}
      />
    );
  }

  // It's a movie/show
  return (
    <ImageHint 
      backdropUrl={media.backdropUrl}
      title={media.title}
    />
  );
}
