/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
SELECT category.name AS category,
       COUNT(film.film_id) AS number_of_films
FROM film_category
JOIN category ON film_category.category_id = category.category_id
JOIN film ON film_category.film_id = film.film_id
GROUP BY category.name
ORDER BY number_of_films DESC;
/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
SELECT CONCAT(actor.first_name, ' ', actor.last_name) AS name,
       COUNT(film_actor.actor_id) AS number_of_films
FROM film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY name
ORDER BY number_of_films DESC
LIMIT 10;
/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/

/*.....SQL.....*/
SELECT category.name,
       SUM(payment.amount) AS total_amount
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film_category.film_id = film.film_id
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY category.name
ORDER BY SUM(payment.amount) DESC
LIMIT 1;
/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
SELECT title
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL;
/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
SELECT CONCAT(actor.first_name, ' ', actor.last_name) AS name,
       COUNT(film_category.film_id) AS COUNT
FROM film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film_category ON film_actor.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Children'
GROUP BY actor.first_name,
         actor.last_name
ORDER BY COUNT DESC
LIMIT 3;