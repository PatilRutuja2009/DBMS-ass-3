mysql> insert into book values(128,'DBMS','korth',650,'2014-01-01',4);
Query OK, 1 row affected (0.05 sec)

mysql> insert into book values(128,'RDBMS','Mac_Crow_Hill',670,'2016-03-05',6);
ERROR 1062 (23000): Duplicate entry '128' for key 'PRIMARY'
mysql> insert into book values(129,'RDBMS','Mac_Crow_Hill',670,'2016-03-05',6);
Query OK, 1 row affected (0.03 sec)

mysql> insert into book values(130,'CN','Parth',550,'2015-02-10',7);
Query OK, 1 row affected (0.04 sec)

mysql> select * from book;
+-----------+-------+----------------+--------+---------------------+-----------+
| Book_ISBN | Title | Publisher_Name | Price  | Date_of_Publication | Book_Copy |
+-----------+-------+----------------+--------+---------------------+-----------+
|       123 | abc   | xyz            | 200.00 | 2018-10-05          |         3 |
|       124 | pqr   | lmn            | 200.00 | 2018-10-12          |         4 |
|       125 | lmn   | xyz            | 300.00 | 2018-05-12          |         5 |
|       126 | def   | ghi            | 250.00 | 2018-05-20          |         1 |
|       127 | abcd  | wxy            | 256.00 | 2018-05-22          |         6 |
|       128 | DBMS  | korth          | 650.00 | 2014-01-01          |         4 |
|       129 | RDBMS | Mac_Crow_Hill  | 670.00 | 2016-03-05          |         6 |
|       130 | CN    | Parth          | 550.00 | 2015-02-10          |         7 |
+-----------+-------+----------------+--------+---------------------+-----------+
8 rows in set (0.00 sec)

mysql> insert into Book_Author values(128,'korth','pune');
Query OK, 1 row affected (0.04 sec)

mysql> insert into Book_Author values(129,'amarjeet','pune');
Query OK, 1 row affected (0.04 sec)

mysql> insert into Book_Author values(130,'saurabh','baramti');
Query OK, 1 row affected (0.03 sec)

mysql> update book set where Publisher_Name='Mac_crow_Hill' where Book_ISBN=128;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where Publisher_Name='Mac_crow_Hill' where Book_ISBN=128' at line 1
mysql> update book set Publisher_Name='Mac_crow_Hill' where Book_ISBN=128;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from book;
+-----------+-------+----------------+--------+---------------------+-----------+
| Book_ISBN | Title | Publisher_Name | Price  | Date_of_Publication | Book_Copy |
+-----------+-------+----------------+--------+---------------------+-----------+
|       123 | abc   | xyz            | 200.00 | 2018-10-05          |         3 |
|       124 | pqr   | lmn            | 200.00 | 2018-10-12          |         4 |
|       125 | lmn   | xyz            | 300.00 | 2018-05-12          |         5 |
|       126 | def   | ghi            | 250.00 | 2018-05-20          |         1 |
|       127 | abcd  | wxy            | 256.00 | 2018-05-22          |         6 |
|       128 | DBMS  | Mac_crow_Hill  | 650.00 | 2014-01-01          |         4 |
|       129 | RDBMS | Mac_Crow_Hill  | 670.00 | 2016-03-05          |         6 |
|       130 | CN    | Parth          | 550.00 | 2015-02-10          |         7 |
+-----------+-------+----------------+--------+---------------------+-----------+
8 rows in set (0.00 sec)

mysql> select * from Book_Author where city='pune';
ERROR 1054 (42S22): Unknown column 'city' in 'where clause'
mysql> select * from Book_Author where Author_city='pune';
+------+-------------+-------------+
| ISBN | Author_name | Author_city |
+------+-------------+-------------+
|  123 | Amar        | pune        |
|  129 | amarjeet    | pune        |
|  128 | korth       | pune        |
+------+-------------+-------------+
3 rows in set (0.00 sec)

mysql> slect Title from book where Book_Copy between 10 and 15;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'slect Title from book where Book_Copy between 10 and 15' at line 1
mysql> select Title from book where Book_Copy between 10 and 15;
Empty set (0.00 sec)

