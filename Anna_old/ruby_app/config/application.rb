require 'active_record'
require 'sqlite3'
require 'yaml'

## Detecting absolute app path
APP_DIR = __FILE__.gsub('/config/application.rb', '')

## Opening DB config
config = YAML::load(File.read("#{APP_DIR}/db/config.yml"))
config["development"]["database"] = "#{APP_DIR}/#{config["development"]["database"]}"

## Establishing connection
ActiveRecord::Base.establish_connection(config['development'])

## Loading models
Dir.glob("#{APP_DIR}/app/models/*.rb").each do |file|
    require file
end
