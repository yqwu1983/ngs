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
    blasthit.alen_qlen as alen_qlen,
    (SELECT blasthit.id FROM blasthit
        INNER JOIN sequence AS subject
        ON subject.id = blasthit.subject_id
        WHERE query.id = blasthit.query_id
        AND (
                    query.organism = 'Trypanosoma brucei'
                OR  query.organism = 'Homo sapiens'
                OR (query.organism = 'Saccharomyces cerevisiae' AND query.mitoscore = 100)
            )
        ORDER BY blasthit.evalue ASC
        LIMIT 1
    ) AS bh_id
FROM sequence query
LEFT JOIN blasthit ON blasthit.id = bh_id
LEFT JOIN sequence AS subject ON subject.id = blasthit.subject_id
WHERE subject.organism = 'Euglena gracilis'
;
