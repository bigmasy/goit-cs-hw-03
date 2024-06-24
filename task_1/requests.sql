select * from  tasks where user_id = 1
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new')
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;
select * from users where id not in (select user_id from tasks)
insert into tasks(title, description, status_id, user_id) values ('test', 'test1', 2, 5)
select * from tasks where status_id != (select id from status where name = 'completed') 
delete from tasks where id = 21
select * from users where email like '%@example.org%'
update users set fullname = 'new name' where id = 1
SELECT s.name AS status, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;
SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';
SELECT * FROM tasks WHERE description IS NULL OR description = '';
SELECT u.fullname, t.title
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
