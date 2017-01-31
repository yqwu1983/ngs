with open(hits_file , 'wb') as hits_file:
	dict_writer = csv.DictWriter(hits_file, keys)
	dict_writer.writer.writerow(keys)
	dict_writer.writerows(hit_records)
hits_file.closed
