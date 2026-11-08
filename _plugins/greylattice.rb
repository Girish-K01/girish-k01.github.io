# frozen_string_literal: true

# GreyLattice posts for the Blog page (/blog/).
#
# At build time this reads the GreyLattice Substack RSS feed and exposes the posts as
# site.data["greylattice"] (newest first). If the feed can't be fetched (offline, Substack
# down, rate limited), the committed snapshot _data/greylattice.json is used instead, so a
# build never fails because of the feed. The deploy workflow also rebuilds weekly, so new
# posts appear without a commit.
#
#   GREYLATTICE_OFFLINE=1   skip the network and use the snapshot
#   GREYLATTICE_SNAPSHOT=1  rewrite the snapshot from the live feed (then commit it)
require "cgi/escape"
require "json"
require "net/http"
require "rexml/document"
require "time"

module GreyLattice
  FEED_URL = "https://greylattice.substack.com/feed"
  SNAPSHOT = "_data/greylattice.json"
  CACHE_SECONDS = 3600 # `jekyll serve` rebuilds on every save; don't refetch each time
  IMAGE_WIDTH = 320 # the blog list shows images at about 144px wide

  class Generator < Jekyll::Generator
    priority :highest

    class << self
      attr_accessor :cache, :cached_at
    end

    def generate(site)
      posts = cached_posts || fetch_posts
      if posts
        self.class.cache = posts
        self.class.cached_at = Time.now
        site.data["greylattice"] = posts
        write_snapshot(site, posts) if ENV["GREYLATTICE_SNAPSHOT"]
      else
        count = Array(site.data["greylattice"]).size
        Jekyll.logger.warn "GreyLattice:", "feed unavailable; using #{SNAPSHOT} (#{count} posts)"
      end
    end

    private

    def cached_posts
      at = self.class.cached_at
      self.class.cache if at && Time.now - at < CACHE_SECONDS
    end

    def fetch_posts
      return nil if ENV["GREYLATTICE_OFFLINE"]

      uri = URI(FEED_URL)
      response = Net::HTTP.start(uri.host, uri.port, use_ssl: true, open_timeout: 5, read_timeout: 15) do |http|
        http.get(uri.request_uri, "User-Agent" => "girish-k01.github.io site build")
      end
      unless response.is_a?(Net::HTTPSuccess)
        Jekyll.logger.warn "GreyLattice:", "feed returned HTTP #{response.code}"
        return nil
      end
      parse(response.body)
    rescue StandardError => e
      Jekyll.logger.warn "GreyLattice:", "#{e.class}: #{e.message}"
      nil
    end

    def parse(xml)
      posts = []
      REXML::Document.new(xml).elements.each("rss/channel/item") do |item|
        text = ->(name) { item.elements[name]&.text.to_s.strip }
        enclosure = item.elements["enclosure"]
        type = enclosure ? enclosure.attributes["type"].to_s : ""
        image = if type.start_with?("image/")
                  enclosure.attributes["url"]
                else
                  text.call("content:encoded")[/<img[^>]+src="([^"]+)"/, 1]
                end
        posts << {
          "title" => CGI.unescapeHTML(text.call("title")),
          "url" => text.call("link"),
          "date" => Time.parse(text.call("pubDate")).utc.strftime("%Y-%m-%d"),
          "summary" => CGI.unescapeHTML(text.call("description")),
          "audio" => type.start_with?("audio/"),
          "image" => resize(image),
        }
      end
      posts.empty? ? nil : posts.sort_by { |p| p["date"] }.reverse
    end

    # Substack's image CDN resizes on request; the list only needs IMAGE_WIDTH, not the original.
    def resize(url)
      return nil if url.nil? || url.empty?
      return url unless url.include?("substackcdn.com/image/fetch/")

      if url.match?(/[\/,]w_\d+/)
        url.sub(/([\/,])w_\d+/, "\\1w_#{IMAGE_WIDTH}")
      else
        url.sub("/image/fetch/", "/image/fetch/w_#{IMAGE_WIDTH},c_limit,")
      end
    end

    def write_snapshot(site, posts)
      File.write(site.in_source_dir(SNAPSHOT), JSON.pretty_generate(posts) + "\n")
      Jekyll.logger.info "GreyLattice:", "wrote #{SNAPSHOT} (#{posts.size} posts)"
    end
  end
end
