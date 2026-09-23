-- Create "users" table
CREATE TABLE `users` (
  `id` integer NOT NULL,
  `username` varchar NOT NULL,
  `email` varchar NOT NULL,
  `password_hash` varchar NOT NULL,
  `created_at` datetime NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY (`id`)
);
