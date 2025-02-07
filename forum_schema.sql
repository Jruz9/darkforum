DROP DATABASE IF EXISTS Forum;
CREATE DATABASE Forum;
USE Forum;

CREATE TABLE Users (
	users_id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    passcode VARCHAR(255) NOT NULL,
    PRIMARY KEY (users_id)
);

CREATE TABLE Posts (
	posts_id INT AUTO_INCREMENT,
    users_id INT,
    post_title VARCHAR(255) NOT NULL,
    post_text VARCHAR(10000) NOT NULL,
    post_author VARCHAR(255) NOT NULL,
    post_likes INT,
    post_dislikes INT,
    post_created_date VARCHAR(255) NOT NULL,
    PRIMARY KEY (posts_id),
    FOREIGN KEY (users_id) REFERENCES Users(users_id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Comments (
	comments_id INT AUTO_INCREMENT,
    users_id INT,
    comment_text VARCHAR(10000) NOT NULL,
    comment_author VARCHAR(255) NOT NULL,
    comment_posts_id INT,
    PRIMARY KEY (comments_id),
    FOREIGN KEY (users_id) REFERENCES Users(users_id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (comment_posts_id) REFERENCES Posts(posts_id) ON UPDATE CASCADE ON DELETE SET NULL
);