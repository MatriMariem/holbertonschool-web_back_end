-- a SQL script that creates a stored procedure AddBonus that
-- adds a new correction for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id) WHERE id = used_id;
END//
DELIMITER ;
