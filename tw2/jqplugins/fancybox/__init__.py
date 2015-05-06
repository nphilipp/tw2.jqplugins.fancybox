# -*- coding: utf-8 -*-
#
# tw2.jquery.fancybox - a jQuery FancyBox widget
#
# Copyright © 2010, 2013 Nils Philippsen <nils@tiptoe.de>
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
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import pkg_resources
pkg_resources.require("tw2.core >= 2.0")
pkg_resources.require("tw2.jquery >= 2.0")

from tw2.core import Widget, JSLink, CSSLink, Link, Param
from tw2.jquery.base import jquery_js, jQuery

__all__ = ("mousewheel_js", "fancybox_js", "fancybox_css", "FancyBox")

FANCYBOX_VERSION = "1.3.4"
MOUSEWHEEL_VERSION = "3.0.4"
EASING_VERSION = "1.3"

# JS Links

mousewheel_js = JSLink(modname=__name__,
        filename="static/jquery.mousewheel-%s.pack.js" % MOUSEWHEEL_VERSION)

easing_js = JSLink(modname=__name__,
        filename="static/jquery.easing-%s.pack.js" % EASING_VERSION)

fancybox_js = JSLink(modname=__name__,
        filename="static/jquery.fancybox-%s.pack.js" % FANCYBOX_VERSION)

# CSS Link

fancybox_css = CSSLink(modname=__name__,
        filename="static/jquery.fancybox-%s.css" % FANCYBOX_VERSION)

# Other resources

static_resources = Link(modname=__name__, filename="static", whole_dir=True)

# Widget

def NDParam(*p, **k):
    k.setdefault('default', None)
    return Param(*p, **k)

class FancyBox(Widget):
    resources = [fancybox_css, jquery_js, mousewheel_js, easing_js,
            fancybox_js, static_resources]

    fancybox_attrnames = (
            'padding', 'margin', 'opacity', 'modal', 'cyclic', 'scrolling',
            'width', 'height', 'autoScale', 'autoDimensions', 'centerOnScroll',
            'ajax', 'swf', 'hideOnOverlayClick', 'hideOnContentClick',
            'overlayShow', 'overlayOpacity', 'overlayColor',
            'titleShow', 'titlePosition', 'titleFromAlt', 'titleFormat',
            'transitionIn', 'transitionOut', 'speedIn', 'speedOut',
            'changeSpeed', 'changeFade', 'easingIn', 'easingOut',
            'showCloseButton', 'showNavArrows', 'enableEscapeButton',
            'onStart', 'onCancel', 'onComplete', 'onCleanup', 'onClosed')

    selector = Param("Selector specifying images to be decorated")

    padding = NDParam("Space between FancyBox wrapper and content")

    margin = NDParam("Space between viewport and FancyBox wrapper")

    opacity = NDParam("When True, transparency of content is changed "
                        "for elastic transitions")

    modal = NDParam("When True, 'overlayShow' is set to True and "
                      "'hideOnOverlayClick', 'hideOnContentClick', "
                      "'enableEscapeButton', 'showCloseButton' "
                      "are set to False")

    cyclic = NDParam("When True, galleries will be cyclic, allowing you to "
                       "keep pressing next/back.")

    scrolling = NDParam("Set the overflow CSS property to create or hide "
                          "scrollbars. Can be set to 'auto', 'yes', or 'no'")

    width = NDParam("Width for content types 'iframe' and 'swf'. Also set "
                      "for inline content if 'autoDimensions' is set to False")

    height = NDParam("Height for content types 'iframe' and 'swf'. Also set "
                       "for inline content if 'autoDimensions' is set to False")

    autoScale = NDParam("If True, FancyBox is scaled to fit in viewport")

    autoDimensions = NDParam("For inline and ajax views, resizes the view "
                               "to the element received. Make sure it has "
                               "dimensions otherwise this will give "
                               "unexpected results")

    centerOnScroll = NDParam("When True, FancyBox is centered while "
                               "scrolling page")

    ajax = NDParam("Ajax options. Note: 'error' and 'success' will be "
                     "overwritten by FancyBox")

    swf = NDParam("Params to put on the swf object")

    hideOnOverlayClick = NDParam("Toggle if clicking the overlay should "
                                   "close FancyBox")

    hideOnContentClick = NDParam("Toggle if clicking the content should "
                                   "close FancyBox")

    overlayShow = NDParam("Toggle overlay")

    overlayOpacity = NDParam("Opacity of the overlay (from 0 to 1; "
                               "default - 0.3)")

    overlayColor = NDParam("Color of the overlay")

    titleShow = NDParam("Toggle title")

    titlePosition = NDParam("The position of title. Can be set to "
                              "'outside', 'inside' or 'over'")

    titleFromAlt = NDParam("Whether to use the alt property for the title.")

    titleFormat = NDParam("Callback to customize title area. You can set "
                            "any html - custom image counter or even custom "
                            "navigation")

    transitionIn = transitionOut = NDParam(
            "The transition type. Can be set to 'elastic', 'fade' or 'none'")

    speedIn = speedOut = NDParam(
            "Speed of the fade and elastic transitions, in milliseconds")

    changeSpeed = NDParam("Speed of resizing when changing gallery items, "
                            "in milliseconds")

    changeFade = NDParam("Speed of the content fading while changing "
                           "gallery items")

    easingIn = easingOut = NDParam("Easing used for elastic animations")

    showCloseButton = NDParam("Toggle close button")

    showNavArrows = NDParam("Toggle navigation arrows")

    enableEscapeButton = NDParam("Toggle if pressing Esc button closes "
                                   "FancyBox")

    onStart = NDParam("Will be called right before attempting to load "
                        "the content")

    onCancel = NDParam("Will be called after loading is canceled")

    onComplete = NDParam("Will be called once the content is displayed")

    onCleanup = NDParam("Will be called just before closing")

    onClosed = NDParam("Will be called once FancyBox is closed")

    template = ""

    def prepare(self):
        super(FancyBox, self).prepare()
        if not self.selector:
            raise ValueError("FancyBox needs a selector")

        if (getattr(self, 'scrolling', None) and
            self.scrolling not in ('auto', 'yes', 'no')):
            raise ValueError("Scrolling must be 'auto', 'yes' or 'no'")

        if (getattr(self, 'overlayOpacity', None) and
            not (0.0 < float(self.overlayOpacity) < 1.0)):
            raise ValueError("Overlay opacity must be between 0.0 and 1.0")

        if (getattr(self, 'titlePosition', None) and
            self.titlePosition not in ('outside', 'inside', 'over')):
            raise ValueError("Title position must be 'outside', 'inside' "
                             "or 'over'")

        if (getattr(self, 'transitionIn', None) and
            self.transitionIn not in ('elastic', 'fade', 'none')):
            raise ValueError("In transition must be 'elastic', 'fade' or "
                             "'none'")

        if (getattr(self, "transitionOut", None) and
            self.transitionOut not in ('elastic', 'fade', 'none')):
            raise ValueError("Out transition must be 'elastic', 'fade' or "
                             "'none'")

        params = {}
        for name in self.fancybox_attrnames:
            if getattr(self, name, None):
                params[name] = getattr(self, name)

        call = jQuery(self.selector).fancybox(params)
        self.add_call(call)

    def generate_output(self, displays_on):
        return u""