mysql> update book set Book_Copy=12 where Book_ISBN=128;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update book set Book_Copy=14 where Book_ISBN=129;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update book set Book_Copy=10 where Book_ISBN=123;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from book;
+-----------+-------+----------------+--------+---------------------+-----------+
| Book_ISBN | Title | Publisher_Name | Price  | Date_of_Publication | Book_Copy |
+-----------+-------+----------------+--------+---------------------+-----------+
|       123 | abc   | xyz            | 200.00 | 2018-10-05          |        10 |
|       124 | pqr   | lmn            | 200.00 | 2018-10-12          |         4 |
|       125 | lmn   | xyz            | 300.00 | 2018-05-12          |         5 |
|       126 | def   | ghi            | 250.00 | 2018-05-20          |         1 |
|       127 | abcd  | wxy            | 256.00 | 2018-05-22          |         6 |
|       128 | DBMS  | Mac_crow_Hill  | 650.00 | 2014-01-01          |        12 |
|       129 | RDBMS | Mac_Crow_Hill  | 670.00 | 2016-03-05          |        14 |
|       130 | CN    | Parth          | 550.00 | 2015-02-10          |         7 |
+-----------+-------+----------------+--------+---------------------+-----------+
8 rows in set (0.00 sec)

mysql> select b.Book_ISBN,Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and a.city='pune';
ERROR 1054 (42S22): Unknown column 'a.city' in 'where clause'
mysql> select b.Book_ISBN,Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and a.Author_city='pune';
+-----------+-------+----------------+--------+---------------------+-----------+
| Book_ISBN | Title | Publisher_Name | Price  | Date_of_Publication | Book_Copy |
+-----------+-------+----------------+--------+---------------------+-----------+
|       123 | abc   | xyz            | 200.00 | 2018-10-05          |        10 |
|       128 | DBMS  | Mac_crow_Hill  | 650.00 | 2014-01-01          |        12 |
|       129 | RDBMS | Mac_Crow_Hill  | 670.00 | 2016-03-05          |        14 |
+-----------+-------+----------------+--------+---------------------+-----------+
3 rows in set (0.00 sec)

mysql> select Title from book where Book_Copy between 10 and 15;
+-------+
| Title |
+-------+
| abc   |
| DBMS  |
| RDBMS |
+-------+
3 rows in set (0.00 sec)

mysql> update book set Publisher_Name='Tata Mac crow Hill' where Book_ISBN=128;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update book set Book_copy=10 where Publisher_Name='Tata Mac crow Hill';
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from book;
+-----------+-------+--------------------+--------+---------------------+-----------+
| Book_ISBN | Title | Publisher_Name     | Price  | Date_of_Publication | Book_Copy |
+-----------+-------+--------------------+--------+---------------------+-----------+
|       123 | abc   | xyz                | 200.00 | 2018-10-05          |        10 |
|       124 | pqr   | lmn                | 200.00 | 2018-10-12          |         4 |
|       125 | lmn   | xyz                | 300.00 | 2018-05-12          |         5 |
|       126 | def   | ghi                | 250.00 | 2018-05-20          |         1 |
|       127 | abcd  | wxy                | 256.00 | 2018-05-22          |         6 |
|       128 | DBMS  | Tata Mac crow Hill | 650.00 | 2014-01-01          |        10 |
|       129 | RDBMS | Mac_Crow_Hill      | 670.00 | 2016-03-05          |        14 |
|       130 | CN    | Parth              | 550.00 | 2015-02-10          |         7 |
+-----------+-------+--------------------+--------+---------------------+-----------+
8 rows in set (0.00 sec)

mysql> select Publisher_Name from book order by Book_Copy;
+--------------------+
| Publisher_Name     |
+--------------------+
| ghi                |
| lmn                |
| xyz                |
| wxy                |
| Parth              |
| xyz                |
| Tata Mac crow Hill |
| Mac_Crow_Hill      |
+--------------------+
8 rows in set (0.00 sec)

mysql> select Publisher_Name,Book_Copy from book order by Book_Copy;
+--------------------+-----------+
| Publisher_Name     | Book_Copy |
+--------------------+-----------+
| ghi                |         1 |
| lmn                |         4 |
| xyz                |         5 |
| wxy                |         6 |
| Parth              |         7 |
| xyz                |        10 |
| Tata Mac crow Hill |        10 |
| Mac_Crow_Hill      |        14 |
+--------------------+-----------+
8 rows in set (0.00 sec)

mysql> select Publisher_Name,Book_Copy from book order by Date_of_Publication;
+--------------------+-----------+
| Publisher_Name     | Book_Copy |
+--------------------+-----------+
| Tata Mac crow Hill |        10 |
| Parth              |         7 |
| Mac_Crow_Hill      |        14 |
| xyz                |         5 |
| ghi                |         1 |
| wxy                |         6 |
| xyz                |        10 |
| lmn                |         4 |
+--------------------+-----------+
8 rows in set (0.00 sec)

