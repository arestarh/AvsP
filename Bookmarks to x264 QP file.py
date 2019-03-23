import os, io

# run in thread
bookmarks = avsp.GetBookmarkList()
bookmarks.sort()
filename = avsp.GetSaveFilename(
                title=_('Save chapter file as...'), 
                default=os.path.splitext(
                    avsp.GetScriptFilename(propose='general', only='base'))[0],
                filefilter = '|'.join((_('QP files') + ' (*.qpf)|*.qpf',
                                       _('Text files') + ' (*.txt)|*.txt', 
                                       _('All files') + ' (*.*)|*.*')))
if not filename:
    return

with io.open(filename, mode='w', encoding='utf8') as f:
    for item in bookmarks:
        s = '%s K -1'% item
        f.write(s.decode('utf8') + '\n')
