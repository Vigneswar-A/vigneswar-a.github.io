select person1, person2, count(duration) as call_count, sum(duration) as total_duration from (SELECT case 
    when from_id < to_id then from_id else to_id
    end as person1,
    case
    when from_id > to_id then from_id else to_id end as person2 , duration from calls) group by person1, person2
      
    
