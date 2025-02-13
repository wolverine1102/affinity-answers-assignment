QUERIES = {
    "tiger_count" : """
                    SELECT COUNT(*)
                    FROM taxonomy
                    WHERE species LIKE '%Panthera tigris%';
                    """,

    "sumatran_tiger_ncbi" : """
                            SELECT ncbi_id
                            FROM taxonomy
                            WHERE species LIKE '%Sumatran tiger%';
                            """,

    "rice_with_longest_DNA" : """
                                SELECT t.ncbi_id, t.species, r.length
                                FROM rfamseq r
                                JOIN taxonomy t ON r.ncbi_id = t.ncbi_id
                                WHERE t.species LIKE 'Oryza%'
                                ORDER BY r.length DESC
                                LIMIT 1;
                                """,
}