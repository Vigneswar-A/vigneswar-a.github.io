SELECT id, CASE
    WHEN P_ID is NULL THEN 'Root'
    WHEN ID IN (SELECT P_ID FROM TREE) THEN 'Inner'
    ELSE 'Leaf'
    end as type
 FROM TREE 
    
                    

