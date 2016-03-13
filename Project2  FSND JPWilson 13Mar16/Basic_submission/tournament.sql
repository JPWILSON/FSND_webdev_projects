-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament; 

CREATE DATABASE tournament;

\c tournament;


--This is the actual start of the database schema
CREATE TABLE players(
	id SERIAL PRIMARY KEY,
	name TEXT not null
);

CREATE TABLE matches(
	winner INTEGER REFERENCES players(id),
	loser INTEGER REFERENCES players(id),
	PRIMARY KEY(winner, loser) 
);


CREATE OR REPLACE VIEW winners AS 
	SELECT name, id, COUNT(winner) AS wins
		FROM players LEFT JOIN matches
		ON players.id = matches.winner
		GROUP BY name, id
		ORDER BY wins DESC;


CREATE OR REPLACE VIEW losers AS 
	SELECT name, id, COUNT(loser) AS losses
		FROM players LEFT JOIN matches 
		ON players.id = matches.loser
		GROUP BY name, id
		ORDER BY losses DESC;

--ORDER: id, name, wins, matches
CREATE OR REPLACE VIEW standings AS 
	SELECT winners.id, 
			winners.name, 
			winners.wins, 
			(winners.wins + losers.losses) AS matches
		FROM winners FULL OUTER JOIN losers
		ON winners.id = losers.id
		ORDER BY winners.wins DESC;