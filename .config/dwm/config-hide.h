static const unsigned int borderpx = 2;   /* border pixel of windows */
static const unsigned int snap     = 32;  /* snap pixel */
static const unsigned int gappih    = 12;       /* horiz inner gap between windows */
static const unsigned int gappiv    = 12;       /* vert inner gap between windows */
static const unsigned int gappoh    = 12;       /* horiz outer gap between windows and screen edge */
static const unsigned int gappov    = 12;       /* vert outer gap between windows and screen edge */
static const int smartgaps          = 0;        /* 1 means no outer gap when there is only one window */
static const unsigned int gappx    = 0;   /* pixel gap between clients */
static const int showbar           = 1;   /* 0 means no bar */
static const int topbar            = 1;   /* 0 means bottom bar */
static const int horizpadbar       = 0;   /* horizontal padding for statusbar */
static const int vertpadbar        = 3;   /* vertical padding for statusbar */

/* static const char *fonts[]     = {"Nerd Font Mono:weight=bold:size=10:antialias=true:hinting=true","SymbolsNerdFont:size=10:antialias=true:autohint=true","NotoColorEmoji:size=11:antialias=true:autohint=true"}; */


/* static const char *fonts[]     = {"Mononoki Fira Code Sans SouceCodePro Mono:bold:size=9:antialias=true:autohint=true"}; */
static const char *fonts[]     = { "SymbolsNerdFont:size=10:antialias=true:autohint=true", "FuraCode Nerd Font:style=Medium:size=11" };

static const char col_1[]  = "#44475a"; /* #44475a */
static const char col_2[]  = "#44475a";
static const char col_3[]  = "#f8f8f2"; /* #f8f8f2 */
static const char col_4[]  = "#be4949"; /* #be4949 */
static const char col_5[]  = "#000000"; /* #000000 */


static const unsigned int baralpha    = 0xff;
static const unsigned int borderalpha = OPAQUE;
static const char *colors[][3]        = {
                 /*               fg     bg    border  */
                [SchemeNorm] = { col_3, col_1, col_2 },
                [SchemeSel]  = { col_5, col_3, col_3 },
                [SchemeTitle]  = { col_3, col_1,  col_1  },                
};

static const unsigned int alphas[][3] = {
                 /*              fg      bg        border     */
                [SchemeNorm] = { OPAQUE, baralpha, borderalpha },
                [SchemeSel]  = { OPAQUE, baralpha, borderalpha },
                [SchemeTitle]  = { OPAQUE, baralpha, borderalpha },
};


/* tagging */
 static const char *tags[] = { " Home", " Chrome", " Burpsuite", " Telegram", " Alacritty", " LinkedIn", " Twitter", " Github", " Bugs " };

 static const Rule rules[] = {
     /* xprop(1):
      *  WM_CLASS(STRING) = instance, class
      *  WM_NAME(STRING) = title
      */
     /* class               instance    title       tags mask     isfloating   monitor */
     { "Home",              NULL,       NULL,       0,            0,           -1 }, // tag 1
     { "Chromium",          NULL,       NULL,       1 << 1,       0,           -1 }, // tag 2
     { "burp-StartBurp",    NULL,       NULL,       1 << 2,       0,           -1 }, // tag 3
     { "TelegramDesktop",   NULL,       NULL,       1 << 3,       0,           -1 }, // tag 4
     { "Alacritty",         NULL,       NULL,       1 << 4,       0,           -1 }, // tag 5
     { "Min",               NULL,       NULL,       1 << 5,       0,           -1 }, // tag 6
     { "qutebrowser",       NULL,       NULL,       1 << 6,       0,           -1 }, // tag 7
};

/* layout(s) */
static const float mfact     = 0.50; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 0;    /* 1 means respect size hints in tiled resizals */

#include "layouts.c"
static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "[]=",      tile },    /* first entry is default */
	{ "><>",      NULL },    /* no layout function means floating behavior */
	{ "[M]",      monocle },
	{ "HHH",      grid },
	{ NULL,       NULL },
};

