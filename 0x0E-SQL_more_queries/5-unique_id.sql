-- Create table `unique_id` with unique constraint on `id`
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
