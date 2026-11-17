#!/bin/sh
# Ping IndexNow (Bing etc.) after publishing changes. Run from repo root.
URLS=$(grep -o '<loc>[^<]*</loc>' sitemap.xml | grep -v '/assets/' | sed 's/<[^>]*>//g' | sed 's/.*/"&"/' | paste -sd, -)
curl -s -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' \
  -d "{\"host\":\"livingwater-pws.com\",\"key\":\"03ece7c22a731657bc87f6a29cbab873\",\"keyLocation\":\"https://livingwater-pws.com/03ece7c22a731657bc87f6a29cbab873.txt\",\"urlList\":[$URLS]}"
echo done
