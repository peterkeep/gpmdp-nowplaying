# Google Play Music Desktop Player: Now Playing

This script reads the current song information from GPMDP's `playback.json` file, and prints the information.

When GPMDP is closed (or isn't playing/paused), it does not display anything.

This can be used via terminal, genmon, etc. to print now playing information.

## Screenshots

![](https://raw.githubusercontent.com/peterkeep/gpmdp-nowplaying/master/screenshot1.png)


![](https://raw.githubusercontent.com/peterkeep/gpmdp-nowplaying/master/screenshot2.png)

## Usage

Make the python script executable by navigating to the folder containing `./nowplaying`:

`cd .nowplaying`

`chmod +x gpmdp-np.py`

Now the script can be run via terminal command with: `./gpmdp-np.py`
