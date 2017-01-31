select count(*) from sequence where organism = 'Euglena gracilis' and loc='M';
7938

select count(*) from sequence where organism = 'Euglena gracilis' and loc='M' and mitoscore != 100;
7842

select count(*) from sequence where organism = 'Euglena gracilis' and loc='M' and locrate <= 2;
1616

select count(*) from sequence where organism = 'Euglena gracilis' and loc='M' and locrate <= 2 and mitoscore != 100;
1571

select count(*) from sequence where organism = 'Euglena gracilis' and mitoscore = 100;
223

select count(*) from sequence where organism = 'Euglena gracilis' and loc='M' and mitoscore = 100;
96

select count(*) from sequence where organism = 'Euglena gracilis' and mitoscore = 100 and loc!='M';
127

select count(*) from sequence where organism = 'Euglena gracilis' and mitoscore = 100 and loc='M' and locrate <= 2;
45

select count(*) from sequence where organism = 'Euglena gracilis' and mitoscore = 100 and loc='M' and locrate > 2;
51

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

3763

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

2828

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Homo sapiens'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

3086

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens')
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

4867

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

4710

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

3896

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;

5393

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.loc = 'M'
group by query.id) as count_table;

1199

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100
group by query.id) as count_table;

72

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100 and query.loc = 'M'
group by query.id) as count_table;

23

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100 and query.loc = 'M' and query.locrate <= 2
group by query.id) as count_table;

13

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100 and query.loc = 'M' and query.locrate > 2
group by query.id) as count_table;

10

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100 and query.loc = 'M' and query.locrate = 1
group by query.id) as count_table;

5

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100 and query.loc = 'M' and query.locrate > 1
group by query.id) as count_table;

18

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore != 100 and query.loc = 'M' and query.locrate > 1
group by query.id) as count_table;

1087

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore != 100 and query.loc = 'M' and query.locrate = 1
group by query.id) as count_table;

89

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.loc = 'M' and query.locrate = 1
group by query.id) as count_table;

94

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore = 100 and query.loc !='M'
group by query.id) as count_table;

49

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore != 100 and query.loc ='M'
group by query.id) as count_table;

1176


select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore != 100 and query.loc = 'M' and query.locrate > 2
group by query.id) as count_table;

866

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.mitoscore != 100 and query.loc = 'M' and query.locrate <= 2
group by query.id) as count_table;

310

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3 and query.loc = 'M' and query.locrate <= 2
group by query.id) as count_table;

323

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
    and query.mitoscore = 100
group by query.id) as count_table;

51

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
    and query.mitoscore = 100
group by query.id) as count_table;

43

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Homo sapiens'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
    and query.mitoscore = 100
group by query.id) as count_table;

64




###########################################################################################################################################




select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

2830

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

2023

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Homo sapiens'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

2062

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens')
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

3730

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

3473

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

2911

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
group by query.id) as count_table;

4103

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.loc = 'M'
group by query.id) as count_table;

907

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore = 100
group by query.id) as count_table;

56

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore = 100 and query.loc = 'M'
group by query.id) as count_table;

14

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore = 100 and query.loc = 'M' and query.locrate <= 2
group by query.id) as count_table;

8

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore = 100 and query.loc = 'M' and query.locrate > 2
group by query.id) as count_table;

6

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore = 100 and query.loc !='M'
group by query.id) as count_table;

42

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore != 100 and query.loc ='M'
group by query.id) as count_table;

893

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore != 100 and query.loc = 'M' and query.locrate > 2
group by query.id) as count_table;

639

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.mitoscore != 100 and query.loc = 'M' and query.locrate <= 2
group by query.id) as count_table;

254

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100))
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5 and query.loc = 'M' and query.locrate <= 2
group by query.id) as count_table;

262

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
    and query.mitoscore = 100
group by query.id) as count_table;

42

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
    and query.mitoscore = 100
group by query.id) as count_table;

38

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Homo sapiens'
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5
    and query.mitoscore = 100
group by query.id) as count_table;

49


