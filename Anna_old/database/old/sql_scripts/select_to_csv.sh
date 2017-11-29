sqlite3 -header -csv mitoproteome.db < ~/bioinformatics/ngs/database/final_query.sql > /home/anna/bioinformatics/phd/euglena_project/results.csv

sqlite3 -header -csv /home/anna/Dropbox/PhD/mitoproteome.db < ~/bioinformatics/ngs/database/final_reverse.sql > /home/anna/bioinformatics/phd/euglena_project/results_reverse.csv

sqlite3 -header -csv /home/anna/Dropbox/PhD/mitoproteome.db < ~/bioinformatics/ngs/database/final_reverse_all.sql > /home/anna/bioinformatics/phd/euglena_project/all_results_reverse.csv
