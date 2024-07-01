--Отримати всі завдання певного користувача
SELECT * FROM  tasks WHERE user_id = 1
--Вибрати завдання за певним статусом
SELECT * FROM tasks WHERE status_id = (SELECT id FROM STATUS WHERE NAME = 'new')
--Оновити статус конкретного завдання
UPDATE tasks SET status_id = (SELECT id FROM STATUS WHERE NAME = 'in progress') WHERE id = 1;
--Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id not in (SELECT user_id FROM tasks)
--Додати нове завдання для конкретного користувача
INSERT into tasks(title, description, status_id, user_id) values ('test', 'test1', 2, 5)
--Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM STATUS WHERE NAME = 'completed') 
--Видалити конкретне завдання
delete FROM tasks WHERE id = 21
--Знайти користувачів з певною електронною поштою
SELECT * FROM users WHERE email like '%@example.org%'
--Оновити ім'я користувача
UPDATE users set fullname = 'new NAME' WHERE id = 1
--Отримати кількість завдань для кожного статусу
SELECT s.NAME AS STATUS, COUNT(t.id) AS task_count
FROM STATUS s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.NAME;
--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';
--Отримати список завдань, що не мають опису.
SELECT * FROM tasks WHERE description IS NULL OR description = '';
--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
SELECT u.fullname, t.title
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN STATUS s ON t.status_id = s.id
WHERE s.NAME = 'in progress';
--Отримати користувачів та кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
