class CreateSequences < ActiveRecord::Migration
  def change
    create_table :sequences do |t|
        t.string :name, null: false
        t.timestamps
    end
  end
end
