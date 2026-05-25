# frozen_string_literal: true
# rbs_inline: enabled

# Walks the current directory looking for media files with the given extension
# and rewrites their filenames so the space delimiter becomes a configurable
# character (and `N-` disc prefixes become `DiscN/` subdirectories).
class Application
  class InvalidModeError < StandardError; end

  # @rbs extension: String
  # @rbs delimiter: String
  # @rbs mode: String
  # @rbs return: void
  def self.run(extension: '.m4a', delimiter: '_', mode: 'd')
    instance = new(extension:, delimiter:, mode:)
    instance.validate_mode!
    instance.replace
  end

  # @rbs extension: String
  # @rbs delimiter: String
  # @rbs mode: String
  # @rbs return: void
  def initialize(extension: '.m4a', delimiter: '_', mode: 'd')
    @paths     = Dir[File.join('.', '**', "*#{extension}")]
    @extension = extension
    @delimiter = delimiter
    @mode      = mode
  end

  # @rbs return: void
  def replace
    output "Target extension is `#{extension}`"
    return announce_empty if paths.empty?

    announce_start
    apply_renames
    announce_finish
  end

  # @rbs return: void
  def validate_mode!
    case mode
    when 'd', 'e'
      nil
    else
      raise InvalidModeError, "#{mode} is invalid mode. Provide either `d`(default) or `e`."
    end
  end

  private

  attr_reader :paths, :extension, :delimiter, :mode

  # @rbs return: void
  def announce_empty
    output "========== [#{exec_mode}] No #{extension} Remains =========="
  end

  # @rbs return: void
  def announce_start
    output "========== [#{exec_mode}] Total File Count to Clean: #{paths.length} =========="
    output "========== [#{exec_mode}] The delimiters of those files will be replaced with `#{delimiter}` =========="
    output "========== [#{exec_mode}] Start! =========="
  end

  # @rbs return: void
  def announce_finish
    output "========== [#{exec_mode}] Done! =========="
    output "========== [#{exec_mode}] Total Target File Count: #{paths.length} =========="
  end

  # @rbs return: void
  def apply_renames
    file_conversion_map.each do |before, after|
      output "========== [#{exec_mode}] Replacing the delimiter: `#{before}` => `#{after}` =========="
      rename(before, after) if mode == 'e'
    end
  end

  # @rbs before: String
  # @rbs after: String
  # @rbs return: void
  def rename(before, after)
    FileUtils.mkdir_p(File.dirname(after)) if after.match?(%r{Disc\d{1}/})
    FileUtils.mv(before, after) if before != after
  end

  # @rbs bash: Hash[String, String]
  # @rbs return: Hash[String, String]
  def file_conversion_map(hash = {})
    @file_conversion_map ||= paths.map.with_object(hash) do |path, acc|
      acc[path] = after(path)
    end
  end

  # @rbs path: String
  # @rbs return: String
  def after(path)
    elements     = path.split('/')
    elements[-1] = rewrite_filename(elements.last)
    elements.join('/')
  end

  # @rbs filename: String
  # @rbs return: String
  def rewrite_filename(filename)
    return filename.gsub(/(?<track_number>\d{2})\s/, "\\k<track_number>#{delimiter}") unless filename.match?(/^\d{1}-/)

    filename
      .gsub(/^(?<disc_number>\d{1})-/, 'Disc\k<disc_number>/')
      .gsub(%r{(?<disc_number>Disc\d{1})/(?<track_number>\d{2})\s}, "\\k<disc_number>/\\k<track_number>#{delimiter}")
  end

  # @rbs return: String
  def exec_mode
    @exec_mode ||= mode == 'e' ? 'EXECUTION' : 'DRY RUN'
  end

  # @rbs return: bool
  def test_env?
    caller(0..0).first.split('/').last.include?('minitest.rb')
  end

  # @rbs message: String
  # @rbs return: void
  def output(message)
    puts message unless test_env?
  end
end
