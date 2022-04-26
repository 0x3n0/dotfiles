//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/	 	/*Update Interval*/	/*Update Signal*/
  /* {" ", "/home/sec/.config/dwm/dwmblocks/scripts/recordscreen",		    360,		        2}, */

	{"", "cat /tmp/recordingicon 2>/dev/null",	0,	9},

    	{"  ", "$HOME/.config/dwm/dwmblocks/scripts/wifi",		        360,	            0},

	{"", "$HOME/.config/dwm/dwmblocks/scripts/brightness",      0,      9},

	{" ﮮ ", "$HOME/.config/dwm/dwmblocks/scripts/upt",		        60,		            2},

	{"  ", "$HOME/.config/dwm/dwmblocks/scripts/pacupdate",		360,		        9},
	
	{"  ", "$HOME/.config/dwm/dwmblocks/scripts/memory",	        6,		            1},

	{"  ", "$HOME/.config/dwm/dwmblocks/scripts/volume",			2,		            10},

	{"  ", "$HOME/.config/dwm/dwmblocks/scripts/clock",			5,		            0},
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim = '|';
