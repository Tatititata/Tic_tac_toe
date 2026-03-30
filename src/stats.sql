select player, 
    case 
        when (loss + tie) = 0 then 999999
        else win::float / (loss + tie)
    end as ratio
from

(select ft.player, 
sum (case when player = winner_id then 1 else 0 end) as win,
sum (case when (player != winner_id and winner_id is not null) then 1 else 0 end) as loss,
sum (case when winner_id is null then 1 else 0 end) as tie

from
(select player_o_id as player, winner_id from games
where status = 'finished'
union all
select player_x_id as player, winner_id from games
where status = 'finished') as ft

group by player)

order by ratio desc;
