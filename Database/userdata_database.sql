----
-- phpLiteAdmin database dump (http://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.7.1
-- Exported: 9:39am on April 25, 2018 (CEST)
-- database file: ./demo/81e9974e6f98d75/nhufas
----
BEGIN TRANSACTION;

----
-- Table structure for userdata
----
CREATE TABLE [userdata] ([id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, [username] TEXT NOT NULL, [password] INTEGER NOT NULL);

----
-- Data dump for userdata, a total of 5 rows
----
INSERT INTO "userdata" ("id","username","password") VALUES ('1','tnntech','123456');
INSERT INTO "userdata" ("id","username","password") VALUES ('3','vinh','100');
INSERT INTO "userdata" ("id","username","password") VALUES ('4','trai','50');
INSERT INTO "userdata" ("id","username","password") VALUES ('5','tnntech','0');
INSERT INTO "userdata" ("id","username","password") VALUES ('9','tnntech','1111');
COMMIT;