/* key definitions */
#define MODKEY Mod4Mask
#define TAGKEYS(CHAIN,KEY,TAG) \
	{ MODKEY,                       CHAIN,    KEY,      view,           {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask,           CHAIN,    KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ShiftMask,             CHAIN,    KEY,      tag,            {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, CHAIN,    KEY,      toggletag,      {.ui = 1 << TAG} },

#define CMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }
/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* dmenu */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
/* If you are using the standard dmenu program, use the following. */
static const char *dmenucmd[]    = { "dmenu_run", "-l", "15", "-c", "-bw", "2", NULL };

/* If you are using the dmenu-distrotube-git program, use the following for a cooler dmenu! */
/* static const char *dmenucmd[]    = { "dmenu_run", "-g", "10", "-l", "48", "-p", "Run: ", NULL };
*/
/* the st terminal with tabbed */
static const char *termcmd[]     = { "st", NULL };
/* An alternative way to launch st along with the fish shell */
/* static const char *termcmd[]     = { "st", "-e fish", NULL }; */
static const char *tabtermcmd[]  = { "tabbed", "-r", "2", "st", "-w", "''", NULL };

static Key keys[] = {
	/* modifier             chain key  key        function        argument */
	{ MODKEY|ShiftMask,     -1,        XK_Return, spawn,          {.v = dmenucmd } },
	{ MODKEY,               -1,        XK_Return, spawn,          {.v = termcmd } },
	{ Mod1Mask,             -1,        XK_Return, spawn,          {.v = tabtermcmd } },
	{ MODKEY,               -1,        XK_b,      togglebar,      {0} },
	{ MODKEY|ShiftMask,     -1,        XK_j,      rotatestack,    {.i = +1 } },
	{ MODKEY|ShiftMask,     -1,        XK_k,      rotatestack,    {.i = -1 } },
	{ MODKEY,               -1,        XK_j,      focusstack,     {.i = +1 } },
	{ MODKEY,               -1,        XK_k,      focusstack,     {.i = -1 } },
	{ MODKEY,               -1,        XK_i,      incnmaster,     {.i = +1 } },
	{ MODKEY,               -1,        XK_d,      incnmaster,     {.i = -1 } },
	{ MODKEY,               -1,        XK_h,      setmfact,       {.f = -0.05} },
	{ MODKEY,               -1,        XK_l,      setmfact,       {.f = +0.05} },
	{ MODKEY|Mod4Mask,      -1,      	XK_h,      incrgaps,       {.i = +1 } },
  { MODKEY|Mod4Mask,      -1,       	XK_l,      incrgaps,       {.i = -1 } },
  { MODKEY|Mod4Mask|ShiftMask, -1,	XK_h,      incrogaps,      {.i = +1 } },
  { MODKEY|Mod4Mask|ShiftMask,    -1,	XK_l,      incrogaps,      {.i = -1 } },
  { MODKEY|Mod4Mask|ControlMask,  -1,	XK_h,      incrigaps,      {.i = +1 } },
  { MODKEY|Mod4Mask|ControlMask,  -1,	XK_l,      incrigaps,      {.i = -1 } },
  { MODKEY|Mod4Mask,              -1,	XK_0,      togglegaps,     {0} },
  { MODKEY|Mod4Mask|ShiftMask,    -1,	XK_0,      defaultgaps,    {0} },
  { MODKEY,                       -1,	XK_y,      incrihgaps,     {.i = +1 } },
  { MODKEY,                       -1,	XK_o,      incrihgaps,     {.i = -1 } },
  { MODKEY|ControlMask,           -1,	XK_y,      incrivgaps,     {.i = +1 } },
  { MODKEY|ControlMask,           -1,	XK_o,      incrivgaps,     {.i = -1 } },
  { MODKEY|Mod4Mask,              -1,	XK_y,      incrohgaps,     {.i = +1 } },
  { MODKEY|Mod4Mask,              -1,	XK_o,      incrohgaps,     {.i = -1 } },
  { MODKEY|ShiftMask,             -1,	XK_y,      incrovgaps,     {.i = +1 } },
  { MODKEY|ShiftMask,             -1,	XK_o,      incrovgaps,     {.i = -1 } },
	{ MODKEY|ControlMask,   -1,        XK_Return, zoom,           {0} },
	{ MODKEY,               -1,        XK_Tab,    view,           {0} },
	{ MODKEY|ShiftMask,     -1,        XK_c,      killclient,     {0} },


    /* Layout manipulation */
	{ MODKEY,               -1,        XK_Tab,    cyclelayout,    {.i = -1 } },
	{ MODKEY|ShiftMask,     -1,        XK_Tab,    cyclelayout,    {.i = +1 } },
	{ MODKEY,               -1,        XK_space,  setlayout,      {0} },
	{ MODKEY|ShiftMask,     -1,        XK_space,  togglefloating, {0} },

    /* Switch to specific layouts */
	{ MODKEY,               -1,        XK_t,      setlayout,      {.v = &layouts[0]} },
	{ MODKEY,               -1,        XK_f,      setlayout,      {.v = &layouts[1]} },
	{ MODKEY,               -1,        XK_m,      setlayout,      {.v = &layouts[2]} },
	{ MODKEY,               -1,        XK_g,      setlayout,      {.v = &layouts[3]} },

	{ MODKEY,               -1,        XK_0,      view,           {.ui = ~0 } },
	{ MODKEY|ShiftMask,     -1,        XK_0,      tag,            {.ui = ~0 } },

    /* Switching between monitors */
	{ MODKEY,               -1,        XK_comma,  focusmon,       {.i = -1 } },
	{ MODKEY,               -1,        XK_period, focusmon,       {.i = +1 } },
	{ MODKEY|ShiftMask,     -1,        XK_comma,  tagmon,         {.i = -1 } },
	{ MODKEY|ShiftMask,     -1,        XK_period, tagmon,         {.i = +1 } },

    /* Keybindings for programs using the format SUPER + ALT + "key" */
    { MODKEY|Mod1Mask,      -1,        XK_r,      spawn,          CMD("recording") },
	{ MODKEY|Mod1Mask,      -1,        XK_g,      spawn,          CMD("qutebrowser gist.github.com/0x3n0") },
	{ MODKEY|Mod1Mask,      -1,        XK_l,      spawn,          CMD("qutebrowser linkedin.com") },
    { MODKEY|Mod1Mask,      -1,        XK_y,      spawn,          CMD("qutebrowser youtube.com") },
    { MODKEY|Mod1Mask,      -1,        XK_i,      spawn,          CMD("qutebrowser instgaram.com") },
    { MODKEY|Mod1Mask,      -1,        XK_w,      spawn,          CMD("qutebrowser web.whatsapp.com") },
    { MODKEY|Mod1Mask,      -1,        XK_t,      spawn,          CMD("qutebrowser twitter.com") },
	{ MODKEY|Mod1Mask,      -1,        XK_b,      spawn,          CMD("min") },
	{ MODKEY|Mod1Mask,      -1,        XK_c,      spawn,          CMD("telegram-desktop") },
	{ MODKEY|Mod1Mask,      -1,        XK_f,      spawn,          CMD("pcmanfm") },
    { Mod1Mask,          	-1,        XK_x,      spawn,          CMD("flameshot gui") },


	TAGKEYS(                -1,        XK_1,                      0)
	TAGKEYS(                -1,        XK_2,                      1)
	TAGKEYS(                -1,        XK_3,                      2)
	TAGKEYS(                -1,        XK_4,                      3)
	TAGKEYS(                -1,        XK_5,                      4)
	TAGKEYS(                -1,        XK_6,                      5)
	TAGKEYS(                -1,        XK_7,                      6)
	TAGKEYS(                -1,        XK_8,                      7)
	TAGKEYS(                -1,        XK_9,                      8)
	{ MODKEY|ShiftMask,     -1,        XK_q,	  quit,		      {0} },
    { MODKEY|ShiftMask,     -1,        XK_r,      quit,           {1} },
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static Button buttons[] = {
	/* click           event mask   button          function        argument */
	{ ClkLtSymbol,     0,           Button1,        setlayout,      {0} },
	{ ClkLtSymbol,     0,           Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,     0,           Button2,        zoom,           {0} },
	{ ClkStatusText,   0,           Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,    MODKEY,      Button1,        movemouse,      {0} },
	{ ClkClientWin,    MODKEY,      Button2,        togglefloating, {0} },
	{ ClkClientWin,    MODKEY,      Button3,        resizemouse,    {0} },
	{ ClkTagBar,       0,           Button1,        view,           {0} },
	{ ClkTagBar,       0,           Button3,        toggleview,     {0} },
	{ ClkTagBar,       MODKEY,      Button1,        tag,            {0} },
	{ ClkTagBar,       MODKEY,      Button3,        toggletag,      {0} },
};
