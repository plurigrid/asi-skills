#!/usr/bin/env ruby
# extract_bumpus.rb - Extract Bumpus papers via Mathpix
# Sources credentials from ~/.topos/.env

require 'dotenv'
Dotenv.load(File.expand_path('~/.topos/.env'))

require 'mathpix'
require 'fileutils'

OUTPUT_DIR = File.expand_path('../papers', __dir__)
FileUtils.mkdir_p(OUTPUT_DIR)

Mathpix.configure do |config|
  config.app_id = ENV['MATHPIX_APP_ID']
  config.app_key = ENV['MATHPIX_APP_KEY']
  config.timeout = 120
end

BUMPUS_PAPERS = [
  { arxiv: "2207.06091", name: "structured_decompositions", title: "Structured Decompositions" },
  { arxiv: "2302.05575", name: "compositional_algorithms", title: "Compositional Algorithms on Compositional Data" },
  { arxiv: "2104.01841", name: "spined_categories", title: "Spined Categories" },
  { arxiv: "2402.00206", name: "time_varying_data", title: "Unified Theory of Time-Varying Data" },
  { arxiv: "2408.15184", name: "pushing_tree_decomps", title: "Pushing Tree Decompositions Forward" },
  { arxiv: "2407.03488", name: "failures_compositionality", title: "Failures of Compositionality" },
]

def process_paper(paper)
  arxiv_id = paper[:arxiv]
  name = paper[:name]
  pdf_url = "https://arxiv.org/pdf/#{arxiv_id}.pdf"
  
  puts "📄 Processing: #{paper[:title]} (#{arxiv_id})..."
  
  begin
    conversion = Mathpix
      .document(pdf_url)
      .with_formats(:markdown, :latex)
      .with_tables(include_table_html: true)
      .with_diagrams
      .convert
    
    puts "   ⏳ Waiting for conversion..."
    conversion.wait_until_complete(max_wait: 600, poll_interval: 5.0)
    
    result = conversion.result
    
    # Save markdown
    md_path = File.join(OUTPUT_DIR, "#{name}.md")
    File.write(md_path, result.markdown)
    puts "   ✓ Saved: #{md_path}"
    
    # Save LaTeX
    tex_path = File.join(OUTPUT_DIR, "#{name}.tex")
    File.write(tex_path, result.latex) if result.latex
    puts "   ✓ Saved: #{tex_path}"
    
    # Extract and save equations
    if result.equations && result.equations.any?
      eq_path = File.join(OUTPUT_DIR, "#{name}_equations.txt")
      equations = result.equations.map { |eq| eq['latex'] || eq['text'] }.compact
      File.write(eq_path, equations.join("\n\n---\n\n"))
      puts "   ✓ Extracted #{equations.count} equations"
    end
    
    {
      name: name,
      arxiv: arxiv_id,
      page_count: result.page_count || 0,
      equation_count: result.equations&.count || 0,
      success: true
    }
    
  rescue => e
    puts "   ✗ Error: #{e.message}"
    { name: name, arxiv: arxiv_id, success: false, error: e.message }
  end
end

puts "=" * 60
puts "Bumpus Corpus Extraction via Mathpix"
puts "Output: #{OUTPUT_DIR}"
puts "=" * 60
puts

results = BUMPUS_PAPERS.map { |paper| process_paper(paper) }

puts
puts "=" * 60
puts "Summary"
puts "=" * 60

success_count = results.count { |r| r[:success] }
puts "Processed: #{success_count}/#{results.count} papers"

results.each do |r|
  status = r[:success] ? "✓" : "✗"
  puts "  #{status} #{r[:name]}: #{r[:page_count]} pages, #{r[:equation_count]} equations"
end

# Generate index
index_path = File.join(OUTPUT_DIR, "INDEX.md")
File.open(index_path, 'w') do |f|
  f.puts "# Bumpus Corpus Index"
  f.puts
  f.puts "Generated: #{Time.now}"
  f.puts
  f.puts "| Paper | arXiv | Pages | Equations |"
  f.puts "|-------|-------|-------|-----------|"
  results.each do |r|
    f.puts "| [#{r[:name]}](#{r[:name]}.md) | #{r[:arxiv]} | #{r[:page_count]} | #{r[:equation_count]} |"
  end
end
puts
puts "Index saved to: #{index_path}"
