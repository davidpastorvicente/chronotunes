import { songSets } from '../data/songs';
import { movieSets } from '../data/movies';

/**
 * Load media items based on category and content set
 * @param {string} category - 'songs', 'movies', or 'all'
 * @param {string} contentSet - 'everything', 'english', 'spanish', or 'new'
 * @returns {Array} Array of media items
 */
export function loadMediaByCategory(category, contentSet) {
  let selectedMedia;
  
  if (category === 'songs') {
    selectedMedia = songSets[contentSet]?.songs || songSets.everything.songs;
  } else if (category === 'movies') {
    selectedMedia = movieSets[contentSet]?.movies || movieSets.everything.movies;
  } else if (category === 'all') {
    // Mix both songs and movies
    const songs = songSets[contentSet]?.songs || songSets.everything.songs;
    const movies = movieSets[contentSet]?.movies || movieSets.everything.movies;
    selectedMedia = [...songs, ...movies];
  }
  
  return selectedMedia;
}
