SELECT
    query.seqid as query_id,
    query.function as query_function,
    query.mitoscore as query_mitoscore,
    query.loc as query_loc,
    query.locrate as query_locrate,
    query.organism as query_organism,
    subject.seqid as subject_id,
    subject.function as subject_function,
    blasthit.evalue as evalue,
    blasthit.qlen as qlen,
    blasthit.slen as slen,
    blasthit.length as length,
    blasthit.alen_slen as alen_slen,
    blasthit.alen_qlen as alen_qlen
    FROM sequence query
    INNER JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE subject.organism = 'Euglena gracilis'
    AND blasthit.evalue < 0.00001 AND blasthit.alen_slen > 0.3
    AND (query.organism = 'Trypanosoma brucei'
        OR  query.organism = 'Homo sapiens'
        OR (query.organism = 'Saccharomyces cerevisiae' AND subject.mitoscore = 100)
        )
;