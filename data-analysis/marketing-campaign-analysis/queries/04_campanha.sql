

        select
        sum("AcceptedCmp1") as primeira_campanha,
        sum("AcceptedCmp2") as segunda_campanha,
        sum("AcceptedCmp3") as terceira_campanha,
        sum("AcceptedCmp4") as quarta_campanha,
        sum("AcceptedCmp5") as quinta_campanha
    from marketing_data
    where to_char("Dt_Customer"::date, 'YYYY-MM') = '2012-08';

	