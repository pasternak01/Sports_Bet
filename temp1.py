import re

year = 2025

urls = [f"https://www.tennisexplorer.com/madrid/{year}/atp-men/",
       f"https://www.tennisexplorer.com/madrid-wta/{year}/wta-women/"]
matches =[]

for url in urls:
       match = re.search(r'([^/]+)/?$', url)
       if match:
          matches.append(match.group(1))




print(matches)
