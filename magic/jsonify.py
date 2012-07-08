import re

def cap_lower(name):
	capname = name.capitalized()
	lowername = name.lower()
	# already camel-cased
	if len(re.findall('[A-Z]', name)) > 0:
		capname = name
		lowername = lowername[0]+re.sub(r'([A-Z])',r'_\1',capname[1:]).lower()
		lowername = re.sub("u_r_l", "url", lowername)
	return (capname, lowername)

def blockify(block, *args, **kwargs):
	capblock, lowerblock = cap_lower(block)
	print "{block:"+capblock+"}"
	if len(args) == 0:
		args = [block]
	for name in args:
		capname, lowername = cap_lower(name)
		print "  "+lowername+": {JSPlaintext"+capname+"},"
	for blockname in kwargs:
		capname, lowername = cap_lower(blockname)
		blockarg = kwargs[blockname]
		print "  {block:"+capname+"}"
		if isinstance(blockarg, list):
			print "    "+lowername+": {"
			for variant in blockarg:
				variant = str(variant)
				print "      "+variant+": {JSPlaintext"+capname+"-"+variant+"},"
			print "    }"
		else:
			capvalue, lowervalue = cap_lower(blockarg)
			print "    "+lowervalue+": {JSPlaintext"+capvalue+"},"
		print "  {/block:"+capname+"}"
	print "{/block:"+block+"}"

blockify("link","URL","name","target",description="description")

blockify("chat", title="title")

blockify("lines", "name", "line", "UserNumber", label="label")

blockify("audio", PlayCount="playcount", AudioEmbed=[250,400,500,640], caption="caption", Artist="Artist", AlbumArt="AlbumArtURL", TrackName="TrackName", ExternalAudio="ExternalAudioURL")

blockify("ExternalAudio","ExternalAudioURL")

blockify("video", "PlayCount", "FormattedPlayCount", "PlayCountWithLabel", Video=[500,400,250], caption="caption")

blockify("Answer", "question", "answer", "asker", AskerPortraitURL=[16,24,30,40,48,64,96,128])

blockify("NoteCount", "NoteCount", "NoteCountWithLabel")

blockify("Tags", "Tag", "URLSafeTag", "TagURL", "TagURLChrono")

blockify("ContentSource", "SourceURL", "SourceTitle")
blockify("SourceLogo", "BlackLogoURL", "LogoWidth", "LogoHeight")

blockify("GroupMember", name="GroupMemberName", title="GroupMemberTitle", URL="GroupMemberURL", PortraitURL=[16,24,30,40,48,64,96,128])

blockify("PostAuthorPortraitURL", PostAuthorPortraitURL=[16,24,30,40,48,64,96,128])

blockify("Followed", "FollowedName", "FollowedTitle", "FollowedURL", FollowedPortraitURL=[16,24,30,40,48,64,96,128])

blockify("PreviousDayPage", "PreviousDayPage")
blockify("NextDayPage")