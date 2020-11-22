SELECT MIN(CreationDate) as min_date, 
MAX(CreationDate) as max_date, AVG(Score) as avg_score
FROM POSTS;

SELECT year(CreationDate) as "year", month(CreationDate) as "month", count(*) as "count"
FROM Posts
GROUP BY year(CreationDate),month(CreationDate)
ORDER BY "year","month";

SELECT year(CreationDate) as "year", month(CreationDate) as "month", PostTypeId,
       count(*) as "count"
FROM Posts
GROUP BY year(CreationDate),month(CreationDate),PostTypeId
ORDER BY PostTypeId, "count" DESC;

SELECT Name, count(*) as "count"
FROM badges
GROUP BY Name
HAVING count(*)>=20
ORDER BY count(*) DESC;

SELECT Id, DisplayName, Location
FROM Users
WHERE (Location LIKE '%NY%') OR (Location LIKE '%New York%');

SELECT category_name, product_name, list_price
FROM Products p
LEFT OUTER JOIN Categories c
ON c.category_id = p.category_id
ORDER BY category_name, product_name;

SELECT first_name, last_name, line1, city, state, zip_code
FROM Addresses a
LEFT OUTER JOIN Customers c
ON c.customer_id = a.customer_id
WHERE email_address = "allan.sherwood@yahoo.com";

SELECT first_name, last_name, line1, city, state, zip_code
FROM Customers c
LEFT OUTER JOIN Addresses a
ON c.customer_id = a.customer_id
WHERE address_id =  shipping_address_id;

SELECT last_name, first_name, order_date, product_name, item_price, discount_amount, quantity
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
INNER JOIN Order_Items oi ON o.order_id = oi.order_id
INNER JOIN Products p ON oi.product_id = p.product_id
ORDER BY last_name, order_date, product_name;

SELECT p1.product_name, p1.list_price
FROM Products p1, Products p2
WHERE (p1.list_price = p2.list_price) AND (p1.product_name != p2.product_name) 
ORDER BY p1.product_name, p2.product_name;

SELECT order_id, order_date, "SHIPPED" as ship_status
FROM Orders
WHERE ship_date is not NULL
UNION
SELECT order_id, order_date, "NOT SHIPPED" as ship_status
FROM Orders
WHERE ship_date is NULL;

SELECT DISTINCT Category_name, p.count, Max_Price
FROM Categories c
LEFT Join
	(SELECT category_id, count(*) 'count', max(list_price) Max_Price
     FROM products
     GROUP BY category_id) p
ON p.category_id = c.category_id
WHERE p.count > 0
ORDER BY p.count DESC;

SELECT c.email_address, count(op.order_id) as 'count', op.Total_Price
FROM customers c
LEFT OUTER JOIN
	( SELECT o.customer_id, o.order_id, 
         sum((item_price - discount_amount)*quantity) as Total_Price
      FROM orders o
      LEFT OUTER JOIN order_items oi
      ON o.order_id = oi.order_id
      GROUP BY o.order_id) op
ON c.customer_id = op.customer_id
GROUP BY c.customer_id
Having count(op.order_id) > 1
ORDER BY count(op.order_id) DESC;

SELECT c.email_address, op.count
FROM customers c
LEFT OUTER JOIN
	( SELECT o.customer_id, count(DISTINCT product_id) as 'count'
      FROM orders o
      LEFT OUTER JOIN order_items oi
      ON o.order_id = oi.order_id
      GROUP BY o.customer_id) op
ON c.customer_id = op.customer_id
WHERE op.count > 1;

SELECT product_name, list_price,
	    CASE
        WHEN list_price > AVG_P
        THEN "Yes"
        ELSE "NO" 
        END Above_AVG
FROM products p,
	( SELECT AVG(list_price) as AVG_P
      FROM products) ap
ORDER BY list_price DESC;

SELECT product_name, list_price
FROM products p,
	( SELECT AVG(list_price) as AVG_P
      FROM products) ap
WHERE list_price > AVG_P
ORDER BY list_price DESC;

SELECT category_name
FROM Categories c
WHERE NOT EXISTS (select * from products p
			WHERE c.category_id = p.category_id);
            
select * from products p, Categories c
WHERE c.category_id = p.category_id;

SELECT t.email_address, max(order_total) Largest_Order
FROM
	(SELECT email_address, order_id, order_total
	FROM customers c
	LEFT OUTER JOIN
		( SELECT o.customer_id, o.order_id,
		sum((item_price - discount_amount)*quantity) as order_total
		FROM orders o
		LEFT OUTER JOIN order_items oi
		ON o.order_id = oi.order_id
		GROUP BY o.order_id) op
	ON c.customer_id = op.customer_id) t
GROUP BY t.email_address;

SELECT list_price, FORMAT(list_price,1) as One_dight,
		CONVERT(list_price,SIGNED) as Int_d,
        CAST(list_price AS SIGNED) as Int_d2,
        date_added as DATE0,
        CAST(date_added AS DATE) as DATE1,
        cast(date_added as char(7)) as DATE1,
        CAST(date_added AS TIME) as TIME1
FROM products; 

SELECT product_name, discount_percent
FROM products
WHERE discount_percent NOT IN (select discount_percent from products 
			group by discount_percent having count(*) > 1)
ORDER BY product_name;

SELECT card_number, LENGTH(card_number) as length, 
SUBSTRING(card_number, -4 ) as Last_4, 
concat("XXXX-XXXX-XXXX-",SUBSTRING(card_number, -4 )) as Hiden
FROM orders;