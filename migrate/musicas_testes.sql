USE onnemusic;

INSERT INTO `onnemusic`.`genero`
(`genero`,
`icone`,
`cor`)
VALUES
("Rock", "", "black"),
("Pop", "", "yellow"),
("MPB", "", "#FACADA");

INSERT INTO `onnemusic`.`musica`
(
`cantor`,
`duracao`,
`nome`,
`url_capa`,
`genero`)
VALUES
("Britney Spears",
"03:20",
"Toxic",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjrC2S0F4Krq1Hp-S9gt4N6zvuuAyjspyoNA&s",
"Pop"),
("System of a Down ",
"03:39",
"Toxicity",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTP-bgn127KvfcTJxjqRQrO4qU8eN-6gGb6Eg&s",
"Rock");
