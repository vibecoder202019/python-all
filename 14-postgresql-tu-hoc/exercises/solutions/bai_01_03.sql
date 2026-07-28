-- Giải bài 1–3 (schema demo)
SET search_path TO demo;

CREATE TABLE IF NOT EXISTS genres (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS book_genres (
    book_id  INTEGER REFERENCES books(id),
    genre_id INTEGER REFERENCES genres(id),
    PRIMARY KEY (book_id, genre_id)
);

INSERT INTO genres (name) VALUES ('Văn học'), ('Kinh dị'), ('Self-help')
ON CONFLICT (name) DO NOTHING;

INSERT INTO book_genres (book_id, genre_id)
SELECT 1, id FROM genres WHERE name = 'Văn học'
ON CONFLICT DO NOTHING;
INSERT INTO book_genres (book_id, genre_id)
SELECT 3, id FROM genres WHERE name = 'Kinh dị'
ON CONFLICT DO NOTHING;

-- Bài 2
SELECT b.title, a.name AS author, g.name AS genre
FROM books b
JOIN authors a ON b.author_id = a.id
LEFT JOIN book_genres bg ON b.id = bg.book_id
LEFT JOIN genres g ON bg.genre_id = g.id
ORDER BY g.name NULLS LAST, b.title;

-- Bài 3
SELECT a.country,
       COUNT(DISTINCT a.id) AS authors,
       COUNT(b.id) AS books,
       ROUND(AVG(b.price), 0) AS avg_price
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
GROUP BY a.country;
