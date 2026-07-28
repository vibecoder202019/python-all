-- Dự án Library — Bước 1: Schema cơ bản
SET search_path TO library;

CREATE TABLE authors (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    country    VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE books (
    id         SERIAL PRIMARY KEY,
    title      VARCHAR(200) NOT NULL,
    isbn       VARCHAR(20) UNIQUE,
    author_id  INTEGER NOT NULL REFERENCES authors(id) ON DELETE RESTRICT,
    price      NUMERIC(10, 2) CHECK (price >= 0),
    copies     INTEGER DEFAULT 1 CHECK (copies >= 0),
    published  DATE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE members (
    id         SERIAL PRIMARY KEY,
    email      VARCHAR(100) UNIQUE NOT NULL,
    name       VARCHAR(100) NOT NULL,
    phone      VARCHAR(20),
    joined_at  DATE DEFAULT CURRENT_DATE,
    active     BOOLEAN DEFAULT TRUE
);

CREATE TABLE loans (
    id          SERIAL PRIMARY KEY,
    book_id     INTEGER NOT NULL REFERENCES books(id),
    member_id   INTEGER NOT NULL REFERENCES members(id),
    loan_date   DATE DEFAULT CURRENT_DATE,
    due_date    DATE NOT NULL,
    return_date DATE,
    status      VARCHAR(20) DEFAULT 'active'
        CHECK (status IN ('active', 'returned', 'overdue'))
);

-- Seed data
INSERT INTO authors (name, country) VALUES
    ('Nguyễn Nhật Ánh', 'Việt Nam'),
    ('Haruki Murakami', 'Nhật Bản'),
    ('Paulo Coelho', 'Brazil'),
    ('J.K. Rowling', 'Anh');

INSERT INTO books (title, isbn, author_id, price, copies, published) VALUES
    ('Cho tôi xin một vé đi tuổi thơ', '978-604-1-001', 1, 85000, 5, '2008-01-01'),
    ('Mắt biếc', '978-604-1-002', 1, 92000, 3, '2010-01-01'),
    ('Kafka bên bờ biển', '978-604-2-001', 2, 120000, 2, '2002-01-01'),
    ('Harry Potter 1', '978-604-4-001', 4, 150000, 4, '1997-06-26'),
    ('Alchemist', '978-604-3-001', 3, 75000, 6, '1988-01-01');

INSERT INTO members (email, name, phone) VALUES
    ('minh@example.com', 'Nguyễn Văn Minh', '0901234567'),
    ('lan@example.com', 'Trần Thị Lan', '0912345678'),
    ('hoa@example.com', 'Lê Thị Hoa', '0923456789');

SELECT '=== Schema + seed data ===' AS info;
SELECT 'authors' AS tbl, COUNT(*) FROM authors
UNION ALL SELECT 'books', COUNT(*) FROM books
UNION ALL SELECT 'members', COUNT(*) FROM members;
