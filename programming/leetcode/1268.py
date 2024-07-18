select user_id as buyer_id, to_char(join_date, 'yyyy-mm-dd') as join_date, sum(
    case
        when to_char(order_date, 'yyyy') = '2019' then 1
        else 0
    end
        ) as orders_in_2019
        
    from (Users left join Orders on user_id = buyer_id) group by join_date, user_id