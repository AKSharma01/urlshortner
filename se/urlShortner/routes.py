from views import Shortner, DisplayShortn, Home, FilterShortner
urls =[
	('/', ['GET'], Home.as_view('home')),
	('/short', ['POST'], Shortner.as_view('shortner')),
	('/<shortnerId>', ['GET','PUT','DELETE'], DisplayShortn.as_view('nnn')),
	('/json/<shortnerId>', ['GET'], FilterShortner.as_view('khn'))
]