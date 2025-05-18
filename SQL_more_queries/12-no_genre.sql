-- no genre
SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE NOT EXISTS (

)
