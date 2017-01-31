select subject.function from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id
limit 100;

select subject.function from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id
limit 1000;

Tripanosoma brucei
Saccharomyces cerevisiae
Homo sapiens
Euglena gracilis