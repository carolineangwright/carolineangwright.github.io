with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    "fill%3D'var(--c-deep-teal)'",
    "fill%3D'var(--c-deep-teal)';display:none",
    1
)

# Also hide via display:none on the div itself
content = content.replace(
    "perspective-origin:720px 18px;pointer-events:auto;position:static;position-anchor:none;position-area:none;position-try-fallbacks:none;position-try-order:normal;position-visibility:anchors-visible;print-color-adjust:economy;quotes:auto;r:0px;reading-flow:normal;reading-order:0;resize:none;right:auto;rotate:none;row-gap:normal;ruby-align:space-around;ruby-position:over;rx:auto;ry:auto;scale:none;scroll-behavior:auto;scroll-initial-target:none;scroll-margin-block-end:0px;scroll-margin-block-start:0px;scroll-margin-bottom:0px;scroll-margin-inline-end:0px;scroll-margin-inline-start:0px;scroll-margin-left:0px;scroll-margin-right:0px;scroll-margin-top:0px;scroll-marker-group:none;scroll-padding-block-end:auto;scroll-padding-block-start:auto;scroll-padding-bottom:auto;scroll-padding-inline-end:auto;scroll-padding-inline-start:auto;scroll-padding-left:auto;scroll-padding-right:auto;scroll-padding-top:auto;scroll-snap-align:none;scroll-snap-stop:normal;scroll-snap-type:none;scroll-target-group:none;scroll-timeline-axis:block;scroll-timeline-name:none;scrollbar-color:auto;scrollbar-gutter:auto;scrollbar-width:none;shape-image-threshold:0;shape-margin:0px;shape-outside:none;shape-rendering:auto;speak:normal;stop-color:rgb(0, 0, 0);stop-opacity:1;stroke:none;stroke-dasharray:none;stroke-dashoffset:0px;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-width:1px;tab-size:8;table-layout:auto;text-align:start;text-align-last:auto;text-anchor:start;text-autospace:no-autospace;text-box-edge:auto;text-box-trim:none;text-combine-upright:none;text-decoration:none;text-decoration-color:rgb(35, 20, 17);text-decoration-line:none;text-decoration-skip-ink:auto;text-decoration-style:solid;text-decoration-thickness:auto;text-emphasis-color:rgb(35, 20, 17);text-emphasis-position:over;text-emphasis-style:none;text-indent:0px;text-justify:auto;text-orientation:mixed;text-overflow:clip;text-rendering:auto;text-shadow:none;text-size-adjust:auto;text-spacing-trim:normal;text-transform:none;text-underline-offset:auto;text-underline-position:auto;text-wrap-mode:wrap;text-wrap-style:auto;timeline-scope:none;timeline-trigger-activation-range-end:normal;timeline-trigger-activation-range-start:normal;timeline-trigger-active-range-end:auto;timeline-trigger-active-range-start:auto;timeline-trigger-name:none;timeline-trigger-source:auto;top:auto;touch-action:auto;transform:none;transform-box:view-box;transform-origin:720px 18px",
    "display:none;top:auto;touch-action:auto;transform:none;transform-box:view-box;transform-origin:720px 18px",
    1
)

with open('index.html', 'w') as f:
    f.write(content)
print("Done")
