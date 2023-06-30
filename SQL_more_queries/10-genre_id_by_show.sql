-- Lists all shows in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show_genres, tv_shows 
WHERE tv_show_genres.show_id = tv_shows.id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;