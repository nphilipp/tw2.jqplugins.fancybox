# -*- coding: utf-8 -*-
#
# tw.jquery.fancybox - a jQuery FancyBox widget
#
# Copyright © 2010 Nils Philippsen <nils@tiptoe.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from tw.api import Widget, JSLink, CSSLink, js_function
from tw.jquery.base import jquery_js

__all__ = ("mousewheel_js", "fancybox_js", "fancybox_css", "FancyBox")

FANCYBOX_VERSION = "1.3.1"
MOUSEWHEEL_VERSION = "3.0.2"

# JS Links

mousewheel_js = JSLink(modname=__name__,
        filename="static/jquery.mousewheel-%s.pack.js" % MOUSEWHEEL_VERSION)

fancybox_js = JSLink(modname=__name__,
        filename="static/jquery.fancybox-%s.pack.js" % FANCYBOX_VERSION)

# CSS Link

fancybox_css = CSSLink(modname=__name__,
        filename="static/jquery.fancybox-%s.css" % FANCYBOX_VERSION)

# Widget

class FancyBox(Widget):
    javascript = [jquery_js, mousewheel_js, fancybox_js]
    css = [fancybox_css]

    fancybox_attrnames = (
            'padding', 'margin', 'opacity', 'modal', 'cyclic', 'scrolling',
            'width', 'height', 'autoScale', 'autoDimensions', 'centerOnScroll',
            'ajax', 'swf', 'hideOnOverlayClick', 'hideOnContentClick',
            'overlayShow', 'overlayOpacity', 'overlayColor',
            'titleShow', 'titlePosition', 'titleFormat',
            'transitionIn', 'transitionOut', 'speedIn', 'speedOut',
            'changeSpeed', 'changeFade', 'easingIn', 'easingOut',
            'showCloseButton', 'showNavArrows', 'enableEscapeButton',
            'onStart', 'onCancel', 'onComplete', 'onCleanup', 'onClosed')

    def update_params(self, d):
        super(FancyBox, self).update_params(d)

        if not hasattr(d, "selector"):
            raise ValueError("FancyBox needs a selector")

        params = {}
        for name in self.fancybox_attrnames:
            if hasattr(d, name):
                params[name] = getattr(d, name)

        jQuery = js_function('jQuery')
        call = jQuery(d.selector).fancybox(params)
        self.add_call(call)
