#!/usr/bin/env python3
"""
Script to validate and update song years using Deezer API.
Checks songs with deezerId against Deezer's release_date and updates if different.

Usage:
    python3 update-years.py
"""

import requests
import re
import time

def extract_songs_from_file(filepath):
    """Extract all songs from the songs.js file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match songs with deezerId
    pattern = r'\{\s*title:\s*"([^"]+)",\s*artist:\s*"([^"]+)",\s*year:\s*(\d+)(?:,\s*youtubeId:\s*"([^"]*)")?(?:,\s*deezerId:\s*"([^"]*)")?\s*\}'
    
    songs = []
    for match in re.finditer(pattern, content):
        song = {
            'title': match.group(1),
            'artist': match.group(2),
            'year': int(match.group(3)),
            'youtubeId': match.group(4) if match.group(4) else None,
            'deezerId': match.group(5) if match.group(5) else None
        }
        songs.append(song)
    
    return songs, content

def fetch_deezer_year(deezer_id):
    """Fetch release year from Deezer API."""
    try:
        url = f"https://api.deezer.com/track/{deezer_id}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            release_date = data.get('release_date')
            
            if release_date:
                # Release date format: YYYY-MM-DD
                year = int(release_date.split('-')[0])
                return year, release_date
        
        return None, None
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None, None

def update_year_in_file(filepath, title, artist, old_year, new_year):
    """Update the year for a specific song in songs.js."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the specific song and update its year
    pattern = rf'(\{{\s*title:\s*"{re.escape(title)}",\s*artist:\s*"{re.escape(artist)}",\s*year:\s*)\d+(\s*,)'
    
    def replacer(match):
        return match.group(1) + str(new_year) + match.group(2)
    
    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    filepath = 'src/data/songs.js'
    
    print("=" * 70)
    print("Year Validator & Updater for Hitster Game")
    print("Validates song years against Deezer API")
    print("=" * 70)
    print()
    
    # Extract songs from file
    print("📖 Reading songs.js file...")
    songs, content = extract_songs_from_file(filepath)
    print(f"✓ Found {len(songs)} songs in file\n")
    
    # Filter songs with Deezer IDs
    songs_with_deezer = [s for s in songs if s['deezerId']]
    
    if not songs_with_deezer:
        print("⚠️  No songs with Deezer IDs found!")
        return
    
    print(f"🔍 Found {len(songs_with_deezer)} songs with Deezer IDs")
    print(f"⏭️  Skipping {len(songs) - len(songs_with_deezer)} songs without Deezer IDs")
    print(f"📏 Only flagging differences of ±2 years or less\n")
    
    print("🎧 Validating years against Deezer API...\n")
    
    updates = []
    errors = []
    correct = []
    large_diff = []
    
    for i, song in enumerate(songs_with_deezer, 1):
        print(f"[{i}/{len(songs_with_deezer)}] {song['title']} - {song['artist']}")
        print(f"  Current year: {song['year']}", end="")
        
        deezer_year, release_date = fetch_deezer_year(song['deezerId'])
        
        if deezer_year is None:
            errors.append(song)
            print(f" → ✗ Failed to fetch from Deezer")
        elif deezer_year != song['year']:
            year_diff = abs(deezer_year - song['year'])
            if year_diff <= 2:
                updates.append({
                    'song': song,
                    'old_year': song['year'],
                    'new_year': deezer_year,
                    'release_date': release_date,
                    'diff': year_diff
                })
                print(f" → ⚠️  MISMATCH! Deezer says {deezer_year} (release: {release_date}) [±{year_diff}y]")
            else:
                large_diff.append({
                    'song': song,
                    'old_year': song['year'],
                    'new_year': deezer_year,
                    'release_date': release_date,
                    'diff': year_diff
                })
                print(f" → ℹ️  Large diff: Deezer says {deezer_year} (release: {release_date}) [±{year_diff}y - SKIPPED]")
        else:
            correct.append(song)
            print(f" → ✓ Correct")
        
        # Small delay to avoid rate limiting
        if i < len(songs_with_deezer):
            time.sleep(0.2)
    
    print()
    print("=" * 70)
    print("SUMMARY:")
    print(f"  ✓ Correct years: {len(correct)}")
    print(f"  ⚠️  Years to update (±2y): {len(updates)}")
    print(f"  ℹ️  Large differences (>2y, skipped): {len(large_diff)}")
    print(f"  ✗ Errors: {len(errors)}")
    print("=" * 70)
    print()
    
    # Show all mismatches within ±2 years
    if updates:
        print("⚠️  YEAR MISMATCHES FOUND (±2 years):\n")
        for update in updates:
            song = update['song']
            print(f"  • {song['title']} by {song['artist']}")
            print(f"    Current: {update['old_year']} → Deezer: {update['new_year']} (released {update['release_date']}) [±{update['diff']}y]")
        
        print()
        response = input("❓ Update all mismatched years in songs.js? (y/n): ").strip().lower()
        
        if response == 'y':
            print("\n💾 Updating songs.js file...")
            for update in updates:
                song = update['song']
                update_year_in_file(
                    filepath, 
                    song['title'], 
                    song['artist'], 
                    update['old_year'], 
                    update['new_year']
                )
            print(f"✓ Updated {len(updates)} song years in {filepath}")
            print("\n📋 Changes made:")
            for update in updates:
                song = update['song']
                print(f"  • {song['title']}: {update['old_year']} → {update['new_year']}")
        else:
            print("\n⏭️  Skipped updates. No changes made.")
    else:
        print("✅ All song years match Deezer data (within ±2 years)!")
    
    # Show large differences that were skipped
    if large_diff:
        print(f"\nℹ️  Large year differences found (>2 years, NOT updated):")
        for item in large_diff:
            song = item['song']
            print(f"  - {song['title']} by {song['artist']}")
            print(f"    Current: {item['old_year']} vs Deezer: {item['new_year']} (±{item['diff']} years)")
    
    # Show errors
    if errors:
        print("\n⚠️  Failed to validate these songs:")
        for song in errors:
            print(f"  - {song['title']} by {song['artist']} (Deezer ID: {song['deezerId']})")
    
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
