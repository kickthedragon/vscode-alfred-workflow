import sys
import os
import json
import plistlib


with open('info.plist', 'rb') as fp:
	info = plistlib.load(fp);

alfred_results = []


projects = info['variables']['PROJECTS_PATH']

query = sys.argv[1]

folderList = os.listdir(projects)


filteredList = []

for l in folderList:
	if query in l:
		filteredList.append(l)


sortedFolders = sorted(filteredList)



for dir in sortedFolders:
	if dir != '.DS_Store':
		result = {
				"title": dir,
				"arg": projects + '/' + dir,
				"icon": {
					"path": "icon/iu.png"
				}
			} 
		alfred_results.append(result)

response = json.dumps({
		"items": alfred_results
	})

sys.stdout.write(response)

