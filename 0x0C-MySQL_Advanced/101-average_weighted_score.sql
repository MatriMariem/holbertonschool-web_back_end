-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers
BEGIN
CALL ComputeAverageWeightedScoreForUser (SELECT id FROM users);
END//
DELIMITER ;
