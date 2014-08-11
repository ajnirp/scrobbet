require 'sinatra'
require 'net/http'
require 'digest'
require 'nokogiri'

SCROBBLE_ROOT = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = ##
SECRET = ##

helpers do

	def sendrequest(data)
		sig = data.sort.map{|key, val| key + val}.join + SECRET
		data['api_sig'] = Digest::MD5.hexdigest(sig)
		return Net::HTTP.post_form(URI.parse(SCROBBLE_ROOT), data)
	end

end

post '/scrobble' do
	data = {
		'method' => 'track.scrobble',
		'api_key' => API_KEY,
		'sk' => params[:sk],
		'timestamp' => params[:timestamp],
		'artist' => params[:artist],
		'track' => params[:track],
		'album' => params[:album]
	}
	response = sendrequest(data)
	Nokogiri::Slop(response.body).lfm.attr('status')
end

post '/gettoken' do
	data = 	{
		'method' => 'auth.getToken', 
		'api_key' => API_KEY
	}
	response = sendrequest(data)
	Nokogiri::Slop(response.body).lfm.token.content
end

post '/getsession' do
	data = {
		'method' => 'auth.getSession',
		'api_key' => API_KEY,
		'token' => params[:token]
	}
	response = sendrequest(data)
	Nokogiri::Slop(response.body).lfm.session.key.content
end

