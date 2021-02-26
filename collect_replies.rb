require 'nokogiri'
require 'open-uri'
require 'json'

NITTER_INSTANCES = [
    'https://nitter.42l.fr',
    'https://nitter.nixnet.services',
    'https://nitter.13ad.de',
    'https://nitter.pussthecat.org',
    'https://nitter.mastodont.cat',
    'https://nitter.tedomum.net',
    'https://nitter.fdn.fr',
    'https://nitter.1d4.us',
    'https://nitter.kavin.rocks',
    'https://tweet.lambda.dance',
    'https://nitter.cc',
    'https://nitter.weaponizedhumiliation.com',
    'https://nitter.vxempire.xyz',
    'https://nitter.unixfox.eu',
    'https://nitter.domain.glass',
    'https://nitter.himiko.cloud',
    'https://nitter.eu',
    'https://nitter.ethibox.fr',
    'https://nitter.namazso.eu',
    'https://nitter.mailstation.de',
    'https://nitter.actionsack.com',
    'https://nitter.cattube.org',
]

file = File.open('./threads.txt')
$threads = file.readlines()
file.close

$tweets = []

def start_thread!

    Thread.new {
        $instance = ''

        def rotate_instance!
            $instance = NITTER_INSTANCES.sample

            puts "rotated to " + $instance
        end

        rotate_instance!

        i = 0

        # tweets.each do |tweet|
        while true do
            thread = $threads.sample.strip!
            $threads.delete(thread)

            i += 1

            if i % 2 == 0
                rotate_instance!
            end

            url = $instance + thread

            begin
                doc = Nokogiri::HTML(URI.open(url))
                puts url
            rescue
                puts 'we\'ve had an accident uwu'
                rotate_instance!
                next
            end

            replies = doc.css('.tweet-content').map {|t| t.content}
            base_tweet = replies.first
            replies.delete(base_tweet)

            tweet = {
                :content => base_tweet,
                :replies => replies
            }

            $tweets.push(tweet)

            puts ''
            puts tweet
            puts ''
            # puts $tweets
            File.write('tweet_replies.json', $tweets.to_json)
        end


        # file = File.open('tweet_replies.json')
        # file.write(tweets.to_json)
        # file.close
    }

end

start_thread!
start_thread!
start_thread!
start_thread!
start_thread!

while true do; end
