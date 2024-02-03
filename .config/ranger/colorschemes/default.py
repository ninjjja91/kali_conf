# | | / /
# | |/ / _   _  ___ ____
# |    \| | | |/ _ \_  /  Author: Kyoz
# | |\  \ |_| | (_) / /   Github: github.com/banminkyoz
# \_| \_/\__, |\___/___|  Email : banminkyoz@gmail.com
#         __/ |
#        |___/

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import default_colors, reverse, bold, normal, default


# pylint: disable=too-many-branches,too-many-statements
class Default(ColorScheme):
    progress_bar_color = 88

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = 109
                bg = 230
            if context.border:
                fg = 57
            if context.image:
                fg = 84
            if context.video:
                fg = 191
            if context.audio:
                fg = 156
            if context.document:
                fg = 18
            if context.container:
                attr |= bold
                fg = 156
            if context.directory:
                attr |= bold
                fg = 75
            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                attr |= bold
                fg = 81
            if context.socket:
                fg = 227
                attr |= bold
            if context.fifo or context.device:
                fg = 242
                if context.device:
                    attr |= bold
            if context.link:
                fg = 75 if context.good else 227
                bg = 82
            if context.bad:
                bg = 221
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (190, 93):
                    fg = 154
                else:
                    fg = 184
            if not context.selected and (context.cut or context.copied):
                fg = 63
                bg = 127
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = 191
            if context.badinfo:
                if attr & reverse:
                    bg = 158
                else:
                    fg = 87

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg =93
            elif context.directory:
                fg = 82
            elif context.tab:
                if context.good:
                    bg = 82
            elif context.link:
                fg = 63

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 120
                elif context.bad:
                    fg = 232
            if context.marked:
                attr |= bold | reverse
                fg = 226
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 229
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = 84
                attr &= ~bold
            if context.vcscommit:
                fg = 184
                attr &= ~bold

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 118

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = 166
            elif context.vcschanged:
                fg = 75
            elif context.vcsunknown:
                fg = 75
            elif context.vcsstaged:
                fg = 141
            elif context.vcssync:
                fg = 84
            elif context.vcsignored:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync:
                fg = 84
            elif context.vcsbehind:
                fg = 155
            elif context.vcsahead:
                fg = 75
            elif context.vcsdiverged:
                fg = 227
            elif context.vcsunknown:
                fg = 75

        return fg, bg, attr
