select trim(to_char(day, 'Day'))  || ', ' || 
trim(to_char(day, 'Month')) || ' ' || to_number(trim(to_char(day, 'dd'))) || ', ' || trim( to_char(day, 'YYYY' ))  day  from days;