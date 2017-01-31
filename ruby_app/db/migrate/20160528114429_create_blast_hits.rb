class CreateBlastHits < ActiveRecord::Migration
  def change
    create_table :blast_hits do |t|
        t.integer :query_id, null: false
        t.integer :subject_id, null: false
    end
  end
end
