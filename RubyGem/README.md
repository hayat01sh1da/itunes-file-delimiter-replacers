## 1. Environment

- Ruby 4.0.6
- Gemfile 4.1.0.beta1
- Bundler 4.1.0.beta1

## 2. Installation

```command
$ gem install spreen-tracks
```

For development, install the dependencies via Gemfile and Bundler:

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

Run the command inside your music directory — with no options it dry-runs, printing every rename it would perform without touching a file:

```command
$ cd ~/Music
$ track-delimiter
Target extension is `.m4a`
========== [DRY RUN] Total File Count to Clean: 4 ==========
========== [DRY RUN] The delimiters of those files will be replaced with `_` ==========
========== [DRY RUN] Start! ==========
========== [DRY RUN] Replacing the delimiter: `./Artist/Album1/1-01 Title.m4a` => `./Artist/Album1/Disc1/01_Title.m4a` ==========
========== [DRY RUN] Replacing the delimiter: `./Artist/Album1/2-01 Title.m4a` => `./Artist/Album1/Disc2/01_Title.m4a` ==========
========== [DRY RUN] Replacing the delimiter: `./Artist/Album2/01 Title.m4a` => `./Artist/Album2/01_Title.m4a` ==========
========== [DRY RUN] Replacing the delimiter: `./Artist/Album2/02 Title.m4a` => `./Artist/Album2/02_Title.m4a` ==========
========== [DRY RUN] Done! ==========
========== [DRY RUN] Total Target File Count: 4 ==========
```

When the plan looks right, execute it with `--mode e`; `--extension` and `--delimiter` override the defaults:

```command
$ track-delimiter --mode e
$ track-delimiter --extension .mp3 --delimiter - --mode e
```

As a library:

```ruby
require 'spreen_tracks' # or require 'spreen-tracks'

SpreenTracks::Application.run                            # dry run over ./**/*.m4a
SpreenTracks::Application.run(delimiter: '-', mode: 'e') # execute the renames
```

## 4. Unit Test

```command
$ rake
Run options: --seed 21935

# Running:

..........

Finished in 2.362223s, 4.2333 runs/s, 10.1599 assertions/s.

10 runs, 24 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ bundle exec rubocop
Inspecting 12 files
............

12 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ bundle exec rbs-inline --output sig/generated/ .
🎉 Generated 7 RBS files under sig/generated
$ bundle exec steep check
# Type checking files:

..............

No type error detected. 🫖
```

## 7. Build

```command
$ gem build spreen-tracks.gemspec
$ gem install ./spreen-tracks-0.1.0.gem
```
