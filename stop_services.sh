
#!/bin/bash

# Etsi ja lopeta kaikki pyörivät uv-prosessit
echo "Sammutetaan palvelut..."

# Etsi kaikki uv-prosessit ja tapa ne
pkill -f 'uv run'

echo "Kaikki palvelut on sammutettu."
