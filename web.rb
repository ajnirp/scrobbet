require 'sinatra'
require 'net/http'
require 'digest'
require 'nokogiri'

SCROBBLE_ROOT = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '***REMOVED***'
SECRET = '***REMOVED***'
SESSION_KEY = '052193ef1eb095c233ad803d3a20aae9'

get '/scrobble' do
	data = {
		'method' => 'track.scrobble',
		'api_key' => API_KEY,
		'sk' => SESSION_KEY,
		'timestamp' => params[:timestamp],
		'artist' => params[:artist],
		'track' => params[:track],
		'album' => params[:album]
	}
	sig = data.sort.map{|key, val| key + val}.join + SECRET
	data['api_sig'] = Digest::MD5.hexdigest(sig)
	response = Net::HTTP.post_form(URI.parse(SCROBBLE_ROOT), data)
	Nokogiri::Slop(response.body).lfm.attr('status')
end
