class cprint:
    def __init__(self):
        pass

    def __call__(self, text, foreground="", background="", underline=False, bold=False):
        '''get text and change attribute'''
        self.text = text
        self.underline = underline
        self.foreground = foreground
        self.background = background
        self.bold = bold
        self.fcolors = {'default':39,
                       'black':30,
                       'red':31,
                       'green':32,
                       'yellow':33,
                       'blue':34,
                       'magenta':35,
                       'cyan':36,
                       'light_gray':37,
                       'dark_gray':90,
                       'light_red':91,
                       'light_green':92,
                       'light_yellow':93,
                       'light_blue':94,
                       'light_magenta':95,
                       'light_cyan':96,
                       'white':97}
        self.bcolors = {'default':49,
                       'black':40,
                       'red':41,
                       'green':42,
                       'yellow':43,
                       'blue':44,
                       'magenta':45,
                       'cyan':46,
                       'light_gray':47,
                       'dark_gray':100,
                       'light_red':101,
                       'light_green':102,
                       'light_yellow':103,
                       'light_blue':104,
                       'light_magenta':105,
                       'light_cyan':106,
                       'white':107}
        # get foreground number
        self.template = "\033[%BOLD%;%UNDERLINE%;%BG%;%FG%m%TEXT%\033[0m"
        if self.foreground:
            self.c_f = self.fcolors[self.foreground]
            self.template = self.template.replace("%FG%", str(self.c_f))
        else:
            self.f_default = self.fcolors['default']
            self.template = self.template.replace("%FG%", str(self.f_default))
        # get background number
        if self.background:
            self.c_b = self.bcolors[self.background]
            self.template = self.template.replace("%BG%", str(self.c_b))
        else:
            self.b_default = self.bcolors['default']
            self.template = self.template.replace("%BG%", str(self.b_default))

        if self.underline:
            self.template = self.template.replace("%UNDERLINE%", str(4))
        else:
            self.template = self.template.replace("%UNDERLINE%;", "")

        if self.bold:
            self.template = self.template.replace("%BOLD%", str(1))
        else:
            self.template = self.template.replace("%BOLD%;", "")

        self.template = self.template.replace("%TEXT%", self.text)
        print(self.template)