mysql> select Publisher_Name,Date_of_Publication,Book_Copy from book order by Date_of_Publication;
+--------------------+---------------------+-----------+
| Publisher_Name     | Date_of_Publication | Book_Copy |
+--------------------+---------------------+-----------+
| Tata Mac crow Hill | 2014-01-01          |        10 |
| Parth              | 2015-02-10          |         7 |
| Mac_Crow_Hill      | 2016-03-05          |        14 |
| xyz                | 2018-05-12          |         5 |
| ghi                | 2018-05-20          |         1 |
| wxy                | 2018-05-22          |         6 |
| xyz                | 2018-10-05          |        10 |
| lmn                | 2018-10-12          |         4 |
+--------------------+---------------------+-----------+
8 rows in set (0.00 sec)

mysql> select Publisher_Name from book where Publisher_Name like 'k%'
    -> ;
Empty set (0.00 sec)

mysql> select b.Book_ISBN,Publisher_Name from book b,Book_Author a where b.Book_ISBN=a.ISBN and a.Author_Name like 'k%';
+-----------+--------------------+
| Book_ISBN | Publisher_Name     |
+-----------+--------------------+
|       128 | Tata Mac crow Hill |
+-----------+--------------------+
1 row in set (0.00 sec)

mysql> select Publisher_Name from book order by Publisher_Name;
+--------------------+
| Publisher_Name     |
+--------------------+
| ghi                |
| lmn                |
| Mac_Crow_Hill      |
| Parth              |
| Tata Mac crow Hill |
| wxy                |
| xyz                |
| xyz                |
+--------------------+
8 rows in set (0.00 sec)

mysql> select Publisher_Name,Date_of_Publication from book order by Date_of_Publication;
+--------------------+---------------------+
| Publisher_Name     | Date_of_Publication |
+--------------------+---------------------+
| Tata Mac crow Hill | 2014-01-01          |
| Parth              | 2015-02-10          |
| Mac_Crow_Hill      | 2016-03-05          |
| xyz                | 2018-05-12          |
| ghi                | 2018-05-20          |
| wxy                | 2018-05-22          |
| xyz                | 2018-10-05          |
| lmn                | 2018-10-12          |
+--------------------+---------------------+
8 rows in set (0.01 sec)

mysql> select a.ISBN,Author_Name,Author_City,b.Book_ISBN,Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and Author_Name='korth';
+------+-------------+-------------+-----------+-------+--------------------+--------+---------------------+-----------+
| ISBN | Author_Name | Author_City | Book_ISBN | Title | Publisher_Name     | Price  | Date_of_Publication | Book_Copy |
+------+-------------+-------------+-----------+-------+--------------------+--------+---------------------+-----------+
|  128 | korth       | pune        |       128 | DBMS  | Tata Mac crow Hill | 650.00 | 2014-01-01          |        10 |
+------+-------------+-------------+-----------+-------+--------------------+--------+---------------------+-----------+
1 row in set (0.00 sec)

mysql> delete a.ISBN,Author_Name,Author_City,b.Book_ISBN,Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book
ERROR 1109 (42S02): Unknown table 'ISBN' in MULTI DELETE
mysql> delete a.ISBN,Author_Name,Author_City,b.Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and Author_Name='korth';
ERROR 1109 (42S02): Unknown table 'ISBN' in MULTI DELETE
mysql> delete b.Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and Author_Name='korth'; ERROR 1109 (42S02): Unknown table 'Title' in MULTI DELETE
mysql> delete b.Book_ISBN,Title,Publisher_Name,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and Author_Name='korth';
ERROR 1109 (42S02): Unknown table 'Book_ISBN' in MULTI DELETE
mysql> delete b.Book_ISBN,Publisher_Name,Title,Price,Date_of_Publication,Book_Copy from book b,Book_Author a where b.Book_ISBN=a.ISBN and a.Author_Name='korth';
ERROR 1109 (42S02): Unknown table 'Book_ISBN' in MULTI DELETE
mysql> mysql> select Book_Copy from book where Date_of_Publication between '2014-01-01' and current_date;
+-----------+
| Book_Copy |
+-----------+
|        10 |
|         4 |
|         5 |
|         1 |
|         6 |
|        10 |
|        14 |
|         7 |
+-----------+
8 rows in set (0.02 sec)

mysql> select Book_Copy,Date_of_publication from book where Date_of_Publication between '2014-01-01' and current_date;
+-----------+---------------------+
| Book_Copy | Date_of_publication |
+-----------+---------------------+
|        10 | 2018-10-05          |
|         4 | 2018-10-12          |
|         5 | 2018-05-12          |
|         1 | 2018-05-20          |
|         6 | 2018-05-22          |
|        10 | 2014-01-01          |
|        14 | 2016-03-05          |
|         7 | 2015-02-10          |
+-----------+---------------------+
8 rows in set (0.00 sec)

