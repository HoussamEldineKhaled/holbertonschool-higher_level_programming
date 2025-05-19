-- no genre
SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE NOT EXISTS (
SELECT 1
FROM tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id
)
ORDER BY tv_shows.title ASC;
