-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
UPDATE users
@projs = SELECT SUM(score * (SELECT weight FROM projects WHERE id = corrections.project_id)) FROM corrections WHERE corrections.user_id = user_id;
@ws = SUM(weight) FROM projects WHERE id = (SELECT project_id FROM corrections WHERE user_id = user_id);
SET average_score = (@projs / @ws) WHERE id = user_id;
END//
DELIMITER ;
