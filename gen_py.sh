#!/bin/bash
# -- 'On the road to pragmatism' -- #
TSTAMP="$(date +%d)/$(date +%m)/$(date +%Y)"
echo '#!/usr/bin/python' > $1
echo '# Created by' $(whoami)'@'$(hostname) >> $1
echo '# On:' $TSTAMP >> $1
echo '# --- Preamble --- #' >> $1
echo '# --- Declarations --- #' >> $1
echo '# --- Functions --- #' >> $1
echo 'def main ():' >> $1
echo '# --- Main --- #' >> $1
echo 'if __name__ == "__main__":' >> $1
echo '  main()' >> $1
# ----------------------------------#

