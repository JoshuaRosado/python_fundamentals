SELECT * FROM users
LEFT JOIN tweets ON users.id = tweets.user_id
WHERE users.id = 1;

SELECT tweets.tweet AS kobe_tweets
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;

SELECT first_name, tweet
FROM users
LEFT JOIN faves 
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.id = faves.user_id
WHERE users.id = 2;



SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 1 OR users.id = 2;


SELECT users.first_name AS followed, users2.first_name AS follower
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users AS users2
ON users2.id = follows.follower_id
WHERE users.id = 1;


SELECT *
FROM users
WHERE users.id NOT IN (
SELECT follower_id
FROM follows
WHERE followed_id = 2
) AND users.id != 2;


SELECT users.first_name as user, COUNT(users2.first_name) as follower_count
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users AS users2
ON users2.id = follows.follower_id
WHERE users.id = 1
GROUP BY users.id;

SELECT first_name, tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id;

SELECT first_name, tweet
FROM users
JOIN tweets
ON users.id = tweets.user_id;




