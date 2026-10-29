require_relative "lib/crawlora/bo3/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-bo3"
  spec.version = Crawlora::Bo3::VERSION
  spec.summary = "BO3.gg API client for Crawlora (28 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted BO3.gg API. Covers Counter-Strike and Valorant matches, teams, players, tournaments, rankings, news, and statistics across 28 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bo3-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-bo3", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-bo3/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
