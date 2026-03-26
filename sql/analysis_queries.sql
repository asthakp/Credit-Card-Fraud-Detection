use fraud_db;

-- total transactions
select count(*) as total_transactions
 from transactions;

-- Fraud vs Non_fraud transactions
select class, count(*) as total 
from transactions
group by class;

-- Fraud Rate --
select
(sum(case when class=1 then 1 else 0 end))/count(*) * 100 as 'Fraud Rate'
from transactions;

-- Average Fraud Amount VS Normal Amount
select class, avg(amount) as avg_amount
from transactions
group by class;

-- Fraud transactions with highest amounts
select * from transactions
where class=1
order by amount desc
limit 10;