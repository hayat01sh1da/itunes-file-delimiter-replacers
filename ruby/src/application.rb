# rbs_inline: enabled

require 'fileutils'

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
    output "========== [#{exec_mode}] No #{extension} Remains ==========" and return if paths.empty?
    output "========== [#{exec_mode}] Total File Count to Clean: #{paths.length} =========="
    output "========== [#{exec_mode}] The delimiters of those files will be replaced with `#{delimiter}` =========="
    output "========== [#{exec_mode}] Start! =========="

    file_conversion_map.each do |before, after|
      output "========== [#{exec_mode}] Replacing the delimiter: `#{before}` => `#{after}` =========="

      if mode == 'e'
        FileUtils.mkdir_p(File.dirname(after)) if after.match?(/Disc\d{1}\//)
        FileUtils.mv(before, after) if before != after
      end
    end

    output "========== [#{exec_mode}] Done! =========="
    output "========== [#{exec_mode}] Total Target File Count: #{paths.length} =========="
  end

  # @rbs return: void
  def validate_mode!
    case mode
    when 'd', 'e'
      return
    else
      raise InvalidModeError, "#{mode} is invalid mode. Provide either `d`(default) or `e`."
    end
  end

  private

  attr_reader :paths, :extension, :delimiter, :mode

  # @rbs bash: Hash[String, String]
  # @rbs return: Hash[String, String]
  def file_conversion_map(hash = {})
    @file_conversion_map ||= paths.map.with_object(hash) { |path, hash|
      hash[path] = after(path)
    }
  end

  # @rbs path: String
  # @rbs return: String
  def after(path)
    elements     = path.split('/')
    old_filename = elements.last

    new_filename = if old_filename.match?(/^\d{1}\-/)
      old_filename
        .gsub(/^(?<disc_number>\d{1})\-/, 'Disc\k<disc_number>/')
        .gsub(/(?<disc_number>Disc\d{1})\/(?<track_number>\d{2})\s/, '\k<disc_number>/\k<track_number>' + delimiter)
    else
      old_filename.gsub(/(?<track_number>\d{2})\s/, '\k<track_number>' + delimiter)
    end

    elements[-1] = new_filename
    elements.join('/')
  end

  # @rbs return: String
  def exec_mode
    @exec_mode ||= mode == 'e' ? 'EXECUTION' : 'DRY RUN'
  end

  # @rbs return: bool
  def test_env?
    caller[-1].split('/').last.match?(/minitest\.rb/)
  end

  # @rbs message: String
  # @rbs return: void
  def output(message)
    puts message unless test_env?
  end
end
